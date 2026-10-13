#!/usr/bin/env python3
"""Validate the PT2323 audio paths in KiCad's exported netlist."""
import argparse
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--kicad-cli', default='kicad-cli')
args = parser.parse_args()
project = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as directory:
    output = Path(directory)/'receiver.xml'
    subprocess.run([args.kicad_cli, 'sch', 'export', 'netlist', '--format', 'kicadxml',
                    '--output', str(output), str(project/'SabidosReceiver.kicad_sch')], check=True)
    root = ET.parse(output).getroot()

nets = {}
for net in root.findall('./nets/net'):
    members = {(node.get('ref'), node.get('pin')) for node in net}
    for member in members:
        nets[member] = members
values = {c.get('ref'): c.findtext('value') for c in root.findall('./components/comp')}
def connected(first, second):
    assert second in nets[first], f'{first} does not connect to {second}'

# Selector output -> 270 ohm resistor -> AC coupling -> correct processor input.
for outpin, resistor, capacitor, inpin in (
    ('22','R37','C1','11'), ('21','R36','C6','4'), ('20','R35','C3','9'),
    ('19','R34','C4','6'), ('18','R33','C2','10'), ('17','R20','C5','5')):
    connected(('U3',outpin),(resistor,'2'))
    connected((resistor,'1'),(capacitor,'2'))
    connected((capacitor,'1'),('U2',inpin))
    assert values[resistor] == '270R'

for group in range(4):
    for side, pin in enumerate((str(1+group), str(28-group))):
        capacitor = f'C{40+2*group+side}'
        resistor = f'R{46+2*group+side}'
        connector = f'J{7+group}'
        connected(('U3',pin),(capacitor,'1'))
        connected((capacitor,'2'),(connector,'1' if side == 0 else '3'))
        connected((capacitor,'2'),(resistor,'1'))
        connected((resistor,'2'),(connector,'2'))
        connected((connector,'2'),('U3','14'))
        assert values[capacitor] == '10uF' and values[resistor] == '100k'

connected(('U3','15'),('U2','25'))
connected(('U3','16'),('U2','24'))
connected(('U3','12'),('U2','20'))
print('PT2323: six processor paths, eight stereo inputs, ground, power and I2C verified.')
