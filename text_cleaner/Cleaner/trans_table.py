import os
from glob import glob

current_path = os.path.dirname(os.path.abspath(__file__))
mapping_path = os.path.join(current_path, '..', 'mapping')
mapping_files = glob(f'{mapping_path}/*py')
mapping_files = sorted(mapping_files)

mapping_table = {}
for file in mapping_files:
    mapping = {}
    with open(file) as f:
        exec(f.read())
    mapping_table.update(mapping)

mapping_table = {k: v for k, v in mapping_table.items() if k != v}
translate_table = {ord(k): v for k, v in mapping_table.items() if k != v}
