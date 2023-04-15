from ds_store import DSStore
from mac_alias import Alias

ds_store_file = 'COPY'  # Replace with the path to your .DS_Store file

with DSStore.open(ds_store_file, 'r') as d:
    for i in d:
        print(f'Filename: {i.filename}')
        print(f'Code: {i.code}')
        print(f'Type Code: {i.typeCode}')
        
        if i.typeCode == "alis":
            try:
                alias = Alias.from_bytes(i.raw_value())
                target = alias.target
                print(f'Alias target: {target}')
            except Exception as e:
                print(f'Error resolving alias: {e}')
        
        print('------------------------------------')
