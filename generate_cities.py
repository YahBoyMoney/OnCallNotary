import os
import json

# City data with neighborhoods and coordinates
cities = [
    {
        "name": "San Bernardino",
        "slug": "san-bernardino",
        "zip": "92401-92427",
        "lat": 34.1083449,
        "lng": -117.2897652,
        "neighborhoods": [
            "Downtown San Bernardino", "North Park", "Del Rosa", "University District",
            "Mountain View", "Verdemont", "Westside", "North End", "Arden-Guthrie"
        ]
    },
    {
        "name": "Colton",
        "slug": "colton",
        "zip": "92313, 92324",
        "lat": 34.0739014,
        "lng": -117.3136545,
        "neighborhoods": [
            "Reche Canyon", "Grand Terrace", "Lytle Creek", "South Colton"
        ]
    },
    {
        "name": "Rialto",
        "slug": "rialto",
        "zip": "92376, 92377",
        "lat": 34.1063986,
        "lng": -117.370324,
        "neighborhoods": [
            "North Rialto", "South Rialto", "West Rialto", "East Rialto", "Bud Bender"
        ]
    },
    {
        "name": "Highland",
        "slug": "highland",
        "zip": "92346",
        "lat": 34.1283442,
        "lng": -117.2086513,
        "neighborhoods": [
            "East Highland", "Highland Hills", "Greenspot"
        ]
    },
    {
        "name": "Redlands",
        "slug": "redlands",
        "zip": "92373, 92374, 92375",
        "lat": 34.0555693,
        "lng": -117.1825381,
        "neighborhoods": [
            "Downtown Redlands", "Smiley Heights", "East Valley", "North Redlands"
        ]
    },
    {
        "name": "Fontana",
        "slug": "fontana",
        "zip": "92331, 92334, 92335, 92336, 92337",
        "lat": 34.0922335,
        "lng": -117.435048,
        "neighborhoods": [
            "North Fontana", "South Fontana", "Sierra Lakes", "Jurupa Hills"
        ]
    },
    {
        "name": "Riverside",
        "slug": "riverside",
        "zip": "92501-92509, 92513-92519, 92521, 92522",
        "lat": 33.9533487,
        "lng": -117.3961564,
        "neighborhoods": [
            "Downtown Riverside", "Canyon Crest", "Wood Streets", "La Sierra"
        ]
    },
    {
        "name": "Ontario",
        "slug": "ontario",
        "zip": "91758, 91761, 91762, 91764",
        "lat": 34.0633443,
        "lng": -117.6508876,
        "neighborhoods": [
            "Downtown Ontario", "Euclid Avenue", "Vineyard", "Mountain View"
        ]
    },
    {
        "name": "Rancho Cucamonga",
        "slug": "rancho-cucamonga",
        "zip": "91701, 91730, 91737, 91739",
        "lat": 34.1063986,
        "lng": -117.5931084,
        "neighborhoods": [
            "Victoria Gardens", "Alta Loma", "Etiwanda", "Cucamonga"
        ]
    }
]

def generate_city_pages():
    # Read the template
    with open(os.path.join('areas', '_template.html'), 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Create areas directory if it doesn't exist
    os.makedirs('areas', exist_ok=True)
    
    for city in cities:
        # Skip if already exists and not San Bernardino (we'll keep the existing one)
        output_file = os.path.join('areas', f"{city['slug']}.html")
        if os.path.exists(output_file) and city['slug'] != 'san-bernardino':
            print(f"Skipping {city['name']} - file already exists")
            continue
        
        # Generate neighborhood tags
        neighborhood_tags = '\n'.join([
            f'<span class="neighborhood-tag">{n}</span>' 
            for n in city['neighborhoods']
        ])
        
        # Replace placeholders
        content = template
        content = content.replace('[CITY]', city['name'])
        content = content.replace('[CITY-SLUG]', city['slug'])
        content = content.replace('[ZIP]', city['zip'])
        content = content.replace('[LAT]', str(city['lat']))
        content = content.replace('[LONG]', str(city['lng']))
        content = content.replace('[NEIGHBORHOODS]', ', '.join(city['neighborhoods']))
        content = content.replace('[NEIGHBORHOOD_TAGS]', neighborhood_tags)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Generated {city['name']} page at {output_file}")

if __name__ == "__main__":
    generate_city_pages()
