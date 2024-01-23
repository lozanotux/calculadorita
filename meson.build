# project name and programming language
project(
    'com.github.lozanotux.calculadorita', 'c',
    version: '1.0.0',
    license: 'GPL3+',
)

# Dependencies
dependency('gtk4')
dependency('libadwaita-1')

# Include the translations module
gnome = import('gnome')
python = import('python') # Meson new Python module https://mesonbuild.com/Python-module.html

# Python specific section
project_id = meson.project_name()

message('Looking for dependencies')
py_installation = python.find_installation('python3')
if not py_installation.found()
    error('No valid python3 binary found')
else
    message('Found python3 binary')
endif

python_dir = join_paths(get_option('prefix'), py_installation.get_install_dir())
message (python_dir)
DATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
bindir = join_paths(get_option('prefix'), get_option('bindir'))
message (bindir)

conf = configuration_data()
conf.set('DATA_DIR', DATA_DIR)
conf.set('PYTHON_DIR', python_dir)
conf.set('VERSION', meson.project_version())
conf.set('APPID', project_id)
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('LOCALE_DIR', join_paths(get_option('prefix'), get_option('localedir')))

install_subdir(
  'calculadorita',
  install_dir: python_dir
)

message('Preparing binary file')
configure_file(
  input: 'calculadorita.in',
  output: project_id,
  configuration: conf,
  install_dir: bindir
)

install_data(
    'data' / 'calculadorita.desktop',
    install_dir: get_option('datadir') / 'applications',
    rename: meson.project_name() + '.desktop'
)

install_data(
    'data' / 'calculadorita.metainfo.xml',
    install_dir: get_option('datadir') / 'metainfo',
    rename: meson.project_name() + '.metainfo.xml'
)
# End Python Section

# Load CSS file
# Tell meson where to find our resources file and to compile it as a GResource
gresource = gnome.compile_resources(
    'gresource',
    'data' / 'css.gresource.xml',
    source_dir: 'data'
)

subdir('data')

# Install our icons in all the required sizes
icon_sizes = ['16', '24', '32', '48', '64', '128']

foreach i : icon_sizes
    install_data(
        'data' / 'icons' / i + '.svg',
        install_dir: get_option('datadir') / 'icons' / 'hicolor' / i + 'x' + i / 'apps',
        rename: meson.project_name() + '.svg'
    )
    install_data(
        'data' / 'icons' / i + '.svg',
        install_dir: get_option('datadir') / 'icons' / 'hicolor' / i + 'x' + i + '@2' / 'apps',
        rename: meson.project_name() + '.svg'
    )
endforeach

gnome.post_install(
    glib_compile_schemas: true,
    gtk_update_icon_cache: true,
    update_desktop_database: true,
)