# Copyright 2021 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Git Project Task Connector",
    "version": "14.0.0.0.0",
    "author": "Elabore",
    "maintainer": "False",
    "website": "False",
    "license": "AGPL-3",
    "category": "False",
    "summary": "Link project task to Git issues",
    "description": """
   :image: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
=============================
Git Project Task Connector
=============================
This module provides link functionnalities between project tasks and Git issues:
- a user can create an Git issue on a Git platform from a project task
- a user can link an existing Git issue to a project task
- the list of issues linked to the task is displayed with the issues' status

Installation
============
Just install Git Project Task Connector, all dependencies will be installed by default.

Known issues / Roadmap
======================

Bug Tracker
===========
Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/development-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------
* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=f3db262>`_.

Contributors
------------
* Stéphan Sainléger <https://github.com/stephansainleger>

Funders
-------
The development of this module has been financially supported by:
* Elabore (https://elabore.coop)
* Lokavaluto (https://lokavaluto.fr)

Maintainer
----------
This module is maintained by ELABORE.

""",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "project",
    ],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "wizard/link_issue.xml",
        "wizard/create_issue.xml",
        "views/project_task.xml",
        "views/git_issue.xml",
        "views/git_repository.xml",
        "views/res_config_settings_view.xml",
        "views/menus.xml",
        "data/git_issue_data.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
