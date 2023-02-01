
if __name__ == "__main__":
    import json
    
    with open('test_description.oml', 'r') as file:
        lines = file.readlines()

        cis = []
        capture = False
        group = None

        for index, line in enumerate(lines):
            if capture: group.append(line)
            if line.strip().startswith('ci ') and '[' not in line:
                cis.append(line)
            elif line.strip().startswith('ci ') and '[' in line:
                cis.append(line)
                capture = True
                group = []
            elif line.strip().startswith(']'):
                if group:
                    cis.append(group)
                capture = False
                group = None

        concepts = {}
        for i in cis:
            if not isinstance(i, list):
                temp_concept = i.strip(' \tci[\n').split(' : ')[1].split(':')[0]
                temp_ci = i.strip(' \tci[\n').split(' : ')[1].split(':')[1]
                if temp_concept not in concepts:
                    concepts[temp_concept] = {temp_ci : {}}
                else:
                    concepts[temp_concept][temp_ci] = {}
            elif isinstance(i, list):
                for j in i:
                    if ":" in j:
                        temp_attribute = j.strip(' //\tci]\n').split(':')[1].split(" ", 1)[0]
                        temp_value = j.strip(' //\tci]\n').split(':')[1].split(" ", 1)[1]
                        concepts[temp_concept][temp_ci][temp_attribute] = temp_value

    
    with open('test_description.json', 'w', encoding='utf-8') as f:
        json.dump(concepts, f, ensure_ascii=False, indent=4)
