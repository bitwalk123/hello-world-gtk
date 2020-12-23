project('Hello World', 'c', version: '1.0')

gtkdep = dependency('gtk4')

sources = files('hello-world-gtk.c')

executable('hello', sources, dependencies: gtkdep, install: true)
install_data('hello.desktop', install_dir : get_option('datadir') / 'applications')
install_data('hello.svg', install_dir : get_option('datadir') / 'icons/hicolor/scalable/apps')
