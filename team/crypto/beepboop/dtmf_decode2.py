dtmf_mapping = {
    '1': '1', '2': 'ABC2', '3': 'DEF3',
    '4': 'GHI4', '5': 'JKL5', '6': 'MNO6',
    '7': 'PQRS7', '8': 'TUV8', '9': 'WXYZ9',
    '0': '0'
}

key_sequence = "8-44-33 333-444-777-33-9-2-555-555 44-2-7777 22-555-666-222-55-33-3 100 7-2-222-55-33-8-7777"
                T H  E  F   I   R   E  W A L   L   H  A S    B  L   O   C   K  E  D 100 P A C   K  E  T S
def decode_key_sequence(key_sequence, dtmf_mapping):
    decoded_text = ''
    for key_group in key_sequence.split():
        for key, chars in dtmf_mapping.items():
            if key_group[0] in chars:
                decoded_text += chars[len(key_group) % len(chars) - 1]
                break
    return decoded_text

decoded_text = decode_key_sequence(key_sequence, dtmf_mapping)
print(decoded_text)
