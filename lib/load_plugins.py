# -*- coding: utf-8 -*-
__author__ = "SadLin"


from pluginbase import  PluginBase
import os
def load_plugins():
    current_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    plugin_dir = os.path.join(current_dir,'plugin')
    plugin_base = PluginBase(
        package='plugin',searchpath=[plugin_dir]
    )
    plugin_source = plugin_base.make_plugin_source(
        searchpath=[plugin_dir], persist=True
    )
    plugin_dict = {}
    for plugin_name in plugin_source.list_plugins():
        plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)
    return plugin_dict

def show_waf_list():
    plugin_dict = load_plugins()
    for plugin in plugin_dict.values():
        print plugin.NAME