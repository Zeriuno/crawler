#CRAWLER

Définition du besoin

##QU’EST-CE QU’UN cRAWLER ?

Un robot d'indexation (ou littéralement araignée du Web ; en anglais web crawler ou web spider) est un logiciel qui explore automatiquement le Web. Il est généralement conçu pour collecter les ressources (pages Web, images, vidéos, documents Word, PDF ou PostScript, etc.), afin de permettre à un moteur de recherche de les indexer.


##Fonctionnalités attendues

> Faire un crawler qui recherche des mots clefs dans une page.

> Puis crawling des pages associés qui contiennent x% des mêmes mots jusqu'à un certain niveau.

##Présentation des résultats

##Questions

* ~~Réexpliciter le principe d’indexation~~
* ~~Convenir des technos à utiliser sur le projet~~
* Définir le niveau attendu pour la présence des mots clefs: pourcentage de pertinence des résultats.
* Définir un nombre de mots clefs max à rechercher: un ou plusieurs? Un pour l'instant.
* Format de la présentation des résultats : liste (éventuellement des graphes).
* Nécessité de garder les résultats. Pas dans un premier temps.
* ~~Récupérer les données via du PHP et intégration des données dans une base de données MySQL~~
* Comment éviter les liens morts? On ne garde que les réponses 200 HTTP.
* Que faire s’il y a des captcha? On considère le problème comme marginal et non traité par le programme.
* Texte uniquement ou bien d'autres ressources (images)?
* Eviter les URL doubles (avec "#source?twitter")
* Respecte les robots.txt? Oui.

##Ressources exploitables

* Kimono, transformer des sites en APIs
Parfois, on a besoin de récupérer un flux de données provenant d'un site tiers. Dans ce cas, un service génial va vous changer la vie : kimono. Pour le moment totalement gratuit, ce service vous permet de définir un schéma de crawl pour les pages web, et d'en faire une API exploitable. Kimono est donc très utile pour rendre des données non-structurées en un fichier JSON facilement exploitable. Ce service dispose de beaucoup d'options, et s'adapte donc à de nombreux besoins. Il est assez facile de gérer un grand nombre d'APIs.

Actuellement, j'utilise Kimono pour crawler des offres d'emploi, dans le cadre de mon projet Dooock. J'ai défini plus de 60 APIs, qui donnent un flux d'environ 800 annonces par jour. Une tâche CRON consulte chaque jour les différents endpoints d'API et les ajoute en base.

En gros, Kimono est super intéressant parce qu'il est :

Très facile à mettre en place
Totalement gratuit (pour le moment)
Très flexible, grâce à ses nombreuses options, comme la périodicité des crawls
Liens / ressources

https://www.kimonolabs.com/
http://blog.kimonolabs.com/ (des articles super intéressants)


##Liens

* http://fr.lookcloseseefar.com/prototypage-rapide-creer-son-premier-data-crawler/
* http://liris.cnrs.fr/mehdi.kaytoue/sujets/synthese-scrap-crawl/synthese-2013-Scraping-Crawling.pdf
* http://geekmeup.fr/comment-automatiser-le-web-robot-crawler-scraper/
* http://buzut.fr/2012/04/23/comment-creer-un-crawler-web-en-php/
* http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/web/web_intro.html
* http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/
