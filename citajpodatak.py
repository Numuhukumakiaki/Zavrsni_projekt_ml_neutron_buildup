data = []

with open("podaci_konacno1.train", "r") as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()
        try:
            neutron_buildup = float(parts[0])
            values = {}
            for p in parts[1:]:
                key_str, val_str = p.split(":")
                values[int(key_str)] = float(val_str)
            
            row = (neutron_buildup, values[1], values[2], values[3])
            data.append(row)
        except (ValueError, KeyError, IndexError) as e:
            print(f"Error parsing line {line_num}: {e}")
            continue

print(data[0:10])
