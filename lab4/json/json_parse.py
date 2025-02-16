import json
with open('sample-data.json', 'r') as file:
    data = json.load(file)
    print('Interface Status')
    print('='*80)
    print('DN                                                 Description           Speed    MTU')
    print('-------------------------------------------------- --------------------  ------  ------')
    data = data["imdata"]

    for iter_data in data:
        attributes = iter_data["l1PhysIf"]["attributes"]
        dn = attributes["dn"]
        description = attributes["descr"]
        speed = attributes["speed"]
        mtu = attributes["mtu"]

        print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")

