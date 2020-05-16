favorite_languages = {
    'jen': ['C', 'ruby'],
    'sarah': ['c'],
    'edward': ['python', 'Java'],
    'phil': ['C++', 'js']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
