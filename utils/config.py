categories = {
    "Corpos d'água": ["Rio/Córrego", "Lago/Lagoa", "Reservatório"],
    "Vegetação": ["Floresta", "Mata Ciliar", "Grama/Pastagem", "Vegetação Arbustiva"],
    "Áreas Urbanas": ["Edificações", "Rodovias", "Áreas Pavimentadas"],
    "Uso do Solo": ["Agricultura", "Áreas de Extração", "Áreas Industriais"],
    "Outros Elementos Naturais": ["Montanhas/Elevações", "Planícies", "Praias", "Dunas"]
}

initial_category = list(categories.keys())[0]
initial_subcategory = categories[initial_category][0]