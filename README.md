[Reference](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)

## Migrations from WP

Migrate via

pelican-import --wpfile -m markdown -o content --dir-page /media/sf_VBoxShare/marcosantoni.wordpress.2016-08-24.xml

Download all images via WP Plugin downML. Place them in content/images

Replace images url with

cat weighted-random-sampling-with-postgresql.md | sed 's/http:\/\/www.marco.*2016\/[0-9][0-9]\//\{filename\}\/images\//' > weighted-random-sampling-with-postgresql_01.md
