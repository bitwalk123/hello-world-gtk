project('Hello World', 'c', version: '1.0')

gtkdep = dependency('gtk4')
sources = files('hello-world-gtk.c')
executable('hello', sources, dependencies: gtkdep, install: true)
