designFile = "C:/Users/Public/Documents/Altium/Projects/Led Panel/PDNAnalyzer_Output/Led Panel/odb.tgz"

powerNets = ["3V3"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J?", "1") ],
"ground_pins": [ ("J?", "2") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("D1", "2") ],
"ground_pins": [ ("D1", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("D2", "2") ],
"ground_pins": [ ("D2", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("D3", "2") ],
"ground_pins": [ ("D3", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("D4", "2") ],
"ground_pins": [ ("D4", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("D5", "2") ],
"ground_pins": [ ("D5", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("D6", "2") ],
"ground_pins": [ ("D6", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("D7", "2") ],
"ground_pins": [ ("D7", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("D8", "2") ],
"ground_pins": [ ("D8", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("D9", "2") ],
"ground_pins": [ ("D9", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("D10", "2") ],
"ground_pins": [ ("D10", "1") ],
"current": 0.35,
"Rpin": 0.285714285714286,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.3, 'Thickness': 0.0014986},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
