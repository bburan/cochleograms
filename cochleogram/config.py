CELLS = ('IHC', 'OHC1', 'OHC2', 'OHC3', 'Extra')


CHANNEL_CONFIG = {
    'CtBP2': { 'display_color': 'red'},
    'MyosinVIIa': {'display_color': 'blue'},
    'GluR2': {'display_color': 'green'},
    'GlueR2': {'display_color': 'green'},
    'PMT': {'display_color': 'white'},
    'DAPI': {'display_color': 'white'},

    # Channels are tagged as unknown if there's difficulty parsing the channel
    # information from the file.
    'Unknown 1': {'display_color': 'red'},
    'Unknown 2': {'display_color': 'green'},
    'Unknown 3': {'display_color': 'blue'},
}


TOOL_KEY_MAP = {
    's': 'spiral',
    'e': 'exclude',
    'c': 'cells',
    't': 'tile',
}


CELL_KEY_MAP = {
    'i': 'IHC',
    '1': 'OHC1',
    '2': 'OHC2',
    '3': 'OHC3',
    '4': 'Extra',
}
