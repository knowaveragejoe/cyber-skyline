dtmf_mapping = {
    '1': '1', '2': 'ABC2', '3': 'DEF3',
    '4': 'GHI4', '5': 'JKL5', '6': 'MNO6',
    '7': 'PQRS7', '8': 'TUV8', '9': 'WXYZ9',
    '0': '0', 'A': '*', 'B': '#'
}

dtmf_sequence = '7221001108108111443211910139118101329810110111032111611#41211051101033211611132114101979910432121111117321141011039711B410010551100103321211111171143210112201161011120100101100321199711B4131497110116121B463284104410132102108971033210511145328375845688477704549485357'

def decode_dtmf(dtmf_sequence, dtmf_mapping):
    decoded_text = ''
    for tone in dtmf_sequence:
        for key, chars in dtmf_mapping.items():
            if tone in chars:
                decoded_text += key
                break
    return decoded_text

decoded_text = decode_dtmf(dtmf_sequence, dtmf_mapping)
print(decoded_text)