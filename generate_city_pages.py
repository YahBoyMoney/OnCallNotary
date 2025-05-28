import os

# List of cities to generate pages for
cities = [
    "Highland",
    "Rialto",
    "Colton",
    "Redlands",
    "Riverside",
    "Fontana",
    "Ontario",
    "Rancho Cucamonga"
]

template_path = os.path.join("areas", "san-bernardino.html")

# Read the template file
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

for city in cities:
    slug = city.lower().replace(" ", "-")
    content = template
    # Replace city-specific text and URLs
    content = content.replace("San Bernardino", city)
    content = content.replace("san-bernardino", slug)
    content = content.replace("San_Bernardino", city.replace(" ", "_"))
    content = content.replace("san-bernardino.jpg", f"{slug}.jpg")
    content = content.replace(
        'https://oncallnotarysb.com/areas/san-bernardino.html',
        f'https://oncallnotarysb.com/areas/{slug}.html'
    )
    content = content.replace(
        '"sameAs": "https://en.wikipedia.org/wiki/San_Bernardino,_California"',
        f'"sameAs": "https://en.wikipedia.org/wiki/{city},_California"'
    )

    output_path = os.path.join("areas", f"{slug}.html")
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(content)

print(f"Generated city landing pages for: {', '.join(cities)}")
