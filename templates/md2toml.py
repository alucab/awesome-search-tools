#! /usr/bin/env -S pipx run
# Requirements:
#     click==8.*
#     Jinja2==3.*
#     tomli==2.*

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

import click
import jinja2 as j2
import tomli

import re

regex = r"^\* \[(.*)\]\s*\((.+)\) - (.*)$"

test_str = ("## Contents\n"
	"* [MongoDB](#mongodb)\n"
	"* [Algolia](#algolia)\n"
	"* [Elasticsearch](#elasticsearch)\n"
	"* [Memory](#memory)\n"
	"* [UI Interface](#ui-interface)\n"
	"* [Datasets](#datasets)\n"
	"* [Projects](#projects)\n\n"
	"## MongoDB\n\n"
	"* [Full-Text Search in MongoDB](http://code.tutsplus.com/tutorials/full-text-search-in-mongodb--cms-24835) - How to Full-Text Search in MongoDB.\n"
	"* [mongoosastic](https://github.com/mongoosastic/mongoosastic) - Index Mongoose models into elasticsearch automatically.\n"
	"* [mongoose-text-search](https://github.com/aheckmann/mongoose-text-search) - MongoDB 2.4 text search support for mongoose.\n"
	"* [elmongo](https://github.com/jtremback/elmongo) - Give your Mongoose data the Power of Elasticsearch.\n"
	" \n"
	"## Algolia\n\n"
	"* [figolia](https://github.com/webstylestory/figolia) - Keep your Algolia search indexes in sync with your Firebase datasets.\n"
	"* [mongoolia](https://github.com/algolia/mongoolia) - Keep your mongoose schemas synced with Algolia.\n"
	"* [algolia-webcrawler](https://github.com/DeuxHuitHuit/algolia-webcrawler) - Simple node worker that crawls sitemaps in order to keep an algolia index up-to-date.\n"
	"* [algolia-sitemap](https://github.com/algolia/algolia-sitemap) - A Node.js library allowing you to generate sitemaps from an Algolia index.\n\n"
	"## Elasticsearch\n\n"
	"* [esta](https://github.com/dwyl/esta) - Simple + Fast ElasticSearch Node.js client.\n\n"
	"## Memory\n\n"
	"* [elasticlunr](http://elasticlunr.com/) - Lightweight full-text search engine in JavaScript for browser search and offline search.\n"
	"* [lunr](http://lunrjs.com) - A bit like Solr, but much smaller and not as bright.\n"
	"* [pouchdb-quick-search](https://github.com/nolanlawson/pouchdb-quick-search) - Full-text search engine on top of PouchDB.\n"
	"* [search-index](https://github.com/fergiemcdowall/search-index) - A persistent, network resilient, full text search library for the browser and Node.js.\n"
	"* [reds](https://github.com/tj/reds) - A light-weight, insanely simple full text search module backed by Redis.\n"
	"* [fulltext-engine](https://github.com/eugeneware/fulltext-engine) - Full text search backed by levelup/leveldb engine.\n"
	"* [levi](https://github.com/cshum/levi) - Stream based full-text search for Node.js and browsers.\n"
	"* [minisearch](https://github.com/lucaong/minisearch) - Tiny but powerful in-memory fulltext search engine written in JavaScript.\n"
	"* [flexsearch](https://github.com/nextapps-de/flexsearch) - Next-Generation full text search library for Browser and Node.js.\n"
	"* [tinysearch](https://github.com/tinysearch/tinysearch) - This is a lightweight, fast, full-text search engine for static websites.\n"
	"* [stork](https://github.com/jameslittle230/stork) - Fast web search, made for static sites.\n"
	"  \n"
	"## UI Interface\n\n"
	"* [Searchkit](http://www.searchkit.co/) - UI components for Elasticsearch.\n"
	"* [Searchbox](https://shipow.github.io/searchbox/) - Just a searchbox generator.\n"
	"* [algolia/places](https://github.com/algolia/places) - Turn any <input> into an address autocomplete.\n\n"
	"## Datasets\n\n"
	"* [algolia/datasets](https://github.com/algolia/datasets) - Interesting datasets you could use with Algolia.\n\n"
	"## Projects\n\n"
	"* [NPM Trends](https://github.com/johnmpotter/npm-trends) - NPM package comparison app based on Elasticsearch.\n"
	"* [tweetarchive](https://github.com/paulsmith/tweetarchive) - Full-text search for your Twitter archive based on PostgreSQL.")
def _dumps_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, list):
        return f"[{', '.join(_dumps_value(v) for v in value)}]"
    else:
        raise TypeError(f"{type(value).__name__} {value!r} is not supported")

def dumps(toml_dict, table=""):
    def tables_at_end(item):
        _, value = item
        return isinstance(value, dict)

    toml = []
    for key, value in sorted(toml_dict.items(), key=tables_at_end):
        if isinstance(value, dict):
            table_key = f"{table}.{key}" if table else key
            toml.append(f"\n[{table_key}]\n{dumps(value, table_key)}")
        else:
            toml.append(f"{key} = {_dumps_value(value)}")
    return "\n".join(toml)
    
matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    project ={}
    

    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        if groupNum == 1 :
            project[match.group(1)]={}
        elif groupNum == 2 :
            project[match.group(1)]["url"] = match.group(groupNum)
        elif groupNum ==3 : 
            project[match.group(1)]["descr"] = match.group(groupNum)
    
    print(dumps(project, table=""))