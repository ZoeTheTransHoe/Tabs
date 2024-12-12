project('tabs',
          version: '0.1.0',
    meson_version: '>= 1.0.0',
  default_options: [ 'warning_level=2', 'werror=false', ],
)

gnome = import('gnome')
python = import('python')


subdir('data')
subdir('src')
subdir('po')

profile = get_option('profile')
if profile == 'development'
    app_id = 'org.zoey.Tabs.Devel'
  prefix = '/org/zoey/Tabs/Devel'
elif profile == 'release'
  app_id = 'org.zoey.Tabs'
  prefix = '/org/zoey/Tabs'
endif

gnome.post_install(
     glib_compile_schemas: true,
    gtk_update_icon_cache: true,
  update_desktop_database: true,
)
