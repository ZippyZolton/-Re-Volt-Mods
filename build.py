#!/usr/bin/env python

import json
import glob
import datetime
import os


""" Generate repository list """

base_url = "https://re-volt.gitlab.io/rvio/repos/"

repo_names = glob.glob("*.json")
repo_names.sort()

repo_urls = [f"{base_url}{name}" for name in repo_names]

repos = {
    "repos": repo_urls
}

with open("repos.json", "w") as f:
    json.dump(repos, f, indent=4)


""" Generate web page """

page_header = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="generator" content="GitLab Pages">
    <title>Content Repositories</title>
  </head>
  <body>
"""

page_footer = """
  </body>
</html>
"""

with open("index.html", "w") as f:
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M")

    f.write(page_header)
    f.write("<h1>Content Repositories</h1>\n")

    f.write("<p>The default set of repositories available in <a href=\"https://re-volt.gitlab.io/rvgl-launcher\">RVGL Launcher</a>.<br/>")
    f.write("Contribute your own by visiting the <a href=\"https://gitlab.com/re-volt/rvio/repos\">project page</a>.</p>")

    f.write("<ul>\n")
    for repo in repo_names:
        name, _ = os.path.splitext(repo)
        f.write(f"<li><a href=\"{repo}\">{name}</a></li>\n")
    f.write("</ul>\n")

    f.write("<hr>\n")
    f.write(f"<p>Generated on {now}</p>")
    f.write(page_footer)
