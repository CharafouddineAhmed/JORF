# CodeNapoleon Programme

Est un programme en python permettant de parser et/ou convertir intelligement les fichiers XML JORF en JSON. Ces fichiers de sortie seront ensuite indexer dans la base Elasticsearch dans l"idée d'alimenter l'application web CodeNapoleon.

## Description de chaque programme

| Nom fichier | description |
| ------ | ------ |
| index_article.py | Ce programme traite uniquement les fichiers sous l’arborescence article. Il identifie les differentes balises des fichiers XML pour ainsi ignorer le batise XML. Il converti enfin les fichiers en json. Puis les indexes dans la base ES. |
| cell | cell | 

## Dépendance

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Contributing
1.  Ahmed CHARAFOUDDINE (ahmed.charafouddine@gmail.com)

## License
Il s'agit d'un projet privée.