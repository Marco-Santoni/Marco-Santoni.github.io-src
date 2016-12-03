[Reference 1](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)
[Reference 2](http://mathamy.com/migrating-to-github-pages-using-pelican.html)
[Pelican Make Command](https://github.com/getpelican/pelican-blog/blob/master/Makefile)

## Setup

```bash
# add the publish repo in subfolder
git clone git@github.com:Marco-Santoni/Marco-Santoni.github.io.git
mv Marco-Santoni.github.io.git output

make html && make serve
# visit http://localhost:8000/
make publish
# --On OSX only
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
# --

```

## Migrations from WP

Migrate via

pelican-import --wpfile -m markdown -o content --dir-page /media/sf_VBoxShare/marcosantoni.wordpress.2016-08-24.xml

Download all images via WP Plugin downML. Place them in content/images

Replace images url with

cat weighted-random-sampling-with-postgresql.md | sed 's/http:\/\/www.marco.*2016\/[0-9][0-9]\//\{filename\}\/images\//' > weighted-random-sampling-with-postgresql_01.md
