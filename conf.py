# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


import os
import sys
import subprocess

def whereis(binary):
    command = 'which' if os.name != 'nt' else 'where'
    try:
        sub = subprocess.run([command, binary], text=True, capture_output=True)
        return sub.stdout
    except BaseException as e:
        print(f"Warning: {binary} is not found")
        return ''

doxyrest_bin_path = whereis('doxyrest')
doxyrest_dir_path = os.path.dirname(doxyrest_bin_path)
doxyrest_share_path = doxyrest_dir_path + "/../share/doxyrest/sphinx"
sys.path.insert(1, os.path.abspath(doxyrest_share_path))

# -- Project information -----------------------------------------------------

project = 'isa-l_crypto'
copyright = '2022, many'
author = 'many'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['doxyrest','cpplexer','sphinx2dita'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

ditaxml_make_flat=True
ditaxml_flat_map_to_title=True
ditaxml_shorten_alias=True
ditaxml_gen_index=True
ditaxml_topic_meta={}
ditaxml_topic_meta["audience"]="emtaudience:business/btssbusinesstechnologysolutionspecialist/softwaredeveloper"
ditaxml_topic_meta["content type"]="Short Title"
ditaxml_topic_meta["description"]="Prerequisites and installation instructions"
ditaxml_topic_meta["document title"]="Your cool project title"
ditaxml_topic_meta["download url"]=""
ditaxml_topic_meta["IDZ custom tags"]="idzcustomtags:productdocumentation"
ditaxml_topic_meta["keywords"]="None"
ditaxml_topic_meta["language"]="en"
ditaxml_topic_meta["location"]="us"
ditaxml_topic_meta["menu"]="/content/data/globalelements/US/en/sub-navigation/idz/idz-spcltools"
ditaxml_topic_meta["operating system"]=""
ditaxml_topic_meta["programming language"]=""
ditaxml_topic_meta["software"]=""
ditaxml_topic_meta["primaryOwner"]="Name, Your (your.name@intel.com)"
ditaxml_topic_meta["programidentifier"]="idz"
ditaxml_topic_meta["published date"]="10/05/2020"
ditaxml_topic_meta["resourcetypeTag"]="emtcontenttype:document"
ditaxml_topic_meta["secondary contenttype"]="emtcontenttype:document/guide/developerguide/developergettingstartedguide"
ditaxml_topic_meta["security classification"]="Intel Confidential"
ditaxml_topic_meta["shortDescription"]="Installation instructions"
ditaxml_topic_meta["shortTitle"]="Your cool project title"
ditaxml_topic_meta["entitlement"]="intel_usr,iot_tcc"
ditaxml_topic_meta["entitlementtype"]="any"
ditaxml_topic_meta["noindexfollowarchive"]="true"
ditaxml_prod_info={}
ditaxml_prod_info["prodname"]=""
ditaxml_prod_info["version"]="0.11"
ditaxml_data_about={}
ditaxml_data_about["intelswd_aliasprefix"]={"datatype":"webAttr","value":"get-started-with-intel-time-coordinated-computing-tools-0-11"}
