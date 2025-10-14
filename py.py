import json

# Ler o arquivo JSON
with open('C:\\Users\\Reich\\OneDrive\\Documentos\\Projectfather\\LightLocal\\data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Substituir "por Robocop 400 5 7 6 7" por "por Christopher" em todas as features
for feature in data['features']:
    properties = feature['properties']
    
    # Substituir no nome
    if 'por Christopher' in properties['name']:
        properties['name'] = properties['name'].replace('por Christopher', 'por ChMH')
    
    # Substituir na descrição
    if 'por Christopher' in properties['description']:
        properties['description'] = properties['description'].replace('por Christopher', 'por ChMH')

# Salvar o arquivo modificado (pode ser o mesmo ou um novo arquivo)
with open('C:\\Users\\Reich\\OneDrive\\Documentos\\Projectfather\\LightLocal\\data_modified.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("Substituição concluída! Arquivo salvo como 'data_modified.json'")