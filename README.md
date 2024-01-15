# Awesome Search Tools And Libraries

The following is a list of search tools and libraries useful to implement information retrieval in process or as an external component. Every component selected has to be Open Source or with a reasonable free tier if delivered in Saas mode.
I started this catalog as there are only Elastic Search or Algolia pages while plenty of interesting and lighter alternatives do exist.

- [Awesome Search Tools And Libraries](#awesome-search-tools-and-libraries)
  - [Tools](#tools)
  - [Libraries](#libraries)
  - [In Memory](#in-memory)
  - [Saas](#saas)
  - [Heavy Weights](#heavy-weights)
    - [Elasticsearch](#elasticsearch)
    - [Algolia](#algolia)
  - [Database](#database)
    - [Mongo DB](#mongo-db)
  - [By Language](#by-language)
    - [Go](#go)
    - [Javascript/Node.js](#javascriptnodejs)
    - [Java](#java)
  - [Information Sources](#information-sources)
  - [Credits](#credits)
  - [License](#license)

## Tools

- [Sonic](https://github.com/valeriansaliou/sonic) **—** Fast, lightweight & schema-less search backend. An alternative to Elasticsearch that runs on a few MBs of RAM.Sonic is a fast, lightweight and schema-less search backend. It ingests search texts and identifier tuples that can then be queried against in a microsecond's time.
- [Zincsearch](https://github.com/zincsearch/zincsearch) **—** ZincSearch is a search engine that does full text indexing. It is a lightweight alternative to Elasticsearch and runs using a fraction of the resources. It uses bluge as the underlying indexing library and provide integrated ingestion and searching GUI

## Libraries

- [Bleve](https://github.com/blevesearch/bleve) **—** A modern text indexing library in go. Index any go data structure (including JSON).Bleve is a search engine that uses Lucene-style full-text search and indexing. This style of search and indexing helps overcome limitations of the default database search such as challenges with characters and advanced search capabilities.
- [Bluge](https://github.com/blugelabs/bluge) **—** Bluge is an indexing/search library for Go. Bluge originated as an evolution of the Bleve search library. Bleve has seen wide adoption, but that success comes with some downside. As companies ship products using Bleve, they require backwards compatibility, and this has led to a slower more incremental progression.Bluge is an attempt to break out of this model, making many breaking changes all at once.

## In Memory

- [elasticlunr](http://elasticlunr.com/) **—** Lightweight full-text search engine in JavaScript for browser search and offline search.
- [lunr](http://lunrjs.com) **—** A bit like Solr, but much smaller and not as bright.
- [pouchdb-quick-search](https://github.com/nolanlawson/pouchdb-quick-search) **—** Full-text search engine on top of PouchDB.
- [search-index](https://github.com/fergiemcdowall/search-index) **—** A persistent, network resilient, full text search library for the browser and Node.js.
- [reds](https://github.com/tj/reds) **—** A light-weight, insanely simple full text search module backed by Redis.
- [fulltext-engine](https://github.com/eugeneware/fulltext-engine) **—** Full text search backed by levelup/leveldb engine.
- [levi](https://github.com/cshum/levi) **—** Stream based full-text search for Node.js and browsers.
- [minisearch](https://github.com/lucaong/minisearch) **—** Tiny but powerful in-memory fulltext search engine written in JavaScript.
- [flexsearch](https://github.com/nextapps-de/flexsearch) **—** Next-Generation full text search library for Browser and Node.js.
- [tinysearch](https://github.com/tinysearch/tinysearch) **—** This is a lightweight, fast, full-text search engine for static websites.
- [stork](https://github.com/jameslittle230/stork) **—** Fast web search, made for static sites.

## Saas

- [Algolia](https://www.algolia.com) **—** Algolia is a proprietary search-as-a-service platform designed for use cases that require high quality and relevant search.
- [Awesome Algolia](https://github.com/algolia/awesome-algolia) **—** A curated list of awesome things related to Algolia, inspired by awesome.re

## Heavy Weights

### Elasticsearch

- [Elasticsearch](https://www.elastic.co) **—** The Elasticsearch Platform (a.k.a. the ELK Stack) enables enterprises to accelerate business outcomes by combining the power of search and AI.
- [Awesome Elasticsearch](https://github.com/dzharii/awesome-elasticsearch) **—** A curated list of the most important and useful resources about elasticsearch: articles, videos, blogs, tips and tricks, use cases. All about Elasticsearch!
- [Searchkit](http://www.searchkit.co/) **—** UI components for Elasticsearch.

### Algolia

- [Algolia](https://www.algolia.com) **—** Algolia is a proprietary search-as-a-service platform designed for use cases that require high quality and relevant search.
- [Awesome Algolia](https://github.com/algolia/awesome-algolia) **—** A curated list of awesome things related to Algolia, inspired by awesome.re
- [algolia/places](https://github.com/algolia/places) **—** Turn any <input> into an address autocomplete.
- [algolia/datasets](https://github.com/algolia/datasets) **—** Interesting datasets you could use with Algolia.
- [algolia-webcrawler](https://github.com/DeuxHuitHuit/algolia-webcrawler) **—** Simple node worker that crawls sitemaps in order to keep an algolia index up-to-date.
- [algolia-sitemap](https://github.com/algolia/algolia-sitemap) **—** A Node.js library allowing you to generate sitemaps from an Algolia index.
- [figolia](https://github.com/webstylestory/figolia) **—** Keep your Algolia search indexes in sync with your Firebase datasets.
- [mongoolia](https://github.com/algolia/mongoolia) **—** Keep your mongoose schemas synced with Algolia.

## Database

### Mongo DB

- [Full Text Search in MongoDB](http://code.tutsplus.com/tutorials/full-text-search-in-mongodb--cms-24835) **—** How to Full-Text Search in MongoDB.
- [mongoosastic](https://github.com/mongoosastic/mongoosastic) **—** Index Mongoose models into elasticsearch automatically.
- [mongoose-text-search](https://github.com/aheckmann/mongoose-text-search) **—** MongoDB 2.4 text search support for mongoose.
- [elmongo](https://github.com/jtremback/elmongo) **—** Give your Mongoose data the Power of Elasticsearch.

## By Language

### Go

- [Bleve](https://github.com/blevesearch/bleve) **—** A modern text indexing library in go. Index any go data structure (including JSON).Bleve is a search engine that uses Lucene-style full-text search and indexing. This style of search and indexing helps overcome limitations of the default database search such as challenges with characters and advanced search capabilities.
- [Bluge](https://github.com/blugelabs/bluge) **—** Bluge is an indexing/search library for Go. Bluge originated as an evolution of the Bleve search library. Bleve has seen wide adoption, but that success comes with some downside. As companies ship products using Bleve, they require backwards compatibility, and this has led to a slower more incremental progression.Bluge is an attempt to break out of this model, making many breaking changes all at once.
- [Sonic](https://github.com/valeriansaliou/sonic) **—** Fast, lightweight & schema-less search backend. An alternative to Elasticsearch that runs on a few MBs of RAM.Sonic is a fast, lightweight and schema-less search backend. It ingests search texts and identifier tuples that can then be queried against in a microsecond's time.
- [Zincsearch](https://github.com/zincsearch/zincsearch) **—** ZincSearch is a search engine that does full text indexing. It is a lightweight alternative to Elasticsearch and runs using a fraction of the resources. It uses bluge as the underlying indexing library and provide integrated ingestion and searching GUI

### Javascript/Node.js

- [elasticlunr](http://elasticlunr.com/) **—** Lightweight full-text search engine in JavaScript for browser search and offline search.
- [lunr](http://lunrjs.com) **—** A bit like Solr, but much smaller and not as bright.
- [pouchdb-quick-search](https://github.com/nolanlawson/pouchdb-quick-search) **—** Full-text search engine on top of PouchDB.
- [search-index](https://github.com/fergiemcdowall/search-index) **—** A persistent, network resilient, full text search library for the browser and Node.js.
- [levi](https://github.com/cshum/levi) **—** Stream based full-text search for Node.js and browsers.
- [minisearch](https://github.com/lucaong/minisearch) **—** Tiny but powerful in-memory fulltext search engine written in JavaScript.
- [flexsearch](https://github.com/nextapps-de/flexsearch) **—** Next-Generation full text search library for Browser and Node.js.

### Java

- [Elasticsearch](https://www.elastic.co) **—** The Elasticsearch Platform (a.k.a. the ELK Stack) enables enterprises to accelerate business outcomes by combining the power of search and AI.
- [Awesome Elasticsearch](https://github.com/dzharii/awesome-elasticsearch) **—** A curated list of the most important and useful resources about elasticsearch: articles, videos, blogs, tips and tricks, use cases. All about Elasticsearch!

## Information Sources

- [Awesome Search(For E-Commerce)](https://github.com/algolia/awesome-algolia) **—** Awesome Search - this is all about the (e-commerce, but not only) search and its awesomeness

## Credits

The structure of this page is based on the excellent [Structured Text Tools](https://github.com/dbohdan/structured-text-tools) repository from [D. Bohdan](https://github.com/dbohdan)

## License

The contents of this document is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). By contributing you agree to release your contribution under this license.
