# Splunk UI Kit - Complete Documentation Reference

*Generated from crawled Splunk UI Kit documentation for agent coding assistance*

This document contains comprehensive documentation for the Splunk UI Kit, organized logically for development reference. Each section includes component APIs, examples, and usage patterns.

---

## Table of Contents

- [Overview & Getting Started](#overview)
- [React UI Components](#react-components)
- [Accessibility Guidelines](#accessibility)
- [Themes & Styling](#themes-styling)
- [Visualizations](#visualizations)
- [Utility Libraries](#utilities)
- [Build Tools & Configuration](#build-tools)
- [Other Packages](#other-packages)

---

# Overview & Getting Started {#overview}

*High-level overviews and getting started guides for the Splunk UI Kit ecosystem.*

## Splunk Design System

**Package:** `Accessibility` | **Component:** `Overview`

# A11y Overview

## What is Web Accessibility?

Wikipedia defines web accessibility (a11y) as “the inclusive practice of
ensuring there are no barriers that prevent interaction with, or access to,
websites on the World Wide Web by people with physical disabilities,
situational disabilities, and socio-economic restrictions on bandwidth and
speed.”

## Why is it Important?

Splunk believes that a11y is essential to an inclusive design practice.
Accessible design in our physical world benefits everyone; we’ve all used
sidewalk cutouts or have sent text messages. We’re bringing that same
philosophy into our digital world by making web accessibility a first-class
citizen.

### It’s the right thing to do.

Disabled users* are users, full stop. They are not an “edge case” or “rare”.
Disabled people are the largest minority group in the world, making up 15% of
the world population. In addition, it’s common for an able-bodied person to be
in an environment or a situation where accessible products benefit their use
case, as illustrated in the [Microsoft Inclusive Design
Framework](https://www.microsoft.com/design/inclusive/).

_After discussion with many people from the disabled community, we decided to
use disability-first language in our documentation. We acknowledge the
challenges that may come with this as opposed to person-first language such as
“PWD (people with disabilities)” and offer[Cara Liebowitz’s editorial on
identity-first versus person-first language](https://dfwhcfoundation.org/wp-
content/uploads/2018/10/I-am-Disabled.-On-Identity-First-Versus-People-First-
Language-TBISNAA.pdf) as a resource to our decision. Part of our work is to
continue to listen to the disability community and, as views change, reflect
that in our language and guidelines._

### It’s our responsibility as designers and developers.

The mission to make machine data accessible, usable, and valuable to everyone
drives our commitment to apply inclusive design practices to deliver products
for users of all abilities. The Design System team acknowledges that our
society, software development, and design have a tradition of ableism; we’re
here to build accessible software and show up for the education and hard
conversations too.

### Accessibility is a testament to product quality.

[IBM Carbon](https://www.ibm.com/able/) puts this point succinctly that
“accessibility is not just a practice, it’s a culture and a mindset.” Splunk
UI recognizes that “compliant” isn’t enough; in fact, “compliant” at times
isn’t even usable. We aim to bring Splunk products to the next level by
involving in-house a11y experts and advocates from the beginning of the design
process through production.

### It’s the law.

While this is the last line of defense for why a11y is important, it can’t be
dismissed. Given 21st century laws such as Section 508, Accessibility for
Ontarians with Disabilities Act (AODA), European Accessibility Act (EAA), EN
301 549, and the United Nations Conventions on the Rights of Persons with
Disabilities (UN CRPD), it’s in a company’s best interest to build with a11y
from the start.

## Is the Splunk UI Design System Compliant/Accessible?

Accessibility is not a checkbox on a list, or a “one-and-done” practice.
Accessibility is a journey, not a destination. The Splunk UI Design System is
committed to ensuring digital accessibility for disabled users. We are
continually improving the user experience for everyone, and applying the
relevant accessibility standards. Splunk UI is dedicated to staying on top of
the latest a11y requirements to meet [WCAG 2.1 Level A and AA
guidelines](https://www.w3.org/TR/WCAG21/).

## Where can I learn more?

Check out more of the a11y section for high-level overviews of topics that
pertain to accessibility. For a deeper dive, some of the team’s favorites are:

  * [World Wide Web Consortium Web Accessibility Initiative (W3C WAI) Perspective Videos](https://www.w3.org/WAI/perspective-videos/) As a team, we understand that the disabled community is not a monolith. These short videos can help illuminate how diverse the needs of the disabled community are and how our team can design and code for a range of abilities.
  * [WebAIM (Accessibility in Mind) Resources for Designers](https://webaim.org/resources/designers/) This article summarizes what designers can do to incorporate a11y into designs before dev handoff.

---

## @splunk/babel-preset - 4.0.0

**Package:** `babel-preset` | **Component:** `Overview`

# @splunk/babel-preset

A standardized preset for Babel to work with the latest and greatest
TypeScript and JavaScript have to offer.

## What This Preset Contains

#### [📖 @babel/preset-typescript](https://babeljs.io/docs/en/babel-preset-
typescript)

This preset is used to strip type information from `.ts(x)` files. Doing so
allows us to work on TypeScript files without the overhead of type checking.

For type checking, please use one of the available TypeScript loaders or `tsc`
in your project.

> Note: You may need to specify `--extensions ".ts"` if you're relying on
> `@babel/cli` & `@babel/node` CLIs to handle .ts files.

#### [📖 @babel/preset-env](https://babeljs.io/docs/en/babel-preset-env)

This is a smart preset that allows you to use the latest JavaScript without
needing to micromanage which syntax transforms (and optionally, browser
polyfills) are needed by your target environment(s).

We provide this as-is with only the default options enabled.

#### [📖 @babel/preset-react](https://babeljs.io/docs/en/babel-preset-react)

This preset allows for the transpiling of JSX.

#### [📖 @babel/plugin-proposal-class-
properties](https://babeljs.io/docs/en/babel-plugin-proposal-class-properties)

This plugin is remarkably useful with regards to TypeScript classes as it
allows us to use class field declarations:



    class Bork {
        //Property initializer syntax with type information
        sound: string = "bork";
        // Bound method
        public playSound = () => {
            return this.sound;
        }
    }
    const myBork = new Bork();
    myBork.playSound // "bork"


#### [📖 @babel/plugin-proposal-object-rest-
spread](https://babeljs.io/docs/en/babel-plugin-proposal-object-rest-spreads)

This is the second of two code transforms that we expose.

This allows developers to make use of rest operators inside objects:



    let { x, y, ...z } = { x: 1, y: 2, a: 3, b: 4 };
    //          ^-- { a: 3, b: 4 }


As well as spreads:



    let n = { x, y, ...z }; // { x: 1, y: 2, a: 3, b: 4 }


## Install

#### Step 1: Install the peer dependencies



    $ npm install --save-dev @babel/core^7


#### Step 2: Install the package



    $ npm install --save-dev @splunk/babel-preset


## Usage

Add the preset to your babel configuration:



    {
        "presets": ["@splunk/babel-preset"]
    }


## Options

Each of our presets can consume an options object as such:



    {
        "presets": ["@splunk/babel-preset", {
            // These options are passed to @babel/preset-env
            "envPresetOptions": { ... },
            // These options are passed to @babel/preset-react
            "reactPresetOptions" : { ... },
            // These options are passed to @babel/preset-typescript
            "typescriptPresetOptions": { ... }
        }]
    }


📖Please see the URLs at the top of this file for documentation surrounding
available options for each of these loaders.

Each preset can be disabled:



    {
        "presets": ["@splunk/babel-preset", {
            "envPresetEnabled": false,
            "reactPresetEnabled": false,
            "typescriptPresetEnabled": false
        }]
    }

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `Overview`

# @splunk/create

## What is @splunk/create?

`@splunk/create` generates code and scaffolding for a new Splunk application,
built with React, via CLI.

By using `@splunk/create`, you can quickly start developing with Splunk
provided packages such as [@splunk/react-ui](../react-ui/),
[@splunk/dashboard-core](../dashboard-docs/), and
[@splunk/visualizations](../visualizations/).

What will you create? Check out our [Examples
Gallery](../../toolkits/suit/examplesgallery) for inspiration.

### Requirements

  * Yarn >= 1.2
  * Node >= 22

## Prerequisites

To run your Splunk app locally you will need a local Splunk Enterprise
instance with `$SPLUNK_HOME` set.

For more information on getting a local instance, see the [Splunk Enterprise
downloads page](https://www.splunk.com/en_us/download/splunk-enterprise.html).

### Setting up $SPLUNK_HOME



    # Set SPLUNK_HOME to point to the top-level installation directory
    $ export SPLUNK_HOME=/opt/splunk

    # Add $SPLUNK_HOME/bin to the shell’s path.
    $ export PATH=$SPLUNK_HOME/bin:$PATH

## Getting started

To generate files for a Splunk app, run `npx @splunk/create` from an empty
project folder.



    $ mkdir project-folder
    $ cd project-folder
    $ npx @splunk/create
    #? What do you want to name your Splunk app?: MySplunkApp
    #? What do you want to name your new page?: MyPage
    #? What type of page would you like to create?: Add a Basic Page

Next, install project dependencies:



    $ yarn setup

You’ll now have two main directories, one for the created React page and one
for the created Splunk app.

  * packages/my-page
  * packages/my-splunk-app

### Splunk demo

Splunk demo will allow you to view your new app inside your local Splunk
instance:



    # navigate to your app folder
    $ cd packages/my-splunk-app

    # link the app to your local Splunk instance
    $ yarn link:app

    # check that the link is set (optional)
    $ ls -l $SPLUNK_HOME/etc/apps/my-splunk-app

    # restart Splunk (will start Splunk if not already started)
    $ splunk restart

    # navigate to the root project directory
    $ cd ../../

    # start the Splunk app
    $ yarn start

This will watch both your my-splunk-app and my-page folders for changes and
rebundle.

You should now see your app in the left hand menu of the Splunk Enterprise
home page, typically located at <https://localhost:8000>.

There is no hot-reloading within Splunk, you'll need to manually refresh the
page to see changes.

If you are not seeing your changes you can try:

  * hard reloading Shift+Command+R (Ctrl+Shift+R on Windows) in Google Chrome
  * [disabling Splunk asset cache](https://dev.splunk.com/enterprise/docs/developapps/manageknowledge/assetcaching/) (not recommended for production environments)
  * using <https://localhost:8000/en-US/_bump>

### Local React demo

Sometimes developing within Splunk is not the most efficient, which is why we
also provide a local development environment specifically for your React page.



    # navigate to the page directory
    $ cd packages/my-page

    # start the local development demo
    $ yarn run start:demo

Go to <http://localhost:8080/> to see your new React page in action.

Page files are located in packages/my-page/src. Make a change to a file to see
it update in the demo.

## What’s next

  * Check out our tutorials -> [Tutorial: Creating a todo list](/Packages/create//TodoList)
  * Learn about the dev tools available in your new project -> [Dev Tools](/Packages/create//DevTools)
  * Learn more about how your Splunk app is set up -> [Generated Splunk app code](/Packages/create//GeneratedCode)
  * Learn how to package your Splunk app -> [Packaging a @splunk/create app](/Packages/create//PackagingYourApp)
  * Check out examples for inspiration -> [Examples Gallery](../../toolkits/suit/examplesgallery)

---

## Splunk Design System

**Package:** `CRUD` | **Component:** `Overview`

# C.R.U.D. Actions Overview

C.R.U.D. stands for Create, Read, Update, and Delete. These are the core tasks
users perform to manage content across Splunk products. Understanding C.R.U.D.
helps us design consistent, task-focused experiences that align with user
goals.

[Create](/Blueprints/CRUD/Create)

Create or add something new to the system — like a dashboard, alert, report,
or rule. This is often the starting point of a workflow.

Read

View existing content to understand status, details, or outcomes. This is the
most frequent passive action.

Update

Covers any action where users modify existing content — from quick edits to
more complex changes across multiple fields or steps.

Delete

Removes content that is no longer needed. Often includes confirmation to
prevent accidental or irreversible actions.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Datasourcesoverview`

# Data source

A `DataSource` is a javascript module that provides the data that powers a
dashboard.

Guide

API

## `setup` and `teardown`

The `setup` and `teardown` methods can be called only once per data source.
Override these functions to run a bootstrap cleanup such as establishing and
destroying connections.

For example:



    import { DataSource } from '@splunk/datasources';

    class MyDataSource extends DataSource {
        setup() {
            this.searchJob = this.createSearchJob();
        }

        teardown() {
            this.searchJob.destroy();
            delete this.searchJob;
        }

        createSearchJob() {
            // ...
        }
    }

## `request`

The `request` call implements data fetching logic. An `Observable` must be
returned for each call. Data sources will then push the data to the `Observer`
(the module that subscribes/listens to this `Observable`) via the
`observer.next` function.

The following example is a data source which always returns empty data.



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.next({
                    data: DataSet.empty(),
                });

                observer.complete();
                return () => {
                    // do nothing
                };
            };
        }
    }

An asynchronous fetch can also be implemented. For example:



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                const interval = setInterval(() => {
                    observer.next({
                        data: DataSet.fromJSONCols(
                            [{ name: 'x' }, { name: 'y' }, { name: 'z' }],
                            [['a', 'b', 'c'], [4, 5, 6], [70, 80, 90]];
                        ),
                    });
                }, 5000);

                return () => {
                    clearInterval(interval);
                };
            };
        }
    }

### Metadata

Data sources can return metadata using the `meta` property. Visualizations and
inputs can decide how to use the metadata. The framework has built-in UI for
the follow metadata fields:

  * If `meta.percentComplete` is provided, it will be used to display progress bar. The value range is 0-100.
  * If `meta.status` and `meta.statusMessage` are provided, they will be used to display status icon and corresponding tooltip.
    * `meta.status` value can be one of the following: `['queued', 'parsing', 'running', 'pause', 'finalizing', 'failed', 'done', 'canceled']`.
    * `meta.statusMessage` value can be any string.
  * If `meta.lastUpdated` and/or `meta.isRealTimeSearch` is provided, it will be used to display last updated time. The timestamp format should be consumable by the [Moment library](https://momentjs.com/docs/#/parsing/string/).



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.next({
                    data: DataSet.empty(),
                    meta: {
                        totalCount: 0,
                        status: 'running',
                        statusMessage:
                            'Search is running, but not enough data to render visualization',
                        sid: '123.456',
                        percentComplete: 50,
                        isRealTimeSearch: false,
                        lastUpdated: '2020-07-15T16:35:49.768Z',
                    },
                });

                observer.complete();
                return () => {
                    // do nothing
                };
            };
        }
    }

### Error

Data sources can return errors by calling the `error` method on the
`observer`. The argument provided to the call of `error` should contain two
properties:

  1. `level` must be a string, one of: `info`, `warning`, or `error`
  2. `message` must be any string and should contain more descriptive information about the state



    import { DataSource } from '@splunk/datasources';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.error({
                    level: 'error',
                    message: 'help!!',
                });

                return () => {
                    // do nothing
                };
            };
        }
    }

### Request parameters

Request parameters define how data is formatted for the client. A
`requestParams` object usually contains following parameters:

#### count

The maximum number of results to return.

#### offset

The first result (inclusive) from which to begin returning data. This value is
0-indexed.

Use `offset` and `count` together to implement result pagination.

#### sort

Sorting of the results, expressed as an object.

For example, sort the field `_time` in descending order:



    {
        "sort": {
            "_time": "desc"
        }
    }

#### requireTotalCount

True if `totalCount` has to be returned as part of `meta`. This is often
required in table and events viewer visualizations.

## Data source definition defaults

Dashboard definition can contain default values for data sources' `options`
field. There are different levels of granularity:

  * Global defaults: these defaults will apply to all data sources
  * Data source type defaults: these defaults will apply to a specific type of data source

If both data source type defaults and global defaults present, data source
type defaults overrides global defaults.

Here's an example:



    const definition = {
        defaults: {
            dataSources: {
                global: {
                    options: {
                        queryParameters: {
                            earliest: '-4h@m',
                        },
                    },
                },
                'ds.search': {
                    options: {
                        queryParameters: {
                            latest: 'now',
                        },
                    },
                },
            },
        },
        dataSources: {
            dsId2: {
                type: 'ds.search',
                options: {
                    refresh: '5s',
                    refreshType: 'delay',
                },
            },
        },
    };

    /*
    The above definition will consolidate to the following:
    {
        dsId2: {
            type: 'ds.search',
            options: {
                refresh: '5s',
                refreshType: 'delay',
                queryParameters: {
                    earliest: '-4h@m',
                    latest: 'now',
                },
            },
        },
    }
    */

## Tokens

If a data source's `options` contains tokens, the token values will be
interpreted properly based on the `tokenBinding` values.

## Data source implementation metadata

Data source implementations should also provide metadata in a static
**config** property. This instructs the editing interfaces what capabilities
are available to the end user, and how to validate the data source settings in
source mode. Data sources which do not have a static **config** property will
not be displayed in the data panel, and will not be able to be created or
edited by end users, but they will still operate as normal for pre-configured
dashboards.

Field| Type| Description
---|---|---
title| string| The name to display for the data source type, e.g. 'Ad hoc
Search'
displayDataSourceItemListByDefault| boolean| Flag to determine if data sources
of this type should be shown
canCreateDataSource| boolean| Flag to determine if users can create new data
sources of this type
dataSourceRemoveVerb| string| Word to use to describe a remove operations,
e.g. 'delete'
isDataSourceNameEditable| boolean| Flag to turn on editing of the data source
names
getDataSourceName| Function| A method to return a data source's name given its
configuration
defaultOptions| Function or Object| An object containing the default
configuration for a new data source, or a function accepting the dashboard
definition and search type that returns the same.
editorConfig| Array| Future Use: An array describing configuration for the
dynamic editor component
optionsSchema| Object| A JSONSchema configuration describing the valid
configuration of a data source. Used to validate code in source mode.

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** ``

# Data source

A `DataSource` is a javascript module that provides the data that powers a
dashboard.

Guide

API

## `setup` and `teardown`

The `setup` and `teardown` methods can be called only once per data source.
Override these functions to run a bootstrap cleanup such as establishing and
destroying connections.

For example:



    import { DataSource } from '@splunk/datasources';

    class MyDataSource extends DataSource {
        setup() {
            this.searchJob = this.createSearchJob();
        }

        teardown() {
            this.searchJob.destroy();
            delete this.searchJob;
        }

        createSearchJob() {
            // ...
        }
    }

## `request`

The `request` call implements data fetching logic. An `Observable` must be
returned for each call. Data sources will then push the data to the `Observer`
(the module that subscribes/listens to this `Observable`) via the
`observer.next` function.

The following example is a data source which always returns empty data.



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.next({
                    data: DataSet.empty(),
                });

                observer.complete();
                return () => {
                    // do nothing
                };
            };
        }
    }

An asynchronous fetch can also be implemented. For example:



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                const interval = setInterval(() => {
                    observer.next({
                        data: DataSet.fromJSONCols(
                            [{ name: 'x' }, { name: 'y' }, { name: 'z' }],
                            [['a', 'b', 'c'], [4, 5, 6], [70, 80, 90]];
                        ),
                    });
                }, 5000);

                return () => {
                    clearInterval(interval);
                };
            };
        }
    }

### Metadata

Data sources can return metadata using the `meta` property. Visualizations and
inputs can decide how to use the metadata. The framework has built-in UI for
the follow metadata fields:

  * If `meta.percentComplete` is provided, it will be used to display progress bar. The value range is 0-100.
  * If `meta.status` and `meta.statusMessage` are provided, they will be used to display status icon and corresponding tooltip.
    * `meta.status` value can be one of the following: `['queued', 'parsing', 'running', 'pause', 'finalizing', 'failed', 'done', 'canceled']`.
    * `meta.statusMessage` value can be any string.
  * If `meta.lastUpdated` and/or `meta.isRealTimeSearch` is provided, it will be used to display last updated time. The timestamp format should be consumable by the [Moment library](https://momentjs.com/docs/#/parsing/string/).



    import { DataSource } from '@splunk/datasources';
    import { DataSet } from '@splunk/datasource-utils';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.next({
                    data: DataSet.empty(),
                    meta: {
                        totalCount: 0,
                        status: 'running',
                        statusMessage:
                            'Search is running, but not enough data to render visualization',
                        sid: '123.456',
                        percentComplete: 50,
                        isRealTimeSearch: false,
                        lastUpdated: '2020-07-15T16:35:49.768Z',
                    },
                });

                observer.complete();
                return () => {
                    // do nothing
                };
            };
        }
    }

### Error

Data sources can return errors by calling the `error` method on the
`observer`. The argument provided to the call of `error` should contain two
properties:

  1. `level` must be a string, one of: `info`, `warning`, or `error`
  2. `message` must be any string and should contain more descriptive information about the state



    import { DataSource } from '@splunk/datasources';

    class MyDataSource extends DataSource {
        request(requestParams = {}) {
            return (observer) => {
                observer.error({
                    level: 'error',
                    message: 'help!!',
                });

                return () => {
                    // do nothing
                };
            };
        }
    }

### Request parameters

Request parameters define how data is formatted for the client. A
`requestParams` object usually contains following parameters:

#### count

The maximum number of results to return.

#### offset

The first result (inclusive) from which to begin returning data. This value is
0-indexed.

Use `offset` and `count` together to implement result pagination.

#### sort

Sorting of the results, expressed as an object.

For example, sort the field `_time` in descending order:



    {
        "sort": {
            "_time": "desc"
        }
    }

#### requireTotalCount

True if `totalCount` has to be returned as part of `meta`. This is often
required in table and events viewer visualizations.

## Data source definition defaults

Dashboard definition can contain default values for data sources' `options`
field. There are different levels of granularity:

  * Global defaults: these defaults will apply to all data sources
  * Data source type defaults: these defaults will apply to a specific type of data source

If both data source type defaults and global defaults present, data source
type defaults overrides global defaults.

Here's an example:



    const definition = {
        defaults: {
            dataSources: {
                global: {
                    options: {
                        queryParameters: {
                            earliest: '-4h@m',
                        },
                    },
                },
                'ds.search': {
                    options: {
                        queryParameters: {
                            latest: 'now',
                        },
                    },
                },
            },
        },
        dataSources: {
            dsId2: {
                type: 'ds.search',
                options: {
                    refresh: '5s',
                    refreshType: 'delay',
                },
            },
        },
    };

    /*
    The above definition will consolidate to the following:
    {
        dsId2: {
            type: 'ds.search',
            options: {
                refresh: '5s',
                refreshType: 'delay',
                queryParameters: {
                    earliest: '-4h@m',
                    latest: 'now',
                },
            },
        },
    }
    */

## Tokens

If a data source's `options` contains tokens, the token values will be
interpreted properly based on the `tokenBinding` values.

## Data source implementation metadata

Data source implementations should also provide metadata in a static
**config** property. This instructs the editing interfaces what capabilities
are available to the end user, and how to validate the data source settings in
source mode. Data sources which do not have a static **config** property will
not be displayed in the data panel, and will not be able to be created or
edited by end users, but they will still operate as normal for pre-configured
dashboards.

Field| Type| Description
---|---|---
title| string| The name to display for the data source type, e.g. 'Ad hoc
Search'
displayDataSourceItemListByDefault| boolean| Flag to determine if data sources
of this type should be shown
canCreateDataSource| boolean| Flag to determine if users can create new data
sources of this type
dataSourceRemoveVerb| string| Word to use to describe a remove operations,
e.g. 'delete'
isDataSourceNameEditable| boolean| Flag to turn on editing of the data source
names
getDataSourceName| Function| A method to return a data source's name given its
configuration
defaultOptions| Function or Object| An object containing the default
configuration for a new data source, or a function accepting the dashboard
definition and search type that returns the same.
editorConfig| Array| Future Use: An array describing configuration for the
dynamic editor component
optionsSchema| Object| A JSONSchema configuration describing the valid
configuration of a data source. Used to validate code in source mode.

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

---

## @splunk/dashboard-extension-webpack-plugin - 3.0.1

**Package:** `dashboard-extension-webpack-plugin` | **Component:** `Overview`

# @splunk/dashboard-extension-webpack-plugin

A Webpack plugin for building Splunk dashboard extensions.

It replaces the initial `define` with a `require` so that the extension module
is executed.

Consider using the dashboard configuration file provided by `@splunk/webpack-
configs` instead of using this plugin directly.

## Install

Install the package:



    npm install --save-dev @splunk/dashboard-extension-webpack-plugin


## Usage

Import and add the plugin to your webpack configuration:



    import DashboardPlugin from '@splunk/dashboard-extension-webpack-plugin';

    {
        plugins: [new DashboardPlugin()]
    }

---

## @splunk/eslint-config - 5.0.0

**Package:** `eslint-config` | **Component:** ``

# @splunk/eslint-config

This package provides extendable ESLint configuration objects. Currently, the
following configs are available:

  * `browser` \- For code that runs in the browser.
  * `browser-prettier` \- For browser code that is formatted by [prettier](https://github.com/prettier/prettier).
  * `node` \- For node scripts.
  * `node-prettier` \- For node scripts that are automatically formatted with [prettier](https://github.com/prettier/prettier).

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install --save-dev babel-eslint@^10 eslint@^8 eslint-config-airbnb@^19 eslint-plugin-import@^2 eslint-plugin-jsx-a11y@^6 eslint-plugin-react@^7 eslint-plugin-react-hooks@^4


  2. Install the package:

         npm install --save-dev @splunk/eslint-config


ESLint requires dependencies to be installed as peer dependencies. See [this
issue on github](https://github.com/eslint/eslint/issues/3458) for more
background.

## Usage

Add the appropriate entry to your eslint configuration:



    {
        extends: "@splunk/eslint-config/browser"
    }


Or



    {
        extends: "@splunk/eslint-config/browser-prettier"
    }


Or



    {
        extends: "@splunk/eslint-config/node"
    }


Or



    {
        extends: "@splunk/eslint-config/node-prettier"
    }

---

## @splunk/moment - 0.7.0

**Package:** `moment` | **Component:** ``

# @splunk/moment

A package of [Moment](http://momentjs.com/) and [Moment
Timezone](http://momentjs.com/timezone) plugins for Splunk Enterprise
timezones, and formatting for locales with second and millisecond precision.

## Install

Install the package:



    npm install @splunk/moment


## Usage

Import moment from the Splunk UI package. This provides a Moment class with
the timezone and timezone util plugins.



    import moment from '@splunk/moment';


Create new moment instances in the server timezone and locale.



    const time1 = moment.newSplunkTime({time: 1490500800});
    const time2 = moment.newSplunkTime({time: '10/10/2017', format: 'l'});


Manipulate and query times using the [Moment](http://momentjs.com/docs/) API.



    time1.subtract(1, 'day').startOf('day';);
    const isBefore = time1.isBefore(time2);


Format Times using second or millisecond precision



    const displayValue = time1.splunkFormat('lls');


## Advanced Usage

If used in an environment without the `window.$C` properties set by
`splunkweb`, there are functions to setup and use the plugins with raw
timezone data from Splunk Enterprise.

The timezone data can be retrieved from `services/search/timeparser/tz`. _To
access this service from the client, the endpoint must be exposed in
web.conf._

For example:



    http://localhost:8000/en-US/splunkd/__raw/services/search/timeparser/tz


Set this data as the default Splunk Enterprise timezone, which can be used for
creating and manipulating times.



    const splunkTimezoneName = moment.setDefaultSplunkTimezone(zoneData);

    const time = moment.newSplunkTime({time: 1490500800}); // uses the default timezone
    const nowInTokyo = moment.tz('Asia/Tokyo').locale('ja_JP');
    const nowAtServer = nowInTokyo.clone().tz(splunkTimezoneName).locale('en_US');

---

## Splunk Design System

**Package:** `Overview` | **Component:** ``

# Page not found

The page you are trying to view does not seem to exist.

---

## @splunk/react-events-viewer - 28.1.0

**Package:** `react-events-viewer` | **Component:** `Overview`

# EventsViewer

This component provides the Events Viewer with the options to select your
display style and configuration options like pagination and number of events.

To get started with @splunk/react-events-viewer:

## Install



    npm install @splunk/react-events-viewer

Or



    yarn add @splunk/react-events-viewer

---

## @splunk/react-field-summary - 28.1.0

**Package:** `react-field-summary` | **Component:** `Overview`

# Field Summary

The Field Summary List is a component that lists out fields available from
running a query. Each field can bring up a summary panel showing its most
common values and statistics.

## Install



    npm install @splunk/react-field-summary

Or



    yarn add @splunk/react-field-summary

---

## @splunk/react-icons - 5.3.0

**Package:** `react-icons` | **Component:** `Overview`

# @splunk/react-icons

A library of various icons in React.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install react@^16 react-dom@^16 styled-components@^5

  2. Install the package:

         npm install @splunk/react-icons

## Production builds

Both `@splunk/react-icons` and React support production and development
builds. The production build removes warnings and guidance from the output. To
create a production build, set the environment variable `NODE_ENV` to
`"production"` and use the webpack
[DefinePlugin](https://webpack.js.org/plugins/define-plugin/) to inject the
variable into the code.

---

## @splunk/react-page - 8.1.0

**Package:** `react-page` | **Component:** ``

# @splunk/react-page

Loads a React component into the latest layout from the Splunk Enterprise
server, including the Splunk bar, app bar, and a footer around your page
content.

This package dynamically loads the Layout API from the correct location.

Using this package requires `splunkd` partials to be loaded on the page.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install react@^16 react-dom@^16 styled-components@^5

  2. Install the package:

         npm install @splunk/react-page

## Usage

In a basic scenario, the layout takes a React element and an optional options
object.



    import layout from '@splunk/react-page';
    import MyPage from 'pages/MyPage';

    layout(<MyPage />, { pageTitle: 'A React Page', hideFooter: true, layout: 'fixed' });

### React 18

To use the new [createRoot](https://react.dev/reference/react-
dom/client/createRoot#createroot) functionality introducted in React 18, use
the `'@splunk/react-page/18'` import instead of `@splunk/react-page`.



    import layout from '@splunk/react-page/18';
    import MyPage from 'pages/MyPage';

    layout(<MyPage />, { pageTitle: 'A React Page', hideFooter: true, layout: 'fixed' });

---

## @splunk/react-search - 7.0.1

**Package:** `react-search` | **Component:** `Overview`

# @splunk/react-search

This component provides the search bar with a time range picker and search
button. It allows the user to provide custom syntaxes for the search bar
input, but if none are provided, default SPL syntax is used.

## Install



    npm install @splunk/react-search

Or



    yarn add @splunk/react-search

---

## @splunk/react-sparkline - 0.6.3

**Package:** `react-sparkline` | **Component:** `Overview`

# @splunk/react-sparkline

A library of React sparkline chart components.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install react@^16 react-dom@^16 styled-components@^5


  2. Install the package:

         npm install @splunk/react-sparkline

---

## @splunk/react-time-range - 11.1.1

**Package:** `react-time-range` | **Component:** ``

# @splunk/react-time-range

Time range picker components and supporting utils for working with splunkweb.

## Install



    npm install @splunk/react-time-range

Or



    yarn add @splunk/react-time-range

## Base Components vs Splunkweb Components

  * The Base Components have been completely isolated from Splunkweb, so they may be ported to other systems. However, it doesn't have capabilities that require Splunkweb:
    * No support for epoch times. Only ISO is supported.
    * Relative time strings cannot be previewed.
    * Presets must be provided.
  * Splunkd components require several $C variables to be defined:
    * locale
    * splunkdPath

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `Overview`

# @splunk/react-toast-notifications

A package for creating toast notifications in a React application.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install react@^16 styled-components@^5

  2. Install the package:

         npm install @splunk/react-toast-notifications

## Usage

Only import these **once**. See Usage for details.



    import ToastMessages from '@splunk/react-toast-notifications/ToastMessages';
    import Toaster, { makeCreateToast } from '@splunk/react-toast-notifications/Toaster';


    import { TOAST_TYPES } from '@splunk/react-toast-notifications/ToastConstants';

## Production builds

Both `@splunk/react-toast-notifications` and React support production and
development builds. The production build removes warnings and guidance from
the output. To create a production build, set the environment variable
`NODE_ENV` to `"production"` and use the webpack
[DefinePlugin](https://webpack.js.org/plugins/define-plugin/) to inject the
variable into the code.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Overview`

<!-- No content extracted -->

---

## @splunk/react-visualization-utils - 2.0.0

**Package:** `react-visualization-utils` | **Component:** ``

# React Visualization Utils

Utilities for fetching, parsing, evaluating and manipulating visualization
props.

The library comes with typescript declaration file which will provide
documentation inline in development environments.

## Install



    npm install @splunk/react-visualization-utils


Or



    yarn add @splunk/react-visualization-utils

---

## @splunk/search-job - 3.1.0

**Package:** `search-job` | **Component:** ``

# @splunk/search-job

A class that simplifies creating and accessing Splunk search jobs.

## Install

Install the package:



    npm install @splunk/search-job


## Usage



    import SearchJob from '@splunk/search-job';


The API of the SearchJob class is based on
[Observables](http://reactivex.io/rxjs/manual/overview.html#introduction).
Each method returns an Observable that can be subscribed to and will emit data
over the lifecycle of the search job. A few examples are provided here.

### Create a Simple SearchJob



    const mySearchJob = SearchJob.create({
        search: 'index=_internal | head 10',
        earliest_time: '-60m@m',
        latest_time: 'now',
    });


### Create a SearchJob in a Specific Context



    const mySearchJob = SearchJob.create({
        search: 'index=_internal | head 10',
        earliest_time: '-60m@m',
        latest_time: 'now',
    }, {
        app: 'awesome_app',
        owner: 'admin',
    });


### Create a SearchJob from a Saved Search



    const mySearchJob = SearchJob.fromSavedSearch({
        name: 'My Saved Search',
        app: 'search',
        owner: 'admin',
    });


### Get Search Progress



    const progressSubscription = mySearchJob.getProgress().subscribe(searchState => {
        // Do something with the searchState.
    });

    // Later, if the search is no longer needed, and is not complete,
    // unsubscribe to release resources.
    progressSubscription.unsubscribe();


### Get Search Results

Search results will only emit when the search is complete. See
`getResultsPreview` to get a preview of results before the search is complete.



    const resultsSubscription = mySearchJob.getResults().subscribe(results => {
        // Do something with the results.
    });

    // Later, if the results are no longer needed, and the search is not complete,
    // unsubscribe to release resources.
    resultsSubscription.unsubscribe();


### Errors and Completion

All Observables support three callbacks: `next`, `error`, and `complete`.



    const progressSubscription = mySearchJob.getProgress().subscribe({
        next: searchState => {
            // Do something with the search state.
        },
        error: err => {
            // The search failed. Do something with the err.
        },
        complete: () => {
            // The search has completed successfully.
        },
    });

---

## @splunk/splunk-utils - 3.3.0

**Package:** `splunk-utils` | **Component:** ``

# @splunk/splunk-utils

A collection of utilities for working with Splunk Enterprise.

## Install

Install the package:



    npm install @splunk/splunk-utils

---

## @splunk/stylelint-config - 5.0.0

**Package:** `stylelint-config` | **Component:** ``

# @splunk/stylelint-config

A standardized stylelint config. It's designed to work well with `styled-
components` and `prettier`, but can be used independently as well.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install --save-dev stylelint@^13


  2. Install the package:

         npm install --save-dev @splunk/stylelint-config


## Usage

Add the package to your stylelint configuration file. If you don't have one,
create `stylelint.config.js` in the root directory of your package.



    module.exports = {
        extends: '@splunk/stylelint-config'
    };

---

## Splunk Design System

**Package:** `SUIT` | **Component:** `Overview`

# Splunk UI Toolkit

Splunk UI Toolkit (SUIT) is the basic tools and components necessary for
building Splunk applications using React, Typescript and styled-components.

Splunk UI Toolkit has three major packages, plus [many others](/Packages) that
can be used to build a Splunk application:

  * [Splunk UI Design System](/DesignSystem)
  * [Splunk Dashboard Framework](/Packages/dashboard-docs)
  * [Splunk Visualizations](/Packages/visualizations)

You can quickly start developing by using [Splunk Create](/Packages/create);
see what's possible to build with SUIT in the [Examples
gallery](./ExamplesGallery); or follow the [Toolkit
tutorials](/Packages/create/TodoList) for more in-depth guidance on how to
start building a Splunk Application using SUIT.

## Contact us

If you have a question or need help, join the [splunk-usergroups Slack
workspace](https://splk.it/slack) and reach out to us in the
[#splunkui](https://splunk-usergroups.slack.com/archives/C1E110684) and
[#webplatform](https://splunk-usergroups.slack.com/archives/C01CYF27FSS)
channels.

You can also email us at
[webplatform@splunk.com](mailto:webplatform@splunk.com).

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `Overview`

# @splunk/themes

A collection of Splunk software theme variables and mixins. This package
provides functions that can be useful in React, styled-components and other
frameworks. Themes consist of plain objects containing primitives such as
strings and numbers. Functions are used for mixins.

## Install

Install the package:



    yarn add @splunk/themes

    -or-

    npm install @splunk/themes


`react@^18` and `styled-components@^5"` are required peer dependencies for all
capabilities except `getTheme()`.

## React Usage

A theme context is created at the root of the application using
`SplunkThemeProvider`.



    import SplunkThemeProvider from '@splunk/themes/SplunkThemeProvider';

    <SplunkThemeProvider family="prisma" density="compact" colorScheme="light">
         ...
    </SplunkThemeProvider>;

## Styled Components Usage

Components are themed using `pick()`, `variables`, `mixins`.



    import { pick, variables, mixins } from '@splunk/themes';
    import styled from 'styled-components';

    const Wrapper = styled.div`
        ${mixins.reset()};

        color: ${pick({
             enterprise: variables.textColor,
             prisma: variables.contentColorDefault
        })};
    `;

## Generic Usage

Theme variables are also available outside of React and styled-components.



    import getTheme from '@splunk/themes/getTheme';

    const baseTheme = getTheme({family: 'prisma', colorScheme: 'light', density: 'compact' });

    console.log(baseTheme.family, baseTheme.focusColor);

---

## @splunk/time-range-utils - 3.0.1

**Package:** `time-range-utils` | **Component:** `Overview`

# @splunk/time-range-utils

Utilities for fetching, parsing, evaluating and manipulating time ranges.

## Install



    npm install @splunk/time-range-utils


Or



    yarn add @splunk/time-range-utils


## IE11 and Safari Support

The `timeParser` module relies on `window.fetch` and `window.Promise`. IE11
requires a polyfill for both. Safari 10.0 and lower require a polyfill for
fetch. Since polyfills create globals, they are not included in the
`@splunk/time-range-utils` package. To support these browsers, ensure
polyfills, such as `whatwg-fetch` and `promise-polyfill`, are included as a
part of your build.

The `time` module does not use `window.fetch` or `window.Promise`.

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** ``

# @splunk/ui-utils

A library of common UI utilities.

## Install



    npm install @splunk/ui-utils

## Usage

Individual functions can be imported from several named modules.

Boolean example:



    import { normalizeBoolean } from '@splunk/ui-utils/boolean';

Cookie example:



    import { getEntry } from '@splunk/ui-utils/cookie';

Filter example:



    import { filterByKeywords } from '@splunk/ui-utils/filter';

Focus example:



    import { takeFocus } from '@splunk/ui-utils/focus';

Format example:



    import { smartTrim } from '@splunk/ui-utils/format';

Id example:



    import { createDOMID } from '@splunk/ui-utils/id';

Internationalization example:



    import { _ } from '@splunk/ui-utils/i18n';

Keyboard example:



    import { isNumber } from '@splunk/ui-utils/keyboard';

Math example:



    import { strictParseFloat } from '@splunk/ui-utils/math';

Scroll example:



    import { scrollIntoViewIfNeeded } from '@splunk/ui-utils/scroll';

Style example:



    import { toClassName } from '@splunk/ui-utils/style';

User Agent example:



    import { isIE11 } from '@splunk/ui-utils/userAgent';

---

## Splunk Design System

**Package:** `unknown` | **Component:** ``

# Page not found

The page you are trying to view does not seem to exist.

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** ``

## @splunk/visualizations

A visualization is a React component that you can use in an application like
Dashboard Studio, add to a custom application using Splunk UI and Unified
Dashboard Framework (UDF), or include as a chart in a web page. Because the
components are packaged in a library, you can use them in search, dashboards,
and many other applications across the Splunk product line. A visualization
provides a graphical representation of what can occasionally be complex data,
and lets you see the data in a meaningful and structured way. It also helps
you to understand the data and provides support for data-driven decision
making.

The visualizations library consists of React components built on top of
Highcharts and D3.js. If you’re familiar with these libraries, you can build
on that knowledge and add tooltips, legends, and data series to a chart. You
can choose from more than 20 different visualizations that show data in a
variety of formats. If you would like to use Splunk visualizations in your
applications, read on to learn more.

Documentation for the Splunk Visualizations library can be found at
[@splunk/visualizations](https://splunkui.splunk.com/Packages/visualizations).

## Install

Install @splunk/visualizations

  1. Install peer dependencies

         npm install react@^18 react-dom@^18 styled-components@5 @splunk/visualization-context --save

  2. Install the visualizations package

         npm install @splunk/visualizations

## Using the Components

In your dashboard presets:



    import SingleValue from '@splunk/visualizations/SingleValue';
    import SingleValueIcon from '@splunk/visualizations/SingleValueIcon';
    import ChoroplethSvg from '@splunk/visualizations/ChoroplethSvg';

    export default {
        visualizations: {
            'splunk.singlevalue': SingleValue,
            'splunk.singlevalueicon': SingleValueIcon,
            'splunk.choropleth.svg': ChoroplethSvg,
        },
    };

Outside of a dashboard:



    import Line from '@splunk/visualizations/Line';

    const MyAppWithSplunkLineChart = props => {
        const { dataSource } = props; // see API page for dataSource shape
        return <Line width={600} height={400} dataSources={{ primary: dataSource }} />;
    };

## Get started with visualizations

You can use UDF to create dashboards with visualizations, or you can work
directly with the visualizations library. If you're not familiar with UDF, it
is a unified library of UI components that render a dashboard for developers
who write JavaScript, and is well suited for Splunk Enterprise and Splunk
Cloud Platform apps. For developers, UDF offers:

  * two distinct layout systems, as well as custom layout
  * search lifecycle management
  * inputs for text entry, dropdown, multiselect, timerange, and numbers
  * Splunk visualizations to enhance data presentation
  * tokens to pass runtime values within a dashboard

To install the UDF library, see the setup guide in the [Quick
Start](https://splunkui.splunk.com/Packages/dashboard-
docs/?path=%2FQuickStart). When you have it installed, follow the quick start
to install dependencies and learn about using the libraries.

You can also include visualizations in single page apps by using
visualizations directly. To use visualizations directly, follow the [Splunk UI
tutorials](https://splunkui.splunk.com/Create/Overview) to create a component
and a simple app. The tutorials will create the app structure for other
development.

Install the visualizations libraries and dependencies listed in the
[Visualizations docs](https://splunkui.splunk.com/Packages/visualizations).
Some of the packages may have been installed with the Splunk UI setup.

## Customize a visualization

A React visualization is reusable bits of code that you can use in an app or
dashboard. Each visualization component's documentation includes the
following:

  * Overview and commonly used configurations
  * Examples of how to use various options
  * Options available and their respective types and defaults
  * Events available and their respective payloads

**Examples** depict a visualization as it will appear in an app or dashboard.
When you click on **Show Code** , the UI displays the React component code.

**Options** provide an extensive set of builtin properties that you configure.
In React, properties are referred to as props. You can set props
programmatically, or use an app to set them. For every visualization, there is
a description and a type. In some cases, a prop value is selected from a set
of values or an enumeration. In other cases, the author specifies the value of
a prop. By setting props, you can change fonts, colors, data sources, or
opacity of colors in a chart. Default values exist for most components so you
can also leave a prop as is.

**Events** offer a mechanism to capture user activity on a chart. Activities
can include point clicks on a chart or legend, range selection on a chart, as
well as events like holding the pointer over a point or moving the pointer
away. Each platform visualization has a tab for events that lists the events
available for the chart. When an event occurs, such as a point click, the
click event captures the data. You can use the data to drill down further by
using the data points. For more information, see the [Interaction
Guide](https://splunkui.splunk.com/Packages/visualizations/?path=%2FInteractionGuide).

Dynamic options syntax (DOS), also referred to as DSL in the docs, exposes
even more functionality in charts. A chart that presents text or background
display according to a threshold value makes a data presentation more
impactful. Dynamic options are a domain-specific language to bind data to
options and make data presentation more reflective of changes. The dynamic
options syntax consists of data sources, selector functions, and formatters.
In the dynamic options syntax, the categories can be combined to create a
pipeline. The pipeline begins with a data source, then includes selector
functions to extract the data of interest, and formatters to transform and map
the data. For more information about dynamic options syntax, see
[DSL](https://splunkui.splunk.com/Packages/visualizations/?path=%2FDSL).

---

## @splunk/webpack-configs - 7.0.2

**Package:** `webpack-configs` | **Component:** ``

# @splunk/webpack-configs

Standardized webpack configuration files for apps and components.

## Install

Install the package and its dependencies.

  1. Install the peer dependencies:

         npm install --save-dev @babel/core@^7 babel-loader@^8 webpack@^4


  2. Install the package:

         npm install --save-dev @splunk/webpack-configs


## Usage

### Base Configuration



    const webpackMerge = require('webpack-merge');
    const baseConfig = require('@splunk/webpack-configs').default;

    module.exports = webpackMerge(baseConfig, {
        entry: {...},
        output: {...},
    });


### Component Library

A configuration for building a library of shareable components.



    const webpackMerge = require('webpack-merge');
    const baseComponentConfig = require('@splunk/webpack-configs/component.config').default;

    module.exports = webpackMerge(baseComponentConfig, {
    entry: {...},
    output: {...},
    });


### Dashboard Extensions



    const webpackMerge = require('webpack-merge');
    const baseDashboardConfig = require('@splunk/webpack-configs/dashboard.config').default;

    module.exports = webpackMerge(baseDashboardConfig, {
        entry: {...},
        output: {...},
    });


`@splunk/dashboard-extension-webpack-plugin` must be added as a dev dependency
if this configuration is used.

### Options

All configurations export a `create` function that accepts the following
options:

  * `babelTypescript` \- Includes `.ts` and `.tsx` files in the `babel-loader` configuration used by all configurations. Defaults to `true`.



    const webpackMerge = require('webpack-merge');
    const createBaseConfig = require('@splunk/webpack-configs').create;

    module.exports = webpackMerge(createBaseConfig({ babelTypescript: false }), {
        entry: {...},
        output: {...},
    });

---

# React UI Components {#react-components}

*Individual React UI components with APIs, props, and usage examples.*

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `ChangeLog`

<!-- No content extracted -->

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Checkbox`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf(true, false, 'indeterminate')
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no

### Checkbox API

#### Props

checked

Setting this value makes the component controlled. If set, the onChange callback is required. A setting of "indeterminate" is considered unchecked for the purposes of form submission.

PropType:| oneOf(true, false, 'indeterminate')
---|---
Required:| no

children

The content to display inside the checkbox label.

PropType:| node
---|---
Required:| no

defaultChecked

Set this property instead of checked to make the component uncontrolled.

PropType:| bool
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Mark the component as having an error.

PropType:| bool
---|---
Required:| no

inert

PropType:| bool
---|---
Required:| no

inputRef

A React ref which is set to the input element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

Fires when the checked state changes.

PropType:| func
---|---
Required:| no

value

Returned by the onChange handler and submitted during form submission if the checkbox is checked. This defaults to "on" if the input is checked.

Required:| no
---|---

#### Props

checked

Setting this value makes the component controlled. If set, the onChange callback is required. A setting of "indeterminate" is considered unchecked for the purposes of form submission.

PropType:| oneOf(true, false, 'indeterminate')
---|---
Required:| no

children

The content to display inside the checkbox label.

PropType:| node
---|---
Required:| no

defaultChecked

Set this property instead of checked to make the component uncontrolled.

PropType:| bool
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Mark the component as having an error.

PropType:| bool
---|---
Required:| no

inert

PropType:| bool
---|---
Required:| no

inputRef

A React ref which is set to the input element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

Fires when the checked state changes.

PropType:| func
---|---
Required:| no

value

Returned by the onChange handler and submitted during form submission if the checkbox is checked. This defaults to "on" if the input is checked.

Required:| no
---|---

## Test Hooks

#### Element Selectors

checkbox

The root of the `Checkbox`.

Example:| [data-test="checkbox"]
---|---
Attribute:| data-test
Value:| checkbox
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

toggle

Matches the toggle of the checkbox.

Example:| [data-test="checkbox"] [data-test="toggle"]
---|---
Attribute:| data-test
Value:| toggle
Scope Describes where to look for the element.:| In the `Checkbox` root.

label

Matches the label of the checkbox.

Example:| [data-test="checkbox"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| Unique within `Checkbox`.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Chip`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf('info', 'success', 'warning', 'error', 'outline')
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| yes
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| any
---|---
Required:| no

### Chip API

#### Props

appearance

Sets the severity or type of this `Chip`. Setting this prop causes the `backgroundColor` prop to be ignored.

PropType:| oneOf('info', 'success', 'warning', 'error', 'outline')
---|---
Required:| no

backgroundColor

Changes the background color of the `Chip`. Hexadecimal colors and valid color names are allowed, such as `#ffffff` or `white`. If the `appearance` prop is set, this prop is ignored.

PropType:| string
---|---
Required:| no

children

PropType:| node
---|---
Required:| yes

disabled

Disables the `Chip`.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

foregroundColor

Changes the text and icon color of the `Chip`. Hexadecimal colors and valid color names are allowed, such as `#ffffff` or `white`.

PropType:| string
---|---
Required:| no

icon

The icon to show before the label. See the Icon component for more information.

PropType:| node
---|---
Required:| no

onRequestRemove

Includes a remove button if callback is set.

PropType:| func
---|---
Required:| no

value

Includes this value in `onRequestRemove` callbacks.

PropType:| any
---|---
Required:| no

#### Props

appearance

Sets the severity or type of this `Chip`. Setting this prop causes the `backgroundColor` prop to be ignored.

PropType:| oneOf('info', 'success', 'warning', 'error', 'outline')
---|---
Required:| no

backgroundColor

Changes the background color of the `Chip`. Hexadecimal colors and valid color names are allowed, such as `#ffffff` or `white`. If the `appearance` prop is set, this prop is ignored.

PropType:| string
---|---
Required:| no

children

PropType:| node
---|---
Required:| yes

disabled

Disables the `Chip`.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

foregroundColor

Changes the text and icon color of the `Chip`. Hexadecimal colors and valid color names are allowed, such as `#ffffff` or `white`.

PropType:| string
---|---
Required:| no

icon

The icon to show before the label. See the Icon component for more information.

PropType:| node
---|---
Required:| no

onRequestRemove

Includes a remove button if callback is set.

PropType:| func
---|---
Required:| no

value

Includes this value in `onRequestRemove` callbacks.

PropType:| any
---|---
Required:| no

## Test Hooks

#### Element Selectors

chip

The root of the `Chip`.

Example:| [data-test="chip"]
---|---
Attribute:| data-test
Value:| chip
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

label

Example:| [data-test="chip"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| In the `Chip` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Color`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| array
---|---
Default:| defaultPalette
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no

### Color API

#### Props

append

Append removes border from the right side.

PropType:| bool
---|---
Required:| no

defaultValue

Set this property instead of value to make value uncontrolled.

PropType:| string
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Add a disabled attribute and prevent clicking.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Add an error attribute.

PropType:| bool
---|---
Required:| no

hideInput

Set this property to hide the hex value text input in the initial appearance. The input will still appear inside the dropdown when opened.

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

A callback that receives the value of a newly selected color.

PropType:| func
---|---
Required:| no

palette

An array of optional color swatch values (hexadecimal or 'transparent'). The 'transparent' option should only be put at the start or end of the palette.

PropType:| array
---|---
Default:| defaultPalette
Required:| no

prepend

This has no effect on the appearance at this time but is recommended to be used when a control is joined to the left. Styles may change in the future.

PropType:| bool
---|---
Required:| no

value

The value of the color (hexadecimal or 'transparent'). Setting this value makes the property controlled. An `onChange` callback is required.

PropType:| string
---|---
Required:| no

#### Props

append

Append removes border from the right side.

PropType:| bool
---|---
Required:| no

defaultValue

Set this property instead of value to make value uncontrolled.

PropType:| string
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Add a disabled attribute and prevent clicking.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Add an error attribute.

PropType:| bool
---|---
Required:| no

hideInput

Set this property to hide the hex value text input in the initial appearance. The input will still appear inside the dropdown when opened.

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

A callback that receives the value of a newly selected color.

PropType:| func
---|---
Required:| no

palette

An array of optional color swatch values (hexadecimal or 'transparent'). The 'transparent' option should only be put at the start or end of the palette.

PropType:| array
---|---
Default:| defaultPalette
Required:| no

prepend

This has no effect on the appearance at this time but is recommended to be used when a control is joined to the left. Styles may change in the future.

PropType:| bool
---|---
Required:| no

value

The value of the color (hexadecimal or 'transparent'). Setting this value makes the property controlled. An `onChange` callback is required.

PropType:| string
---|---
Required:| no

## Test Hooks

#### Element Selectors

color

The root of the `Color`.

Example:| [data-test="color"]
---|---
Attribute:| data-test
Value:| color
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

swatch (toggle)

Matches the toggle swatch.

Example:| [data-test="color"] [data-test="toggle-swatch"]
---|---
Attribute:| data-test
Value:| toggle-swatch
Scope Describes where to look for the element.:| In the `Color` root.

swatch (generic)

Matches all color swatches in the popover palette.

Example:| #${popoverId} [data-test="swatch"]
---|---
Attribute:| data-test
Value:| swatch
Scope Describes where to look for the element.:| In the `Color` popover palette.

swatch (specific)

Matches a particular swatch by its value.

Example:| #${popoverId} [data-test="swatch"][data-test-value="target-option"]
---|---
Attribute:| data-test-value
Value:| One of the color values set in the `palette` prop.
Scope Describes where to look for the element.:| In the `Color` popover palette.

textbox

The textbox in the popover palette.

Example:| #${popoverId} [data-test="textbox"]
---|---
Attribute:| data-test
Value:| textbox
Scope Describes where to look for the element.:| In the `Color` popover palette.

textbox-swatch

Displays the color entered in the text box and can be clicked to submit that color.

Example:| #${popoverId} [data-test="textbox-swatch"]
---|---
Attribute:| data-test
Value:| textbox-swatch
Scope Describes where to look for the element.:| In the `Color` popover palette.

tool-bar

Matches the toolbar of swatches in the popover palette.

Example:| #${popoverId} [data-test="tool-bar"]
---|---
Attribute:| data-test
Value:| tool-bar
Scope Describes where to look for the element.:| In the `Color` popover palette.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `DefinitionList`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| oneOf('fixed', 'auto', 'stacked')
---|---
Default:| 'fixed'
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Default:| '120px'
Required:| no
PropType:| node
---|---
Required:| yes
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| yes
PropType:| oneOfType(func, object)
---|---
Required:| no

### DefinitionList API

#### Props

children

PropType:| node
---|---
Required:| no

descriptionWidth

Defines the width of the `Description`. Can be set to a specific pixel or string value. If not specified, will fill to take up available space. This prop is ignored when `layout="stacked"`.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

layout

Sets the layout style for the definition list.

  * `fixed`: The `Term` uses a fixed width. The `Description` fills remaining available space.
  * `auto`: Both `Term` and `Description` size proportionally based on their container, taking an equal portion of available space.
  * `stacked`: `Term` is displayed above the `Description`. Custom `termWidth` and `descriptionWidth` are ignored. Both `Term` and `Description` size proportionally.



`fixed` layout is the current default. In the next major version, this prop will default to `auto`.

PropType:| oneOf('fixed', 'auto', 'stacked')
---|---
Default:| 'fixed'
Required:| no

separatorCharacter

Sets the character used to separate key-value pair. Only supported in `layout="fixed"` and `layout="auto"`. Will not be rendered in `layout="stacked"`.

PropType:| string
---|---
Required:| no

termWidth

Defines the width of the `Term`. Can be set to a specific pixel or string value. The default value is ignored when `layout="auto"`. This prop is ignored when `layout="stacked"`.

PropType:| string
---|---
Default:| '120px'
Required:| no

#### Props

children

PropType:| node
---|---
Required:| no

descriptionWidth

Defines the width of the `Description`. Can be set to a specific pixel or string value. If not specified, will fill to take up available space. This prop is ignored when `layout="stacked"`.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

layout

Sets the layout style for the definition list.

  * `fixed`: The `Term` uses a fixed width. The `Description` fills remaining available space.
  * `auto`: Both `Term` and `Description` size proportionally based on their container, taking an equal portion of available space.
  * `stacked`: `Term` is displayed above the `Description`. Custom `termWidth` and `descriptionWidth` are ignored. Both `Term` and `Description` size proportionally.



`fixed` layout is the current default. In the next major version, this prop will default to `auto`.

PropType:| oneOf('fixed', 'auto', 'stacked')
---|---
Default:| 'fixed'
Required:| no

separatorCharacter

Sets the character used to separate key-value pair. Only supported in `layout="fixed"` and `layout="auto"`. Will not be rendered in `layout="stacked"`.

PropType:| string
---|---
Required:| no

termWidth

Defines the width of the `Term`. Can be set to a specific pixel or string value. The default value is ignored when `layout="auto"`. This prop is ignored when `layout="stacked"`.

PropType:| string
---|---
Default:| '120px'
Required:| no

### DefinitionList.Term API

Container component for a `DefinitionList` term.

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

### DefinitionList.Description API

Container component for a `DefinitionList` description.

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

## Test Hooks

#### Element Selectors

definition-list

The root of the `DefinitionList`.

Example:| [data-test="definition-list"]
---|---
Attribute:| data-test
Value:| definition-list
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

description

The description of the `DefinitionList`.

Example:| [data-test="definition-list"] [data-test="description"]
---|---
Attribute:| data-test
Value:| description
Scope Describes where to look for the element.:| definition-list

term

The term of the `DefinitionList`.

Example:| [data-test="definition-list"] [data-test="term"]
---|---
Attribute:| data-test
Value:| term
Scope Describes where to look for the element.:| definition-list

## Accessibility

Card Layout provides a container to responsively arrange and resize Cards.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Divider`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf('default', 'weak', 'strong')
---|---
Default:| 'default'
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| oneOf('horizontal', 'vertical')
---|---
Default:| 'horizontal'
Required:| no

### Divider API

#### Props

appearance

Changes the border color of the `Divider`. `Divider`s with `appearance="weak"` will not meet accessibility requirements to be perceivable. If the component should be perceivable, consider the other contrast compliant `appearance` values. Otherwise, apply the `decorative` prop.

PropType:| oneOf('default', 'weak', 'strong')
---|---
Default:| 'default'
Required:| no

decorative

Remove semantics of the divider.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

orientation

Sets the orientation of this `Divider`.

PropType:| oneOf('horizontal', 'vertical')
---|---
Default:| 'horizontal'
Required:| no

#### Props

appearance

Changes the border color of the `Divider`. `Divider`s with `appearance="weak"` will not meet accessibility requirements to be perceivable. If the component should be perceivable, consider the other contrast compliant `appearance` values. Otherwise, apply the `decorative` prop.

PropType:| oneOf('default', 'weak', 'strong')
---|---
Default:| 'default'
Required:| no

decorative

Remove semantics of the divider.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

orientation

Sets the orientation of this `Divider`.

PropType:| oneOf('horizontal', 'vertical')
---|---
Default:| 'horizontal'
Required:| no

## Test Hooks

#### Element Selectors

divider

The divider.

Example:| [data-test="divider"]
---|---
Attribute:| data-test
Value:| divider
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Dropdown`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| bool
---|---
Default:| true
Required:| no
PropType:| oneOfType(node, func)
---|---
Required:| no
PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no
PropType:| oneOf('above', 'below', 'left', 'right', 'vertical', 'horizontal')
---|---
Default:| 'below'
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'tabKey', 'toggleClick', ]
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| element
---|---
Required:| yes

### Dropdown API

#### Props

canCoverAnchor

Enables the `Dropdown` to be rendered over the toggle if there isn't enough room to render it in a direction.

PropType:| bool
---|---
Default:| true
Required:| no

children

The content of the `Dropdown`. If a function is provided, it is invoked with an object containing `anchorHeight`, `anchorWidth`, `maxHeight`, `maxWidth`, and `placement`, and is expected to return renderable content.

PropType:| oneOfType(node, func)
---|---
Required:| no

closeReasons

An array of reasons for which this `Dropdown` closes.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no

defaultPlacement

The default placement of the `Dropdown`. It might be rendered in a different direction depending on the space available and the `repositionMode`.

PropType:| oneOf('above', 'below', 'left', 'right', 'vertical', 'horizontal')
---|---
Default:| 'below'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusToggleReasons

An array of reasons for which to set focus on the toggle. Only the subset of `closeReasons` is honored. When `Menu.Items` open a Modal or other dialog, it might be necessary to remove the 'contentClick' reason to allow focus to be passed to the dialog.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'tabKey', 'toggleClick', ]
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

onRequestClose

A callback function invoked with a data object containing the event, if applicable, and a reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

A callback function invoked with a data object containing the event.

PropType:| func
---|---
Required:| no

open

If an open prop is provided, this component behaves as a controlled component(Opens new window). The consumer is responsible for handling the open/close state. If no open prop is provided, the component handles the open/close state internally.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no

retainFocus

Keeps focus within the Popover while open. Only use this for inputs used in a form control. Do not use this when the Dropdown contains a Menu because Menu handles its own focus.

PropType:| bool
---|---
Default:| false
Required:| no

takeFocus

When true, the Popover automatically takes focus when 'open' changes to `true`. Disable this for a Popover that has shows on hover, such as a tooltip.

PropType:| bool
---|---
Default:| true
Required:| no

toggle

A toggle, such as a button or equivalent component that accepts `ref`, must be passed. `aria-haspopup`, `aria-expanded`, and `aria-controls` attributes are applied to the toggle to support accessibility. The result of the `ref` placed on the toggle must be an instance of `HTMLElement`. Results that are instances of class components are not supported. Also see "Forwarding Refs"(Opens new window).

PropType:| element
---|---
Required:| yes

#### Props

canCoverAnchor

Enables the `Dropdown` to be rendered over the toggle if there isn't enough room to render it in a direction.

PropType:| bool
---|---
Default:| true
Required:| no

children

The content of the `Dropdown`. If a function is provided, it is invoked with an object containing `anchorHeight`, `anchorWidth`, `maxHeight`, `maxWidth`, and `placement`, and is expected to return renderable content.

PropType:| oneOfType(node, func)
---|---
Required:| no

closeReasons

An array of reasons for which this `Dropdown` closes.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no

defaultPlacement

The default placement of the `Dropdown`. It might be rendered in a different direction depending on the space available and the `repositionMode`.

PropType:| oneOf('above', 'below', 'left', 'right', 'vertical', 'horizontal')
---|---
Default:| 'below'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusToggleReasons

An array of reasons for which to set focus on the toggle. Only the subset of `closeReasons` is honored. When `Menu.Items` open a Modal or other dialog, it might be necessary to remove the 'contentClick' reason to allow focus to be passed to the dialog.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'tabKey', 'toggleClick', ]
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

onRequestClose

A callback function invoked with a data object containing the event, if applicable, and a reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

A callback function invoked with a data object containing the event.

PropType:| func
---|---
Required:| no

open

If an open prop is provided, this component behaves as a controlled component(Opens new window). The consumer is responsible for handling the open/close state. If no open prop is provided, the component handles the open/close state internally.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no

retainFocus

Keeps focus within the Popover while open. Only use this for inputs used in a form control. Do not use this when the Dropdown contains a Menu because Menu handles its own focus.

PropType:| bool
---|---
Default:| false
Required:| no

takeFocus

When true, the Popover automatically takes focus when 'open' changes to `true`. Disable this for a Popover that has shows on hover, such as a tooltip.

PropType:| bool
---|---
Default:| true
Required:| no

toggle

A toggle, such as a button or equivalent component that accepts `ref`, must be passed. `aria-haspopup`, `aria-expanded`, and `aria-controls` attributes are applied to the toggle to support accessibility. The result of the `ref` placed on the toggle must be an instance of `HTMLElement`. Results that are instances of class components are not supported. Also see "Forwarding Refs"(Opens new window).

PropType:| element
---|---
Required:| yes

## Test Hooks

#### Element Selectors

dropdown

The root of the `Dropdown`.

Example:| [data-test="dropdown"]
---|---
Attribute:| data-test
Value:| dropdown
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `DualListbox`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| arrayOf(shape({name: string, label: string}))
---|---
Required:| yes
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no

### DualListbox API

#### Props

children

All children must be instances of `DualListbox.Option`.

PropType:| node
---|---
Required:| no

controlled

When true, `Options`'s `listName` and `selected` state props are fully controlled.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

fill

When true, fill height and width of the relative parent container.

PropType:| bool
---|---
Default:| false
Required:| no

inline

When false, display as inline-block with the default width. Ignored if `fill=true` set.

PropType:| bool
---|---
Default:| false
Required:| no

lists

List identifiers. `name` should map to child `Option`s `listName` prop, and will be returned with event calls. `label` will be used for visual and assistive text.

PropType:| arrayOf(shape({name: string, label: string}))
---|---
Required:| yes

onChange

Callback for selected options moving from one list to another.

PropType:| func
---|---
Required:| no

onSelect

Callback for single selected/de-select actions.

PropType:| func
---|---
Required:| no

#### Props

children

All children must be instances of `DualListbox.Option`.

PropType:| node
---|---
Required:| no

controlled

When true, `Options`'s `listName` and `selected` state props are fully controlled.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

fill

When true, fill height and width of the relative parent container.

PropType:| bool
---|---
Default:| false
Required:| no

inline

When false, display as inline-block with the default width. Ignored if `fill=true` set.

PropType:| bool
---|---
Default:| false
Required:| no

lists

List identifiers. `name` should map to child `Option`s `listName` prop, and will be returned with event calls. `label` will be used for visual and assistive text.

PropType:| arrayOf(shape({name: string, label: string}))
---|---
Required:| yes

onChange

Callback for selected options moving from one list to another.

PropType:| func
---|---
Required:| no

onSelect

Callback for single selected/de-select actions.

PropType:| func
---|---
Required:| no

## Test Hooks

#### Element Selectors

dual-listbox

The root of the `DualListbox`.

Example:| [data-test="dual-listbox"]
---|---
Attribute:| data-test
Value:| dual-listbox
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

listbox

Matches all `Listbox`s in the `DualListbox`.

Example:| [data-test="dual-listbox"] [data-test="listbox"]
---|---
Attribute:| data-test
Value:| listbox
Scope Describes where to look for the element.:| In the `DualListbox` root.

option

Matches all `Options`s in the `Listbox`.

Example:| [data-test="dual-listbox"] [data-test="listbox"] [data-test="option"]
---|---
Attribute:| data-test
Value:| option
Scope Describes where to look for the element.:| In the `Listbox` root.

move-to-primary-button

The move to primary (left) listbox button.

Example:| [data-test="dual-listbox"] [data-test="move-to-primary"]
---|---
Attribute:| data-test
Value:| move-to-primary
Scope Describes where to look for the element.:| In the `DualListbox` root.

move-to-secondary-button

The move to secondary (right) listbox button.

Example:| [data-test="dual-listbox"] [data-test="move-to-secondary"]
---|---
Attribute:| data-test
Value:| move-to-secondary
Scope Describes where to look for the element.:| In the `DualListbox` root.

select-all

Matches all select-all `Switch`s in the `DualListbox`.

Example:| [data-test="dual-listbox"] [data-test="select-all"] [data-test="button"]
---|---
Attribute:| data-test
Value:| button
Scope Describes where to look for the element.:| In the associated list.

## Accessibility

Card Layout provides a container to responsively arrange and resize Cards.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `File`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| any
---|---
Required:| no
PropType:| string
---|---
Required:| yes
PropType:| number
---|---
Required:| no

### File API

File provides the ability to accept files and present uploaded files. It does not provide file readers, only a reference to the file. This can be used to post binary content, or upload using an array buffer.

#### Props

accept

The accept attribute for the file browser. This does not filter dropped items, which must be filtered manually. File will create a default "supports" message based on this value.

PropType:| string
---|---
Required:| no

allowMultiple

Allow the user to upload multiple files.

PropType:| bool
---|---
Required:| no

children

PropType:| node
---|---
Required:| no

disabled

Prevents user from dropping files.

PropType:| bool
---|---
Required:| no

dropAnywhere

File can be dropped anywhere on the page.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the component in an error state. This has no effect on the full-screen File. Note: File.Item has a separate error property.

PropType:| bool
---|---
Required:| no

fullscreen

There can only be one File component on the page as it will take all files dropped on the page.

PropType:| bool
---|---
Required:| no

help

Show help text.

PropType:| node
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

name

The name is returned with onRequestAdd and onRequestRemove events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onRequestAdd

A callback for when the user selects one or more files. The function is passed a file reference, which can then be used to read the file. This may be used to enforce file constraints or upload the file.

PropType:| func
---|---
Required:| no

onRequestRemove

A callback for when the user requests to remove a file. The function is passed the event and an object with the Item's index and name: `(event, {index, name})`.

PropType:| func
---|---
Required:| no

onRequestRetry

A callback for when the user requests to retry the upload after upload resulted in error. The function is passed the event and an object with the Item's index and name: `(event, {index, name})`.

PropType:| func
---|---
Required:| no

supportsMessage

PropType:| node
---|---
Required:| no

#### Props

accept

The accept attribute for the file browser. This does not filter dropped items, which must be filtered manually. File will create a default "supports" message based on this value.

PropType:| string
---|---
Required:| no

allowMultiple

Allow the user to upload multiple files.

PropType:| bool
---|---
Required:| no

children

PropType:| node
---|---
Required:| no

disabled

Prevents user from dropping files.

PropType:| bool
---|---
Required:| no

dropAnywhere

File can be dropped anywhere on the page.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the component in an error state. This has no effect on the full-screen File. Note: File.Item has a separate error property.

PropType:| bool
---|---
Required:| no

fullscreen

There can only be one File component on the page as it will take all files dropped on the page.

PropType:| bool
---|---
Required:| no

help

Show help text.

PropType:| node
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

name

The name is returned with onRequestAdd and onRequestRemove events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onRequestAdd

A callback for when the user selects one or more files. The function is passed a file reference, which can then be used to read the file. This may be used to enforce file constraints or upload the file.

PropType:| func
---|---
Required:| no

onRequestRemove

A callback for when the user requests to remove a file. The function is passed the event and an object with the Item's index and name: `(event, {index, name})`.

PropType:| func
---|---
Required:| no

onRequestRetry

A callback for when the user requests to retry the upload after upload resulted in error. The function is passed the event and an object with the Item's index and name: `(event, {index, name})`.

PropType:| func
---|---
Required:| no

supportsMessage

PropType:| node
---|---
Required:| no

### File.Item API

#### Props

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the Item in an error state.

PropType:| bool
---|---
Default:| false
Required:| no

itemId

A unique for this file.

PropType:| any
---|---
Required:| no

name

The name is displayed on the item.

PropType:| string
---|---
Required:| yes

uploadPercentage

If the uploadPercentage is 0, the item is assumed to be queued. If the upload is complete or not applicable, uploadPercentage must be undefined.

PropType:| number
---|---
Required:| no

#### Props

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the Item in an error state.

PropType:| bool
---|---
Default:| false
Required:| no

itemId

A unique for this file.

PropType:| any
---|---
Required:| no

name

The name is displayed on the item.

PropType:| string
---|---
Required:| yes

uploadPercentage

If the uploadPercentage is 0, the item is assumed to be queued. If the upload is complete or not applicable, uploadPercentage must be undefined.

PropType:| number
---|---
Required:| no

## Test Hooks

#### Element Selectors

file

The root of the `File`.

Example:| [data-test="file"]
---|---
Attribute:| data-test
Value:| file
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

file-input

The file input DOM element.

Example:| [data-test="file"] [data-test="file-input"]
---|---
Attribute:| data-test
Value:| file-input
Scope Describes where to look for the element.:| In the `File` root.

label

The file label DOM element.

Example:| [data-test="file"] [data-test="file-label"]
---|---
Attribute:| data-test
Value:| file-label
Scope Describes where to look for the element.:| In the `File` root.

item (generic)

Matches all of the current `File.Item`s. To select a specific `File.Item` add a data attribute to uniquely identify it.

Example:| [data-test="file"] [data-test="item"]
---|---
Attribute:| data-test
Value:| item
Scope Describes where to look for the element.:| In the `File` root.

remove

Matches the remove button.

Example:| [data-test="file"] [data-test="specific-item"] [data-test="remove"]
---|---
Attribute:| data-test
Value:| remove
Scope Describes where to look for the element.:| In the `File.Item`.

label

Matches the label of the `File.Item`.

Example:| [data-test="file"] [data-test="specific-item"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| In the `File.Item`.

support

Matches the support element.

Example:| [data-test="file"] [data-test="file-supports"]
---|---
Attribute:| data-test
Value:| file-supports
Scope Describes where to look for the element.:| In the `File` root.

help

Matches the help element.

Example:| [data-test="file"] [data-test="help"]
---|---
Attribute:| data-test
Value:| help
Scope Describes where to look for the element.:| In the `File` root.

## Accessibility

Card Layout provides a container to responsively arrange and resize Cards.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `FormRows`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| string
---|---
Default:| _('Add row')
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| node
---|---
Required:| no

### FormRows API

#### Props

addLabel

Label on the Add row button. Ignored when menu prop is defined.

PropType:| string
---|---
Default:| _('Add row')
Required:| no

disabled

Disable the Add row button, the Remove button and the sort/drag action.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

header

Header for the rows.

PropType:| node
---|---
Required:| no

menu

Replaces Add row button with custom content or controls.

PropType:| node
---|---
Required:| no

onRequestAdd

Callback when the Add row button is clicked. If `onRequestAdd` is defined, 'onRequestRemove' should be defined in `<FormRows.Row>`. Neither should be defined for a reorder-only variant of `<FormRows>`.

PropType:| func
---|---
Required:| no

onRequestMove

Callback when sort action completes. Omit this to make rows unsortable.

PropType:| func
---|---
Required:| no

#### Props

addLabel

Label on the Add row button. Ignored when menu prop is defined.

PropType:| string
---|---
Default:| _('Add row')
Required:| no

disabled

Disable the Add row button, the Remove button and the sort/drag action.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

header

Header for the rows.

PropType:| node
---|---
Required:| no

menu

Replaces Add row button with custom content or controls.

PropType:| node
---|---
Required:| no

onRequestAdd

Callback when the Add row button is clicked. If `onRequestAdd` is defined, 'onRequestRemove' should be defined in `<FormRows.Row>`. Neither should be defined for a reorder-only variant of `<FormRows>`.

PropType:| func
---|---
Required:| no

onRequestMove

Callback when sort action completes. Omit this to make rows unsortable.

PropType:| func
---|---
Required:| no

### FormRows.Row API

#### Props

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

index

Index of the row. This is required if the rows are sortable.

PropType:| number
---|---
Required:| no

onRequestRemove

Callback when Remove button is clicked.

PropType:| func
---|---
Required:| no

value

The contents of Row

PropType:| node
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

index

Index of the row. This is required if the rows are sortable.

PropType:| number
---|---
Required:| no

onRequestRemove

Callback when Remove button is clicked.

PropType:| func
---|---
Required:| no

value

The contents of Row

PropType:| node
---|---
Required:| no

## Test Hooks

#### Element Selectors

form-rows

The root of the `FormRows`.

Example:| [data-test="form-rows"]
---|---
Attribute:| data-test
Value:| form-rows
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

add-row

Add a row to the form.

Example:| [data-test="form-rows"] [data-test="add-row"]
---|---
Attribute:| data-test
Value:| add-row
Scope Describes where to look for the element.:| In the `FormRows` root.

row (generic)

Matches all `FormRows.Row`s. To select a specific `Row`, add a `data-test` attribute to uniquely identify it.

Example:| [data-test="form-rows"] [data-test="row"]
---|---
Attribute:| data-test
Value:| row
Scope Describes where to look for the element.:| In the `FormRows` root.

remove

Removes the row from the form.

Example:| [data-test="form-rows"] [data-test="specific-row"] [data-test="remove"]
---|---
Attribute:| data-test
Value:| remove
Scope Describes where to look for the element.:| In the `FormRows.Row`.

drag-handle

Matches the drag handle for the row.

Example:| [data-test="form-rows"] [data-test="specific-row"] [data-test="drag-handle"]
---|---
Attribute:| data-test
Value:| drag-handle
Scope Describes where to look for the element.:| In the `FormRows.Row`.

`data-test`

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Image`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| arrayOf(string)
---|---
Default:| ['gif', 'jpeg', 'jpg', 'png']
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| func
---|---
Required:| no

### Image API

Image provides the ability to accept image files and present a preview of the image.

#### Props

allowExtensions

Specify the allowed image extensions. Should be an array of image extensions, e.g., ['gif', 'jpg', 'png'].

PropType:| arrayOf(string)
---|---
Default:| ['gif', 'jpeg', 'jpg', 'png']
Required:| no

defaultFilename

The default file name of the selected image. In order to render selected image preview, need to set valid defaultFilename (end with allowed image extensions, e.g., 'default.png') and defaultImageDataURI at the same time.

PropType:| string
---|---
Required:| no

defaultImageDataURI

The default selected image data (as data URI). Need to set with defaultFilename at the same time.

PropType:| string
---|---
Required:| no

disabled

Prevents user from selecting or dropping images.

PropType:| bool
---|---
Required:| no

dropAnywhere

Image can be dropped anywhere on the page.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the component in an error state.

PropType:| bool
---|---
Required:| no

onImageChange

A callback for when the image changes. The function is passed an object containing two keys: `filename` and `imageDataURI`. Both are `null` if the image was removed.

PropType:| func
---|---
Required:| no

#### Props

allowExtensions

Specify the allowed image extensions. Should be an array of image extensions, e.g., ['gif', 'jpg', 'png'].

PropType:| arrayOf(string)
---|---
Default:| ['gif', 'jpeg', 'jpg', 'png']
Required:| no

defaultFilename

The default file name of the selected image. In order to render selected image preview, need to set valid defaultFilename (end with allowed image extensions, e.g., 'default.png') and defaultImageDataURI at the same time.

PropType:| string
---|---
Required:| no

defaultImageDataURI

The default selected image data (as data URI). Need to set with defaultFilename at the same time.

PropType:| string
---|---
Required:| no

disabled

Prevents user from selecting or dropping images.

PropType:| bool
---|---
Required:| no

dropAnywhere

Image can be dropped anywhere on the page.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Show the component in an error state.

PropType:| bool
---|---
Required:| no

onImageChange

A callback for when the image changes. The function is passed an object containing two keys: `filename` and `imageDataURI`. Both are `null` if the image was removed.

PropType:| func
---|---
Required:| no

## Test Hooks

#### Element Selectors

image

The root of the `Image`.

Example:| [data-test="image"]
---|---
Attribute:| data-test
Value:| image
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

preview

Matches the preview.

Example:| [data-test="image"] [data-test="preview"]
---|---
Attribute:| data-test
Value:| preview
Scope Describes where to look for the element.:| In the `Image` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Licenses`

<!-- No content extracted -->

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Menu`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| oneOf('roving', 'normal', 'never')
---|---
Default:| 'roving'
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no
PropType:| oneOfType(bool, oneOf('dimmed', 'disabled'))
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOfType(bool, string)
---|---
Required:| no
PropType:| oneOf('menuitem', 'menuitemradio', 'menuitemcheckbox', 'listboxitem', 'option')
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('checkmark', 'checkbox')
---|---
Default:| 'checkmark'
Required:| no
PropType:| oneOfType(bool, oneOf('some'))
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| bool
---|---
Required:| no

### Menu API

#### Props

children

Must be `Menu.Item`, `Menu.Heading`, or `Menu.Divider`. Interactive elements are not supported as children.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusMode

Specifies whether the menu accept/retain focus and how the focus behaves.

  * `never`: `Menu` will never take focus, and the Menu.Item will not have a focus-like appearance.
  * `normal`: `Menu` and its children follow the normal focus order of DOM without any interference.
  * `roving`: Single tab stop. Use up/down arrow keys to navigate and loop through Menu.Items.



PropType:| oneOf('roving', 'normal', 'never')
---|---
Default:| 'roving'
Required:| no

stopScrollPropagation

Prevents scrolling from propagating to the parent containers when the top or bottom of the `Menu` is reached.

PropType:| bool
---|---
Required:| no

#### Props

children

Must be `Menu.Item`, `Menu.Heading`, or `Menu.Divider`. Interactive elements are not supported as children.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusMode

Specifies whether the menu accept/retain focus and how the focus behaves.

  * `never`: `Menu` will never take focus, and the Menu.Item will not have a focus-like appearance.
  * `normal`: `Menu` and its children follow the normal focus order of DOM without any interference.
  * `roving`: Single tab stop. Use up/down arrow keys to navigate and loop through Menu.Items.



PropType:| oneOf('roving', 'normal', 'never')
---|---
Default:| 'roving'
Required:| no

stopScrollPropagation

Prevents scrolling from propagating to the parent containers when the top or bottom of the `Menu` is reached.

PropType:| bool
---|---
Required:| no

### Menu.Item API

#### Props

active

Active shows a temporarily selected state, similar to that of focus. This is used when filtering the `Menu` items in Multiselect, Select, and ComboBox and when navigating with arrows.

PropType:| bool
---|---
Required:| no

children

Becomes the label. Must be a string if using `matchRanges`.

PropType:| node
---|---
Required:| no

description

Additional information to explain the option.

PropType:| string
---|---
Required:| no

descriptionPosition

The description text might appear to the right of the label or under the label.

PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no

disabled

Prevents user interaction and adds disabled styling. If set to `dimmed`, the component is able to be focused, and is more easily located. If set to `disabled`, the disabled attribute is set which makes the component unable to be focused and more difficult to locate. The default behavior when `disabled={true}` is `dimmed`.

PropType:| oneOfType(bool, oneOf('dimmed', 'disabled'))
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

endAdornment

Adornment after the label.

PropType:| node
---|---
Required:| no

hasSubmenu

Adds an icon to the right to show that there is a submenu. To implement submenus, use the `SlidingPanels` component.

PropType:| bool
---|---
Required:| no

matchRanges

Sections of the label string to highlight as a match.

PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no

onClick

Callback for click events.

PropType:| func
---|---
Required:| no

openInNewContext

Open the "to" link in a new context, which is usually a new tab or window based on browser settings.

An icon and a screen reader message is added to indicate this behavior to users. The default message is "(Opens new window)"; this can be customized by passing a string instead of boolean to `openInNewContext`.

PropType:| oneOfType(bool, string)
---|---
Required:| no

role

The default role is inferred from the other props. `selectable` with a `selectableAppearance` of 'checkmark' defaults to `menuitemradio`. `selectable` with a `selectableAppearance` of 'checkbox' defaults to `menuitemcheckbox`. Otherwise, the role defaults to `menuitem`.

PropType:| oneOf('menuitem', 'menuitemradio', 'menuitemcheckbox', 'listboxitem', 'option')
---|---
Required:| no

selectable

Enables selection for this item and reserves space for the control. Required when using `selected` or `selectableAppearance`.

PropType:| bool
---|---
Required:| no

selectableAppearance

Specifies the type of selection control to display when `selectable` is enabled.

PropType:| oneOf('checkmark', 'checkbox')
---|---
Default:| 'checkmark'
Required:| no

selected

Controls the selection state of the item. The selection control (checkmark or checkbox) is only rendered when `selectable` is enabled.

When `selectableAppearance = 'checkmark'`:

  * `true` shows a checkmark.



When `selectableAppearance = 'checkbox'`:

  * `true` renders a checked box.
  * `'some'` renders an indeterminate box (`aria-checked="mixed"`).
  * `false` renders an unchecked box.



PropType:| oneOfType(bool, oneOf('some'))
---|---
Required:| no

startAdornment

Adornment in front of the label.

PropType:| node
---|---
Required:| no

to

The URL or path to link to.

PropType:| string
---|---
Required:| no

truncate

When `true`, wrapping is disabled and any additional text is truncated using an ellipsis.

PropType:| bool
---|---
Required:| no

#### Props

active

Active shows a temporarily selected state, similar to that of focus. This is used when filtering the `Menu` items in Multiselect, Select, and ComboBox and when navigating with arrows.

PropType:| bool
---|---
Required:| no

children

Becomes the label. Must be a string if using `matchRanges`.

PropType:| node
---|---
Required:| no

description

Additional information to explain the option.

PropType:| string
---|---
Required:| no

descriptionPosition

The description text might appear to the right of the label or under the label.

PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no

disabled

Prevents user interaction and adds disabled styling. If set to `dimmed`, the component is able to be focused, and is more easily located. If set to `disabled`, the disabled attribute is set which makes the component unable to be focused and more difficult to locate. The default behavior when `disabled={true}` is `dimmed`.

PropType:| oneOfType(bool, oneOf('dimmed', 'disabled'))
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

endAdornment

Adornment after the label.

PropType:| node
---|---
Required:| no

hasSubmenu

Adds an icon to the right to show that there is a submenu. To implement submenus, use the `SlidingPanels` component.

PropType:| bool
---|---
Required:| no

matchRanges

Sections of the label string to highlight as a match.

PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no

onClick

Callback for click events.

PropType:| func
---|---
Required:| no

openInNewContext

Open the "to" link in a new context, which is usually a new tab or window based on browser settings.

An icon and a screen reader message is added to indicate this behavior to users. The default message is "(Opens new window)"; this can be customized by passing a string instead of boolean to `openInNewContext`.

PropType:| oneOfType(bool, string)
---|---
Required:| no

role

The default role is inferred from the other props. `selectable` with a `selectableAppearance` of 'checkmark' defaults to `menuitemradio`. `selectable` with a `selectableAppearance` of 'checkbox' defaults to `menuitemcheckbox`. Otherwise, the role defaults to `menuitem`.

PropType:| oneOf('menuitem', 'menuitemradio', 'menuitemcheckbox', 'listboxitem', 'option')
---|---
Required:| no

selectable

Enables selection for this item and reserves space for the control. Required when using `selected` or `selectableAppearance`.

PropType:| bool
---|---
Required:| no

selectableAppearance

Specifies the type of selection control to display when `selectable` is enabled.

PropType:| oneOf('checkmark', 'checkbox')
---|---
Default:| 'checkmark'
Required:| no

selected

Controls the selection state of the item. The selection control (checkmark or checkbox) is only rendered when `selectable` is enabled.

When `selectableAppearance = 'checkmark'`:

  * `true` shows a checkmark.



When `selectableAppearance = 'checkbox'`:

  * `true` renders a checked box.
  * `'some'` renders an indeterminate box (`aria-checked="mixed"`).
  * `false` renders an unchecked box.



PropType:| oneOfType(bool, oneOf('some'))
---|---
Required:| no

startAdornment

Adornment in front of the label.

PropType:| node
---|---
Required:| no

to

The URL or path to link to.

PropType:| string
---|---
Required:| no

truncate

When `true`, wrapping is disabled and any additional text is truncated using an ellipsis.

PropType:| bool
---|---
Required:| no

### Menu.Heading API

A non-interactive `Menu` item used to separate and label groups of `Menu` items.

#### Props

children

PropType:| node
---|---
Required:| no

outerStyle

PropType:| object
---|---
Required:| no

title

Renders this heading as a title to describe the whole `Menu`, which should only be enabled for the first heading in a `Menu`.

PropType:| bool
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| no

outerStyle

PropType:| object
---|---
Required:| no

title

Renders this heading as a title to describe the whole `Menu`, which should only be enabled for the first heading in a `Menu`.

PropType:| bool
---|---
Required:| no

### Menu.Divider API

A non-interactive menu item used to visually separate groups of items in the menu.

## Test Hooks

#### Element Selectors

menu

The root of the `Menu`.

Example:| [data-test="menu"]
---|---
Attribute:| data-test
Value:| menu
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

item

Matches all `Menu.Item`s in the `Menu`.

Example:| [data-test="menu"] [data-test="item"]
---|---
Attribute:| data-test
Value:| item
Scope Describes where to look for the element.:| In the `Menu` root.

match

Matches all wrappers around each piece of text matching the filter.

Example:| [data-test="menu"] [data-test="item"] [data-test="match"]
---|---
Attribute:| data-test
Value:| match
Scope Describes where to look for the element.:| In the `Menu.Item` root.

label

Matches the label of a specific `Menu.Item`. Item data-test-value should be added by developers.

Example:| [data-test="menu"] [data-test-value="target-item"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| In specific `Menu.Item` root.

description

Matches the description of a specific `Menu.Item`. Item data-test-value should be added by developers.

Example:| [data-test="menu"] [data-test-value="target-item"] [data-test="description"]
---|---
Attribute:| data-test
Value:| description
Scope Describes where to look for the element.:| In specific `Menu.Item` root.

heading

Matches all `Menu.Heading`s in the `Menu`.

Example:| [data-test="menu"] [data-test="heading"]
---|---
Attribute:| data-test
Value:| heading
Scope Describes where to look for the element.:| In the `Menu` root.

divider

Matches all `Menu.Divider`s in the `Menu`.

Example:| [data-test="menu"] [data-test="divider"]
---|---
Attribute:| data-test
Value:| divider
Scope Describes where to look for the element.:| In the `Menu` root.

selected

Matches all selected `Menu.Item` in the `Menu`.

Example:| [data-test="menu"] [data-test="item"][data-test-selected="true"]
---|---
Attribute:| data-test-selected
Value:| true
Scope Describes where to look for the element.:| In the `Menu` root.

## Accessibility

Card Layout provides a container to responsively arrange and resize Cards.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Migration`

<!-- No content extracted -->

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Monogram`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| string
---|---
Default:| 'theme'
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| yes
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOfType(oneOf('small', 'medium', 'large'), number)
---|---
Default:| 'medium'
Required:| no
Type| string
---|---
Required| Yes
Type| string
---|---

### Monogram API

@deprecated Monogram has been deprecated and will be removed in a future major version. Use Avatar instead.

#### Props

backgroundColor

All CSS color definitions are supported, such as `#223344` or `red`. If set to `auto` the background color is derived from the `initials` prop. Using `theme` enables the theme default.

PropType:| string
---|---
Default:| 'theme'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and `null` when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

initials

The contents of this `Monogram`. Must not exceed three characters in length.

PropType:| string
---|---
Required:| yes

name

The name is returned with `onClick` events, which can be used to identify the control when multiple controls share an `onClick` callback. Not to be confused with `initials`.

PropType:| string
---|---
Required:| no

onClick

Enables interactive mode.

PropType:| func
---|---
Required:| no

size

Adjusts the size of the `Monogram`.

PropType:| oneOfType(oneOf('small', 'medium', 'large'), number)
---|---
Default:| 'medium'
Required:| no

#### Props

backgroundColor

All CSS color definitions are supported, such as `#223344` or `red`. If set to `auto` the background color is derived from the `initials` prop. Using `theme` enables the theme default.

PropType:| string
---|---
Default:| 'theme'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and `null` when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

initials

The contents of this `Monogram`. Must not exceed three characters in length.

PropType:| string
---|---
Required:| yes

name

The name is returned with `onClick` events, which can be used to identify the control when multiple controls share an `onClick` callback. Not to be confused with `initials`.

PropType:| string
---|---
Required:| no

onClick

Enables interactive mode.

PropType:| func
---|---
Required:| no

size

Adjusts the size of the `Monogram`.

PropType:| oneOfType(oneOf('small', 'medium', 'large'), number)
---|---
Default:| 'medium'
Required:| no

## Test Hooks

#### Element Selectors

monogram

The root of the `Monogram`.

Example:| [data-test="monogram"]
---|---
Attribute:| data-test
Value:| monogram
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

label

Example:| [data-test="monogram"] [data-test="initials"]
---|---
Attribute:| data-test
Value:| initials
Scope Describes where to look for the element.:| In the `Monogram` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Multiselect`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('above', 'below', 'vertical')
---|---
Default:| 'vertical'
Required:| no
PropType:| array
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf(false, true, 'controlled')
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Default:| _('No matches')
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| string
---|---
Default:| _('Select...')
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('none', 'flip')
---|---
Default:| 'flip'
Required:| no
PropType:| oneOf('buttongroup', 'checkbox', 'none')
---|---
Required:| no
PropType:| oneOf('nextOpen', 'immediately', 'never')
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| array
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| yes
PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no
PropType:| oneOf('info', 'success', 'warning', 'error')
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(string, number, bool)
---|---
Required:| yes
PropType:| node
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| bool
---|---
Required:| no

### Multiselect API

#### Props

allowNewValues

Allow the user to add arbitrary values.

PropType:| bool
---|---
Required:| no

animateLoading

PropType:| bool
---|---
Required:| no

append

Append removes rounded borders and the border from the right side.

PropType:| bool
---|---
Required:| no

children

`children` should be `Multiselect.Option`, `Multiselect.Heading`, or `Multiselect.Divider`.

PropType:| node
---|---
Required:| no

compact

When compact, options are shown as checkboxes and the input is a single line. This is useful when placing the Multiselect in a horizontal bar, such as a filter.

PropType:| bool
---|---
Required:| no

controlledFilter

If true, this component will not handle filtering. The parent must update the Options based on the onFilterChange value.

Ignored in `compact` mode if the `filter` prop is provided.

PropType:| bool
---|---
Required:| no

defaultPlacement

The default placement of the dropdown menu. It might be rendered in a different direction depending upon the space available.

PropType:| oneOf('above', 'below', 'vertical')
---|---
Default:| 'vertical'
Required:| no

defaultValues

Set this property instead of value to keep the value uncontrolled.

PropType:| array
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Disable adding and removing.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Display as in an error.

PropType:| bool
---|---
Required:| no

filter

Determines whether to show the filter box. When true, the children are automatically filtered based on the label. When controlled, the parent component must provide a onFilterChange callback and update the children.

Only supported when `compact=true`.

PropType:| oneOf(false, true, 'controlled')
---|---
Required:| no

footerMessage

The footer message can show additional information, such as a truncation message.

PropType:| node
---|---
Required:| no

inline

Make the control an inline block with variable width.

PropType:| bool
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

inputRef

A React ref which is set to the input element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

isLoadingOptions

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

loadingMessage

The loading message to show when isLoadingOptions.

PropType:| node
---|---
Required:| no

menuStyle

Style properties to apply to the Menu. This is primarily used to override the width of the menu should it need to be wider than the toggle Button.

PropType:| object
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

noOptionsMessage

The noOptionsMessage is shown when there are no children and it's not loading, such as when there are no Options matching the filter. This can be customized to the type of content, for example: "No matching dashboards". You can insert other content, such as an error message, or communicate a minimum number of characters to enter to see results.

PropType:| node
---|---
Default:| _('No matches')
Required:| no

onChange

A callback to receive the change events. If values is set, this callback is required. This must set the values prop to retain the change.

PropType:| func
---|---
Required:| no

onClose

A callback function invoked when the popover closes.

PropType:| func
---|---
Required:| no

onFilterChange

A callback with the change event and value of the filter box. Providing this callback and setting controlledFilter to true enables you to filter and update the children by other criteria.

PropType:| func
---|---
Required:| no

onOpen

A callback function invoked when the popover opens.

PropType:| func
---|---
Required:| no

onScroll

A callback function invoked when the menu is scrolled.

PropType:| func
---|---
Required:| no

onScrollBottom

A callback function for loading additional list items. Called when the list is scrolled to the bottom or all items in the list are visible. This is called with an event argument if this is the result of a scroll.

This should be set this to `null` when all items are loaded.

PropType:| func
---|---
Required:| no

placeholder

If 'value' is undefined or doesn't match an item, the Button will display this text.

PropType:| string
---|---
Default:| _('Select...')
Required:| no

prepend

Prepend removes rounded borders from the left side.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip')
---|---
Default:| 'flip'
Required:| no

selectAllAppearance

Warning

Deprecated

Value 'buttongroup'

Determines how to display Select all/Clear all. Only supported when `compact=true`.

The 'buttongroup' value is deprecated and will be removed in a future major version.

PropType:| oneOf('buttongroup', 'checkbox', 'none')
---|---
Required:| no

showSelectedValuesFirst

When `compact=true`, move selected values to the top of the list on next open (default), immediately, or not at all.

PropType:| oneOf('nextOpen', 'immediately', 'never')
---|---
Required:| no

tabConfirmsNewValue

Pressing Tab while entering an input confirms the new value. Requires `allowNewValues`.

PropType:| bool
---|---
Required:| no

values

Value will be matched to one of the children to deduce the label and/or icon for the toggle.

PropType:| array
---|---
Required:| no

#### Props

allowNewValues

Allow the user to add arbitrary values.

PropType:| bool
---|---
Required:| no

animateLoading

PropType:| bool
---|---
Required:| no

append

Append removes rounded borders and the border from the right side.

PropType:| bool
---|---
Required:| no

children

`children` should be `Multiselect.Option`, `Multiselect.Heading`, or `Multiselect.Divider`.

PropType:| node
---|---
Required:| no

compact

When compact, options are shown as checkboxes and the input is a single line. This is useful when placing the Multiselect in a horizontal bar, such as a filter.

PropType:| bool
---|---
Required:| no

controlledFilter

If true, this component will not handle filtering. The parent must update the Options based on the onFilterChange value.

Ignored in `compact` mode if the `filter` prop is provided.

PropType:| bool
---|---
Required:| no

defaultPlacement

The default placement of the dropdown menu. It might be rendered in a different direction depending upon the space available.

PropType:| oneOf('above', 'below', 'vertical')
---|---
Default:| 'vertical'
Required:| no

defaultValues

Set this property instead of value to keep the value uncontrolled.

PropType:| array
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Disable adding and removing.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Display as in an error.

PropType:| bool
---|---
Required:| no

filter

Determines whether to show the filter box. When true, the children are automatically filtered based on the label. When controlled, the parent component must provide a onFilterChange callback and update the children.

Only supported when `compact=true`.

PropType:| oneOf(false, true, 'controlled')
---|---
Required:| no

footerMessage

The footer message can show additional information, such as a truncation message.

PropType:| node
---|---
Required:| no

inline

Make the control an inline block with variable width.

PropType:| bool
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

inputRef

A React ref which is set to the input element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

isLoadingOptions

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

loadingMessage

The loading message to show when isLoadingOptions.

PropType:| node
---|---
Required:| no

menuStyle

Style properties to apply to the Menu. This is primarily used to override the width of the menu should it need to be wider than the toggle Button.

PropType:| object
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

noOptionsMessage

The noOptionsMessage is shown when there are no children and it's not loading, such as when there are no Options matching the filter. This can be customized to the type of content, for example: "No matching dashboards". You can insert other content, such as an error message, or communicate a minimum number of characters to enter to see results.

PropType:| node
---|---
Default:| _('No matches')
Required:| no

onChange

A callback to receive the change events. If values is set, this callback is required. This must set the values prop to retain the change.

PropType:| func
---|---
Required:| no

onClose

A callback function invoked when the popover closes.

PropType:| func
---|---
Required:| no

onFilterChange

A callback with the change event and value of the filter box. Providing this callback and setting controlledFilter to true enables you to filter and update the children by other criteria.

PropType:| func
---|---
Required:| no

onOpen

A callback function invoked when the popover opens.

PropType:| func
---|---
Required:| no

onScroll

A callback function invoked when the menu is scrolled.

PropType:| func
---|---
Required:| no

onScrollBottom

A callback function for loading additional list items. Called when the list is scrolled to the bottom or all items in the list are visible. This is called with an event argument if this is the result of a scroll.

This should be set this to `null` when all items are loaded.

PropType:| func
---|---
Required:| no

placeholder

If 'value' is undefined or doesn't match an item, the Button will display this text.

PropType:| string
---|---
Default:| _('Select...')
Required:| no

prepend

Prepend removes rounded borders from the left side.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip')
---|---
Default:| 'flip'
Required:| no

selectAllAppearance

Warning

Deprecated

Value 'buttongroup'

Determines how to display Select all/Clear all. Only supported when `compact=true`.

The 'buttongroup' value is deprecated and will be removed in a future major version.

PropType:| oneOf('buttongroup', 'checkbox', 'none')
---|---
Required:| no

showSelectedValuesFirst

When `compact=true`, move selected values to the top of the list on next open (default), immediately, or not at all.

PropType:| oneOf('nextOpen', 'immediately', 'never')
---|---
Required:| no

tabConfirmsNewValue

Pressing Tab while entering an input confirms the new value. Requires `allowNewValues`.

PropType:| bool
---|---
Required:| no

values

Value will be matched to one of the children to deduce the label and/or icon for the toggle.

PropType:| array
---|---
Required:| no

### Multiselect.Option API

An option within a `Multiselect`.

#### Props

children

When provided, `children` is rendered instead of the `label`.

Caution: The element(s) passed here must be pure.

PropType:| node
---|---
Required:| no

description

Additional information to explain the option, such as "Recommended".

PropType:| string
---|---
Required:| no

descriptionPosition

The description text may appear to the right of the label or under the label.

PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no

disabled

If disabled=true, the option is grayed out and cannot be clicked.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

hidden

Adding hidden options can be useful for resolving the selected display label and icon, when the option should not be in the list. This scenario can arise when Select's filter is controlled, because the selected item may be filtered out; and when a legacy option is valid, but should no longer be displayed as a selectable option.

PropType:| bool
---|---
Required:| no

icon

The icon to show before the label. See the @splunk/react-icons package for drop in icons.

Caution: The element(s) passed here must be pure. All icons in the react-icons package are pure.

PropType:| node
---|---
Required:| no

label

The text to show for the option when `children` is not defined. When filtering, the `label` is used for matching to the filter text.

PropType:| string
---|---
Required:| yes

matchRanges

Sections of the label string to highlight as a match. This is automatically set for uncontrolled filters, so it's not normally necessary to set this property when using filtering.

PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no

selectedAppearance

The `Chip` appearance to use if the option is selected. Not supported in compact mode.

PropType:| oneOf('info', 'success', 'warning', 'error')
---|---
Required:| no

selectedBackgroundColor

The `Chip` background color to use if the option is selected. Not supported in compact mode.

PropType:| string
---|---
Required:| no

selectedForegroundColor

The `Chip` foreground color to use if the option is selected. Not supported in compact mode.

PropType:| string
---|---
Required:| no

truncate

When `true`, wrapping is disabled and any additional text is ellipsised.

PropType:| bool
---|---
Required:| no

value

The label and/or icon will be placed on the Control's toggle if it matches this value.

PropType:| oneOfType(string, number, bool)
---|---
Required:| yes

#### Props

children

When provided, `children` is rendered instead of the `label`.

Caution: The element(s) passed here must be pure.

PropType:| node
---|---
Required:| no

description

Additional information to explain the option, such as "Recommended".

PropType:| string
---|---
Required:| no

descriptionPosition

The description text may appear to the right of the label or under the label.

PropType:| oneOf('right', 'bottom')
---|---
Default:| 'bottom'
Required:| no

disabled

If disabled=true, the option is grayed out and cannot be clicked.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

hidden

Adding hidden options can be useful for resolving the selected display label and icon, when the option should not be in the list. This scenario can arise when Select's filter is controlled, because the selected item may be filtered out; and when a legacy option is valid, but should no longer be displayed as a selectable option.

PropType:| bool
---|---
Required:| no

icon

The icon to show before the label. See the @splunk/react-icons package for drop in icons.

Caution: The element(s) passed here must be pure. All icons in the react-icons package are pure.

PropType:| node
---|---
Required:| no

label

The text to show for the option when `children` is not defined. When filtering, the `label` is used for matching to the filter text.

PropType:| string
---|---
Required:| yes

matchRanges

Sections of the label string to highlight as a match. This is automatically set for uncontrolled filters, so it's not normally necessary to set this property when using filtering.

PropType:| arrayOf(shape({start: number, end: number}))
---|---
Required:| no

selectedAppearance

The `Chip` appearance to use if the option is selected. Not supported in compact mode.

PropType:| oneOf('info', 'success', 'warning', 'error')
---|---
Required:| no

selectedBackgroundColor

The `Chip` background color to use if the option is selected. Not supported in compact mode.

PropType:| string
---|---
Required:| no

selectedForegroundColor

The `Chip` foreground color to use if the option is selected. Not supported in compact mode.

PropType:| string
---|---
Required:| no

truncate

When `true`, wrapping is disabled and any additional text is ellipsised.

PropType:| bool
---|---
Required:| no

value

The label and/or icon will be placed on the Control's toggle if it matches this value.

PropType:| oneOfType(string, number, bool)
---|---
Required:| yes

### Multiselect.Heading API

A non-interactive `Menu` item used to separate and label groups of `Menu` items.

#### Props

children

PropType:| node
---|---
Required:| no

outerStyle

PropType:| object
---|---
Required:| no

title

Renders this heading as a title to describe the whole `Menu`, which should only be enabled for the first heading in a `Menu`.

PropType:| bool
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| no

outerStyle

PropType:| object
---|---
Required:| no

title

Renders this heading as a title to describe the whole `Menu`, which should only be enabled for the first heading in a `Menu`.

PropType:| bool
---|---
Required:| no

### Multiselect.Divider API

A non-interactive menu item used to visually separate groups of items in the menu.

## Test Hooks

#### Element Selectors

multiselect

The root of the `Multiselect`.

Example:| [data-test="multiselect"]
---|---
Attribute:| data-test
Value:| multiselect
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

textbox

The textbox used for entering values. Not available in `compact` mode. See also `toggle`.

Example:| [data-test="multiselect"] [data-test="textbox"]
---|---
Attribute:| data-test
Value:| textbox
Scope Describes where to look for the element.:| In the `Multiselect` root.

selected-option (generic)

Matches all selected options. Selected option can be removed by clicking on it. Not available in `compact` mode.

Example:| [data-test="multiselect"] [data-test="selected-option"]
---|---
Attribute:| data-test
Value:| selected-option
Scope Describes where to look for the element.:| In the `Multiselect` root.

selected-option (specific)

Matches a specific selected option. Not available in `compact` mode.

Example:| [data-test="multiselect"] [data-test="selected-option"][data-test-value="target-option-value"]
---|---
Attribute:| data-test-value
Value:| The `value` prop of the target `Multiselect.Option`
Scope Describes where to look for the element.:| In the `Multiselect` root.

label

Matches the label of the selected option.

Example:| [data-test="multiselect"] [data-test="selected-option"][data-test-value="target-option-value"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| In the selected `Multiselect.Option` root.

option (generic)

Matches all `Multiselect.Option`s in the popover menu.

Example:| #${popoverId} [data-test="option"]
---|---
Attribute:| data-test
Value:| option
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

option (specific)

Matches a specific `Multiselect.Option` in the popover menu.

Example:| #${popoverId} [data-test="option"][data-test-value="target-option-value"]
---|---
Attribute:| data-test-value
Value:| The `value` prop of the target `Multiselect.Option`
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

match

Matches all wrappers around each piece of text matching the filter.

Example:| [data-test="menu"] [data-test="option"] [data-test="match"]
---|---
Attribute:| data-test
Value:| match
Scope Describes where to look for the element.:| In the `Multiselect.Option` root.

heading

Matches all `Multiselect.Heading` in the popover menu.

Example:| #${popoverId} [data-test="heading"]
---|---
Attribute:| data-test
Value:| heading
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

divider

Matches all `Multiselect.Divider` in the popover menu.

Example:| #${popoverId} [data-test="divider"]
---|---
Attribute:| data-test
Value:| divider
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

footer-message

Matches the footer message.

Example:| #${popoverId} [data-test="footer-message"]
---|---
Attribute:| data-test
Value:| footer-message
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

no-results-message

Matches the message shown when there are no children and the `Multiselect` isn't loading options.

Example:| #${popoverId} [data-test="no-results-message"]
---|---
Attribute:| data-test
Value:| no-results-message
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

select-all

Controls in the popover menu, select all link. Only available in compact mode.

Example:| #${popoverId} [data-test="select-all"]
---|---
Attribute:| data-test
Value:| select-all
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

clear-all

Controls in the popover menu, clear all link. Only available in compact mode.

Example:| #${popoverId} [data-test="clear-all"]
---|---
Attribute:| data-test
Value:| clear-all
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

filter

Controls in the popover menu, filter text box. Only available in compact mode.

Example:| #${popoverId} [data-test="filter"]
---|---
Attribute:| data-test
Value:| filter
Scope Describes where to look for the element.:| In the component's popover.The target element is rendered outside the main component in a popover. To scope the selector correctly, use the popover id.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Number`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Default:| 'en-US'
Required:| no
PropType:| number
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| number
---|---
Default:| 5
Required:| no
PropType:| number
---|---
Default:| 1
Required:| no
PropType:| number
---|---
Required:| no

### Number API

#### Props

append

Append removes the rounded borders and the border from the right side and moves the increment and decrement buttons to the left.

PropType:| bool
---|---
Required:| no

children

PropType:| node
---|---
Required:| no

defaultValue

Set this property instead of value to make the value uncontrolled.

PropType:| number
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Determines if the input is editable.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error.

PropType:| bool
---|---
Required:| no

hideStepButtons

Hides the increment and decrement step buttons if true.

PropType:| bool
---|---
Required:| no

inline

When false, displays as inline-block with the default width.

PropType:| bool
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

inputRef

A React ref which is set to the text input element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

locale

The locale determines the decimal separator. Supported locale formats are: `xx`, `xx-XX`, and `xx_XX`.

PropType:| string
---|---
Default:| 'en-US'
Required:| no

max

The largest allowable value.

PropType:| number
---|---
Required:| no

min

The smallest allowable value.

PropType:| number
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onBlur

A callback for when the input loses focus.

PropType:| func
---|---
Required:| no

onChange

This is equivalent to onInput which is called on keydown, paste, and so on. If value is set, this callback is required. This must set the value prop to retain the change.

PropType:| func
---|---
Required:| no

onClick

A callback for when the input is clicked. This will only trigger when the textbox itself is clicked and will not trigger for other parts of the component such as the step buttons.

PropType:| func
---|---
Required:| no

onFocus

A callback for when the input takes focus.

PropType:| func
---|---
Required:| no

onKeyDown

A keydown callback can be used to prevent a certain input by utilizing the event argument.

PropType:| func
---|---
Required:| no

onKeyUp

A keyup callback.

PropType:| func
---|---
Required:| no

onSelect

A callback for when the user selects text.

PropType:| func
---|---
Required:| no

prepend

Prepend removes rounded borders from the left side. This cannot be used in combination with append.

PropType:| bool
---|---
Required:| no

roundTo

The number of decimal places for rounding. Set to zero to limit input to integers. Negative numbers are supported. For instance, -2 will round to the nearest hundred.

PropType:| number
---|---
Default:| 5
Required:| no

step

The amount of increment and decrement applied by the buttons and arrow keys.

PropType:| number
---|---
Default:| 1
Required:| no

value

The contents of the input. Setting this value makes the property controlled. A callback is required.

PropType:| number
---|---
Required:| no

#### Props

append

Append removes the rounded borders and the border from the right side and moves the increment and decrement buttons to the left.

PropType:| bool
---|---
Required:| no

children

PropType:| node
---|---
Required:| no

defaultValue

Set this property instead of value to make the value uncontrolled.

PropType:| number
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Determines if the input is editable.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error.

PropType:| bool
---|---
Required:| no

hideStepButtons

Hides the increment and decrement step buttons if true.

PropType:| bool
---|---
Required:| no

inline

When false, displays as inline-block with the default width.

PropType:| bool
---|---
Required:| no

inputId

An id for the input, which may be necessary for accessibility, such as for aria attributes.

PropType:| string
---|---
Required:| no

inputRef

A React ref which is set to the text input element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

locale

The locale determines the decimal separator. Supported locale formats are: `xx`, `xx-XX`, and `xx_XX`.

PropType:| string
---|---
Default:| 'en-US'
Required:| no

max

The largest allowable value.

PropType:| number
---|---
Required:| no

min

The smallest allowable value.

PropType:| number
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onBlur

A callback for when the input loses focus.

PropType:| func
---|---
Required:| no

onChange

This is equivalent to onInput which is called on keydown, paste, and so on. If value is set, this callback is required. This must set the value prop to retain the change.

PropType:| func
---|---
Required:| no

onClick

A callback for when the input is clicked. This will only trigger when the textbox itself is clicked and will not trigger for other parts of the component such as the step buttons.

PropType:| func
---|---
Required:| no

onFocus

A callback for when the input takes focus.

PropType:| func
---|---
Required:| no

onKeyDown

A keydown callback can be used to prevent a certain input by utilizing the event argument.

PropType:| func
---|---
Required:| no

onKeyUp

A keyup callback.

PropType:| func
---|---
Required:| no

onSelect

A callback for when the user selects text.

PropType:| func
---|---
Required:| no

prepend

Prepend removes rounded borders from the left side. This cannot be used in combination with append.

PropType:| bool
---|---
Required:| no

roundTo

The number of decimal places for rounding. Set to zero to limit input to integers. Negative numbers are supported. For instance, -2 will round to the nearest hundred.

PropType:| number
---|---
Default:| 5
Required:| no

step

The amount of increment and decrement applied by the buttons and arrow keys.

PropType:| number
---|---
Default:| 1
Required:| no

value

The contents of the input. Setting this value makes the property controlled. A callback is required.

PropType:| number
---|---
Required:| no

## Test Hooks

#### Element Selectors

number

The root of the `Number`.

Example:| [data-test="number"]
---|---
Attribute:| data-test
Value:| number
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

textbox

The text box for inputing the value with the keyboard.

Example:| [data-test="number"] [data-test="textbox"]
---|---
Attribute:| data-test
Value:| textbox
Scope Describes where to look for the element.:| In the `Number` root.

increment

A button that increments the value by the step size.

Example:| [data-test="number"] [data-test="increment"]
---|---
Attribute:| data-test
Value:| increment
Scope Describes where to look for the element.:| In the `Number` root.

decrement

A button that decrements the value by the step size.

Example:| [data-test="number"] [data-test="decrement"]
---|---
Attribute:| data-test
Value:| decrement
Scope Describes where to look for the element.:| In the `Number` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Progress`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOf('info', 'success', 'error')
---|---
Default:| 'info'
Required:| no

### Progress API

#### Props

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

percentage

The percentage complete. If unset, no progress bar is shown. Percentage must be a number from 0-100.

PropType:| number
---|---
Required:| no

tooltip

Tooltip defaults to the percentage complete.

PropType:| node
---|---
Required:| no

type

Sets the appearance of the `Progress` component.

Note: `success` and `error` types are not animated.

PropType:| oneOf('info', 'success', 'error')
---|---
Default:| 'info'
Required:| no

#### Props

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

percentage

The percentage complete. If unset, no progress bar is shown. Percentage must be a number from 0-100.

PropType:| number
---|---
Required:| no

tooltip

Tooltip defaults to the percentage complete.

PropType:| node
---|---
Required:| no

type

Sets the appearance of the `Progress` component.

Note: `success` and `error` types are not animated.

PropType:| oneOf('info', 'success', 'error')
---|---
Default:| 'info'
Required:| no

## Test Hooks

#### Element Selectors

progress

The root of the `Progress`.

Example:| [data-test="progress"]
---|---
Attribute:| data-test
Value:| progress
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `RadioBar`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| oneOfType(string, number, bool)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOf('radiogroup', 'menubar')
---|---
Default:| 'radiogroup'
Required:| no
PropType:| oneOfType(string, number, bool)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| any
---|---
Required:| yes

### RadioBar API

RadioBar is a form control that provides the ability to select one option out of a group.

#### Props

children

`children` should be `RadioBar.Option`.

PropType:| node
---|---
Required:| no

defaultValue

The default value. Only applicable if this is an uncontrolled component. Otherwise, use the value prop.

PropType:| oneOfType(string, number, bool)
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Disable all options in the RadioBar. This will override the disabled prop on any individual Option.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error. The buttons will turn red.

PropType:| bool
---|---
Required:| no

inline

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

A callback that receives the new value.

PropType:| func
---|---
Required:| no

role

The role of the RadioBar. The children Options' `role` will be set to `radio` or `menuitemradio` respectively.

PropType:| oneOf('radiogroup', 'menubar')
---|---
Default:| 'radiogroup'
Required:| no

value

The currently selected value. Only applicable if this is a controlled component.

PropType:| oneOfType(string, number, bool)
---|---
Required:| no

#### Props

children

`children` should be `RadioBar.Option`.

PropType:| node
---|---
Required:| no

defaultValue

The default value. Only applicable if this is an uncontrolled component. Otherwise, use the value prop.

PropType:| oneOfType(string, number, bool)
---|---
Required:| no

describedBy

The id of the description. When placed in a ControlGroup, this is automatically set to the ControlGroup's help component.

PropType:| string
---|---
Required:| no

disabled

Disable all options in the RadioBar. This will override the disabled prop on any individual Option.

PropType:| bool
---|---
Default:| false
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error. The buttons will turn red.

PropType:| bool
---|---
Required:| no

inline

PropType:| bool
---|---
Required:| no

labelledBy

The id of the label. When placed in a ControlGroup, this is automatically set to the ControlGroup's label.

PropType:| string
---|---
Required:| no

name

The name is returned with onChange events, which can be used to identify the control when multiple controls share an onChange callback.

PropType:| string
---|---
Required:| no

onChange

A callback that receives the new value.

PropType:| func
---|---
Required:| no

role

The role of the RadioBar. The children Options' `role` will be set to `radio` or `menuitemradio` respectively.

PropType:| oneOf('radiogroup', 'menubar')
---|---
Default:| 'radiogroup'
Required:| no

value

The currently selected value. Only applicable if this is a controlled component.

PropType:| oneOfType(string, number, bool)
---|---
Required:| no

### RadioBar.Option API

#### Props

disabled

Add a disabled attribute and prevent clicking.

PropType:| bool
---|---
Required:| no

endAdornment

Adornment after the label.

PropType:| node
---|---
Required:| no

label

The text shown on the button.

PropType:| string
---|---
Required:| no

startAdornment

Adornment in front of the label.

PropType:| node
---|---
Required:| no

value

The value of the `Option`.

PropType:| any
---|---
Required:| yes

#### Props

disabled

Add a disabled attribute and prevent clicking.

PropType:| bool
---|---
Required:| no

endAdornment

Adornment after the label.

PropType:| node
---|---
Required:| no

label

The text shown on the button.

PropType:| string
---|---
Required:| no

startAdornment

Adornment in front of the label.

PropType:| node
---|---
Required:| no

value

The value of the `Option`.

PropType:| any
---|---
Required:| yes

## Test Hooks

#### Element Selectors

radio-bar

The root of the `RadioBar`.

Example:| [data-test="radio-bar"]
---|---
Attribute:| data-test
Value:| radio-bar
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

option (generic)

Matches all `RadioBar.Option`s.

Example:| [data-test="radio-bar"] [data-test="option"]
---|---
Attribute:| data-test
Value:| option
Scope Describes where to look for the element.:| In the `RadioBar` root.

option (specific)

Matches a specific `RadioBar.Option` in the `RadioBar`.

Example:| [data-test="radio-bar"] [data-test="option"][data-test-value="target-option"]
---|---
Attribute:| data-test-value
Value:| The `value` prop of the target `RadioBar.Option`.
Scope Describes where to look for the element.:| In the `RadioBar` root.

label

Matches the label of a specific `RadioBar.Option`.

Example:| [data-test="radio-bar"] [data-test="option"][data-test-value="target-option"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| In the specific `RadioBar.Option` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Resize`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf('border', 'overlay', 'separator')
---|---
Default:| 'overlay'
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| number
---|---
Default:| 10
Required:| no
PropType:| func
---|---
Required:| yes
PropType:| arrayOf(oneOf('nw', 'n', 'ne', 'w', 'e', 'sw', 's', 'se'))
---|---
Required:| yes
PropType:| oneOf('always', 'on-hover')
---|---
Default:| 'always'
Required:| no

### Resize API

Resize is a utility container with drag handles for resizing.

#### Props

appearance

The appearance of the resize handles. Note: When appearance is 'separator', active full length borders will only appear for 'n', 's', 'e', or 'w' `resizeHandles`.

PropType:| oneOf('border', 'overlay', 'separator')
---|---
Default:| 'overlay'
Required:| no

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

keyIncrement

When focused on a resize handle, the arrow keys will adjust the height or width by this amount with each press.

PropType:| number
---|---
Default:| 10
Required:| no

onRequestResize

A callback which is passed the event and an object with the requested height and width.

PropType:| func
---|---
Required:| yes

resizeHandles

An array of resize handles placements.

PropType:| arrayOf(oneOf('nw', 'n', 'ne', 'w', 'e', 'sw', 's', 'se'))
---|---
Required:| yes

showHandles

The appearance of the resize handles.

PropType:| oneOf('always', 'on-hover')
---|---
Default:| 'always'
Required:| no

#### Props

appearance

The appearance of the resize handles. Note: When appearance is 'separator', active full length borders will only appear for 'n', 's', 'e', or 'w' `resizeHandles`.

PropType:| oneOf('border', 'overlay', 'separator')
---|---
Default:| 'overlay'
Required:| no

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

keyIncrement

When focused on a resize handle, the arrow keys will adjust the height or width by this amount with each press.

PropType:| number
---|---
Default:| 10
Required:| no

onRequestResize

A callback which is passed the event and an object with the requested height and width.

PropType:| func
---|---
Required:| yes

resizeHandles

An array of resize handles placements.

PropType:| arrayOf(oneOf('nw', 'n', 'ne', 'w', 'e', 'sw', 's', 'se'))
---|---
Required:| yes

showHandles

The appearance of the resize handles.

PropType:| oneOf('always', 'on-hover')
---|---
Default:| 'always'
Required:| no

## Test Hooks

#### Element Selectors

resize

The root of the `Resize`.

Example:| [data-test="resize"]
---|---
Attribute:| data-test
Value:| resize
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

resize-n

Matches the north resize handle.

Example:| [data-test="resize"] [data-test="resize-n"]
---|---
Attribute:| data-test
Value:| resize-n
Scope Describes where to look for the element.:| In the `Resize` root.

resize-ne

Matches the northeast resize handle.

Example:| [data-test="resize"] [data-test="resize-ne"]
---|---
Attribute:| data-test
Value:| resize-ne
Scope Describes where to look for the element.:| In the `Resize` root.

resize-e

Matches the east resize handle.

Example:| [data-test="resize"] [data-test="resize-e"]
---|---
Attribute:| data-test
Value:| resize-e
Scope Describes where to look for the element.:| In the `Resize` root.

resize-se

Matches the southeast resize handle.

Example:| [data-test="resize"] [data-test="resize-se"]
---|---
Attribute:| data-test
Value:| resize-se
Scope Describes where to look for the element.:| In the `Resize` root.

resize-s

Matches the south resize handle.

Example:| [data-test="resize"] [data-test="resize-s"]
---|---
Attribute:| data-test
Value:| resize-s
Scope Describes where to look for the element.:| In the `Resize` root.

resize-sw

Matches the southwest resize handle.

Example:| [data-test="resize"] [data-test="resize-sw"]
---|---
Attribute:| data-test
Value:| resize-sw
Scope Describes where to look for the element.:| In the `Resize` root.

resize-w

Matches the west resize handle.

Example:| [data-test="resize"] [data-test="resize-w"]
---|---
Attribute:| data-test
Value:| resize-w
Scope Describes where to look for the element.:| In the `Resize` root.

resize-nw

Matches the northwest resize handle.

Example:| [data-test="resize"] [data-test="resize-nw"]
---|---
Attribute:| data-test
Value:| resize-nw
Scope Describes where to look for the element.:| In the `Resize` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `ScreenReaderContent`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| yes
PropType:| oneOfType(func, object)
---|---
Required:| no

### ScreenReaderContent API

The screen reader text is used to wrap content that is only accessible through screen readers.

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| yes

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

## Test Hooks

#### Element Selectors

screen-reader-content

The root of the `ScreenReaderContent`.

Example:| [data-test="screen-reader-content"]
---|---
Attribute:| data-test
Value:| screen-reader-content
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `SplitButton`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf('default', 'secondary', 'primary', 'destructive', 'destructiveSecondary')
---|---
Default:| 'secondary'
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| func
---|---
Required:| no

### SplitButton API

#### Props

appearance

Warning

Deprecated

Value 'default'

Changes the style of the main button and toggle.

The `default` value is deprecated and will be removed in a future major version.

PropType:| oneOf('default', 'secondary', 'primary', 'destructive', 'destructiveSecondary')
---|---
Default:| 'secondary'
Required:| no

children

Must be `SplitButton.Item`. By default the first child becomes the main button. The remaining children become dropdown items.

PropType:| node
---|---
Required:| no

disabled

Prevents main button and dropdown toggle from being clicked.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Restricts the horizontal size of the button. Set `inline` to `false` to remove the right margin and stretch the button to the full width of its container.

PropType:| bool
---|---
Default:| true
Required:| no

onClick

A callback for when the main button or toggle is clicked.

PropType:| func
---|---
Required:| no

toggleRef

A React ref which is set to the dropdown toggle when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

appearance

Warning

Deprecated

Value 'default'

Changes the style of the main button and toggle.

The `default` value is deprecated and will be removed in a future major version.

PropType:| oneOf('default', 'secondary', 'primary', 'destructive', 'destructiveSecondary')
---|---
Default:| 'secondary'
Required:| no

children

Must be `SplitButton.Item`. By default the first child becomes the main button. The remaining children become dropdown items.

PropType:| node
---|---
Required:| no

disabled

Prevents main button and dropdown toggle from being clicked.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Restricts the horizontal size of the button. Set `inline` to `false` to remove the right margin and stretch the button to the full width of its container.

PropType:| bool
---|---
Default:| true
Required:| no

onClick

A callback for when the main button or toggle is clicked.

PropType:| func
---|---
Required:| no

toggleRef

A React ref which is set to the dropdown toggle when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

### SplitButton.Item API

An item within a `SplitButton`.

#### Props

children

Becomes the label.

PropType:| node
---|---
Required:| no

disabled

Prevents user from clicking the button.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

icon

Applies an icon in front of the label.

PropType:| node
---|---
Required:| no

isMain

Becomes the main button. If no `Item`s have this prop, the first `Item` is the main button.

PropType:| bool
---|---
Required:| no

onClick

A callback for when an item is clicked.

PropType:| func
---|---
Required:| no

#### Props

children

Becomes the label.

PropType:| node
---|---
Required:| no

disabled

Prevents user from clicking the button.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

icon

Applies an icon in front of the label.

PropType:| node
---|---
Required:| no

isMain

Becomes the main button. If no `Item`s have this prop, the first `Item` is the main button.

PropType:| bool
---|---
Required:| no

onClick

A callback for when an item is clicked.

PropType:| func
---|---
Required:| no

## Test Hooks

#### Element Selectors

split-button-container

The root container of the `SplitButton`.

Example:| [data-test="split-button-container"]
---|---
Attribute:| data-test
Value:| split-button-container
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

split-button-toggle

The toggle to open the dropdown.

Example:| [data-test="split-button-toggle"]
---|---
Attribute:| data-test
Value:| split-button-toggle
Scope Describes where to look for the element.:| In the `SplitButton` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `StepBar`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| any
---|---
Required:| yes
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| false
Required:| no
PropType:| any
---|---
Required:| no

### StepBar API

#### Props

activeStepId

The `stepId` of the `StepBar.Step` to activate.

PropType:| any
---|---
Required:| yes

children

Must be `StepBar.Step`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Setting inline to true makes the Step Bar an inline element. It assumes its minimum width.

PropType:| bool
---|---
Default:| false
Required:| no

#### Props

activeStepId

The `stepId` of the `StepBar.Step` to activate.

PropType:| any
---|---
Required:| yes

children

Must be `StepBar.Step`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Setting inline to true makes the Step Bar an inline element. It assumes its minimum width.

PropType:| bool
---|---
Default:| false
Required:| no

### StepBar.Step API

#### Props

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Displays active step with alert icon.

PropType:| bool
---|---
Default:| false
Required:| no

stepId

A unique `id` for this step and used by the `StepBar` to keep track of the open `Step`. Defaults to a zero-based index matching the component's position in `StepBar`.

PropType:| any
---|---
Required:| no

#### Props

children

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Displays active step with alert icon.

PropType:| bool
---|---
Default:| false
Required:| no

stepId

A unique `id` for this step and used by the `StepBar` to keep track of the open `Step`. Defaults to a zero-based index matching the component's position in `StepBar`.

PropType:| any
---|---
Required:| no

## Test Hooks

#### Element Selectors

step-bar

The root of the `StepBar`.

Example:| [data-test="step-bar"]
---|---
Attribute:| data-test
Value:| step-bar
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

step (generic)

Matches all `StepBar.Step`.

Example:| [data-test="step-bar"] [data-test="step"]
---|---
Attribute:| data-test
Value:| step
Scope Describes where to look for the element.:| In the `StepBar` root.

step (specific)

Matches a specific `StepBar.Step` within the `StepBar`.

Example:| [data-test="step-bar"] [data-test-step-id="target-stepId"]
---|---
Attribute:| data-test-step-id
Value:| The `stepId` prop of the target `StepBar.Step`
Scope Describes where to look for the element.:| In the `StepBar` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Switch`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOf('checkbox', 'toggle')
---|---
Default:| 'checkbox'
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOf(true, false, 'some')
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| any
---|---
Required:| no

### Switch API

`Switch` is a basic form control with an on/off state.

#### Props

appearance

Warning

Deprecated

Value 'checkbox'

Determines if the component renders as a checkbox or toggle.

The 'checkbox' value is deprecated and will be removed in a future major version.

PropType:| oneOf('checkbox', 'toggle')
---|---
Default:| 'checkbox'
Required:| no

children

PropType:| node
---|---
Required:| no

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error only when appearance is 'checkbox'.

PropType:| bool
---|---
Required:| no

id

If `Switch` is not provided children as the label, an id can be provided for the control. Set a label's for attribute to this id to link the two elements.

PropType:| string
---|---
Required:| no

inline

Make the control an inline block with variable width.

PropType:| bool
---|---
Required:| no

labelledBy

If `Switch` is not provided children as the label, an id can be provided to another element.

PropType:| string
---|---
Required:| no

onClick

PropType:| func
---|---
Required:| no

selected

'some' is only valid when appearance is 'checkbox'. The current value of `selected` is passed to the onClick handler.

PropType:| oneOf(true, false, 'some')
---|---
Required:| no

selectedLabel

The customized content presented to screen readers when selected.

PropType:| string
---|---
Required:| no

someSelectedLabel

The customized content presented to screen readers when selected="some".

PropType:| string
---|---
Required:| no

toggleRef

A React ref which is set to the toggle when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

unselectedLabel

The customized content presented to screen readers when unselected.

PropType:| string
---|---
Required:| no

value

The `value` is used as an identifier and is passed to the `onClick` handler. This is useful when managing a group of switches with a single `onClick` handler.

PropType:| any
---|---
Required:| no

#### Props

appearance

Warning

Deprecated

Value 'checkbox'

Determines if the component renders as a checkbox or toggle.

The 'checkbox' value is deprecated and will be removed in a future major version.

PropType:| oneOf('checkbox', 'toggle')
---|---
Default:| 'checkbox'
Required:| no

children

PropType:| node
---|---
Required:| no

disabled

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts, and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

error

Highlight the field as having an error only when appearance is 'checkbox'.

PropType:| bool
---|---
Required:| no

id

If `Switch` is not provided children as the label, an id can be provided for the control. Set a label's for attribute to this id to link the two elements.

PropType:| string
---|---
Required:| no

inline

Make the control an inline block with variable width.

PropType:| bool
---|---
Required:| no

labelledBy

If `Switch` is not provided children as the label, an id can be provided to another element.

PropType:| string
---|---
Required:| no

onClick

PropType:| func
---|---
Required:| no

selected

'some' is only valid when appearance is 'checkbox'. The current value of `selected` is passed to the onClick handler.

PropType:| oneOf(true, false, 'some')
---|---
Required:| no

selectedLabel

The customized content presented to screen readers when selected.

PropType:| string
---|---
Required:| no

someSelectedLabel

The customized content presented to screen readers when selected="some".

PropType:| string
---|---
Required:| no

toggleRef

A React ref which is set to the toggle when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

unselectedLabel

The customized content presented to screen readers when unselected.

PropType:| string
---|---
Required:| no

value

The `value` is used as an identifier and is passed to the `onClick` handler. This is useful when managing a group of switches with a single `onClick` handler.

PropType:| any
---|---
Required:| no

## Test Hooks

#### Element Selectors

switch

The root of the `Switch`.

Example:| [data-test="switch"]
---|---
Attribute:| data-test
Value:| switch
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

toggle

Matches the toggle of the switch.

Example:| [data-test="switch"] [data-test="toggle"]
---|---
Attribute:| data-test
Value:| toggle
Scope Describes where to look for the element.:| In the `Switch` root.

label

Matches the label of the switch.

Example:| [data-test="switch"] [data-test="label"]
---|---
Attribute:| data-test
Value:| label
Scope Describes where to look for the element.:| Unique within `Switch`.

## Accessibility

Card Layout provides a container to responsively arrange and resize Cards.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Table`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

Name| Age| Email
---|---|---
Rylan| 42| Angelita_Weimann42@gmail.com
Amelia| 24| Dexter.Trantow57@hotmail.com
Estevan| 56| Aimee7@hotmail.com
Florence| 71| Jarrod.Bernier13@yahoo.com
Tressa| 38| Yadira1@hotmail.com
Name| Email
---|---
Amelia| Dexter.Trantow57@hotmail.com
Estevan| Aimee7@hotmail.com
Florence| Jarrod.Bernier13@yahoo.com
Rylan| Angelita_Weimann42@gmail.com
Tressa| Yadira1@hotmail.com
Name| Email
---|---
Rylan| Angelita_Weimann42@gmail.com
Amelia| Dexter.Trantow57@hotmail.com
Estevan| Aimee7@hotmail.com
Florence| Jarrod.Bernier13@yahoo.com
Tressa| Yadira1@hotmail.com
Name| Email
---|---
Rylan| Angelita_Weimann42@gmail.com
Amelia| Dexter.Trantow57@hotmail.com
Estevan| Aimee7@hotmail.com
Florence| Jarrod.Bernier13@yahoo.com
Tressa| Yadira1@hotmail.com
| Name| Email
---|---|---
| Rylan| Angelita_Weimann42@gmail.com
| Amelia| Dexter.Trantow57@hotmail.com
| Estevan| Aimee7@hotmail.com
| Florence| Jarrod.Bernier13@yahoo.com
| Tressa| Yadira1@hotmail.com
Name| Email
---|---
Amelia| Dexter.Trantow57@hotmail.com
Estevan| Aimee7@hotmail.com
Florence| Jarrod.Bernier13@yahoo.com
Rylan| Angelita_Weimann42@gmail.com
Tressa| Yadira1@hotmail.com
Name| Kind
---|---
S3_bucket_1| Amazon S3
S3_bucket_2| Amazon S3
Splunk_CMP_1| Index
EC_1| View
EC_2| View
Name| Email
---|---
Rylan| Angelita_Weimann42@gmail.com
Amelia| Dexter.Trantow57@hotmail.com
Estevan| Aimee7@hotmail.com
Florence| Jarrod.Bernier13@yahoo.com
Tressa| Yadira1@hotmail.com
Bernice| bernice.Gilbert@gmail.com
Adrian| adrian7456@gmail.com
Ester| esternyc@gmail.com
Andrew| andrew.fillmore2@gmail.com
Felix| felixfelix@hotmail.com
Name| Email| Age
---|---|---
Name| Email| Age
---|---|---
Rylan| Angelita_Weimann42@gmail.com| 27
Amelia| Dexter.Trantow57@hotmail.com| 56
Estevan| Aimee7@hotmail.com| 92
Florence| Jarrod.Bernier13@yahoo.com| 43
Tressa| Yadira1@hotmail.com| 33
| Name| Email
---|---|---
| Rylan| Angelita_Weimann42@gmail.com
| Amelia| Dexter.Trantow57@hotmail.com
| Estevan| Aimee7@hotmail.com
| Florence| Jarrod.Bernier13@yahoo.com
| Tressa| Yadira1@hotmail.com
| Name| Email
---|---|---
| Rylan| Angelita_Weimann42@gmail.com
| Amelia| Dexter.Trantow57@hotmail.com
| Estevan| Aimee7@hotmail.com
| Florence| Jarrod.Bernier13@yahoo.com
| Tressa| Yadira1@hotmail.com
Name| Age| Email| State| Country| Favorite Color| Favorite Day| Occupation| Industry|
---|---|---|---|---|---|---|---|---|---
Rylan| 42| Angelita_Weimann42@gmail.com| CA| US| Orange| Monday| Engineer| Software Development| EditActions
Amelia| 24| Dexter.Trantow57@hotmail.com| NY| US| White| Friday| Engineer| Software| EditActions
Estevan| 56| Aimee7@hotmail.com| IL| US| Green| Saturday| Engineer| Software| EditActions
Florence| 71| Jarrod.Bernier13@yahoo.com| CA| US| Red| Tuesday| Engineer| Software| EditActions
Teresa| 38| Yadira1@hotmail.com| NJ| US| Blue| Wednesday| Engineer| Software| EditActions
| Name| Age| Email
---|---|---|---
| Rylan| 12| Angelita_Weimann42@gmail.com
| Amelia| 23| Dexter.Trantow57@hotmail.com
| Estevan| 19| Aimee7@hotmail.com
| Florence| 20| Jarrod.Bernier13@yahoo.com
| Tressa| 22| Yadira1@hotmail.com
Name| Age| Email
---|---|---
Rylan| 12| Angelita_Weimann42@gmail.com
Amelia| 23| Dexter.Trantow57@hotmail.com
Estevan| 19| Aimee7@hotmail.com
Florence| 20| Jarrod.Bernier13@yahoo.com
Tressa| 22| Yadira1@hotmail.com

* * *

Name|

* * *

Age|

* * *

Email Address
---|---|---
Rylan| 12| Angelita_Weimann42@gmail.com
Amelia| 23| Dexter.Trantow57@hotmail.com
Estevan| 19| Aimee7@hotmail.com
Florence| 20| Jarrod.Bernier13@yahoo.com
Tressa| 22| Yadira1@hotmail.com

* * *

Name|

* * *

Age|

* * *

Email Address
---|---|---
Rylan| 12| Angelita_Weimann42@gmail.com
Amelia| 23| Dexter.Trantow57@hotmail.com
Estevan| 19| Aimee7@hotmail.com
Florence| 20| Jarrod.Bernier13@yahoo.com
Tressa| 22| Yadira1@hotmail.com
Name| Age| Email
---|---|---
Rylan| 42| Angelita_Weimann42@gmail.com
Amelia| 24| Dexter.Trantow57@hotmail.com
Estevan| 56| Aimee7@hotmail.com
Florence| 71| Jarrod.Bernier13@yahoo.com
Tressa| 38| Yadira1@hotmail.com
|

* * *

NameLegal first name|

* * *

Status|

* * *

Birth State|

* * *

Age|

* * *

Email Address|
---|---|---|---|---|---|---
| Adrian| married| MA| 23| adrian7456@gmail.com| EditActions
| Amelia| married| UT| 23| Dexter.Trantow57@hotmail.com| EditActions
| Andrew| single| NM| 16| andrew.fillmore2@gmail.com| EditActions
| Bernice| single| TX| 17| bernice.Gilbert@gmail.com| EditActions
| Ester| single| NY| 88| esternyc@gmail.com| EditActions
| Estevan| single| NY| 19| Aimee7@hotmail.com| EditActions
| Felix| married| CA| 36| felixfelix@hotmail.com| EditActions
| Florence| single| AZ| 20| Jarrod.Bernier13@yahoo.com| EditActions
| Rylan| single| HI| 12| Angelita_Weimann42@gmail.com|
| Tressa| married| CA| 22| yadira1@hotmail.com| EditActions
PropType:| arrayOf(element)
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| oneOf('docked', 'fixed', 'inline')
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| number
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('single', 'multi', 'controlled', 'none')
---|---
Required:| no
PropType:| oneOf('all', 'some', 'none')
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| object
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| element
---|---
Required:| no
PropType:| element
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| any
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(element, arrayOf(element))
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no
PropType:| node
---|---
Required:| no
PropType:| any
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no
PropType:| node
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| string
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| oneOf('asc', 'desc', 'none')
---|---
Default:| 'none'
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| oneOfType(number, oneOf('auto'))
---|---
Required:| no
PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| node
---|---
Required:| yes
PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no
PropType:| string
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'toggleClick', ]
Required:| no
PropType:| string
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| number
---|---
Required:| no
PropType:| node
---|---
Required:| yes
PropType:| oneOf('top', 'bottom')
---|---
Default:| 'top'
Required:| no

### Table API

#### Props

actions

Adds table-level actions. Not compatible with `onRequestResize`.

PropType:| arrayOf(element)
---|---
Required:| no

actionsColumnWidth

Specifies the width of the actions column. Adds an empty header for row actions if no table-level actions are present.

PropType:| number
---|---
Required:| no

children

Must be `Table.Head`, `Table.Body`, or `Table.Caption`.

PropType:| node
---|---
Required:| no

dockOffset

Sets the offset from the top of the window. Only applies when `headType` is 'docked'.

PropType:| number
---|---
Required:| no

dockScrollBar

Docks the horizontal scroll bar at the bottom of the window when the bottom of the table is below the viewport.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

headType

Sets the table head type:

  * `docked`: The head is docked against the window
  * `fixed` : The head is fixed in the table. The table can scroll independently from the head.
  * `inline`: The head isn't fixed, but can scroll with the rest of the table.



PropType:| oneOf('docked', 'fixed', 'inline')
---|---
Required:| no

innerStyle

Style specification for the inner container, which is the scrolling container.

PropType:| object
---|---
Required:| no

onRequestMoveColumn

An event handler for handle the re-order action of Table. The function is passed an options object with `fromIndex` and `toIndex`.

PropType:| func
---|---
Required:| no

onRequestMoveRow

An event handler to handle the reorder rows action of Table. The function is passed an options object with `fromIndex` and `toIndex`.

PropType:| func
---|---
Required:| no

onRequestResizeColumn

An event handler for resize of columns for the current column being resized. The function is passed an event and a data object with `columnId`, `id`, `index`, and `width`.

PropType:| func
---|---
Required:| no

onRequestToggleAllRows

Callback invoked when a user clicks the row selection toggle in the header.

PropType:| func
---|---
Required:| no

onScroll

Callback invoked when a scroll event occurs on the inner scrolling container.

PropType:| func
---|---
Required:| no

outerStyle

Style specification for the outer container.

PropType:| object
---|---
Required:| no

primaryColumnIndex

Indicates the column to use as the primary label for each row.

PropType:| number
---|---
Required:| no

resizableFillLayout

Table will fill parent container. Resizable columns can have a `width` of `auto` only with this prop enabled.

PropType:| bool
---|---
Required:| no

rowExpansion

Adds a column to the table with an expansion button for each row that has expansion content. Supported values:

  * `single`: Only one row can be expanded at a time. If another expansion button is clicked, the currently expanded row closes and the new one opens.
  * `multi`: Allows multiple rows to be expanded at the same time.
  * `controlled`: Allows the expanded state to be externally managed by `expanded` prop of `Row`.
  * `none`: The default with no row expansion.



PropType:| oneOf('single', 'multi', 'controlled', 'none')
---|---
Required:| no

rowSelection

When an `onRequestToggleAllRows` handler is defined, this prop determines the appearance of the toggle all rows button.

PropType:| oneOf('all', 'some', 'none')
---|---
Required:| no

stripeRows

Alternate rows are given a darker background to improve readability.

PropType:| bool
---|---
Required:| no

tableStyle

The style attribute for the table. This is primarily useful for setting the CSS table-layout property.

PropType:| object
---|---
Required:| no

#### Props

actions

Adds table-level actions. Not compatible with `onRequestResize`.

PropType:| arrayOf(element)
---|---
Required:| no

actionsColumnWidth

Specifies the width of the actions column. Adds an empty header for row actions if no table-level actions are present.

PropType:| number
---|---
Required:| no

children

Must be `Table.Head`, `Table.Body`, or `Table.Caption`.

PropType:| node
---|---
Required:| no

dockOffset

Sets the offset from the top of the window. Only applies when `headType` is 'docked'.

PropType:| number
---|---
Required:| no

dockScrollBar

Docks the horizontal scroll bar at the bottom of the window when the bottom of the table is below the viewport.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

headType

Sets the table head type:

  * `docked`: The head is docked against the window
  * `fixed` : The head is fixed in the table. The table can scroll independently from the head.
  * `inline`: The head isn't fixed, but can scroll with the rest of the table.



PropType:| oneOf('docked', 'fixed', 'inline')
---|---
Required:| no

innerStyle

Style specification for the inner container, which is the scrolling container.

PropType:| object
---|---
Required:| no

onRequestMoveColumn

An event handler for handle the re-order action of Table. The function is passed an options object with `fromIndex` and `toIndex`.

PropType:| func
---|---
Required:| no

onRequestMoveRow

An event handler to handle the reorder rows action of Table. The function is passed an options object with `fromIndex` and `toIndex`.

PropType:| func
---|---
Required:| no

onRequestResizeColumn

An event handler for resize of columns for the current column being resized. The function is passed an event and a data object with `columnId`, `id`, `index`, and `width`.

PropType:| func
---|---
Required:| no

onRequestToggleAllRows

Callback invoked when a user clicks the row selection toggle in the header.

PropType:| func
---|---
Required:| no

onScroll

Callback invoked when a scroll event occurs on the inner scrolling container.

PropType:| func
---|---
Required:| no

outerStyle

Style specification for the outer container.

PropType:| object
---|---
Required:| no

primaryColumnIndex

Indicates the column to use as the primary label for each row.

PropType:| number
---|---
Required:| no

resizableFillLayout

Table will fill parent container. Resizable columns can have a `width` of `auto` only with this prop enabled.

PropType:| bool
---|---
Required:| no

rowExpansion

Adds a column to the table with an expansion button for each row that has expansion content. Supported values:

  * `single`: Only one row can be expanded at a time. If another expansion button is clicked, the currently expanded row closes and the new one opens.
  * `multi`: Allows multiple rows to be expanded at the same time.
  * `controlled`: Allows the expanded state to be externally managed by `expanded` prop of `Row`.
  * `none`: The default with no row expansion.



PropType:| oneOf('single', 'multi', 'controlled', 'none')
---|---
Required:| no

rowSelection

When an `onRequestToggleAllRows` handler is defined, this prop determines the appearance of the toggle all rows button.

PropType:| oneOf('all', 'some', 'none')
---|---
Required:| no

stripeRows

Alternate rows are given a darker background to improve readability.

PropType:| bool
---|---
Required:| no

tableStyle

The style attribute for the table. This is primarily useful for setting the CSS table-layout property.

PropType:| object
---|---
Required:| no

### Table.Head API

#### Props

children

Must be `Table.HeadCell`s or `Table.HeadDropdownCell`s.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

Must be `Table.HeadCell`s or `Table.HeadDropdownCell`s.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

### Table.Body API

#### Props

children

Must be `Table.Row`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

Must be `Table.Row`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

### Table.Row API

#### Props

actionPrimary

Adds primary actions. For best results, use an icon-only button style. The `onClick` handler of each action is passed the event and the `data` prop of this row.

PropType:| element
---|---
Required:| no

actionsSecondary

Adds a secondary actions dropdown menu. This prop must be a `Menu`. The `onClick` handler of each action is passed the event and the `data` prop of this row.

PropType:| element
---|---
Required:| no

children

Must be `Table.Cell`.

PropType:| node
---|---
Required:| no

data

This data is returned with the onClick and toggle events as the second argument.

PropType:| any
---|---
Required:| no

disabled

Indicates whether the row selection is disabled.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

expanded

Allows row expansion to be controlled programmatically if the `rowExpansion` prop is set to `controlled` in `Table`.

PropType:| bool
---|---
Required:| no

expansionRow

An optional row that is displayed when this row is expanded, or an array of rows.

PropType:| oneOfType(element, arrayOf(element))
---|---
Required:| no

onClick

Providing an `onClick` handler enables focus, hover, and related styles.

PropType:| func
---|---
Required:| no

onExpansion

An event handler that triggers when the row expansion element is selected.

PropType:| func
---|---
Required:| no

onRequestToggle

An event handler for toggle of the row. resize of columns. The function is passed the event and the `data` prop for this row.

PropType:| func
---|---
Required:| no

rowScreenReaderText

Indicates the row's label when selected or unselected.

PropType:| string
---|---
Required:| no

selected

When an `onRequestToggle` handler is defined, this prop determines the appearance of the toggle.

PropType:| bool
---|---
Required:| no

#### Props

actionPrimary

Adds primary actions. For best results, use an icon-only button style. The `onClick` handler of each action is passed the event and the `data` prop of this row.

PropType:| element
---|---
Required:| no

actionsSecondary

Adds a secondary actions dropdown menu. This prop must be a `Menu`. The `onClick` handler of each action is passed the event and the `data` prop of this row.

PropType:| element
---|---
Required:| no

children

Must be `Table.Cell`.

PropType:| node
---|---
Required:| no

data

This data is returned with the onClick and toggle events as the second argument.

PropType:| any
---|---
Required:| no

disabled

Indicates whether the row selection is disabled.

PropType:| bool
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

expanded

Allows row expansion to be controlled programmatically if the `rowExpansion` prop is set to `controlled` in `Table`.

PropType:| bool
---|---
Required:| no

expansionRow

An optional row that is displayed when this row is expanded, or an array of rows.

PropType:| oneOfType(element, arrayOf(element))
---|---
Required:| no

onClick

Providing an `onClick` handler enables focus, hover, and related styles.

PropType:| func
---|---
Required:| no

onExpansion

An event handler that triggers when the row expansion element is selected.

PropType:| func
---|---
Required:| no

onRequestToggle

An event handler for toggle of the row. resize of columns. The function is passed the event and the `data` prop for this row.

PropType:| func
---|---
Required:| no

rowScreenReaderText

Indicates the row's label when selected or unselected.

PropType:| string
---|---
Required:| no

selected

When an `onRequestToggle` handler is defined, this prop determines the appearance of the toggle.

PropType:| bool
---|---
Required:| no

### Table.Cell API

#### Props

align

Align the text in the cell.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

children

PropType:| node
---|---
Required:| no

data

This data is returned with the onClick events as the second argument.

PropType:| any
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

onClick

Providing an `onClick` handler enables focus, hover, and related styles.

PropType:| func
---|---
Required:| no

#### Props

align

Align the text in the cell.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

children

PropType:| node
---|---
Required:| no

data

This data is returned with the onClick events as the second argument.

PropType:| any
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

onClick

Providing an `onClick` handler enables focus, hover, and related styles.

PropType:| func
---|---
Required:| no

### Table.HeadCell API

#### Props

align

Align the text in the label.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

children

PropType:| node
---|---
Required:| no

columnId

An id that is passed to the `onSort` callback and as `Table`'s `onRequestResizeColumn` callback.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

headCellScreenReaderText

A string used to generate the `aria-label` for the head cell during column reordering.

When the `children` prop is not a string, providing `headCellScreenReaderText` is recommended to improve the screen reader announcements during the reordering interaction.

PropType:| string
---|---
Required:| no

onSort

A callback invoked when this head cell is clicked. If provided, this HeadCell is sortable and renders the appropriate user interface.

PropType:| func
---|---
Required:| no

resizable

Allows the user to resize the column when onRequestResize is passed to the `Table`. Set resizable to `false` to prevent some columns for resizing.

PropType:| bool
---|---
Default:| true
Required:| no

sortDir

The current sort direction of this column.

PropType:| oneOf('asc', 'desc', 'none')
---|---
Default:| 'none'
Required:| no

sortKey

The `sortKey` is passed in the data object to the `onSort` callback, if provided.

PropType:| string
---|---
Required:| no

tooltip

Content to show in a tooltip.

PropType:| node
---|---
Required:| no

truncate

Truncate the text in the label.

PropType:| bool
---|---
Default:| true
Required:| no

width

The width of the column in pixels.

PropType:| oneOfType(number, oneOf('auto'))
---|---
Required:| no

#### Props

align

Align the text in the label.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

children

PropType:| node
---|---
Required:| no

columnId

An id that is passed to the `onSort` callback and as `Table`'s `onRequestResizeColumn` callback.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

headCellScreenReaderText

A string used to generate the `aria-label` for the head cell during column reordering.

When the `children` prop is not a string, providing `headCellScreenReaderText` is recommended to improve the screen reader announcements during the reordering interaction.

PropType:| string
---|---
Required:| no

onSort

A callback invoked when this head cell is clicked. If provided, this HeadCell is sortable and renders the appropriate user interface.

PropType:| func
---|---
Required:| no

resizable

Allows the user to resize the column when onRequestResize is passed to the `Table`. Set resizable to `false` to prevent some columns for resizing.

PropType:| bool
---|---
Default:| true
Required:| no

sortDir

The current sort direction of this column.

PropType:| oneOf('asc', 'desc', 'none')
---|---
Default:| 'none'
Required:| no

sortKey

The `sortKey` is passed in the data object to the `onSort` callback, if provided.

PropType:| string
---|---
Required:| no

tooltip

Content to show in a tooltip.

PropType:| node
---|---
Required:| no

truncate

Truncate the text in the label.

PropType:| bool
---|---
Default:| true
Required:| no

width

The width of the column in pixels.

PropType:| oneOfType(number, oneOf('auto'))
---|---
Required:| no

### Table.HeadDropdownCell API

#### Props

align

Align the text in the label.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

buttonRef

A React ref which is set to the button element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

canCoverHead

If there is not enough room to render the `Popover` in a direction, this option enables it to be rendered over the Head.

PropType:| bool
---|---
Default:| true
Required:| no

children

PropType:| node
---|---
Required:| yes

closeReasons

An array of reasons for which this `Popover` should close.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no

columnId

An id that is passed to the `onRequestOpen`, `onRequestClose` callback and as `Table`'s `onRequestResizeColumn` callback.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusToggleReasons

An array of reasons for which to set focus on the toggle. Only subset of `closeReasons` will be honored. When Menu.Items open a Modal or other dialog, it may be necessary to remove the 'contentClick' reason to allow focus to be passed to the dialog.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'toggleClick', ]
Required:| no

headCellScreenReaderText

A string used to generate the `aria-label` for the head cell during column reordering.

When the `label` prop is not a string, providing `headCellScreenReaderText` is recommended to improve the screen reader announcements during the reordering interaction.

PropType:| string
---|---
Required:| no

label

The label on the heading, which may simply be text or may contain an element with icons or other markup.

PropType:| node
---|---
Required:| no

onRequestClose

A callback function invoked with a data object containing the event (if applicable) and a reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

A callback function invoked with a data object containing the event. (The reason is always toggleClick).

PropType:| func
---|---
Required:| no

open

If an open prop is provided, this component will behave as a controlled component(Opens new window). This means that the consumer is responsible for handling the open/close state. If no open prop is provided, the component will handle the open/close state internally.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no

resizable

Allow the user to resize the column when onRequestResize is passed to the `Table`. Set resizable to false to prevent some columns for resizing.

PropType:| bool
---|---
Default:| true
Required:| no

retainFocus

Keep focus within the Popover while open. Note, Menu handles it's own focus by default, so this is only necessary when the popover contains other types of content.

PropType:| bool
---|---
Required:| no

takeFocus

When true, the Popover will automatically take focus when 'open' changes to true. Disable this for a Popover that has shows on hover, such as a tooltip.

PropType:| bool
---|---
Default:| true
Required:| no

truncate

Truncate the text in the label. `truncate=false` is not compatible with `Table`'s `onRequestResize`.

PropType:| bool
---|---
Default:| true
Required:| no

width

The width of the column in pixels.

PropType:| number
---|---
Required:| no

#### Props

align

Align the text in the label.

PropType:| oneOf('left', 'center', 'right')
---|---
Default:| 'left'
Required:| no

buttonRef

A React ref which is set to the button element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

canCoverHead

If there is not enough room to render the `Popover` in a direction, this option enables it to be rendered over the Head.

PropType:| bool
---|---
Default:| true
Required:| no

children

PropType:| node
---|---
Required:| yes

closeReasons

An array of reasons for which this `Popover` should close.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick', ]
Required:| no

columnId

An id that is passed to the `onRequestOpen`, `onRequestClose` callback and as `Table`'s `onRequestResizeColumn` callback.

PropType:| string
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

focusToggleReasons

An array of reasons for which to set focus on the toggle. Only subset of `closeReasons` will be honored. When Menu.Items open a Modal or other dialog, it may be necessary to remove the 'contentClick' reason to allow focus to be passed to the dialog.

PropType:| arrayOf(oneOf('clickAway', 'contentClick', 'escapeKey', 'offScreen', 'tabKey', 'toggleClick'))
---|---
Default:| [ 'contentClick', 'escapeKey', 'toggleClick', ]
Required:| no

headCellScreenReaderText

A string used to generate the `aria-label` for the head cell during column reordering.

When the `label` prop is not a string, providing `headCellScreenReaderText` is recommended to improve the screen reader announcements during the reordering interaction.

PropType:| string
---|---
Required:| no

label

The label on the heading, which may simply be text or may contain an element with icons or other markup.

PropType:| node
---|---
Required:| no

onRequestClose

A callback function invoked with a data object containing the event (if applicable) and a reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

A callback function invoked with a data object containing the event. (The reason is always toggleClick).

PropType:| func
---|---
Required:| no

open

If an open prop is provided, this component will behave as a controlled component(Opens new window). This means that the consumer is responsible for handling the open/close state. If no open prop is provided, the component will handle the open/close state internally.

PropType:| bool
---|---
Required:| no

repositionMode

See `repositionMode` on `Popover` for details.

PropType:| oneOf('none', 'flip', 'any')
---|---
Default:| 'flip'
Required:| no

resizable

Allow the user to resize the column when onRequestResize is passed to the `Table`. Set resizable to false to prevent some columns for resizing.

PropType:| bool
---|---
Default:| true
Required:| no

retainFocus

Keep focus within the Popover while open. Note, Menu handles it's own focus by default, so this is only necessary when the popover contains other types of content.

PropType:| bool
---|---
Required:| no

takeFocus

When true, the Popover will automatically take focus when 'open' changes to true. Disable this for a Popover that has shows on hover, such as a tooltip.

PropType:| bool
---|---
Default:| true
Required:| no

truncate

Truncate the text in the label. `truncate=false` is not compatible with `Table`'s `onRequestResize`.

PropType:| bool
---|---
Default:| true
Required:| no

width

The width of the column in pixels.

PropType:| number
---|---
Required:| no

### Table.Caption API

Tables that use a docked header must place the caption on the bottom side. Tables that use a fixed header cannot use captions.

#### Props

children

PropType:| node
---|---
Required:| yes

side

The location of the caption relative to the table.

PropType:| oneOf('top', 'bottom')
---|---
Default:| 'top'
Required:| no

#### Props

children

PropType:| node
---|---
Required:| yes

side

The location of the caption relative to the table.

PropType:| oneOf('top', 'bottom')
---|---
Default:| 'top'
Required:| no

## Test Hooks

#### Element Selectors

table

The root of the `Table`.

Example:| [data-test="table"]
---|---
Attribute:| data-test
Value:| table
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

head

Matches the `Table.Head`.

Example:| [data-test="table"] [data-test="head"]
---|---
Attribute:| data-test
Value:| head
Scope Describes where to look for the element.:| In the `Table` root.

fixed-head

Available when `headType` is `fixed`. Matches the `Table.Head` that is detached from the main table and must be used instead of `head` for most interactions.

Example:| [data-test="table"] [data-test="fixed-head"]
---|---
Attribute:| data-test
Value:| fixed-head
Scope Describes where to look for the element.:| In the `Table` root.

docked-head

Matches the detached `Table.Head` when available. Available when `headType` is `docked` and the detached head is rendered based on positional calculations. Use `detached-head` instead of `head` for most interactions when it is rendered.

Example:| [data-test="table"] [data-test="docked-head"]
---|---
Attribute:| data-test
Value:| docked-head
Scope Describes where to look for the element.:| In the `Table` root.

body

Matches the `Table.Body`.

Example:| [data-test="table"] [data-test="body"]
---|---
Attribute:| data-test
Value:| body
Scope Describes where to look for the element.:| In the `Table` root.

toggle-all

Matches the select all rows toggle.

Example:| [data-test="table"] [data-test="toggle-all"]
---|---
Attribute:| data-test
Value:| toggle-all
Scope Describes where to look for the element.:| In the `Table`.

head-cell (generic)

Matches all `Table.HeadCell`s and `Table.HeadDropdownCell`s.

Example:| [data-test="table"] [data-test="head"] [data-test="head-cell"]
---|---
Attribute:| data-test
Value:| head-cell
Scope Describes where to look for the element.:| In the `head`, `fixed-head`, or `docked-head`.

head-cell (specific)

Matches specific `Table.HeadCell`s and `Table.HeadDropdownCell`s with its label.

Example:| [data-test="table"] [data-test="head"] [data-test="head-cell"][data-test-label="specific-head-cell-label"]
---|---
Attribute:| data-test
Value:| data-test-label
Scope Describes where to look for the element.:| In the `head`, `fixed-head`, or `docked-head`.

resize

Matches the resize element of the `Table.HeadCell`.

Example:| [data-test="table"] [data-test="head"] [data-test="specific-head-cell"] [data-test="resize"]
---|---
Attribute:| data-test
Value:| resize
Scope Describes where to look for the element.:| In the `Table.HeadCell`.

row (generic)

Matches all `Table.Row`s.

Example:| [data-test="table"] [data-test="body"] [data-test="row"]
---|---
Attribute:| data-test
Value:| row
Scope Describes where to look for the element.:| In the `Table.Body`.

cell (generic)

Matches all `Table.Cell`s.

Example:| [data-test="table"] [data-test="body"] [data-test="cell"]
---|---
Attribute:| data-test
Value:| cell
Scope Describes where to look for the element.:| In the `Table.Row`.

expand

Matches the row expansion cell.

Example:| [data-test="table"] [data-test="body"] [data-test="specific-row"] [data-test="expand"]
---|---
Attribute:| data-test
Value:| expand
Scope Describes where to look for the element.:| In the `Table.Row`.

toggle

Matches the row selection toggle.

Example:| [data-test="table"] [data-test="body"] [data-test="specific-row"] [data-test="toggle"]
---|---
Attribute:| data-test
Value:| toggle
Scope Describes where to look for the element.:| In the `Table.Row`.

row-actions

Matches the row actions cell.

Example:| [data-test="table"] [data-test="body"] [data-test="specific-row"] [data-test="row-actions"]
---|---
Attribute:| data-test
Value:| row-actions
Scope Describes where to look for the element.:| In the `Table.Row`.

actions-secondary-toggle

Matches the secondary row actions toggle.

Example:| [data-test="table"] [data-test="body"] [data-test="specific-row"] [data-test="actions-secondary-toggle"]
---|---
Attribute:| data-test
Value:| actions-secondary-toggle
Scope Describes where to look for the element.:| In the `Table.Row`.

caption

Matches the table caption.

Example:| [data-test="table"] [data-test="caption"]
---|---
Attribute:| data-test
Value:| caption
Scope Describes where to look for the element.:| In the `Table` root.

`import React, { useState, useCallback } from 'react'; import Cog from '@splunk/react-icons/Cog'; import Pencil from '@splunk/react-icons/Pencil'; import Button from '@splunk/react-ui/Button'; import DL, { Term as DT, Description as DD } from '@splunk/react-ui/DefinitionList'; import Dropdown from '@splunk/react-ui/Dropdown'; import Menu from '@splunk/react-ui/Menu'; import Table from '@splunk/react-ui/Table'; import Tooltip from '@splunk/react-ui/Tooltip'; import Typography from '@splunk/react-ui/Typography'; import { _ } from '@splunk/ui-utils/i18n'; const initialData = [ { name: 'Rylan', age: 42, email: 'Angelita_Weimann42@gmail.com', state: 'CA', country: 'US', favoriteColor: 'Orange', favoriteDay: 'Monday', occupation: 'Engineer', industry: 'Software Development', }, { name: 'Amelia', age: 24, email: 'Dexter.Trantow57@hotmail.com', state: 'NY', country: 'US', favoriteColor: 'White', favoriteDay: 'Friday', occupation: 'Engineer', industry: 'Software', }, { name: 'Estevan', age: 56, email: 'Aimee7@hotmail.com', state: 'IL', country: 'US', favoriteColor: 'Green', favoriteDay: 'Saturday', occupation: 'Engineer', industry: 'Software', }, { name: 'Florence', age: 71, email: 'Jarrod.Bernier13@yahoo.com', state: 'CA', country: 'US', favoriteColor: 'Red', favoriteDay: 'Tuesday', occupation: 'Engineer', industry: 'Software', }, { name: 'Teresa', age: 38, email: 'Yadira1@hotmail.com', state: 'NJ', country: 'US', favoriteColor: 'Blue', favoriteDay: 'Wednesday', occupation: 'Engineer', industry: 'Software', }, ]; const initialColumns = [ { name: 'name', label: 'Name', visible: true }, { name: 'age', label: 'Age', visible: true }, { name: 'email', label: 'Email', visible: true }, { name: 'state', label: 'State', visible: true }, { name: 'country', label: 'Country', visible: true }, { name: 'favoriteColor', label: 'Favorite Color', visible: true }, { name: 'favoriteDay', label: 'Favorite Day', visible: true }, { name: 'occupation', label: 'Occupation', visible: true }, { name: 'industry', label: 'Industry', visible: true }, ]; function RowAction() { const [data] = useState(initialData); const [columns, setColumns] = useState(initialColumns); const [primaryAction, setPrimaryAction] = useState(); const [primaryActionRowData, setPrimaryActionRowData] = useState(); const [secondaryAction, setSecondaryAction] = useState(); const [secondaryActionRowData, setSecondaryActionRowData] = useState(); const handleShowHide = useCallback((e, { name }) => { setColumns((prevColumns) => prevColumns.map((col) => (col.name === name ? { ...col, visible: !col.visible } : col)) ); }, []); const handleEditActionClick = useCallback((e, rowData) => { setPrimaryAction('Edit'); setPrimaryActionRowData(JSON.stringify(rowData)); }, []); const handleSaveActionClick = useCallback((e, rowData) => { setSecondaryAction('Save'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const handleAddActionClick = useCallback((e, rowData) => { setSecondaryAction('Add'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const handleDeleteActionClick = useCallback((e, rowData) => { setSecondaryAction('Delete'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const toggle = ( <Button appearance="subtle" data-test="actions-toggle" icon={<Cog variant="filled" />} /> ); const actions = [ <Dropdown toggle={toggle} key="settings"> <Menu> <Menu.Heading>Show/Hide Columns</Menu.Heading> {columns.map((col) => ( <Menu.Item key={col.name} selectable selected={col.visible} onClick={(e) => handleShowHide(e, { name: col.name })} > {col.label} </Menu.Item> ))} <Menu.Divider /> <Menu.Heading>More actions</Menu.Heading> <Menu.Item>Add new item</Menu.Item> </Menu> </Dropdown>, ]; const rowActionPrimaryButton = ( <Tooltip content={_('Edit')} contentRelationship="label" onClick={handleEditActionClick} style={{ marginRight: 8 }} > <Button appearance="subtle" icon={<Pencil variant="filled" />} /> </Tooltip> ); const rowActionsSecondaryMenu = ( <Menu> <Menu.Item onClick={handleSaveActionClick}>Save</Menu.Item> <Menu.Item onClick={handleAddActionClick}>Add</Menu.Item> <Menu.Item onClick={handleDeleteActionClick}>Delete</Menu.Item> </Menu> ); return ( <div> <Table actions={actions} actionsColumnWidth={104}> <Table.Head> {columns.map( (c) => c.visible && <Table.HeadCell key={c.name}>{c.label}</Table.HeadCell> )} </Table.Head> <Table.Body> {data.map((row) => ( <Table.Row data={row} key={row.email} onClick={() => {}} actionPrimary={rowActionPrimaryButton} actionsSecondary={rowActionsSecondaryMenu} > {columns.map( (c) => c.visible && <Table.Cell key={c.name}>{row[c.name]}</Table.Cell> )} </Table.Row> ))} </Table.Body> </Table> <aside style={{ marginTop: 20 }} aria-live="polite" aria-relevant="text"> <Typography as="p"> Click a primary action or secondary action to see the returned data  </Typography> {primaryActionRowData && ( <div style={{ overflow: 'scroll', marginBottom: 10 }}> <DL> <DT>Primary action:</DT> <DD>&apos;{primaryAction}&apos;</DD> <DT>Data:</DT> <DD> <code>{primaryActionRowData}</code> </DD> </DL> </div> )} {secondaryActionRowData && ( <div style={{ overflow: 'scroll' }}> <DL> <DT>Secondary action:</DT> <DD>&apos;{secondaryAction}&apos;</DD> <DT>Data:</DT> <DD> <code>{secondaryActionRowData}</code> </DD> </DL> </div> )} </aside> </div> ); } export default RowAction;` `import React, { useState, useCallback } from 'react'; import { cloneDeep } from 'lodash'; import Gear from '@splunk/react-icons/enterprise/Gear'; import Pencil from '@splunk/react-icons/enterprise/Pencil'; import Button from '@splunk/react-ui/Button'; import DL, { Term as DT, Description as DD } from '@splunk/react-ui/DefinitionList'; import Dropdown from '@splunk/react-ui/Dropdown'; import Menu from '@splunk/react-ui/Menu'; import Table from '@splunk/react-ui/Table'; import Tooltip from '@splunk/react-ui/Tooltip'; import Typography from '@splunk/react-ui/Typography'; import { _ } from '@splunk/ui-utils/i18n'; const initialHeaders = [ { label: 'Name', key: 'name', align: 'left', width: 180, minWidth: 80, visible: true, tooltip: 'Legal first name', }, { label: 'Status', key: 'status', align: 'left', width: 100, minWidth: 40, visible: true }, { label: 'Birth State', key: 'birthState', align: 'left', width: 120, minWidth: 40, visible: true, }, { label: 'Age', key: 'age', align: 'left', width: 100, minWidth: 40, visible: true }, { label: 'Email Address', key: 'email', align: 'left', width: 400, minWidth: 120, visible: true, }, ]; const initialData = [ { name: 'Rylan', status: 'single', birthState: 'HI', age: 12, email: 'Angelita_Weimann42@gmail.com', selected: false, disabled: true, }, { name: 'Amelia', status: 'married', birthState: 'UT', age: 23, email: 'Dexter.Trantow57@hotmail.com', selected: false, disabled: false, }, { name: 'Estevan', status: 'single', birthState: 'NY', age: 19, email: 'Aimee7@hotmail.com', selected: false, disabled: false, }, { name: 'Florence', status: 'single', birthState: 'AZ', age: 20, email: 'Jarrod.Bernier13@yahoo.com', selected: false, disabled: false, }, { name: 'Tressa', status: 'married', birthState: 'CA', age: 22, email: 'yadira1@hotmail.com', selected: false, disabled: false, }, { name: 'Bernice', status: 'single', birthState: 'TX', age: 17, email: 'bernice.Gilbert@gmail.com', selected: false, disabled: false, }, { name: 'Adrian', status: 'married', birthState: 'MA', age: 23, email: 'adrian7456@gmail.com', selected: false, disabled: false, }, { name: 'Ester', status: 'single', birthState: 'NY', age: 88, email: 'esternyc@gmail.com', selected: false, disabled: false, }, { name: 'Andrew', status: 'single', birthState: 'NM', age: 16, email: 'andrew.fillmore2@gmail.com', selected: false, disabled: false, }, { name: 'Felix', status: 'married', birthState: 'CA', age: 36, email: 'felixfelix@hotmail.com', selected: false, disabled: false, }, ]; function Complex() { const [headers, setHeaders] = useState(initialHeaders); const [data, setData] = useState(initialData); const [sortKey, setSortKey] = useState('name'); const [sortDir, setSortDir] = useState('asc'); const [activeRow, setActiveRow] = useState(undefined); const [activeRowData, setActiveRowData] = useState(undefined); const [primaryAction, setPrimaryAction] = useState(undefined); const [primaryActionRowData, setPrimaryActionRowData] = useState(undefined); const [secondaryAction, setSecondaryAction] = useState(undefined); const [secondaryActionRowData, setSecondaryActionRowData] = useState(undefined); const handleRequestMoveColumn = useCallback(({ fromIndex, toIndex }) => { setHeaders((prevHeaders) => { const updatedHeaders = cloneDeep(prevHeaders); const headerToMove = updatedHeaders[fromIndex]; const insertionIndex = toIndex < fromIndex ? toIndex : toIndex + 1; updatedHeaders.splice(insertionIndex, 0, headerToMove); const removalIndex = toIndex < fromIndex ? fromIndex + 1 : fromIndex; updatedHeaders.splice(removalIndex, 1); return updatedHeaders; }); }, []); const handleSort = useCallback( (e, { sortKey: newSortKey }) => { setSortKey((prevSortKey) => { const prevSortDir = prevSortKey === newSortKey ? sortDir : 'none'; const nextSortDir = prevSortDir === 'asc' ? 'desc' : 'asc'; setSortDir(nextSortDir); return newSortKey; }); }, [sortDir] ); const handleResizeColumn = useCallback( (event, { columnId, index, width }) => { setHeaders((prevHeaders) => { const updatedHeaders = cloneDeep(prevHeaders); // min and max widths can be controlled in the callback. const selectedColumn = updatedHeaders.find(({ key }) => key === columnId); if (selectedColumn) { const widthAboveMinimum = Math.max(width, selectedColumn.minWidth); updatedHeaders[index].width = widthAboveMinimum; return updatedHeaders; } return []; }); }, [setHeaders] ); const handleToggle = useCallback((event, { email }) => { setData((prevData) => { const updatedData = cloneDeep(prevData); const selectedRow = updatedData.find(({ email: rowEmail }) => rowEmail === email); if (selectedRow) { selectedRow.selected = !selectedRow.selected; return updatedData; } return []; }); }, []); const getRowSelectionState = useCallback((rowData) => { const selectedCount = rowData.filter((row) => row.selected).length; const disabledCount = rowData.filter((row) => row.disabled).length; if (selectedCount === 0) return 'none'; if (selectedCount + disabledCount === rowData.length) return 'all'; return 'some'; }, []); const handleToggleAll = useCallback(() => { setData((prevData) => { const updatedData = cloneDeep(prevData); const selected = getRowSelectionState(updatedData) !== 'all'; const finalData = updatedData.map((row) => ({ ...row, selected: row.disabled ? false : selected, })); return finalData; }); }, [getRowSelectionState]); const handleRowClick = useCallback((event, rowData) => { setActiveRow(rowData.name); setActiveRowData(JSON.stringify(rowData)); }, []); const handleShowHide = useCallback((e, { label }) => { setHeaders((prevHeaders) => prevHeaders.map((header) => header.label === label ? { ...header, visible: !header.visible } : header  ) ); }, []); const handleEditActionClick = useCallback((e, rowData) => { setPrimaryAction('Edit'); setPrimaryActionRowData(JSON.stringify(rowData)); }, []); const handleSaveActionClick = useCallback((e, rowData) => { setSecondaryAction('Save'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const handleAddActionClick = useCallback((e, rowData) => { setSecondaryAction('Add'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const handleDeleteActionClick = useCallback((e, rowData) => { setSecondaryAction('Delete'); setSecondaryActionRowData(JSON.stringify(rowData)); }, []); const toggle = ( <Button appearance="subtle" data-test="actions-toggle" icon={<Gear hideDefaultTooltip />} /> ); const actions = [ <Dropdown toggle={toggle} key="settings"> <Menu> <Menu.Heading>Show/Hide Columns</Menu.Heading> {headers.map((header) => ( <Menu.Item key={header.label} selectable selected={header.visible} onClick={(e) => handleShowHide(e, { label: header.label, }) } > {header.label} </Menu.Item> ))} <Menu.Divider /> <Menu.Heading>More actions</Menu.Heading> <Menu.Item>Add new item</Menu.Item> </Menu> </Dropdown>, ]; const rowActionPrimaryButton = ( <Tooltip content={_('Edit')} contentRelationship="label" onClick={handleEditActionClick} style={{ marginRight: 8 }} > <Button appearance="subtle" icon={<Pencil hideDefaultTooltip screenReaderText={null} />} /> </Tooltip> ); const rowActionsSecondaryMenu = ( <Menu> <Menu.Item onClick={handleSaveActionClick}>Save</Menu.Item> <Menu.Item onClick={handleAddActionClick}>Add</Menu.Item> <Menu.Item onClick={handleDeleteActionClick}>Delete</Menu.Item> </Menu> ); return ( <div> <Table onRequestMoveColumn={handleRequestMoveColumn} onRequestResizeColumn={handleResizeColumn} onRequestToggleAllRows={handleToggleAll} rowSelection={getRowSelectionState(data)} headType="fixed" innerStyle={{ maxHeight: 160 }} actions={actions} actionsColumnWidth={104} > <Table.Head> {headers.map((header) => ( <Table.HeadCell key={header.key} columnId={header.key} align={header.align} width={header.width} onSort={handleSort} sortKey={header.key} sortDir={header.key === sortKey ? sortDir : 'none'} tooltip={header.tooltip} > {header.label} </Table.HeadCell> ))} </Table.Head> <Table.Body> {data  .sort((rowA, rowB) => { if (sortDir === 'asc') { return rowA[sortKey] > rowB[sortKey] ? 1 : -1; } if (sortDir === 'desc') { return rowB[sortKey] > rowA[sortKey] ? 1 : -1; } return 0; }) .map((row) => ( <Table.Row key={row.email} actionPrimary={row.disabled ? undefined : rowActionPrimaryButton} actionsSecondary={ row.disabled ? undefined : rowActionsSecondaryMenu  } onRequestToggle={handleToggle} onClick={row.disabled ? undefined : handleRowClick} data={row} selected={row.selected} disabled={row.disabled} > {headers.map((header) => ( <Table.Cell key={`${row.email}-${header.key}`} align={header.align} > {row[header.key]} </Table.Cell> ))} </Table.Row> ))} </Table.Body> </Table> <aside style={{ marginTop: 20 }} aria-live="polite" aria-relevant="text"> <Typography as="p"> Click a primary action, secondary action, or row to see the returned data  </Typography> {activeRowData && ( <div style={{ overflow: 'scroll' }}> <DL> <DT>Row:</DT> <DD>&apos;{activeRow}&apos;</DD> <DT>Data:</DT> <DD> <code>{activeRowData}</code> </DD> </DL> </div> )} {primaryActionRowData && ( <div style={{ overflow: 'scroll', marginBottom: 10 }}> <DL> <DT>Primary action:</DT> <DD>&apos;{primaryAction}&apos;</DD> <DT>Data:</DT> <DD> <code>{primaryActionRowData}</code> </DD> </DL> </div> )} {secondaryActionRowData && ( <div style={{ overflow: 'scroll', marginBottom: 10 }}> <DL> <DT>Secondary action:</DT> <DD>&apos;{secondaryAction}&apos;</DD> <DT>Data:</DT> <DD> <code>{secondaryActionRowData}</code> </DD> </DL> </div> )} </aside> </div> ); } export default Complex;`

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Testing`

<!-- No content extracted -->

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Tooltip`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| number
---|---
Default:| 300
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOf('label', 'description')
---|---
Required:| no
PropType:| oneOf('above', 'below', 'left', 'right')
---|---
Default:| 'above'
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| oneOfType(oneOf('primary', 'secondary'), number)
---|---
Default:| 'primary'
Required:| no
PropType:| shape({x: number, y: number})
---|---
Required:| no
PropType:| func
---|---
Required:| no

### Tooltip API

The Tooltip component wraps arbitrary content to be displayed when the target element is hovered or focused.

#### Props

children

Provide a node to replace the default question mark. For accessibility, ensure that the child can take focus, and that it accepts a `describedBy` string prop which it places as `aria-describedby` on the appropriate internal element.

PropType:| node
---|---
Required:| no

closeDelay

Milliseconds to wait before the tooltip closes.

PropType:| number
---|---
Default:| 300
Required:| no

content

The content of the tooltip. If the content is falsy and the `open` prop is uncontrolled, the tooltip doesn't display.

PropType:| node
---|---
Required:| no

contentRelationship

Tooltips can define the primary label for controls, for example buttons with only an icon, or they can provide an auxiliary description to supplement a control's primary label. This relationship is conveyed to assistive technologies with either the `aria-labelledby` or `aria-describedby` properties. By default, tooltips are a description for their control and use `aria-describedby`. Set `contentRelationship` to `label` when the Tooltip's content is a primary label for the control.

PropType:| oneOf('label', 'description')
---|---
Required:| no

defaultPlacement

The default placement of the `Tooltip`. It might render in a different location if there is not enough space in the default direction.

PropType:| oneOf('above', 'below', 'left', 'right')
---|---
Default:| 'above'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Set inline to `false` when adding a tooltip to a block element.

PropType:| bool
---|---
Default:| true
Required:| no

onRequestClose

Callback function fired when the popover is requested to be closed.

@param {event} event Can be `null` depending on the reason the tooltip is closing. @param {object} data @param {string} data.reason The reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

Callback function fired when the popover is requested to be opened.

@param {event} event @param {object} data @param {string} data.reason The reason for the open request.

PropType:| func
---|---
Required:| no

open

Whether or not the tooltip is shown. Setting this value makes the prop controlled. The onRequestClose and onRequestOpen callbacks are usually used.

PropType:| bool
---|---
Required:| no

openDelay

Milliseconds to wait before the tooltip opens.

PropType:| oneOfType(oneOf('primary', 'secondary'), number)
---|---
Default:| 'primary'
Required:| no

pointTo

Allows the `Tooltip` to point to and align with a different part of the anchor.

This prop is forwarded to Popover. See `Popover`'s `pointTo` prop for more information.

PropType:| shape({x: number, y: number})
---|---
Required:| no

renderAnchor

A function for rendering the element that the tooltip is bound to. If both `renderAnchor` and `children` are passed, `children` will be ignored. The function gets as input props object for the anchor, which contains the necessary event listeners and aria attributes. By default or if `contentRelationship` is passed as `description`, the props object contains keys `aria-describedby` and `describedBy`, but if `contentRelationship` is passed as `label`, `aria-labelledby` and `labelledBy` will be passed instead.

@param {object} props @param {function} props.onFocus @param {function} props.onBlur @param {function} props.onClick @param {string} props['aria-describedby'] @param {string} props.describedBy @param {string} props['aria-labelledby'] @param {string} props.labelledBy @param {"toggle"} props.['data-test'] @param {function} props.elementRef

PropType:| func
---|---
Required:| no

#### Props

children

Provide a node to replace the default question mark. For accessibility, ensure that the child can take focus, and that it accepts a `describedBy` string prop which it places as `aria-describedby` on the appropriate internal element.

PropType:| node
---|---
Required:| no

closeDelay

Milliseconds to wait before the tooltip closes.

PropType:| number
---|---
Default:| 300
Required:| no

content

The content of the tooltip. If the content is falsy and the `open` prop is uncontrolled, the tooltip doesn't display.

PropType:| node
---|---
Required:| no

contentRelationship

Tooltips can define the primary label for controls, for example buttons with only an icon, or they can provide an auxiliary description to supplement a control's primary label. This relationship is conveyed to assistive technologies with either the `aria-labelledby` or `aria-describedby` properties. By default, tooltips are a description for their control and use `aria-describedby`. Set `contentRelationship` to `label` when the Tooltip's content is a primary label for the control.

PropType:| oneOf('label', 'description')
---|---
Required:| no

defaultPlacement

The default placement of the `Tooltip`. It might render in a different location if there is not enough space in the default direction.

PropType:| oneOf('above', 'below', 'left', 'right')
---|---
Default:| 'above'
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

inline

Set inline to `false` when adding a tooltip to a block element.

PropType:| bool
---|---
Default:| true
Required:| no

onRequestClose

Callback function fired when the popover is requested to be closed.

@param {event} event Can be `null` depending on the reason the tooltip is closing. @param {object} data @param {string} data.reason The reason for the close request.

PropType:| func
---|---
Required:| no

onRequestOpen

Callback function fired when the popover is requested to be opened.

@param {event} event @param {object} data @param {string} data.reason The reason for the open request.

PropType:| func
---|---
Required:| no

open

Whether or not the tooltip is shown. Setting this value makes the prop controlled. The onRequestClose and onRequestOpen callbacks are usually used.

PropType:| bool
---|---
Required:| no

openDelay

Milliseconds to wait before the tooltip opens.

PropType:| oneOfType(oneOf('primary', 'secondary'), number)
---|---
Default:| 'primary'
Required:| no

pointTo

Allows the `Tooltip` to point to and align with a different part of the anchor.

This prop is forwarded to Popover. See `Popover`'s `pointTo` prop for more information.

PropType:| shape({x: number, y: number})
---|---
Required:| no

renderAnchor

A function for rendering the element that the tooltip is bound to. If both `renderAnchor` and `children` are passed, `children` will be ignored. The function gets as input props object for the anchor, which contains the necessary event listeners and aria attributes. By default or if `contentRelationship` is passed as `description`, the props object contains keys `aria-describedby` and `describedBy`, but if `contentRelationship` is passed as `label`, `aria-labelledby` and `labelledBy` will be passed instead.

@param {object} props @param {function} props.onFocus @param {function} props.onBlur @param {function} props.onClick @param {string} props['aria-describedby'] @param {string} props.describedBy @param {string} props['aria-labelledby'] @param {string} props.labelledBy @param {"toggle"} props.['data-test'] @param {function} props.elementRef

PropType:| func
---|---
Required:| no

## Test Hooks

#### Element Selectors

tooltip

The root of the `Tooltip`. Note that this attribute is not attached if the anchor element is rendered with the `renderAnchor` prop.

Example:| [data-test="tooltip"]
---|---
Attribute:| data-test
Value:| tooltip
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

toggle

Matches the toggle that triggers open and close events.

Example:| [data-test="tooltip"] [data-test="toggle"]
---|---
Attribute:| data-test
Value:| toggle
Scope Describes where to look for the element.:| In the `Tooltip` root.

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `Tree`

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| node
---|---
Required:| no
PropType:| bool
---|---
Default:| true
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| node
---|---
Required:| no
PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| bool
---|---
Required:| no
PropType:| string
---|---
Required:| yes
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no
PropType:| func
---|---
Required:| no

### Tree API

Used to present a hierarchical list.

#### Props

children

Should contain `Tree.Item`s, can also include other elements to display in between tree items.

PropType:| node
---|---
Required:| no

defaultIndent

Removes default indent from list styles if set to false.

PropType:| bool
---|---
Default:| true
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

#### Props

children

Should contain `Tree.Item`s, can also include other elements to display in between tree items.

PropType:| node
---|---
Required:| no

defaultIndent

Removes default indent from list styles if set to false.

PropType:| bool
---|---
Default:| true
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

### Tree.Item API

#### Props

children

Should contain `Tree.Item`s, can also include other elements to display in between tree items.

PropType:| node
---|---
Required:| no

content

Content to show on the `Tree.Item`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

expanded

Expansion state of the `Tree.Item`.

PropType:| bool
---|---
Required:| no

id

A unique `id` for this item and used by `Tree` to keep track of the focused item.

PropType:| string
---|---
Required:| yes

onFocus

PropType:| func
---|---
Required:| no

onKeyDown

PropType:| func
---|---
Required:| no

onToggleExpansion

Called on expansion state change of the `Tree.Item` and should be used to maintain `expanded`. For proper keyboard accessibility this is required when a `Tree.Item` has children.

PropType:| func
---|---
Required:| no

onToggleSelection

Called on selection state change of the `Tree.Item` and can be used to maintain optional external `Tree.Item` selection state.

PropType:| func
---|---
Required:| no

#### Props

children

Should contain `Tree.Item`s, can also include other elements to display in between tree items.

PropType:| node
---|---
Required:| no

content

Content to show on the `Tree.Item`.

PropType:| node
---|---
Required:| no

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

expanded

Expansion state of the `Tree.Item`.

PropType:| bool
---|---
Required:| no

id

A unique `id` for this item and used by `Tree` to keep track of the focused item.

PropType:| string
---|---
Required:| yes

onFocus

PropType:| func
---|---
Required:| no

onKeyDown

PropType:| func
---|---
Required:| no

onToggleExpansion

Called on expansion state change of the `Tree.Item` and should be used to maintain `expanded`. For proper keyboard accessibility this is required when a `Tree.Item` has children.

PropType:| func
---|---
Required:| no

onToggleSelection

Called on selection state change of the `Tree.Item` and can be used to maintain optional external `Tree.Item` selection state.

PropType:| func
---|---
Required:| no

## Test Hooks

#### Element Selectors

tree

The root of the `Tree`.

Example:| [data-test="tree"]
---|---
Attribute:| data-test
Value:| tree
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

tree-item

Matches all tree items in the `Tree`.

Example:| [data-test="tree"] [data-test="tree-item"]
---|---
Attribute:| data-test
Value:| node
Scope Describes where to look for the element.:| In the `Tree` root.

`import React, { useCallback, useMemo, useState } from 'react'; import styled from 'styled-components'; import ChevronDown from '@splunk/react-icons/ChevronDown'; import ChevronRight from '@splunk/react-icons/ChevronRight'; import Tree from '@splunk/react-ui/Tree'; import { variables } from '@splunk/themes'; const StyledExpansionToggleWrapper = styled.span` display: inline-flex; padding-inline-end: ${variables.spacingSmall}; width: 16px; `; const StyledSpan = styled.span` display: inline-flex; padding: ${variables.spacingXSmall} 0; `; const ExpansionToggle = ({ expanded, treeItemId, onToggleExpansion }) => ( // eslint-disable-next-line jsx-a11y/no-static-element-interactions, jsx-a11y/click-events-have-key-events <span onClick={(e) => { e.preventDefault(); onToggleExpansion?.(e, { treeItemId }); }} > {expanded ? <ChevronDown /> : <ChevronRight />} </span> ); const TreeItemWithExpansion = ({ children, content, expanded, id, onToggleExpansion, ...otherTreeItemProps }) => { const contentWithExpansion = useMemo(() => { const renderExpansionToggle = () => { if (!children) { return undefined; } return ( <ExpansionToggle expanded={expanded || false} onToggleExpansion={onToggleExpansion} treeItemId={id} /> ); }; return ( <StyledSpan> <StyledExpansionToggleWrapper> {renderExpansionToggle()} </StyledExpansionToggleWrapper> {content} </StyledSpan> ); }, [children, content, expanded, id, onToggleExpansion]); return ( <Tree.Item content={contentWithExpansion} expanded={expanded} id={id} onToggleExpansion={onToggleExpansion} {...otherTreeItemProps} > {children} </Tree.Item> ); }; export default function ClickableExpansion() { const [expandedIdsMap, setExpandedIdsMap] = useState( new Map([ ['two', true], ['three', true], ]) ); const handleToggleExpansion = useCallback((event, { treeItemId } = {}) => { if (!treeItemId) { return; } setExpandedIdsMap((prevMap) => { const newMap = new Map(prevMap); if (newMap.has(treeItemId)) { newMap.delete(treeItemId); } else { newMap.set(treeItemId, true); } return newMap; }); }, []); return ( <Tree data-test="tree-fixture"> <TreeItemWithExpansion content="node-0" id="one" /> <TreeItemWithExpansion content="node-1" id="two" expanded={expandedIdsMap.has('two')} onToggleExpansion={handleToggleExpansion} > <TreeItemWithExpansion content="node-1-0" id="three" expanded={expandedIdsMap.has('three')} onToggleExpansion={handleToggleExpansion} > <TreeItemWithExpansion content="node-1-0-0" id="four" /> <TreeItemWithExpansion content="node-1-0-1" id="five" /> </TreeItemWithExpansion> <TreeItemWithExpansion content="node-1-1" id="six" /> </TreeItemWithExpansion> <TreeItemWithExpansion content="node-2" id="seven" /> </Tree> ); }` `import React, { useCallback, useMemo, useRef, useState } from 'react'; import styled from 'styled-components'; import ChevronDown from '@splunk/react-icons/ChevronDown'; import ChevronRight from '@splunk/react-icons/ChevronRight'; import Checkbox from '@splunk/react-ui/Checkbox'; import Tree from '@splunk/react-ui/Tree'; import { variables } from '@splunk/themes'; const StyledExpansionToggleWrapper = styled.span` display: inline-flex; width: 16px; `; const StyledCheckbox = styled(Checkbox)` padding-inline: ${variables.spacingSmall}; `; const StyledSpan = styled.span` align-items: center; display: inline-flex; min-height: 100%; padding: ${variables.spacingXSmall} 0; `; const ExpansionToggle = ({ expanded, onToggleExpansion, treeItemId }) => ( // eslint-disable-next-line jsx-a11y/no-static-element-interactions, jsx-a11y/click-events-have-key-events <span onClick={(e) => { e.preventDefault(); onToggleExpansion?.(e, { treeItemId }); }} > {expanded ? <ChevronDown /> : <ChevronRight />} </span> ); const ItemSelectionCheckbox = ({ selected, onToggleSelection, treeItemId }) => ( // eslint-disable-next-line jsx-a11y/no-static-element-interactions, jsx-a11y/click-events-have-key-events <span onClick={(e) => { e.preventDefault(); onToggleSelection?.(e, { treeItemId }); }} style={{ display: 'inline-flex', userSelect: 'none' }} > <StyledCheckbox checked={selected} inert /> </span> ); const TreeItemWithExpansionAndSelection = ({ children, expanded, id, label, onToggleSelection, onToggleExpansion, selected, ...otherTreeItemProps }) => { const treeItemRef = useRef(null); const content = useMemo(() => { const renderExpansionToggle = () => { if (!children) { return undefined; } return ( <ExpansionToggle expanded={expanded || false} onToggleExpansion={onToggleExpansion} treeItemId={id} /> ); }; return ( <StyledSpan> <StyledExpansionToggleWrapper> {renderExpansionToggle()} </StyledExpansionToggleWrapper> <ItemSelectionCheckbox selected={selected} onToggleSelection={onToggleSelection} treeItemId={id} /> {label} </StyledSpan> ); }, [children, expanded, id, label, onToggleExpansion, onToggleSelection, selected]); return ( <Tree.Item aria-selected={selected ? 'true' : 'false'} content={content} elementRef={treeItemRef} expanded={expanded} id={id} onToggleExpansion={onToggleExpansion} onToggleSelection={onToggleSelection} {...otherTreeItemProps} > {children} </Tree.Item> ); }; export default function ClickableExpansionWithSelection() { const [expandedIdsMap, setExpandedIdsMap] = useState( new Map([ ['two', true], ['three', true], ]) ); const [selectedIdsMap, setSelectedIdsMap] = useState( new Map([ ['two', true], ['three', true], ]) ); const handleToggleExpansion = useCallback((event, { treeItemId } = {}) => { if (!treeItemId) { return; } setExpandedIdsMap((prevMap) => { const newMap = new Map(prevMap); if (newMap.has(treeItemId)) { newMap.delete(treeItemId); } else { newMap.set(treeItemId, true); } return newMap; }); }, []); const handleToggleSelected = useCallback((event, { treeItemId } = {}) => { if (!treeItemId) { return; } setSelectedIdsMap((prevMap) => { const newMap = new Map(prevMap); if (newMap.has(treeItemId)) { newMap.delete(treeItemId); } else { newMap.set(treeItemId, true); } return newMap; }); }, []); return ( <Tree aria-multiselectable="true" data-test="tree-fixture"> <TreeItemWithExpansionAndSelection id="one" label="node-0" onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('one')} /> <TreeItemWithExpansionAndSelection expanded={expandedIdsMap.has('two')} id="two" label="node-1" onToggleExpansion={handleToggleExpansion} onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('two')} > <TreeItemWithExpansionAndSelection id="three" expanded={expandedIdsMap.has('three')} label="node-1-0" onToggleExpansion={handleToggleExpansion} onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('three')} > <TreeItemWithExpansionAndSelection id="four" label="node-1-0-0" onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('four')} /> <TreeItemWithExpansionAndSelection id="five" label="node-1-0-1" onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('five')} /> </TreeItemWithExpansionAndSelection> <TreeItemWithExpansionAndSelection id="six" label="node-1-1" onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('six')} /> </TreeItemWithExpansionAndSelection> <TreeItemWithExpansionAndSelection id="seven" label="node-2" onToggleSelection={handleToggleSelected} selected={selectedIdsMap.has('seven')} /> </Tree> ); }`

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `useKeyPress`

<!-- No content extracted -->

---

## @splunk/react-ui - 5.3.0

**Package:** `react-ui` | **Component:** `WaitSpinner`

## Overview

Card Layout provides a container to responsively arrange and resize Cards.

## Examples

Card Layout provides a container to responsively arrange and resize Cards.

## API

PropType:| oneOfType(func, object)
---|---
Required:| no
PropType:| oneOfType(string, oneOf('null'))
---|---
Default:| _('Waiting')
Required:| no
PropType:| oneOf('small', 'medium', 'large')
---|---
Default:| 'small'
Required:| no

### WaitSpinner API

#### Props

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

screenReaderText

A string to display to screen readers. Set the prop to `null` or an empty string to hide the spinner from screen readers, such as when there is already a text label beside it.

PropType:| oneOfType(string, oneOf('null'))
---|---
Default:| _('Waiting')
Required:| no

size

Size of WaitSpinner.

PropType:| oneOf('small', 'medium', 'large')
---|---
Default:| 'small'
Required:| no

#### Props

elementRef

A React ref which is set to the DOM element when the component mounts and null when it unmounts.

PropType:| oneOfType(func, object)
---|---
Required:| no

screenReaderText

A string to display to screen readers. Set the prop to `null` or an empty string to hide the spinner from screen readers, such as when there is already a text label beside it.

PropType:| oneOfType(string, oneOf('null'))
---|---
Default:| _('Waiting')
Required:| no

size

Size of WaitSpinner.

PropType:| oneOf('small', 'medium', 'large')
---|---
Default:| 'small'
Required:| no

## Test Hooks

#### Element Selectors

wait-spinner

The root of the `WaitSpinner`.

Example:| [data-test="wait-spinner"]
---|---
Attribute:| data-test
Value:| wait-spinner
Scope Describes where to look for the element.:| This is the root element of the component. This selector should be used to scope selectors for elements within the component and to access the state attributes. The root selector can be overriden, and often should be, to uniquely identify a component.

---

# Accessibility Guidelines {#accessibility}

*Accessibility guidelines and best practices for inclusive design.*

## Splunk Design System

**Package:** `Accessibility` | **Component:** `Color`

# Color

## Why Color?

For sighted users, color is one of the first things that conveys meaning,
data, direction, and association. Color can guide the eye to issues that need
attention or can create instant peace of mind. However, not everyone sees
color the same due to various factors like genetics, health conditions, screen
calibration, culture, language, and more. Accessible design takes into account
these circumstances to ensure that the application of colors provides clarity
rather than confusion.

## Color Contrast

Sufficient color contrast is essential for many situations:

  * Low-contrast or low-vision users can accomplish their tasks
  * Content can be viewed from a distance, such as a dashboard on a TV monitor
  * Content can be viewed under extreme conditions, such as on a tablet outside on a bright day

One way of analyzing colors is through color contrast ratio. The ratio
contains two numbers, usually written as (# : 1), where the difference between
the numbers indicates how much relative brightness there is between a specific
sample’s foreground and background colors.

### Web Content Accessibility Guidelines (WCAG) 2.1 Recommends these Contrast
Ratio Guidelines:

  * **4.5:1 contrast ratio for:**
    * Functional text that is 14 pt or smaller
    * Focus border with border-width below 3px
  * **3:1 contrast ratio for:**
    * Text that is 14 pt bold or larger than 18 pt
    * Functional text within an image
    * Functional graphical elements such as an icon button, input border, checkbox, radio button
    * Focus border with border-width greater than or equal to 3px
  * **7:1 contrast ratio for:**
    * Text and images in high-contrast mode

For information about the difference between functional and decorative
elements, check out the [non-text content
documentation](/Community/Accessibility/NonTextContent).

### Disabled Elements

Note that disabled elements do not need to meet color contrast requirements;
this is a common false positive in automated accessibility testing. The
reasoning behind this is if an element is disabled, it shouldn’t be confused
for being active. You can check color contrast with a variety of tools. Splunk
UI Team prefers using [WebAIM (Accessibility in Mind) Color Contrast
Checker](https://webaim.org/resources/contrastchecker/) and [Colour Contrast
Analyzer from TGPi](https://www.tpgi.com/color-contrast-checker/).

## Color+

Everyone sees colors differently. Do not use color as the sole method of
conveying content or distinguishing between visual components. In addition to
using color, define interface elements by using assistive technology such as
alt-text or by using visual indicators other than color such as an underline
on a text link. Satisfy color+ by using the following elements:

  * **Text styling**. Use an underline or bold treatment for link text.
    * NOTE: Disregard this if the ratio of the surrounding text to the link is at least 3:1 and if on hover and focus, the link receives an additional distinction such as becoming underlined.
  * **Icons.** Include alt-text for users on screen readers.
  * **Text.** Avoid acronyms and jargon and use simple, concise language.
  * **Patterns.** In situations with many colors and high information density, like data visualizations, patterns provide a secondary visual alternative when text or icon usage is limited.

## Do’s and Don’ts

### DON’T:

  * Don’t only use color to convey meaning; not everyone sees the same colors.

  * Don’t rely on color for instructions.

### DO:

  * Use color+ to ensure that the spectrum of sighted users can understand the designs.

  * Check for sufficient color contrast with functional text, functional images, and graphical elements such as input borders, checkboxes, and icons.

  * Differentiate inline link text with underline, bold treatment, or an icon.

## Additional Resources

[WebAIM: Visual Disabilities](https://webaim.org/articles/visual/)

[Web Accessibility Perspectives: Colors with Good
Contrast](https://www.youtube.com/watch?v=Hui87z2Vx8o)

[Color Vision Deficiency Simulator](https://www.myndex.com/CVD/)

---

## Splunk Design System

**Package:** `Accessibility` | **Component:** `DataViz`

# A11y and Data Visualizations

As part of an inclusive design practice we need to consider accessibility in
the design of data visualization.

## Color

### Use [sufficient contrast](https://www.w3.org/TR/WCAG21/#contrast-minimum)

  * **Text:** Have you been in that scenario where a visualization on a screen or television has such a low contrast that you have to squint or, worse, walk over to the screen to read? Adequate text contrast increases scannability in low-light, high sun, and more conditions. Web Content Accessibility Guidelines (WCAG) recommends the following:
    * Text and images of text have a contrast ratio of at least 4.5:1.
    * Large text and icons: at least 18 point (typically 24px) or 14 point (typically 18.66px) and bold and have a contrast ratio of at least 3:1.
  * **Data:** Contrast in graphical elements like bar charts, line charts, and pie charts is 3:1 in all scenarios.

### Beware of using too many bright or saturated colors

High contrast is one possible solution in a myriad of low-to-no vision
scenarios. While high-contrast helps some users, other users with repetitive
strain injuries (RSI) or who are recovering from eye surgery or concussions
can be sensitive to high contrast. Ideally, there are options users can choose
from to use what works best for their needs.

## Color And(!)

### [Color](https://www.w3.org/TR/WCAG21/#use-of-color) should not be the only
way to convey meaning

While this feels complex, the reasoning is simple: not everyone sees the same
colors. Many of these additional layers are already existing data
visualization best practices, such as:

  * Patterns in bar charts, line charts, pie charts, etc.
  * Legends to help match color to a specific portion of data
  * Tooltips that convey information using text

## Less Is More

While data density can be powerful, it can also overwhelm users who are new to
a product or have cognitive and learning disabilities, such as ADHD, autism,
dyslexia, and anxiety.

### With [words](https://www.w3.org/TR/WCAG21/#unusual-words):

Use plain language in your data visualization. Strive for concise and
descriptive phrases to ensure that deaf and hard-of-hearing users or non-
native speakers can easily understand the visual information. Avoid jargon and
three-letter acronyms (TLAs) to ensure there’s no confusion.

### With design:

Use negative space to ensure it’s easy to consume the data.

### With [images](https://www.w3.org/TR/WCAG21/#text-alternatives):

If an image is required in a data visualization or dashboard, ensure
alternative text, or alt-text, is included in the design. If the image is non-
functional, mark it as empty (alt=””) for a developer.

## Interactivity

### Do not design critical actions under [hover
effects](https://www.w3.org/TR/WCAG21/#content-on-hover-or-focus)

Not every user can use a mouse, and on mobile devices, hovering is impossible,
therefore any critical actions should be on click or tap, not hover.

### Use [headers and titles](https://www.w3.org/TR/WCAG21/#headings-and-
labels)

Headings help users gain critical context for visualizations and are picked up
by screen readers, meaning information can be read without bloating the code
with ARIA labels.

### Limit [horizontal scrolling](https://www.w3.org/TR/WCAG21/#reflow)

For users with motor impairments, bi-directional scrolling can be difficult or
even impossible. For users who need to zoom in to read tables, it can be
highly frustrating and challenging to consume data with bidirectional
scrolling.

### Offer [keyboard shortcuts](https://www.w3.org/TR/WCAG21/#keyboard-
accessible)

Keyboard shortcuts are not only helpful for users who rely on a screen reader
or have motor impairments, they’re also beneficial for power users who don’t
want to rely on a mouse. Ensure that keyboard shortcuts do not conflict with
screen reader shortcuts.

## Responsiveness

### Responsiveness is a key component of a11y

This helps users on-the-go to view data visualizations on their phone or
tablet. It also helps those with vision impairments such as tunnel vision who
benefit from seeing more on a small screen instead of scrolling back and
forth. Users who use a screen reader might prefer to use it on their phone
over desktop as well.

### Allow zoom in and out capability

Visualizations should be readable from 50%-200% of the original size [without
losing functional text](https://www.w3.org/TR/WCAG21/#resize-text).

### Consider [tap target sizes](https://www.w3.org/TR/WCAG21/#target-size)

Tiny tap targets can cause users to struggle with their fingers, a mouse, or a
[mouthstick](https://medical-dictionary.thefreedictionary.com/mouth+stick).
Make sure that actions are easy for users of all abilities to engage with.

## Motion and Animation

### Beware of [flashing and blinking
speed](https://www.w3.org/TR/WCAG21/#three-flashes-or-below-threshold)

Motion and animation can elevate an experience for users who can see. However,
avoid anything that flashes more than three times in any one second period to
be mindful of people with epilepsy or eye sensitivity. As an innovative
option, [enable user preferences to disable
animation](https://www.w3.org/TR/WCAG21/#animation-from-interactions).

### Consider multiple ways to convey data

When designing for a robust data experience, consider multiple ways to convey
data, especially for users with low-to-no vision. Examples include specific
sounds for loading, error states, and varying pitch to listen to line chart
data (sonification).

### Use [text in place of images](https://www.w3.org/TR/WCAG21/#images-of-
text) in text

It’s sometimes common to freeze a data visualization by using a screenshot or
still image and uploading it to a dashboard. Without alt-text, this image is
not readable to low-to-no vision users and poor image quality can make it
unreadable for everyone. Use text instead of images of text to make sure it is
readable, responsive, and accessible.

## Design Tools And Process

### Check Color Contrast in Design

  * [WebAIM (Accessibility in Mind) Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
  * On Figma, [Color Blind](https://webaim.org/resources/contrastchecker/) and [Able](https://www.figma.com/community/plugin/734693888346260052/Able-%E2%80%93-Friction-free-accessibility)

### Receive feedback on designs from the disabled community

While feedback from the disabled community is very helpful, it’s even better
to include disabled users early in your design process! This inclusive testing
and research can elevate your designs from “legally compliant” to “intuitive
and user-friendly”.

### Collaborate with Developers

Even the most accessible, innovative data visualization, if not developed
correctly, will never reach its intended users. Designers should partner with
developers to ensure proper semantics, headers, and code are implemented to
reflect the intended user experience.

## Resources

[Sarah Fossheim: An Intro to Designing Accessible Data
Viz](https://fossheim.io/writing/posts/accessible-dataviz-design/)

[October 2020 A11y Hour on Color
Contrast](https://docs.google.com/presentation/d/1N_gcDUCzmyMqF6tFvgjQKOxktoa49y56pXx7gXPeW_Y/edit?usp=sharing)

[Stripe Case Study: Designing Accessible Color
Systems](https://stripe.com/blog/accessible-color-systems)

---

## Splunk Design System

**Package:** `Accessibility` | **Component:** `Keyboard`

# Keyboard Interactions

## Why Keyboard Interactions are Important

While keyboards are rarely used in mobile or tablet experiences, they are a
common assistive technology for desktops. You need to consider keyboard
interactions when designing for the following reasons:

  * Some people can’t use a mouse and rely solely on a keyboard.
  * Screen readers rely on a keyboard for navigation.
  * Workflows can be more efficient and time-saving through keyboard shortcuts.
  * In the case of components with poor color contrast, the only way to tell that they’re active is through keyboard interactions.

## Focus Visible

Core to keyboard navigation is a focus indicator or ring around an interactive
element such as a link or form field that enables a keyboard-only user to
identify where on the page or application they are. To prompt a focus visible,
use `TAB` and `SHIFT+TAB` on an interface. The standard order for a focus
indicator is left to right, up and down; however, designers largely determine
this as part of ordering content in a meaningful sequence.

You can style focus indicators in CCS. Before styling, it’s important to
consider the color contrast of the focus indicator against the page background
and any elements that are close to the focus border such as a button border.
If the custom focus border is less than 3px, use a 4.5:1 color contrast ratio,
and if it’s greater than or equal to 3px, use a 3:1 color contrast ratio.

## Keyboard Interactions

Designers and developers have a shared responsibility for interactions.
Designers should annotate them in their designs and developers should follow
through with implementation. Baseline functionality for keyboard includes:

  * `TAB` and `SHIFT+TAB`: Enables a user to progress through a sequence of interactive elements on the page. Tab moves a user forwards, and Shift+Tab moves them backwards.
  * `SPACE` and `SHIFT+SPACE`: Enables a user to scroll through a page
  * `ENTER` or `SPACE`: Once an element has focus, Enter or Space, depending on the component, is used to initiate something, such as an action from a button, a selection from a menu, navigating with a link, or toggling an option.
  * `ESC`: Escape is used to exit an interrupting layer of a user interface, such as a dropdown menu, modal, or banner.
  * `Arrow keys`: Up, down, left, and right are used for navigating a series of options, such as checkboxes, radio buttons, and menus.

## Custom Shortcuts

At times, creating custom keyboard shortcuts is necessary to provide a better
and more holistic user experience. Don’t override widely accepted shortcuts,
for example Ctrl+P is a common browser shortcut to print, and allow users to
override a prescribed custom shortcut within the interface. Letting users
designate their own keyboard preferences gives them the flexibility to
override shortcuts that conflict with shortcuts built into their screen reader
or to create shortcuts that meet the user's range of motion or cognitive
needs.

## Do’s and Don’ts

### Don’t:

  * Don’t hide the focus ring. Designers and developers sometimes mistakenly do this to make a design more minimal without realizing that keyboard-only users rely on this to know where they are in a page or application.
  * Don’t make keyboard functionality available only on hover. Instead, ensure that you can access it using a keyboard and without a mouse.

### Do:

  * Ensure that when a pop-up or modal is closed, the focus indicator returns to the original element that prompted the change in the interface.
  * Keep the focus in the appropriate z-index of a page. For example, if a user opens a modal, focus should move and stay in the modal until it is closed or a user presses Esc.
  * Consider a meaningful sequence as part of the focus indicator and match the reading order to the audience and language of the users.

## Additional Resources

[WebAIM: Keyboard Accessibility](https://webaim.org/techniques/keyboard/)

[Washington University: Providing Focus to
Users](https://www.washington.edu/accessibility/checklist/focus/)

[Microsoft Keyboard Accessibility in Excel](https://support.microsoft.com/en-
us/office/keyboard-shortcuts-in-
excel-1798d9d5-842a-42b8-9c99-9b7213f0040f#picktab=web) (great reference for
keyboard interactions with tables)

---

## Splunk Design System

**Package:** `Accessibility` | **Component:** `NonTextContent`

# Page not found

The page you are trying to view does not seem to exist.

---

# Themes & Styling {#themes-styling}

*Theming system, design tokens, and styling utilities.*

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `ChangeLog`

# Change Log

## 1.2.1 - September 2, 2025

Bug Fixes:

  * Added missing `sansFontFamily` token in Magnetic theme customizer (SUI-8101).

Docs:

  * Added missing data visualization color categories (`categorical2D`, `categorical2L`, `divergent1D`) to design tokens documentation (SUI-8139).

## 1.2.0 - August 5, 2025

New Features:

  * New `lineHeight*` variables (SUI-7993).

Bug Fixes:

  * Updated `skipLink` mixin to override `min-width` and `min-height` properties.

## 1.1.0 - July 2, 2025

New Features:

  * `@splunk/themes/storybook-addon-splunk-themes` now supports disabling 'both' option via `disableDualTheme` story param (SUI-7702).
  * Added `pageBase` mixin for `html` and `body` base styling (SUI-7665).
  * New `skipLink` mixin (SUI-7854)

Bug Fixes:

  * Updated Prisma and Magnetic light syntax token values to maintain 4.5:1 contrast with line highlight (SUI-6644).
    * Tokens updated: `syntaxBlue`, `syntaxBrown`, `syntaxGray`, `syntaxGreen`, `syntaxHighlight`, `syntaxOrange`, `syntaxPink`, `syntaxPurple`, `syntaxRed`, and `syntaxTeal`.
  * Updated `actionColorBackgroundSecondaryActive` token values in Enterprise and Prisma themes to fix visual regression in `Radio Bar` (SUI-7864).
  * Updated `interactiveColorOverlayActive` token values in Prisma and Enterprise themes to match `actionColorBackgroundSecondaryActive` values for consistent active overlay states (SUI-7864).
  * Updated enterprise theme light mode neutral color tokens `neutral300`, `neutral400`, and `neutral500` to fix lightness steps from previous changes. (SUI-7879)
  * Added neutral tokens (`neutral50`, `neutral100`, `neutral200`, `neutral300`, `neutral400`, `neutral500`) to Magnetic theme customizer with light and dark color scheme support, matching Enterprise and Prisma theme. (SUI-7879)

## 1.0.1 - June 5, 2025

Bug Fixes:

  * Corrected `@types/react` peer dependency to allow `@types/react` `16` or `17` (SUI-7838).

## 1.0.0 - June 3, 2025

  * Includes all changes from `1.0.0-beta` and `1.0.0-rc` releases.

Bug Fixes:

  * Color variables `backgroundColorPage`, `backgroundColorNavigation`,`backgroundColorSideBar`,`neutral50`,`neutral100` and `neutral200` in Enterprise light have been updated to align better with Prisma themes (SUI-7584).
  * `@types/react` peer dependency now includes `^16 | ^17` and no longer blocks installation using `npm` in React 16 or 17 environments (SUI-7838).
  * Color variables for `actionColorBorderSecondary*`, `actionColorBackgroundSecondary*`, and `interactiveColorBorderDisabled` have been updated to align with both Prisma and Enterprise themes (SUI-7839).

## 1.0.0-rc.2 - May 28, 2025

  * Release candidate 2.

## 1.0.0-rc.1 - May 14, 2025

API Changes:

  * `SplunkThemeProvider`'s default `density` has been changed from `"comfortable"` to `"compact"` (SUI-5709).

## 1.0.0-beta.5 - May 7, 2025

New Features:

  * New `interactiveColorAccentErrorWeak` variable (SUI-7757).
  * `typography` has reintroduced the `withReset` prop, which defaults to `false`. When set to `true`, it removes all browser-default styles and applies theme-specific defaults (SUI-7638).

## 1.0.0-beta.4 - April 22, 2025

New Features:

  * New `inputBorderWidth` variable (SUI-7384).

API Changes:

  * `typescript` version is now `^5.8.3` (SUI-7601).
  * `borderActiveColor` has been deprecated. (SUI-7633).
    * Use `interactiveColorBorderActive` for Data Entry components or `actionColorBorderSecondaryActive` for Buttons.
  * `backgroundColorHover` have been deprecated. (SUI-7633).
    * Use `interactiveColorOverlayHover` for Data Entry components or `actionColorBackgroundSecondaryHover` for Buttons.
  * `hoverShadow` has been deprecated. See notes on `backgroundColorHover` for hover affordances. (SUI-7621)

Bug Fixes:

  * Fixes broken CSS for Splunk Magnetic's `backgroundColorNavigation` override (SUI-7653).

Deprecations:

  * `statusColor*`s have been deprecated. Instead use the appropriate `notificationColor*` or `severityColor*`(SUI-7303).

## 1.0.0-beta.3 - April 2, 2025

New Features:

  * New `neutral50` variable (SUI-7384).
  * New `notificationColor` variables (SUI-7303).
  * New `severityColor` variables (SUI-7303).

Bug Fixes:

  * Updates `interactiveColorBackground` and `interactiveColorBackgroundDisabled` to be transparent in all themes (SUI-7347).
  * The `@types/react` peer dependency is now correctly set to `^18.2.0` (SUI-7548).

Deprecations:

  * `interactiveColorPrimary` has been deprecated (SUI-3568).

## 1.0.0-beta.2 - March 5, 2025

New Features:

  * New `contentColorLink` variable (SUI-3568).
  * The data-viz variables are supported in all themes (SUI-3568).

API Changes:

  * `accentColor` variable has been removed from Prisma themes (SUI-3568).
  * `borderColor`, `borderColorStrong`, and `borderColorWeak` have had alpha removed from their values (SUI-7340).
  * `embossShadow`, `overlayShadow`, `dragShadow`, and `modalShadow` variables have been updated in Enterprise themes to match Prisma (SUI-7334).
  * Enterprise only tokens have been deprecated: `brandColor*`, `gray*`, `accentColor*`, `errorColor*`, `alertColor*`, `warningColor*`, `successColor*`, `infoColor*`, `diverging*Color*`, and `cat*Color*`.

Deprecations:

  * `linkColor` and `linkColorHover` have been deprecated. Instead use `contentColorLink` (SUI-3568).

## 1.0.0-beta.1 - February 20, 2025

New Features:

  * Enterprise themes now support the `interactiveColorOverlayHover` Prisma alias (SUI-6289).
  * All themes now support color variable `interactiveColorAccent` (SUI-6304).
  * All themes now support color variable `interactiveColorAccentError` (SUI-6395).
  * Enterprise themes now support the `interactiveColorOverlaySelected` Prisma alias.
  * All themes now support color variable `contentBackgroundColorNegativeWeak` (SUI-6395).
  * Enterprise themes now support color variable `contentColorInverted` (SUI-6530).
  * All themes now support color variable `contentColorNegative` (SUI-6408).
  * Prisma themes now support color variable `accentColor` (SUI-6657).
  * All themes now support new `actionColor` tokens (SUI-6616).
  * All themes now support color variable `contentColorAccent` (SUI-6711).
  * All themes now support color variables `contentColorInfo`, `contentColorPositive`, and `contentColorWarning` (SUI-6830).
  * Enterprise themes now support the `interactiveColorOverlayActive` (SUI-6870).
  * All themes now support color variable `interactiveColorAccentErrorStrong` (SUI-6869).
  * All themes now support color variable `interactiveColorBackground` (SUI-6983).
  * New `layout` mixin (SUI-6678).
  * Enterprise themes now support color variable `backgroundColorSidebar` (SUI-7102).

API Changes:

  * `react` and `react-dom` peer dependencies are now `"^16.8.0 || ^17.0.0 || ^18.0.0"`.
  * `px` sizing for `variables.fontSize*` and `mixins.typography` have been replaced with `rem` sizing (SUI-5509).
    * This results in minor differences in text sizing; but is required to meet WCAG 1.4.4 and WCAG 1.4.10.
  * `typography` `size` param no longer supports `56` `36` `32` and `10`.
  * `variables.lineHeight` is no longer defined in `px` to improve readability of font at all scales (SUI-5509).
  * `typography`'s mixin for `Title5`'s has been updated to text color `variables.contentColorActive` in Prisma theme (SUI-5685).
    * This change affects `Heading` and `Typography` components.
  * The font size and line height no longer change with density. The default font-size in Enterprise Compact now is 14px (SUI-5508).
  * `typography`'s `line-height`, `size`, and `font-weight` values have been consolidated between Enterprise and Prisma themes (SUI-5684).
  * `typography`'s `withReset` prop has been removed (SUI-5686).
  * `variables.activeBorder` has been removed (SUI-6362).
  * Spacing variables in Enterprise themes are now aligned with Prisma themes (SUI-6530).
    * `spacingXSmall`, `spacingSmall`, `spacingMedium`, `spacingLarge`, `spacingXLarge`, `spacingXXLarge`, `spacingXXXLarge` have been updated to match Prisma themes.
    * `spacingQuarter`, `spacingHalf`, and `spacing` are deprecated and should not be used.
  * Enterprise theme `statusColor*` variables have been shifted to align brightness values with Prisma themes (SUI-6348).
  * Enterprise theme's `focusShadow` variable has been updated to match Prisma (SUI-6481).
  * Enterprise theme's `focusShadowInset` variable has been updated to match Prisma (SUI-6487).
  * `typography` supports a new scale for line-height that uses unitless values (SUI-6593).
  * `typography` no longer support pixel values for line-height (SUI-6593).
  * `typography` no longer supports the `title7` and `footnote` variants (SUI-6593).
  * `typography` parameters now supports `family: "title"`.
  * `fontSizeXLarge` size has been changed (SUI-6593).
  * Enterprise themes support the `contentColorActive`, `contentColorDefault`, `contentColorDisabled`, `contentColorInverted`, and `contentColorMuted` tokens (SUI-6160).

Deprecations:

  * Enterprise theme tokens `textColor`, `textGray`, and `textDisabledColor` have been deprecated (SUI-6160).
  * Enterprise theme token `backgroundColor` has been deprecated (SUI-6656).
  * `accentColorPositive`, `accentColorWarning`, `accentColorAlert`, and `accentColorNegative` have been deprecated (SUI-3658).

## 0.24.0 - May 6, 2025

Bug Fixes:

  * Added `main` and `types` properties to package.json (SUI-7464).

## 0.23.0 - February 5, 2025

Bug Fixes:

  * Added peer dependencies needed to incorporate the themes package standalone (SUI-6874).

## 0.22.0 - October 1, 2024

New Features:

  * New Status Color tokens for weak and strong variants (SUI-6348).
  * `@splunk/themes/storybook-addon-splunk-themes` now supports showing both versions of a single theme setting side by side (SUI-6281).

## 0.21.0 - August 26, 2024

New Features:

  * Prisma `focusColor` transparency removed to increase contrast and meet accessibility requirements (SUI-6519).

## 0.20.0 - August 7, 2024

New Features:

  * Prisma light theme's `interactiveColorBorder` value has been updated to meet accessibility requirements (SUI-6342).

## 0.19.0 - June 4, 2024

New Features:

  * Enterprise themes now support the following Prisma aliases: `interactiveColorBorderActive`, `interactiveColorBorderHover`, `interactiveColorBorderDisabled`, and `interactiveColorBackgroundDisabled` (SUI-6062).

API Changes:

  * Enterprise theme's `interactiveColorBorder` Prisma alias has been updated in dark mode (SUI-6062).

## 0.18.0 - May 6, 2024

New Features:

  * All themes now support color variables for decorative borders:
    * `borderColorStrong` and `borderColorWeak` added to all themes
    * `borderColor` now also available in Prisma themes
    * Note: Use `interactiveColorBorder` when creating a border for an interactive control

Bug Fixes:

  * Enterprise light theme `interactiveColorBorder` value has been updated to meet contrast requirements.

API Changes:

  * Enterprise theme `borderLightColor` has been deprecated. Instead, use `borderColorWeak`.
  * Enterprise dark theme `borderDarkColor` has been removed. Instead, use `borderColorStrong`.
  * `@splunk/themes/storybook-addon-splunk-themes` has been updated to work with `@storybook@^7` and no longer works with `@storybook@^6` (SUI-6170).

## 0.17.0 - March 21, 2024

New Features:

  * Added new variable `activeBorder`.

## 0.16.4 - December 5, 2023

Bug Fixes:

  * `syntaxColors` have been updated to meet A11y_WCAG 1.4.3 contrast requirements for prisma and enterprise themes (SUI-5750).

## 0.16.3 - October 11, 2023

Bug Fixes:

  * This package should now load correctly in Webpack 4 environments (SUI-5802).

## 0.16.2 - October 4, 2023

Bug Fixes:

  * `typography` mixin's `title4`, `title5`, and `title6` should now correctly follow the font hierarchy (SUI-5668).
    * `title5` is now larger and bolder than `title6` in Prisma themes.
    * `title4` it now larger than `title6` in the Enterprise compact theme.
  * `typography`'s mixin's `title5` color has been changed to `active` in prisma theme to match the Splunk Design System.

API Changes:

  * `list-style` has been removed for `mixins.reset` (SUI-5622).

## 0.16.1 - June 6, 2023

API Changes:

  * Added support for the latest `styled-components@5` (SUI-5467).

## 0.16.0 - April 6, 2023

Breaking Changes:

  * `typography` mixin's `weight` param now only accepts keyword values. Number values have been removed (SUI-5344).

New Features:

  * Added variables for supported font weights; the `typography` mixin's `weight` param supports these as keyword values (SUI-5344).

Bug Fixes:

  * `typography` mixin properly applies correct CSS for `weight` params (SUI-5344).

## 0.15.0 - January 25, 2023

New Features:

  * Added theme specific code in `typography` mixin for title variations (SUI-5272).

Bug Fixes:

  * `mixins` now applies `color-scheme` (SUI-1926).
    * This causes form controls, scrollbars, and other elements to respect the color scheme specified by `ThemeProvider`.
  * Fixes documentation typo in `typography` mixin where 'subtitle' and 'smallSubtitle' should be instead be named 'title6' and 'title7' respectively.

## 0.14.0 - January 10, 2023

New Features:

  * Added `inherit` option for `color` prop in `typography` mixin.

## 0.13.1 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 0.13.0 - September 6, 2022

New Features:

  * Added `typography` mixin (SUI-2809).

## 0.12.0 - August 2, 2022

New Features:

  * Added `zIndexLayer` variable (SUI-2809).

API Changes:

  * Status and accent colors have been updated in Prisma themes.

The amount of distinct color values have been consolidated: e.g.
`statusColorHigh` and `accentColorNegative` are both `#e00000`.

The contrast between these colors have been increased to improve accessibility
(SUI-3758).

## 0.11.0 - May 4, 2022

New Features:

  * Added Data visualization colors to Prisma themes.

## 0.10.1 - April 5, 2022

Bug Fixes:

  * Pinned `styled-components@5.1.1` to avoid breaking changes introduced in `styled-components@5.2.0`.

**`@splunk/themes` is incompatible with styled-components version(s)
`^5.2.0`**.

`styled-components@5.2.0` changed how selectors like `& + &` are compiled;
[styled-components PR#3236](https://github.com/styled-components/styled-
components/pull/3236). This breaks styles that worked in previous versions of
styled-components; [styled-components issue #3265](https://github.com/styled-
components/styled-components/issues/3265).

**Until noted otherwise in a future release of`@splunk/themes` do not use
`styled-components@^5.2.0` with` @splunk/themes`**.

## 0.10.0 - February 23, 2022

New Features:

  * Utility variables, `isPrisma`, `isEnterprise`, `isComfortable`, `isCompact`, `isDark`, and `isLight`, added to `useSplunkTheme()` and `withSplunkTheme()` (SUI-2376).

## 0.9.0 - September 8, 2021

API Changes:

  * Prisma content colors no longer use transparency (SUI-2688).

## 0.8.0 - March 31, 2021

New Features:

  * New variable `backgroundColorDialog`.
  * New Storybook Add-on, `@splunk/themes/storybook-addon-splunk-themes`.

API Changes:

  * `backgroundColorModal` has been removed. Instead, use the new variable `backgroundColorDialog`.

Bug Fixes:

  * Enterprise `draggable` and `draggableDark` assets updated to improve contrast (SUI-2494).

## 0.7.0 - February 4, 2021

0.7.0 is a major departure from previous versions of this library. It has been
optimized to work with React and styled-components, but variables can still be
used for other use cases.

New Features:

  * `overlayColors` mixin supports nested template functions.
  * `compact` variables.

API Changes:

  * `scp` theme renamed to `prisma`.
  * `prisma` `dark` is the default theme.
  * `lite` theme removed. That is, the orange theme for the Splunk Light product was removed.
  * New `SplunkThemeProvider`.
  * New `pick()` function for switching css blocks and variables in styled-components templates.
  * Individual themes are no longer exported directly.
    * Use `useSplunkTheme()` for variables in React components;
    * Use `variables` for variables in styled-components templates;
    * Use `getTheme()` should you need a full list of theme variables for use outside of React and styled-components;
  * Consuming packages no longer need to export their themes.
  * Deprecated variables have been removed from `prisma`.
  * `mixins` are no longer theme-specific – they are theme-aware. That is, one set of mixins work in all themes.
  * `mixins` cannot be used outside of `styled-components`.
  * `reset` mixin no longer supports the `full` and `all` parameters.
  * Enterprise theme `backgroundColor` variable changed to improve contrast ratios for primary `Button`s (SUI-2441).

## 0.6.1 - August 31, 2020

Bug Fixes:

  * `syntaxOrange` and `syntaxBrown` colors corrected in the `scp` theme (SUI-2341).

## 0.6.0 - July 7, 2020

New Features:

  * New `scpLight` theme (SUI-2099).
  * New usage-based variables in `scp` theme.
  * Added `overlayColors` mixin.

API Changes:

  * Changes to variables in the `scp` theme:
    * `gray##` variable removed. Replace with usage-based grays. In limited cases, such as borders, `neutralColor###` may be used.
    * `successColor` variable removed. Replace with `accentColorPositive`.
    * `successColorX##` variable removed. Blend `accentColorPositive` with `interactiveColorOverlayXXX` or use a transparency.
    * `blue#` variable removed. Replace with `interactiveColorPrimary` and possibly blend with `interactiveColorOverlayXXX`.
    * `green1` variable removed. Replace with `accentColorPositive` or `statusColorNormal`.
    * `yellow1` variable removed. Replace with `accentColorWarning` or `statusColorLow`.
    * `orange1` variable removed. Replace with `accentColorAlert` or `statusColorMedium`.
    * `red1` variable removed. Replace with `accentColorNegative` or `statusColorCritical`.
    * `accentColor` variable removed. Replace with `interactiveColorPrimary` or `statusColorInfo`.
    * `accentColorX##` variable removed. Replace with `interactiveColorPrimary` or `statusColorInfo`.
    * `infoColor` variable removed. Replace with `statusColorInfo` or `contentColorActive`.
    * `infoColorX##` variable removed. Blend `accentColorWarning` with `interactiveColorOverlayXXX` or use a transparency.
    * `warningColor` variable removed. Replace with `accentColorWarning`.
    * `warningColorX##` variable removed. Blend `accentColorWarning` with `interactiveColorOverlayXXX` or use a transparency.
    * `alertColor` variable removed. Replace with `accentColorAlert`.
    * `alertColorX##` variable removed. Blend `accentColorPositive` with `interactiveColorOverlayXXX` or use a transparency.
    * `errorColor` variable removed. Replace with `accentColorNegative`.
    * `errorColorX##` variable removed. Blend `accentColorPositive` with `interactiveColorOverlayXXX` or use a transparency.
    * `linkColorHover` variable removed. Remove css or use `linkColor`.
    * `syntaxBlueLight` variable removed. Replace with `syntaxBlue`.
    * `syntaxGreenLight` variable removed. Replace with `syntaxGreen`.
    * `syntaxPurpleLight` variable removed. Replace with `syntaxPurple`.
    * `syntaxRedLight` variable removed. Replace with `syntaxRed`.

Bug Fixes:

  * Focus styles are updated in `enterprise` and Splunk Light `lite` themes to improve accessibility (SPL-188569).

## 0.5.0 - May 1, 2020

API Changes:

  * The `reset` mixin now enables `cursor` inheritance.

## 0.4.2 - February 5, 2020

New Features:

  * Added `screenReaderContent` mixin.

## 0.4.1 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 0.4.0 - October 8, 2019

New Features:

  * Added `scp` theme.

## 0.3.1 - September 12, 2019

New Features:

  * The `reset` mixin now supports an additional argument, `all`.

Bug Fixes:

  * Fixed a visual issue with links that use the `reset` mixin, on Chrome 77 (SUI-1905).

## 0.3.0 - September 13, 2018

New Features:

  * Added `enterpriseDark` theme.

API Changes:

  * Theme modules export only one default object now. Mixins are now nested in `mixins`.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

## 0.2.0 - June 30, 2018

  * Initial Release.

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `GetSettingsFromThemedProps`

# getSettingsFromThemedProps

### getSettingsFromThemedProps(props)

The theme settings in `props.theme` are not considered an API to allow support
for fallbacks and forward compatibility in future versions of
`SplunkThemeProvider`. Use this utility to access `family`, `colorScheme`, and
`density` from a component's props. This is useful in limited migration
scenarios. Use `withSplunkTheme` or `useSplunkTheme` instead.



    import getSettingsFromThemedProps from '@splunk/themes/getSettingsFromThemedProps';
    ...
    const { family, colorScheme } = getSettingsFromThemedProps(props);


props

The themed props passed to a styled-component.

Type| object
---|---
Required| Yes

returns

An object consisting of `{ family, colorScheme, density }`.

Type| object
---|---

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `Layout`

# Layout

### layout()

Layout styles elements for common layout use cases

#### Example



     import styled from 'styled-components';
     import { layout } from '@splunk/themes/mixins';

     const Wrapper = styled.div`
         ${layout()};
     `;

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `Pick`

# pick

### pick(themeOptions)

Pick is used to create theme-specific css.

This example selects an appropriate variable for the current theme.



    import { pick, variables } from '@splunk/themes';

    const Wrapper = styled.div`
         color: ${pick({
             enterprise: {
                 light: variables.grey35,
                 dark:  variables.grey92,
             },
             prisma: variables.contentColorDefault,
         })}
    `;

This example selects an appropriate block of css for the current theme.



     const Label = styled.div`
         ${pick({
             enterprise: css`
                 font-weight: ${variables.fontWeightSemiBold};
             `,
             prisma: css`
                 color: ${variables.contentColorDefault),
             `,
         })}
    `;

themeOptions

An object consisting of a tree of theme options (`enterprise|prisma`,
`light|dark`, or `compact|comfortable`).

Type| object
---|---
Required| Yes

returns

The returned function is called by `styled-components`, which provides the
theme context.

Type| function
---|---

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `PickVariant`

# pickVariant

### pickVariant(propName, themeOptions)

Pick Variant is used to create theme-specific css.

This example selects an appropriate variable for the current theme.



    import { pickVariant } from '@splunk/themes';

    ...

    const Wrapper = styled.div`
         ${pickVariant('appearance', {
             filled: 'background: red',
             open: 'border: 1px solid red',
         })}
    `;

This example selects an appropriate block of css for the current theme.



     const Wrapper = styled.div`
         ${pickVariant('appearance', {
             filled: {
                 enterprise: 'background: green',
                 prisma: 'background: blue',
             },
             open: {
                 enterprise: 'border: 1px solid green',
                 prisma: 'border: 1px solid blue',
             },
         })}
    `;

propName

The prop name used to resolve the variants. The prop value must be a `string`
or `boolean`.

Type| string
---|---
Required| Yes

themeOptions

An object consisting of a tree of theme options, with the prop variants the
top of the tree and optional theme variants below (`enterprise|prisma`,
`light|dark`, or `compact|comfortable`).

Type| object
---|---
Required| Yes

returns

The returned function is called by `styled-components`, which provides the
props and theme context.

Type| function
---|---

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `Typography`

# Typography

### typography([variant], [typographyParams])

A mixin for styling text content using predefined typography variants and/or
customizing font-settings with system parameters: e.g. size, weight, font-
family.

The default variant is `body` and will be used if no variant or settings are
given: i.e. `typography()` or `typography({})`. Variants have the reset
applied by default.

##### Example



    import styled from 'styled-components';
    import { typography } from '@splunk/themes/mixins';

    const MyTitle = styled.h1`
        ${typography('title1')};
    `;

    const MyCustomizedTitle = styled.h1`
        ${typography('title1', { color: 'inverted' })};
    `;

    const CustomTitle = styled.h1`
        ${typography({size: 56, weight: 'light', color: 'inverted' })};
    `;

variant

Use a predefined typography variant: `'body'`, `'title1'`, `'title2'`,
`'title3'`, `'title4'`, `'title5'`, `'title6'`, `'largeBody'`, `'smallBody'`,
`'monoBody'`, or `'monoSmallBody'`,

Type| string
---|---
Required| No

typographyParams

Customize the font settings or element using system values for: `color`,
`family`, `lineHeight`, `size`, `weight` and `withReset`.

Type| object
---|---
Required| No

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `VariablesSC`

# Variables for Styled Components

## Theme Variables

All variables are available in one util for use in styled-component templates.
Each variable is a function which styled-components will call with the
available theme information. If there is no SplunkThemeProvider, variables
will default to Prisma Dark Compact.

Variables will return `undefined` if the variable does not exist in the
current theme.



    import variables from '@splunk/themes/variables';
    import styled from 'styled-components';
    ...
    const PrismaWrapper = styled.div`
        color: ${variables.contentColorDefault};
    `;

Variables may also be imported individually.



    import { contentColorDefault } from '@splunk/themes/variables';
    import styled from 'styled-components';
    ...
    const PrismaWrapper = styled.div`
        color: ${contentColorDefault};
    `;

This function must be used in conjunction with `pick` if different variables
are needed in different themes.



    import { pick, variables } from '@splunk/themes';
    import styled from 'styled-components';

    const Wrapper = styled.div`
        color: ${pick({
             enterprise: variables.textColor,
             prisma: variables.contentColorDefault
        })};
    `;

## Custom Variables

Custom variables cannot be added to this package. However, `pick()` can be
used to create sets of theme variables. These can be then be imported
separately and used as above.



    import pick from '@splunk/themes/pick';

    export const myVariables = {
       orange: pick({
           light: '#C80',
           dark: '#F90',
       }),
       space: pick({
           enterprise: '20px',
           prisma: {
               comfortable: '16px',
               compact: '12px',
           },
       }),
    };

---

## @splunk/themes - 1.2.1

**Package:** `themes` | **Component:** `WithSplunkTheme`

# withSplunkTheme

### withSplunkTheme()

`withSplunkTheme` allows theme variables to be used within a React class
component. This includes the basic configuration of `family`, `colorScheme`
and `density`, as well as all the specific variables available in that theme.

If no data `SplunkThemeProvider` was configured, the Prisma Dark Compact theme
is returned.



    import React, { Component } from 'react';
    import PropTypes from 'prop-types';
    import withSplunkTheme from '@splunk/themes/withSplunkTheme';


    class MyComponent extends Component {
        static propTypes = {
            splunkTheme: PropTypes.object,
        };

        render() {
            const { isComfortable, focusColor } = this.props.splunkTheme;

            const style = {
                color: focusColor,
                padding: isComfortable ? '10px' : '5px',
            }

            return (
                <div style={style}>
                    Hello
                </div>
            )
        }
    }

    const MyComponentWithTheme = withSplunkTheme(MyComponent);
    MyComponentWithTheme.propTypes = MyComponent.propTypes;

    export default MyComponentWithTheme;

---

# Visualizations {#visualizations}

*Chart and visualization components for data display.*

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `API`

# Visualizations API

Visualization is a React component with the following props defined:



    import { Component } from 'react';
    import T from 'prop-types';
    import { noop } from 'lodash';

    class SplunkVisualization extends Component {
        static propTypes = {
            /**
             * display mode
             */
            mode: T.oneOf(['view', 'edit', 'export']).isRequired,
            /**
             * width in pixels or string, defaults to 100%
             */
            width: T.oneOfType([T.string, T.number]).isRequired,
            /**
             * height in pixels or string
             */
            height: T.oneOfType([T.string, T.number]).isRequired,
            /**
             * visualization context used for dynamic option evaluation
             */
            context: T.object,
            /**
             * visualization formatting options
             */
            options: T.object,
            /**
             * A callback to update formatting options that accepts an object with key / value pairs
             */
            onOptionsChange: T.func,
            /**
             * datasource state which include data and request params, object key indicate the datasource type.
             */
            dataSources: T.objectOf(
                T.shape({
                    /**
                     * current request params
                     */
                    requestParams: T.object,
                    /**
                     * current dataset
                     */
                    data: T.shape({
                        fields: T.array,
                        columns: T.array,
                    }),
                    /**
                     * error
                     */
                    error: T.shape({
                        level: T.string,
                        message: T.string,
                    }),
                    /**
                     * meta data that came with the dataset
                     */
                    meta: T.object,
                })
            ),
            /**
             * A callback to trigger event
             */
            onEventTrigger: T.func,
            /**
             * Inform viz if there are handlers listening to events
             */
            hasEventHandlers: T.bool,
            /**
             * A callback to communicate computed props to a consumer
             */
            onComputedProps: T.func,
            /**
             * A callback to obtain visualization api
             */
            vizActionHandlerRef: T.func,
            /**
             * If set to "true" there will be an indication that the visualization data is loading
             */
            loading: T.bool,
            theme: T.object,
            /**
             * A callback to request new data with updated request params
             */
            onRequestParamsChange: T.func,
        };
        static defaultProps = {
            width: '100%',
            height: 250,
            dataSources: {},
            onEventTrigger: () => {},
            mode: 'view',
            hasEventHandlers: false,
            options: {},
            context: {},
            onOptionsChange: () => {},
            vizActionHandlerRef: () => {},
            onComputedProps: () => {},
            loading: false,
            onRequestParamsChange: noop,
        };
    }

    export default SplunkVisualization;

## Basic Principle

### A visualization should

  * Honestly present data with specific formatting options.
  * Communicate events with an `onEventTrigger` callback.
  * Be predictable. Always render identical result given a fixed dataset and options.

### A visualization should NOT

  * Depend on global variables.
  * Issue requests to fetch data.

## Visualization Data

The Visualization component reads data from a dataSources object in json_cols
format.

For example:



    dataSources={{
        primary: {
            requestParams: { offset: 0, count: 20 },
            data: {
                fields: [{ name: 'component' }, { name: 'count' }, { name: 'percent' }],
                columns: [
                            [
                                'splunkd',
                                'splunkd_ui_access',
                                'splunkd_access',
                                'splunk_web_access',
                                'scheduler',
                                'splunk_web_service',
                            ],
                            ['600', '525', '295', '213', '122', '19'],
                            ['87.966380', '50.381304', '60.023780', '121.183272', '70.250513', '90.194752'],
                ],
            },
            meta: { totalCount: 100 },
        },
    }}

### RequestParams

The RequestParams object defines how a visualization reacts with the data
sets.

The following example returns the first 20 results of a given data source:



    {
        requestParams: { offset: 0, count: 20 },
        data: {
            fields: [{ name: 'component' }, { name: 'count' }, { name: 'percent' }],
            columns: [
                        [
                            'splunkd',
                            'splunkd_ui_access',
                            'splunkd_access',
                            'splunk_web_access',
                            'scheduler',
                            'splunk_web_service',
                        ],
                        ['600', '525', '295', '213', '122', '19'],
                        ['87.966380', '50.381304', '60.023780', '121.183272', '70.250513', '90.194752'],
            ],
        },
        meta: { totalCount: 100 },
    }

If necessary, the Visualization component can invoke the
`onRequestParamsChange` callback to request data with updated request
parameters (RequestParams).

For Example:



    this.props.onRequestParamsChange('primary', {
        ...this.props.dataSources.primary.requestParams,
        offset: 20,
        count: 20,
    });

A complete example can be found under _Update RequestParams_ from the Table
visualization.

All available RequestParams are documented in the DataSource module.

### DataSources

DataSource is a module that does the data fetching, see @splunk/datasources
for more details.

  * While Visualization and DataSource are designed to work together, Visualization itself can be used as a standalone React component.
  * Each Visualization can be powered by multiple DataSources - 0 to 1 `primary` DataSource and 0 to n secondary DataSource

### Data Contract

Each visualization exposes a property called `dataContract` to indicate which
datasources are required.

The following snippet is an example data contract:



    const dataContract = {
        requiredDataSources: [
            {
                name: 'primary',
                description: 'DataSource that powers the visualization',
            },
        ],
        optionalDataSources: [
            {
                name: 'annotation',
                description: 'DataSource that populates event annotations',
            },
        ],
        initialRequestParams: {
            primary: { offset: 0, count: 10000 },
        },
    };

From the data contract above, UDF is able to infer that the visualization
requires one datasource called `primary` and supports an optional datasource
called `annotation`. It also exposes initialRequestParams to let datasources
know what parameters to use for the initial fetching of data.

#### Supported DataSources

The data contract contains a property `requiredDataSources` and
`optionalDataSources` to indicate what kind of DataSources it supports.

For example, Table only supports primary DataSource:



    const dataContract = {
        requiredDataSources: [
            {
                name: 'primary',
                description: 'DataSource that powers the visualization',
            },
        ],
        //...
    };

while Line Chart supports an additional annotation DataSource:



    const dataContract = {
        requiredDataSources: [
            {
                name: 'primary',
                description: 'DataSource that powers the visualization',
            },
        ],
        optionalDataSources: [
            {
                name: 'annotation',
                description: 'DataSource that populates event annotations',
            },
        ],
        //...
    };

When a `splitByLayout` configuration option (such as trellis) is used, the
visualization will continue to follow the same data contract.

#### Initial RequestParams

In order to retrieve the first batch of data, the initial RequestParams needs
to be figured out before the Visualization gets rendered. The
`initialRequestParams` property in the `dataContract` serves this purpose.

initialRequestParams can be an object



    initialRequestParams: {
        offset: 0,
        count: 10000,
    }

or a function that takes the visualization options and returns the initial
RequestParams



    initialRequestParams: (options = {}) => ({
        offset: 0,
        count: options.count || 20,
    });

## Meta

Meta object tells visualization extra information besides the data.

For example:



    {
        totalCount: 100, // total results
        progress: 50, // 0-100, current search progress
    }

It's up to the viz implementation to decide whether to use them. Checkout Meta
from DataSource package for details.

## Size

If either `width` or `height` is provided, the visualization will render
within the specified dimensions and handle the size change.

## onComputedProps

`onComputedProps` allows visualizations to communicate calculated props (e.g.
a background color that is calculated based on data) upwards to its consumer.

For Example:



    const TitleContainer = styled.div`
        background-color: ${props => props.backgroundColor};
    `;
    const DashboardWrapper = props => {
        const [state, setState] = useState({ backgroundColor: '#f00' });
        const { title, ...otherVizProps } = props;
        return (
            <>
                <TitleContainer backgroundColor={state.backgroundColor}>{title}</TitleContainer>
                <Visualization {...otherVizProps} onComputedProps={setState} />
            </>
        );
    };

### Visualization Config

The visualization config is used to programmatically reason about a
visualization at build & runtime

A visualization `config` contains the following properties:

  * **key** : Preset key used in the definition. Key format must be 'splunk.type'. Example: splunk.customBar
  * **name** : The canonical name for the visualization. Recommended format is splunk.type Visualization. Example: Custom Bar Visualization
  * **category** : Visualization class. Currently available categories are 'Table', 'Single Value', 'Trends', 'Comparisons', 'Gauge', 'Distributions', 'Shapes', 'Flow' and 'Choropleth Maps'
  * **icon** : A react element that renders an svg icon
  * **dataContract** : The data contract defines the availability for the visualization to use a datasource, and the default configuration for results. This configuration is also used by the editing interface to determine what datasources need to be configured
  * **optionsSchema** : The schema is used to validate the properties of a datasource configuration and is also used in concert with the editor config to provide default values. This should be a standard [json schema](https://json-schema.org/)
  * **editorConfig** : The editor static property defines a configuration that renders an editor in the sidebar
  * **size** : The size dimensions for the visualization
  * **events** : User interaction events that the visualization allows (e.g. click of a Pie slice, hover on a data point in a Line chart)
  * **defaultContext** : A place where DSL configuration variables can be defined. Used when no context is configured
  * **supports** : A list of supported behaviors by the visualization component
  * **themes** : An object that denotes key-value pairs of functions that return resolved values used to style the visualization based on the theme
  * **requiredProps** : A list of properties that must be defined in order for the placeholder to be replaced with the actual vizualization

The following snippet is an example Visualization config:



    const LinkGraphConfig = {
        key: 'splunk.linkgraph',
        name: 'Link Graph',
        icon: LinkGraphIcon,
        optionsSchema: {},
        editorConfig: {},
        events: {},
    };

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `BestPractices`

# Data Visualization Guidelines

Splunk’s data visualization guidelines are a collection of design standards to
help teams build high-quality experiences.

#### Sections:

Principles

Types

Styles

## Principles

### Meaningful

Choose a visualization, style, and layout that accurately portrays the story
you want to tell. Every visualization should convey a message. Ensure the data
visualization is clear, accurate, and comprehensible.

### Essential

Prioritize information that will add to the story rather than distract.
Highlight the most important pieces. Utilize space efficiently and apply
semantic notation when possible.

### Usable

Help users of all levels and devices view and understand your visualization.
Adapt your design for different platforms, languages, and access needs.

## Visualization Types

There are many different ways to visualize data. Select the visualization most
appropriate to convey the desired message and underlying information as
quickly as possible.

The type of visualization to use depends on:

  1. The data you want to use to communicate
  2. What message you want to convey with that data

### Trend

Charts based on the horizontal axis typically display time series data. The
visualization represents data over a period of time.

Stacked charts represent the accumulation of more than one data series.
Position the data series of central importance directly on the axis in order
to best see its development over time.

Use stacked 100% charts if the accumulation of all data series adds to a
whole.

### Comparison

Charts that compare structural (categorical) data.

Bar charts are typically used to compare data of one period or point in time
across multiple categories. By being based on an axis each category is more
easily compared using a common baseline.

Only use a pie chart if you have a single series and would like to highlight
how the partial categorical elements add up to a whole. Do not use multiple
pie charts to compare data. It’s challenging to accurately compare the
difference in size across slices of pie.

### Correlation

Charts that show a correlation between two or more dimensions.

### Flow

Charts that show movement of data between multiple states.

### Spatial

Charts that show how data maps to a two-dimensional area.

### Metric

Charts that show one or more values.

## Styles

Formatting can be used to convey multiple different types of messaging.

The primary ways to use color are to:

  1. Distinguish categories

  2. Express meaning

  3. Highlight important data

It is recommended that no more than 7 colors or series should be used on a
visualization for readability.

### Colors to represent categories

These colors should be used to distinguish discrete categories that do not
have inherent correlation between them.

### Colors to represent change in numeric value

These colors should transition between one color and another. Examples include
change in quantity, temperature, size, volume and more.

##### Sequential

Transition hue, saturation, or lightness

##### Divergent

Transition hue, saturation, or lightness in both directions with a neutral
center.

Check out our other sequential and divergent color palettes [here]().

### Colors to represent status

Colors should have an intentional meaning attached to them if they are being
used to convey a status. Some common colors associated with a specific meaning
are: green for good, red for bad.

### Contrast

Don’t use weak color contrast to display a visualization. Use brighter colors
for dark mode and darker colors for light mode.

Don’t add bright colors to the background of the chart. It’s difficult to see
the visualization and text, and it creates unnecessary visual noise.

### Accessibility

Certain color combinations are difficult to see for viewers who are
colorblind. Ensure that accessible color pallets are being used at all times.

**Color And**

Color should not be the only way to communicate meaning.

### Highlight

**Lines**

Line styles can be used to convey association or differentiation.

For example:

  * A dotted line that’s the same color of a solid line may be interpreted as a previous sample over a similar period of time
  * A bolded line may be used to highlight



**Values**

Show min and max data values on a chart to highlight dips and peaks.

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataFramegetField`

# DataFrame#getField

### getField()

Get the names of each DataSeries in the DataFrame.

returns



    <Table
      options={{
          headers: '> table | getField()'
      }},
      dataSources={{
        primary: {
          data: {
            fields: [
              {
                 name: 'Name'
              },
              {
                 name: 'UserID'
              },
              {
                 name: 'Money Spent'
              },
              {
                 name: 'Most Recent Game'
              },
            ],
            columns: [
              [
                 'Ms. Herman Beer',
                 'Crystal Ziemann',
                 'Phil Bartoletti',
                 'Janis Kiehn V',
                 'Angel Krajcik',
                 'Patti Hodkiewicz IV',
                 'Joanne Emmerich',
                 'Jay Renner',
                 'Ora Borer',
                 'Dr. Bradford Gulgowski'
              ],
              [
                 'Enrico98',
                 'Taylor_Parker83',
                 'Candice_Carroll',
                 'Yolanda_McLaughlin95',
                 'Modesto84',
                 'Elwin52',
                 'Francis8',
                 'Charley.Feeney85',
                 'Jensen_Jacobson74',
                 'Dore_Volkman'
              ],
              [
                 9740890.83,
                 2107983.52,
                 5467223.67,
                 9529184.93,
                 9692275.78,
                 9395814.7,
                 5692737.43,
                 1001734.82,
                 3848531.8,
                 1691776.38
              ],
              [
                 '2020-04-12T06:32:08-07:00',
                 '2020-06-06T16:14:04-07:00',
                 '2020-02-12T09:43:25-08:00',
                 '2020-07-25T13:19:49-07:00',
                 '2020-03-16T21:46:40-07:00',
                 '2020-08-21T08:38:55-07:00',
                 '2020-09-26T16:06:03-07:00',
                 '2020-08-10T14:54:16-07:00',
                 '2020-08-11T16:49:24-07:00',
                 '2020-09-29T03:52:51-07:00'
              ]
            ]
         },
         meta: {
           totalCount: 100
         },
         requestParams: {
           count: 10,
           offset: 0
         }
        }
      }}
    />

    Display the third and fourth DataSeries in a column chart as overlay fields.

    <Column
      options={{
        overlayFields: '> primary | frameBySeriesIndex(2,3) | getField()'
      }},
      dataSources={{
        primary: {
          requestParams: { offset: 0, count: 20},
          data: {
            fields: [
                { name: '_time' },
                { name: 'splunkd' },
                { name: 'splunkd_web_access' },
                { name: 'mongod' },
            ],
            columns: [
                [
                    '2018-05-02T18:15:46.000-07:00',
                    '2018-05-02T18:15:47.000-07:00',
                    '2018-05-02T18:15:48.000-07:00',
                    '2018-05-02T18:15:49.000-07:00',
                    '2018-05-02T18:15:50.000-07:00',
                ],
                ['67228', '83195', '3145', '19332', '29763'],
                ['67228', '83195', '3145', '19332', '29763'],
                ['14881', '17341', '18081', '19774', '10467'],
            ]
          },
          meta: {
            totalCount: 100,
          }
        }
      }}
    />

Type| DataSeries.<string>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataFramegetType`

# DataFrame#getType

### getType()

Get the data type of each DataSeries in the DataFrame.

returns

Type| Array.<string>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataFramemin`

# DataFrame#min

### min()

Get the global minimum value from all numeric DataSeries in the DataFrame.

returns

The following code sample shows how to use min to display the smallest data
point in a data source as a single value.



    <SingleValue
        options={{
            majorValue: '> primary | min()',
            trendDisplay: 'off',
            sparklineDisplay: 'off'
        }}
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: '_time',
                        },
                        {
                            name: 'count',
                        },
                    ],
                    columns: [
                        [
                            '2018-08-19T00:00:00.000+00:00',
                            '2018-08-20T00:00:00.000+00:00',
                            '2018-08-21T00:00:00.000+00:00',
                            '2018-08-22T00:00:00.000+00:00',
                            '2018-08-23T00:00:00.000+00:00',
                            '2018-08-24T00:00:00.000+00:00',
                            '2018-08-25T00:00:00.000+00:00',
                            '2018-08-26T00:00:00.000+00:00',
                        ],
                        ['1', '62', '103', '308', '587', '876', '930', '1320'],
                    ],
                },
                meta: {},
            },
        }}
    />

Type| number
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataPointgetField`

# DataPoint#getField

### getField()

Returns the data field of the point.

returns

Type| DataPoint.<'string'>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataPointgetType`

# DataPoint#getType

### getType()

Returns the data type of the point.

returns

Type| string
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataSeriesgetField`

# DataSeries#getField

### getField()

Returns the data source field which the series belongs to.

returns

Type| DataPoint.<'string'>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataSeriesgetType`

# DataSeries#getType

### getType()

Returns the inferred data type of the series.

returns

Type| string
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataSeriesmax`

# DataSeries#max

### max()

Returns the maximum DataPoint in the series.

returns

Type| DataPoint.<T>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `DataSeriesmin`

# DataSeries#min

### min()

Returns the minimum DataPoint in the series or undefined if no numbers in
series.

returns

Type| DataPoint.<T>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `delta`

# DataSeries#delta

### delta(index)

Finds the delta between the last point and point at the given index. A
negative index can be used, indicating an offset from the end of the sequence.

index

Type| number
---|---
Required| Yes

returns

Type| DataPoint
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `FeatureFlags`

# Feature Flags

Feature flags are a convenient way to toggle features on/off for an
application. You can override these feature flags, and add your own if
contributing to the library. Below is a list of feature flags available for
the Splunk Visualizations library. We’ve added ones for certain major features
or updates so that you may ensure it fits in users’ workflow before
introducing them into your application.

To toggle features on or off for your application you may update the default
value to true or false respectively in `visualization-context`.

## Consuming directly from @splunk/visualizations

To access these flags, wrap any component with the
`FeatureFlagContextProvider`



    import FeatureFlagContext from '@splunk/visualization-context/FeatureFlagContext';

    <FeatureFlagContextProvider value={{ visualizations_enableTrellis: true }}>

        <SingleValue … /> <!-- This component has visualizations_enableTrellis enabled -->

    </FeatureFlagContextProvider>

## Consuming from Unified Dashboard Framework (UDF)

To access these flags, you can use the `useFeatureFlags` hook in any child
component of a `DashboardContextProvider`.



    import { useFeatureFlags } from '@splunk/dashboard-context';

    const MyComponent = () => {
        const { visualizations_enableTrellis } = useFeatureFlags();
    };

If leveraging these visualizations from within UDF you may follow their
guidance on `featureFlags` as documented in Dashboard Context. UDF will
automatically leverage visualization feature flags as defined below.



    | Feature Flag                              | Default                | Description
    | -----------------------------------       |----------------------- | ------------------------------------------------------------------------------------------------------------------
    | visualizations_enableTrellis              | false                  | Supported visualizations can be rendered in trellis layout display mode if `splitByLayout: trellis` is configured.
    | visualizations_enableBubbleMapIcon        | false                  | This enables icon support for map bubble layer.
    | visualizations_enableTooltipIcon          | false                  | This enables icon support for tooltip field names for map bubble layer.
    | visualizations_useWebWorkersForDSL        | false                  | This offloads the DSL evaluation to a web-worker. Every visualization that uses `withDashboardViz` will send the options to a static method `AsyncDynamicOptionsEvaluator.evaluate` which returns a promise. When the DSL evaluation is complete the results are returned back to the viz via the promise.
    | visualizations_enableEventsViewerTags     | false                  | This enables viewing and editing tags in the Events visualization.
    | visualizations_enableDownsampling         | false                  | This enables largest-triangle-three-buckets downsampling for eligible charts with series.
    | visualizations_lazyLoadingDataFrame       | true                   | Builds an internal data structure on demand.
    | visualizations_bypassCloneDeepOptionScope | true                   | Stops cloning of data when evaluating DSL.

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `firstPoint`

# DataSeries#firstPoint

### firstPoint()

Return first dataPoint in series.

returns

Type| DataPoint
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameBySeriesIndexes`

# DataFrame#frameBySeriesIndexes

### frameBySeriesIndexes(...indexes)

Filter a DataFrame by specifying the indexes of the DataSeries you would like
to return. For example, `frameBySeriesIndexes(first_index, second_index,
...)`, where at least one index is required.

indexes

Type| Array.<number>
---|---
Required| Yes

returns

The following code sample shows how to use frameBySeriesIndexes to render a
table that includes the first, second, and fourth DataSeries from the data
source.



    <Table
      options={{
        table: '> primary | frameBySeriesIndexes(0,1,3)'
      }},
      dataSources={{
        primary: {
          data: {
            fields: [
              {
                name: 'Name'
              },
              {
                name: 'UserID'
              },
              {
                name: 'Money Spent'
              },
              {
                name: 'Most Recent Game'
              }
            ],
            columns: [
              [
                'Ms. Herman Beer',
                'Crystal Ziemann',
                'Phil Bartoletti',
                'Janis Kiehn V',
                'Angel Krajcik',
                'Patti Hodkiewicz IV',
                'Joanne Emmerich',
                'Jay Renner',
                'Ora Borer',
                'Dr. Bradford Gulgowski'
              ],
              [
                'Enrico98',
                'Taylor_Parker83',
                'Candice_Carroll',
                'Yolanda_McLaughlin95',
                'Modesto84',
                'Elwin52',
                'Francis8',
                'Charley.Feeney85',
                'Jensen_Jacobson74',
                'Dora_Volkman'
              ],
              [
                9740890.83,
                2107983.52,
                5467223.67,
                9529184.93,
                9692275.78,
                5692737.43,
                1001734.82,
                3848531.8,
                3848531.8
              ],
              [
                '2020-04-12T06:32:08-07:00',
                '2020-06-06T16:14:04-07:00',
                '2020-02-12T09:43:25-08:00',
                '2020-07-25T13:19:49-07:00',
                '2020-03-16T21:46:40-07:00',
                '2020-08-21T08:38:55-07:00',
                '2020-09-26T16:06:03-07:00',
                '2020-08-10T14:54:16-07:00',
                '2020-08-11T16:49:24-07:00',
                '2020-09-29T03:52:51-07:00'
              ]
            ]
          },
          meta: {
            totalCount: 100
          },
          requestParams: {
            count: 10,
            offset: 0
          }
        }
      }}
    />

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameBySeriesIndexRange`

# DataFrame#frameBySeriesIndexRange

### frameBySeriesIndexRange(start, [end])

Filter a DataFrame by specifying the index range [start, end) of the
DataSeries you would like to return. For example,
`frameBySeriesIndexRange(start_index)` or
`frameBySeriesIndexRange(start_index, end_index)`, where at least the starting
index is required.

start

(inclusive)

Type| int
---|---
Required| Yes

end

(optional, exclusive)

Type| int
---|---
Required| No

returns

The following code sample shows how to use frameBySeriesIndexRange to render a
table that includes the first, second, and third series from the data source.



    <Table
      options={{
        table: '> primary | frameBySeriesIndexRange(0,2)'
      }},
      dataSources={{
        primary: {
          data: {
            fields: [
              {
                name: 'Name'
              },
              {
                name: 'UserID'
              },
              {
                name: 'Money Spent'
              },
              {
                name: 'Most Recent Game'
              },
            ],
            columns: [
              [
                'Ms. Herman Beer',
                'Crystal Ziemann',
                'Phil Bartoletti',
                'Janis Kiehn V',
                'Angel Krajcik',
                'Patti Hodkiewicz IV',
                'Joanne Emmerich',
                'Jay Renner',
                'Ora Borer',
                'Dr. Bradford Gulgowski'
              ],
              [
                'Enrico98',
                'Taylor_Parker83',
                'Candice_Carroll',
                'Yolanda_McLaughlin95',
                'Modesto84',
                'Elwin52',
                'Francis8',
                'Charley.Feeney85',
                'Jensen_Jacobson74',
                'Dora_Volkman'
              ],
              [
                9740890.83,
                2107983.52,
                5467223.67,
                9529184.93,
                9692275.78,
                9395814.7,
                5692737.43,
                1001734.82,
                3848531.8,
                1691776.38
              ],
              [
                '2020-04-12T06:32:08-07:00',
                '2020-06-06T16:14:04-07:00',
                '2020-02-12T09:43:25-08:00',
                '2020-07-25T13:19:49-07:00',
                '2020-03-16T21:46:40-07:00',
                '2020-08-21T08:38:55-07:00',
                '2020-09-26T16:06:03-07:00',
                '2020-08-10T14:54:16-07:00',
                '2020-08-11T16:49:24-07:00',
                '2020-09-29T03:52:51-07:00'
              ]
            ]
          },
          meta: {
            totalCount: 100
          },
          requestParams: {
            count: 10,
            offset: 0
          }
        }
      }}
    />

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameBySeriesNames`

# DataFrame#frameBySeriesNames

### frameBySeriesNames(...names)

Filter a DataFrame by specifying the names of the DataSeries you would like to
return. For example, `frameBySeriesNames(first_name, second_name, ...)`, where
at least one series name is required.

names

Type| Array.<string>
---|---
Required| Yes

returns

The following code sample shows how to use frameBySeriesNames to render a
table with the Name and Money Spent columns in the data source.



    <Table
        options={{
            table: '> primary | frameBySeriesNames("Name", "Money Spent")'
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        },
                        {
                            name: 'Money Spent'
                        },
                        {
                            name: 'Most Recent Game'
                        },
                    ],
                    columns: [
                        [
                            'Ms. Herman Beer',
                            'Crystal Ziemann',
                            'Phil Bartoletti',
                            'Janis Kiehn V',
                            'Angel Krajcik',
                            'Patti Hodkiewicz IV',
                            'Joanne Emmerich',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Enrico98',
                            'Taylor_Parker83',
                            'Candice_Carroll',
                            'Yolanda_McLaughlin95',
                            'Modesto84',
                            'Elwin52',
                            'Francis8',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ],
                        [
                            9740890.83,
                            2107983.52,
                            5467223.67,
                            9529184.93,
                            9692275.78,
                            9395814.7,
                            5692737.43,
                            1001734.82,
                            3848531.8,
                            1691776.38
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-02-12T09:43:25-08:00',
                            '2020-07-25T13:19:49-07:00',
                            '2020-03-16T21:46:40-07:00',
                            '2020-08-21T08:38:55-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameBySeriesNamesOrIndexes`

# DataFrame#frameBySeriesNamesOrIndexes

### frameBySeriesNamesOrIndexes(...namesOrIndexes)

Filter a DataFrame by specifying one or more names or indexes of DataSeries
you would like to return. For example,`frameBySeriesNames(first_name_or_index,
second_name_or_index, ...)`, where at least one name or index is required.

namesOrIndexes

Type| string, number
---|---
Required| Yes

returns

The following code sample shows how to use frameBySeriesNamesOrIndexes to
render a table with the Name DataSeries and the fourth DataSeries in the data
source.



    <Table
        options={{
            table: '> primary | frameBySeriesNamesOrIndexes("Name", 3)'
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        },
                        {
                            name: 'Money Spent'
                        },
                        {
                            name: 'Most Recent Game'
                        },
                    ],
                    columns: [
                        [
                            'Ms. Herman Beer',
                            'Crystal Ziemann',
                            'Phil Bartoletti',
                            'Janis Kiehn V',
                            'Angel Krajcik',
                            'Patti Hodkiewicz IV',
                            'Joanne Emmerich',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Enrico98',
                            'Taylor_Parker83',
                            'Candice_Carroll',
                            'Yolanda_McLaughlin95',
                            'Modesto84',
                            'Elwin52',
                            'Francis8',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ],
                        [
                            9740890.83,
                            2107983.52,
                            5467223.67,
                            9529184.93,
                            9692275.78,
                            9395814.7,
                            5692737.43,
                            1001734.82,
                            3848531.8,
                            1691776.38
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-02-12T09:43:25-08:00',
                            '2020-07-25T13:19:49-07:00',
                            '2020-03-16T21:46:40-07:00',
                            '2020-08-21T08:38:55-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00',
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams: {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameBySeriesTypes`

# DataFrame#frameBySeriesTypes

### frameBySeriesTypes(...types)

Filter a DataFrame by specifying one or more types of DataSeries you would
like to return. For example, `frameBySeriesNames(first_type, second_type,
...)`, where at least one type is required.

types

Type| Array.<DataType>
---|---
Required| Yes

returns

The following code sample shows how to use frameBySeriesTypes to render a
table that contains only the string columns in the data source.



    <Table
        options={{
            table: '> primary | frameBySeriesTypes("string")'
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        },
                        {
                            name: 'Money Spent'
                        },
                        {
                            name: 'Most Recent Game'
                        },
                    ],
                    columns: [
                        [
                            'Ms. Herman Beer',
                            'Crystal Ziemann',
                            'Phil Bartoletti',
                            'Janis Kiehn V',
                            'Angel Krajcik',
                            'Patti Hodkiewicz IV',
                            'Joanne Emmerich',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Enrico98',
                            'Taylor_Parker83',
                            'Candice_Carroll',
                            'Yolanda_McLaughlin95',
                            'Modesto84',
                            'Elwin52',
                            'Francis8',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ],
                        [
                            9740890.83,
                            2107983.52,
                            5467223.67,
                            9529184.93,
                            9692275.78,
                            9395814.7,
                            5692737.43,
                            1001734.82,
                            3848531.8,
                            1691776.38
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-02-12T09:43:25-08:00',
                            '2020-07-25T13:19:49-07:00',
                            '2020-03-16T21:46:40-07:00',
                            '2020-08-21T08:38:55-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams: {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameWithoutInternalFields`

# DataFrame#frameWithoutInternalFields

### frameWithoutInternalFields()

Filter a DataFrame by removing all internal fields starting with underscore `_`. For example, if you have a primary data source with the following fields: `_time, _span, date, count, cost, _raw`, then DSL `> primary | frameWithoutInternalFields()` removes all the internal fields and returns the DataFrame with fields `date, count, cost`.

returns

The following code sample shows how to use `frameWithoutInternalFields()` to
remove the internal fields from the data source.



    <Table
        options={{
            table: '> primary | frameWithoutInternalFields()'
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        },
                        {
                            name: '_time'
                        },
                        {
                            name: '_span'
                        },
                    ],
                    columns: [
                        [
                            'Ms. Herman Beer',
                            'Crystal Ziemann',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Enrico98',
                            'Taylor_Parker83',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ],
                        [
                            '1800',
                            '1800',
                            '1800',
                            '1800',
                            '1800'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

This code sample will visualize a table with the `Name` and `UserID` columns,
and the columns of `_time` and `_span` (internal fields) will not be
displayed.

Another example of using `frameWithoutInternalFields()` in a chained DSL:



    <SingleValue
        options={{
            "majorValue": "> primary | frameWithoutInternalFields() | seriesByIndex(0) | lastPoint()"
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: '_time'
                        },
                        {
                            name: '_span'
                        },
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        }
                    ],
                    columns: [
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ],
                        [
                            '1800',
                            '1800',
                            '1800',
                            '1800',
                            '1800'
                        ],
                        [
                            'Patti Hodkiewicz IV',
                            'Joanne Emmerich',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Elwin52',
                            'Francis8',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

This code sample will visualize `Dr. Bradford Gulgowski` as the major value,
because both internal fields (`_time` and `_span`) are removed and index `0`
of the rest of the data frame corresponds to the `Name` column.

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `frameWithoutInternalFieldsExcept`

# DataFrame#frameWithoutInternalFieldsExcept

### frameWithoutInternalFieldsExcept(...names)

Filter a DataFrame by removing all internal fields starting with underscore `_`, except for the fields listed in `names`. For example, if you have a primary data source with the following fields: `_time, _span, date, count, cost, _raw`, then DSL `> primary | frameWithoutInternalFields('_time')` removes all the internal fields except `_time` and returns the DataFrame with fields `_time, date, count, cost`. If you want to remove all the internal fields, use `frameWithoutInternalFields()` instead. If you pass any non-internal fields as parameters, they will be ignored.

names

Type| Array.<string>
---|---
Required| Yes

returns

The following code sample shows how to use
`frameWithoutInternalFieldsExcept(...names)` to remove some internal fields
from the data source, but leaving specified internal fields by their field
names.



    <Table
        options={{
            table: '> primary | frameWithoutInternalFieldsExcept('_time', '_span')'
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        },
                        {
                            name: '_time'
                        },
                        {
                            name: '_span'
                        },
                        {
                            name: '_raw'
                        },
                    ],
                    columns: [
                        [
                            'Ms. Herman Beer',
                            'Joanne Emmerich',
                            'Jay Renner',
                            'Ora Borer',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Enrico98',
                            'Francis8',
                            'Charley.Feeney85',
                            'Jensen_Jacobson74',
                            'Dora_Volkman'
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ],
                        [
                            '1800',
                            '1800',
                            '1800',
                            '1800',
                            '1800'
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

This code sample will visualize the table with the `Name`, `UserID`, `_time`
and `_span` columns, and the `_raw` columns will not be displayed.

Another example of using `frameWithoutInternalFieldsExcept(...names)` in a
chained DSL:



    <SingleValue
        options={{
            "majorValue": "> primary | frameWithoutInternalFieldsExcept('_time') | seriesByIndex(1) | lastPoint()"
        }},
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: '_time'
                        },
                        {
                            name: '_span'
                        },
                        {
                            name: '_raw'
                        },
                        {
                            name: 'Name'
                        },
                        {
                            name: 'UserID'
                        }
                    ],
                    columns: [
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-09-26T16:06:03-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ],
                        [
                            '1800',
                            '1800',
                            '1800',
                            '1800',
                            '1800'
                        ],
                        [
                            '2020-04-12T06:32:08-07:00',
                            '2020-06-06T16:14:04-07:00',
                            '2020-08-10T14:54:16-07:00',
                            '2020-08-11T16:49:24-07:00',
                            '2020-09-29T03:52:51-07:00'
                        ],
                        [
                            'Ms. Herman Beer',
                            'Crystal Ziemann',
                            'Angel Krajcik',
                            'Jay Renner',
                            'Dr. Bradford Gulgowski'
                        ],
                        [
                            'Candice_Carroll',
                            'Elwin52',
                            'Francis8',
                            'Charley.Feeney85',
                            'Dora_Volkman'
                        ]
                    ]
                },
                meta: {
                    totalCount: 100
                },
                requestParams {
                    count: 10,
                    offset: 0
                }
            }
        }}
    />

This code sample will visualize `Dr. Bradford Gulgowski` as the major value,
because the internal fields other than `_time` are excluded, and index `1` of
the rest of the data frame (`_time`, `Name`, `UserID`) corresponds to the
`Name` column.

Type| DataFrame.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `FundamentalsofDSL`

# Fundamentals of DSL

The consolidated visualizations package introduces a DSL to bind options to
data and provide a rich data-driven visualization configuration experience.
While options for a visualization still accept static values, DSL allows for
dynamically configuring option values at runtime based on received data. The
DSL allows the user to read data from a specified identifier, apply formatting
and transformations to the selected data, specify a formatting/transformation
pipeline to process the data, and to use the resultant output as the value for
a given option.

## Data Primitives

The structure of the data the DSL receives can be categorized within three
main Data Primitive structures: `DataFrame`, `DataSeries`, and `DataPoint`.
Within the DSL, the data that is piped from one selector/formatter to another
conforms to one of these given Data Primitive structures (or their raw
equivalents).

A `DataFrame` is comprised of a list of `DataSeries`, a `DataSeries` is a list
of `DataPoints`, and a `DataPoint` holds an individual primitive value (e.g. a
string, number, boolean).

## DSL Selectors

To select the data of interest when configuring a dynamic option, the DSL
exposes a list of selectors to reduce the data from its original structure.
These selectors are defined at the `DataFrame`, `DataSeries`, and `DataPoint`
levels.

## DSL Formatters

DSL formatters allow you to transform and map the data you receive into the
desired format. Some formatters replace the original functions of encoding v1
(e.g. specifying gradients, thresholding, and match values), while others
provide additional data formatting capabilities that were not possible in
encoding v1 (e.g. formatting string data values via units, prepending text to
data, etc.).

## DSL Scopes

The main global scopes that the DSL can read identifiers from are `context`,
`datasources`, `options`, and `themes`. The contents of `context`,
`datasources`, and `options` and scopes are directly defined by the user and
passed into the visualization, while values from `themes` are taken from the
theme variables that the given visualization exposes. In addition to
identifiers found in global scopes, DSL can resolve identifiers at the local
scope as shown in the example below.

### Qualified (global) vs. Unqualified Identifiers

Qualified identifiers are references to DSL-scoped variables which denote the
full path to the DSL-scoped variable value (e.g. `context.foo.bar`). However,
the DSL can also infer the value of local identifiers. For example, if a
deeply nested identifier is defined within `context` and is referenced at the
local scope (such as `context={{ foo: { bar: 'val1', d: '> bar' } }}`), the
DSL defined in `context.foo.d` will be resolved as `val1`.

If an identifier is not prefixed with one of the aforementioned global scopes,
the DSL will first look at the local level (i.e. other identifiers defined at
the same level relative to where the original identifier was defined) to
resolve the value. If this does not return a match, the DSL will look through
the list of identifiers defined at the first level of the global scope objects
to find the identifier (i.e. `context.identifier`, `datasources.identifier`,
`options.identifier`, `themes.identifier`).

The following shows an example of how DSL variable name resolution is
performed.



    <SampleViz
        context={{
            foo: 2,
            bar: 3,
        }}
        options={{
            foo: 1,
            // the DSL will first look at the local scope before searching through context.foo, datasources.foo, and themes.foo
            // in this case, color will be resolved as 1
            color: '> foo',
            // since there is no local match, the DSL will look through the global scopes to find a corresponding identifier
            // in this case, value will be resolved as 3
            value: '> bar',
        }}
    />

## Use

The example below shows a SingleValue visualization configured to use DSL for
dynamically defining certain options.



    import SingleValue from '@splunk/visualizations/SingleValue';

    export default () => (
        <SingleValue
            context={{
                trendColorThresholds: [
                    {
                        from: 1321,
                        value: '#00FFFF',
                    },
                    {
                        to: 1321,
                        value: '#FF00FF',
                    },
                ],
            }}
            options={{
                sparklineValues: '> primary | seriesByIndex(0)',
                trendValue: '> sparklineValues | delta(-2)',
                trendColor: '> trendValue | rangeValue(trendColorThresholds)',
            }}
            dataSources={{
                primary: {
                    // the JSON input for a DataFrame has the structure of { data: { columns: [...], fields: [...], meta: {...} }
                    data: {
                        columns: [
                            ['1', '62', '103', '308', '587', '876', '930', '1320'],
                            [
                                '2018-08-19T00:00:00.000+00:00',
                                '2018-08-20T00:00:00.000+00:00',
                                '2018-08-21T00:00:00.000+00:00',
                                '2018-08-22T00:00:00.000+00:00',
                                '2018-08-23T00:00:00.000+00:00',
                                '2018-08-24T00:00:00.000+00:00',
                                '2018-08-25T00:00:00.000+00:00',
                                '2018-08-26T00:00:00.000+00:00',
                            ],
                        ],
                        fields: [
                            {
                                name: 'foo',
                            },
                            {
                                name: 'bar',
                            },
                        ],
                    },
                    meta: {},
                },
            }}
        />
    );

In this example, DSL is configured for the `sparklineValues`, `trendValue`,
and `trendColor` options.

The `sparklineValues` DSL reads data from the `primary` identifier (which is
defined within the `datasources` global scope) and reads data of a
`DataFrame`-type structure from the `primary` identifier. This data is then
reduced to a `DataSeries` structure by applying the `seriesByIndex` DSL
selector, and the `sparklineValues` option receives this resolved output as
its dynamic value.

The `trendValues` DSL takes the resolved data of the `sparklineValues` (which
now exists at the local scope) and applies the `delta` selector to reduce this
even further to a `DataPoint` data structure.

The `trendColor` DSL applies formatting to the DataPoint by mapping the target
range that the `DataPoint` falls into. The corresponding `DataPoint` value for
the target range is then returned.

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `getRawValue`

# DataFrame#getRawValue

### getRawValue()

Get all values in the DataFrame. This excludes field names.

returns

Type| array
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `InteractionGuide`

# Viz Interactions and Events

## Interaction Structure

Our components trigger event payloads when interacting with parts of the
visualization. These include clicks, mouseovers, selections, and more. For
example, clicking on a column in a column chart will give:



    {
        "name": "splunkd",
        "value": 29763,
        "row._time.value": 1578268800.0,
        "row.mongod.value": 10467,
        "row.splunkd.value": 29763,
        "row.splunkd_web_access.value": 29763
    }

Below is the corresponding column chart when being hovered over that same
point.

Column chart in default state (left) and when a point is being hovered on
(right).

Certain visualizations may require different click interactions depending on
its purpose. A common usage for click interactions is to drill down based on
the given data point, for example. In the above example, this action will
provide the name `splunkd` that may be used to pass a token value in a new
search. There are various actions that may be desirable to set up based on the
visualization and/or use case, but behavior should be consistent and
predictable.

Click interactions for visualization components may vary based on the
necessity of states. There may be times when a part of the visualization needs
to be selected. For example,

  * Timeseries charts allow time range selection to zoom in on a more granular time span
  * LinkGraph requires node selection to highlight and further investigate the important information in the visualization
  * ParallelCoordinates allows selection to highlight lines that intersect that range on the axis

Although you may customize this to suit the needs of your application, we
recommend the following behavior to stay consistent with other Splunk
applications. Visualizations that provide highlighting actions should support
that selection functionality and you may add a menu for further actions. For
example, this action menu could provide options including:

  * Drilldown to url
  * Drilldown to search with a passed token
  * Drilldown to another visualization on the page with a passed token

Below are the events in visualizations that provide payloads that you may use
to trigger various actions. A full comprehensive list can be found in the
Events tab on each visualization in our documentation.



    |-----------------------------------------------------------------------|
    | Type                                               | Event            |
    | -------------------------------------------------- | ---------------- |
    | Charts                                             | legend.click     |
    |                                                    | point.click      |
    | Charts Area, Bar, Bubble, Column,                  | point.mouseover  |
    | Line, Pie, Punchcard, Scatter                      | point.mouseout   |
    | -------------------------------------------------- | ---------------- |
    | Charts (Time series)                               |                  |
    |                                                    | range.select     |
    | Area, Column, Line                                 |                  |
    | -------------------------------------------------- | ---------------- |
    | ChoroplethSVG                                      | area.click       |
    | -------------------------------------------------- | ---------------- |
    | Shapes                                             |                  |
    |                                                    | <shape>.click    |
    | Shapes Ellipse, Rectangle                          |                  |
    | -------------------------------------------------- | ---------------- |
    | Single Values                                      |                  |
    |                                                    | value.click      |
    | SingleValue, SingleValueIcon, SingleValueRadial    |                  |
    | -------------------------------------------------- | ---------------- |
    | Table                                              | cell.click       |
    |-----------------------------------------------------------------------|

## Token Structure

Event payloads can be used to set tokens, display additional information, and
highlight data in connected visualizations.

The Visualizations team recommends implementing the following token structure
and naming to follow consistency across various components in the Splunk
portfolio if you surface tokens.

Users should be able to quickly understand and become familiar with what
tokens they can use and what values they can expect to be returned.



    |---------------------------------------------------------------------------------------|
    |                     |         name        |       value         |row.<fieldname>.value|
    |---------------------|---------------------|---------------------|---------------------|
    | Charts (Axis)       |Y-axis field name of | Y-axis value of the | Value in the        |
    |                     |the series/location  | series/location     | specified series    |
    | Area, Bar, Bubble,  |clicked              | clicked             | corresponding to the|
    | Column, Line,       |                     |                     | location clicked    |
    | Punchcard, Scatter  |                     |                     |                     |
    |---------------------|---------------------|---------------------|---------------------|
    | ChoroplethSVG       | Name of the area    | Value of the area   |                     |
    |                     | clicked             | clicked             |                     |
    |---------------------|---------------------|---------------------|---------------------|
    | Pie                 | Field Name of the   | Value of the        | Value in the        |
    |                     | value clicked       | location clicked    | specified series    |
    |                     |                     |                     | corresponding to the|
    |                     |                     |                     | location clicked    |
    |---------------------|---------------------|---------------------|---------------------|
    | Shapes              |                     |                     |                     |
    |                     |                     |                     |                     |
    | Ellipse, Rectangles |                     |                     |                     |
    |---------------------|---------------------|---------------------|---------------------|
    | Single Values       | Field name of the   | Value of the        |                     |
    |                     | majorValue          | majorValue          |                     |
    | SingleValue,        |                     |                     |                     |
    | SingleValueIcon,    |                     |                     |                     |
    | SingleValueRadial   |                     |                     |                     |
    |---------------------|---------------------|---------------------|---------------------|
    | Table               | Field Name of the   | Value of the        | Value in the        |
    |                     | cell clicked        | cell clicked        | specified series    |
    |                     |                     |                     | corresponding to the|
    |                     |                     |                     | same row as the     |
    |                     |                     |                     | cell clicked        |
    |---------------------------------------------------------------------------------------|

For example, if a user clicks on `71280` in the Table below they may have the
option to pass `row.sourcetype.value` which would return `mongod`.

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `lastPoint`

# DataSeries#lastPoint

### lastPoint()

Return last dataPoint in series.

returns

Type| DataPoint
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `pointByIndex`

# DataSeries#pointByIndex

### pointByIndex(index)

Finds and returns the individual dataPoint at the given index.

index

Type| number
---|---
Required| Yes

returns

Type| DataPoint
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `pointsByIndexes`

# DataSeries#pointsByIndexes

### pointsByIndexes(...indexes)

Finds dataPoint(s) in DataSeries by index(es).

indexes

Type| number
---|---
Required| Yes

returns

Type| DataSeries
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `Prefix`

# Prefix

Prepends the given prefix (passed as a parameter) to the DataPoint.



    <SampleViz
        options={{
            textOption: '> primary | seriesByName("foo") | lastPoint() | prefix("bar")' // returns "bar100"
        }}
        dataSources={{
            primary: {
                data: {
                    fields: [{ name: 'foo' }]
                    columns: [[100, 200]]
                }
            }
        }}
    />

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `seriesByIndex`

# DataFrame#seriesByIndex

### seriesByIndex(index)

Select a DataSeries by specifying the index of the series you want to return.

index

Type| number
---|---
Required| Yes

returns

The following code sample shows how to use seriesByIndex to display the second
series in a data source as a single value.



    <SingleValue
        options={{
            sparklineValues: '> primary | seriesByIndex(1)'
        }}
        dataSources={{
            primary: {
                data: {
                    fields: [
                        {
                            name: '_time',
                        },
                        {
                            name: 'count',
                        },
                    ],
                    columns: [
                        [
                            '2018-08-19T00:00:00.000+00:00',
                            '2018-08-20T00:00:00.000+00:00',
                            '2018-08-21T00:00:00.000+00:00',
                            '2018-08-22T00:00:00.000+00:00',
                            '2018-08-23T00:00:00.000+00:00',
                            '2018-08-24T00:00:00.000+00:00',
                            '2018-08-25T00:00:00.000+00:00',
                            '2018-08-26T00:00:00.000+00:00',
                        ],
                        ['1', '62', '103', '308', '587', '876', '930', '1320'],
                    ],
                },
                meta: {},
            },
        }}
    />

Type| DataSeries.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `seriesByPrioritizedTypes`

# DataFrame#seriesByPrioritizedTypes

### seriesByPrioritizedTypes(...types)

Select a DataSeries by specifying the prioritized types of the DataSeries you
would like to return. The first DataSeries that matches the first type
specified will be returned. If no DataSeries matches the first type specified,
the first DataSeries that matches the second type will be returned, and so on.

types

Type| Array.<DataType>
---|---
Required| Yes

returns

The following code sample shows how to use seriesByPrioritizedTypes to display
the first numeric series in a data source as a single value.

If no numeric series are found in the data, the first series of type string is
displayed. If no string series are found, the first series of type time is
displayed.



    <SingleValue
        options={{
            sparklineValues: '> primary | seriesByPrioritizedTypes'("number", "string", "time"),
        }}
        dataSources={{
            primary: {
                data: {
                    columns: [
                        [
                            '2018-08-19T00:00:00.000+00:00',
                            '2018-08-20T00:00:00.000+00:00',
                            '2018-08-21T00:00:00.000+00:00',
                            '2018-08-22T00:00:00.000+00:00',
                            '2018-08-23T00:00:00.000+00:00',
                            '2018-08-24T00:00:00.000+00:00',
                            '2018-08-25T00:00:00.000+00:00',
                            '2018-08-26T00:00:00.000+00:00',
                        ],
                        [ 'INFO', 'ERROR', 'WARN', 'INFO', 'ERROR', 'WARN', 'INFO', 'WARN'],
                    ],
                    fields: [
                        {
                            name: '_time',
                        },
                        {
                            name: 'status',
                        },
                    ],
                },
                meta: {},
            },
        }}
    />

Type| DataSeries.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `seriesByTypes`

# DataFrame#seriesByTypes

### seriesByTypes(...types)

Select a DataSeries by specifying any acceptable types of the DataSeries you
would like to return. The first DataSeries that matches any of the types
specified will be returned. If no DataSeries matches the type options
specified, no DataSeries will be returned.

types

Type| Array.<DataType>
---|---
Required| Yes

returns

Type| DataSeries.<DataType>
---|---

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `setValue`

# DataFrame#setValue

### setValue(v)

Set all values in the DataFrame to a static TypedValue.

v

Type| TypedValue
---|---
Required| Yes

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `Table`

# Table

Overview

Examples

Options

Events

A table is used to display values across a dataset simply and is especially
useful with qualitative data.

### Tips

  * Consider using color or sparkline formatting to communicate cell values.

## Table Formatting & Alignment

Show codeShow dashboard definition

You may apply formatting to the whole table. For example, set a background
color, header color, fixed header, number and time formatting. Any numbro.js
library option can be used.

* * *

number1|

* * *

time
---|---
1.9531 KiB| 05-02-2018 at 06:10 PM
9.5367 MiB| 05-02-2018 at 06:11 PM
13.0000 B| 05-02-2018 at 06:12 PM
60.0000 B| 05-02-2018 at 06:13 PM
43.0000 B| 05-02-2018 at 06:15 PM

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev12345Next

## Column Formatting & Alignment

Show code

* * *

name|

* * *

ellipsis|

* * *

break-word|

* * *

anywhere
---|---|---|---
Handcrafted Metal Shoes| Handcrafted Metal Shoes| Handcrafted Metal Shoes|
Handcrafted Metal Shoes
Refined Fresh Fish| Refined Fresh Fish| Refined Fresh Fish| Refined Fresh Fish
Small Metal Bacon| Small Metal Bacon| Small Metal Bacon| Small Metal Bacon
Intelligent Rubber Chips| Intelligent Rubber Chips| Intelligent Rubber Chips|
Intelligent Rubber Chips
Incredible Rubber Car| Incredible Rubber Car| Incredible Rubber Car|
Incredible Rubber Car

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev12345Next

## Column Coloring By Gradient

Show code

* * *

foo|

* * *

bar
---|---
1| Sat May 03 2025
3| Mon Jun 02 2025
6| Sun Aug 10 2025
10| Mon Nov 18 2024
15| Sun Jan 26 2025

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev12345Next

## Sparkline Formatting

Show codeShow dashboard definition

Set cell types for different columns to display string or sparkline data.
Customize sparklines with a type and style.

* * *

sourcetype|

* * *

count|

* * *

bytes|

* * *

pattern
---|---|---|---
splunk_web_access| 55829| Source count over time sparkline trend| Source count
over time sparkline trend
splunkd| 56035| Source count over time sparkline trend| Source count over time
sparkline trend
splunkd| 69422| Source count over time sparkline trend| Source count over time
sparkline trend
splunk_web_access| 2528| Source count over time sparkline trend| Source count
over time sparkline trend
splunk_web_service| 61195| Source count over time sparkline trend| Source
count over time sparkline trend
splunkd_access| 92938| Source count over time sparkline trend| Source count
over time sparkline trend
splunk_archiver-2| 61315| Source count over time sparkline trend| Source count
over time sparkline trend
splunkd_access| 57856| Source count over time sparkline trend| Source count
over time sparkline trend
splunkd| 18312| Source count over time sparkline trend| Source count over time
sparkline trend
splunk_archiver-2| 60781| Source count over time sparkline trend| Source count
over time sparkline trend

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev12345…Next

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `Timeline`

# Timeline

#### ⚠️ This is a preview of a new visualization component. Minor updates and
bug fixes should be expected.

Overview

Examples

Options

Events

A timeline visualization displays activity intervals and events over time for
a set of resources. Each resource is represented in a separate lane, where
intervals with a defined start time and duration appear as horizontal bars,
while discrete events with only a start time are shown as circles.

### Tips

  * Use timelines to visualize sequences of events or overlapping activities.
  * Ensure consistent time scaling to maintain accuracy and readability.
  * Best for tracking resource utilization, project timelines, or event patterns over time.

## Single Series

Show codeShow dashboard definition

Use a single series timeline to display activity intervals or events for a
single category of data over time.

Lane 1

Lane 2

Lane 3

Lane 4

Lane 5

Lane 6

Lane 7

## Multi Series

Show codeShow dashboard definition

Use a multi series timeline to compare overlapping activities or different
event types for multiple resources over time.

Lane 1

Lane 2

Lane 3

Lane 4

Lane 5

Lane 6

Lane 7

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `Type`

# Type

Formatter that returns the DataType for each element within the given
DataSeries.



    <SampleViz
        options={{
            option1: '> primary | seriesByIndex(0) | type()' // returns ['number', 'number', 'number']
            option2: '> primary | seriesByIndex(1) | type()' // returns ['string', 'string', 'string']
        }}
        dataSources={{
            data: {
                primary: {
                    columns: [[100, 200, 300], ['string1', 'string2', 'string3']]
                    fields: [{ name: 'foo' }, { name: 'bar' }]
                }
            }
        }}
    />

---

## @splunk/visualizations - 28.1.0

**Package:** `visualizations` | **Component:** `VisualizationsGallery`

# Visualizations Gallery

Categories

Platform Visualizations(1)

## Platform Visualizations

  1. Basic example for Area[Area](?path=%2FArea)

### Chart

Chart with 2 data series.

The chart has 1 X axis displaying _time. Range: 2018-05-02 21:10:46 to
2018-05-02 21:15:50.

The chart has 1 Y axis displaying axis_5. Range: 0 to 750.

Created with Highcharts 9.3.3_timecountpercent9:11 PM ​Wed May 2 ​20189:12
PM9:13 PM9:14 PM9:15 PM0250500750

     *      * End of interactive chart.

  2. Basic example for Bar[Bar](?path=%2FBar)

### Chart

Bar chart with 3 bars.

The chart has 1 X axis displaying component.

The chart has 1 Y axis displaying admin. Range: 0 to 10000.

Created with Highcharts
9.3.3componentadminadminfoobarfoobar01K2K3K4K5K6K7K8K9K10K

     * End of interactive chart.

  3. Basic example for Bubble[Bubble](?path=%2FBubble)

### Chart

Bubble chart with 15 bubbles. Bubble charts are scatter charts where each data
point also has a size value.

The chart has 1 X axis displaying date_hour. Range: 2 to 24.

The chart has 1 Y axis displaying count. Range: 500 to 2500.

Created with Highcharts
9.3.3date_hourcount246810121416182022240.5K1.0K1.5K2.0K2.5K

End of interactive chart.

  4. Basic example for ChoroplethSvg[ChoroplethSvg](?path=%2FChoroplethSvg)

  5. Basic example for Column[Column](?path=%2FColumn)

### Chart

Bar chart with 6 bars.

The chart has 1 X axis displaying _time. Range: 2018-05-02 21:10:46 to
2018-05-02 21:17:30.

The chart has 1 Y axis displaying admin. Range: 0 to 100.

Created with Highcharts 9.3.3_timeadminadmin9:11 PM ​Wed May 2 ​20189:12
PM9:13 PM9:14 PM9:15 PM9:16 PM9:17 PM9:18 PM050100

     * End of interactive chart.

  6. Basic example for Ellipse[Ellipse](?path=%2FEllipse)

  7. Basic example for Events[Events](?path=%2FEvents)

| Time| Event
---|---|---
| [4/2/2018
7:33:49.691 PM]()| `

     * {[-]Collapse all
       *     datetime: "07-16-2018 16:38:11.545 -0700",
       *     log_level: "INFO",
       *     component: "KVStoreServerStats",
       *     data: {[+]Shift click to expand all}
}

`[Show as raw text]()

| [4/2/2018
7:33:49.691 PM]()| 04-02-2018 16:33:49.691 -0700 INFO Metrics - group=thruput,
name=thruput, instantaneous_kbps=0.8775482519547254,
instantaneous_eps=3.5802456751680514, average_kbps=0.7280928568987709,
total_k_processed=4794, kb=27.20703125, ev=111, load_average=2.87744140625

| [4/2/2018
7:33:49.691 PM]()| 04-02-2018 16:33:49.691 -0700 INFO Metrics - group=thruput,
name=thruput, instantaneous_kbps=0.8775482519547254,
instantaneous_eps=3.5802456751680514, average_kbps=0.7280928568987709,
total_k_processed=4794, kb=27.20703125, ev=111, load_average=2.87744140625

| [4/2/2018
7:33:49.691 PM]()| 04-02-2018 16:33:49.691 -0700 INFO Metrics - group=thruput,
name=thruput, instantaneous_kbps=0.8775482519547254,
instantaneous_eps=3.5802456751680514, average_kbps=0.7280928568987709,
total_k_processed=4794, kb=27.20703125, ev=111, load_average=2.87744140625

| [4/2/2018
7:33:49.691 PM]()| 04-02-2018 16:33:49.691 -0700 INFO Metrics - group=thruput,
name=thruput, instantaneous_kbps=0.8775482519547254,
instantaneous_eps=3.5802456751680514, average_kbps=0.7280928568987709,
total_k_processed=4794, kb=27.20703125, ev=111, load_average=2.87744140625

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

  8. Basic example for FillerGauge[FillerGauge](?path=%2FFillerGauge)

02040608010078

  9. Basic example for Image[Image](?path=%2FImage)

  10. Basic example for Line[Line](?path=%2FLine)

### Chart

Line chart with 2 lines.

The chart has 1 X axis displaying _time. Range: 2018-05-02 21:10:46 to
2018-05-02 21:15:50.

The chart has 1 Y axis displaying axis_26. Range: 0 to 750.

Created with Highcharts 9.3.3_timecountpercent9:11 PM ​Wed May 2 ​20189:12
PM9:13 PM9:14 PM9:15 PM0250500750

     *      * End of interactive chart.

  11. Basic example for LinkGraph[LinkGraph](?path=%2FLinkGraph)

country

4

src_ip

6

ip_subnet_16

5

status

6

logged_in

2

http_method

6

Netherlands

1

United Kingdom

2

Senegal

1

China

2

185.130.122.339

1

185.130.12.339

1

44.920.1.554

1

190.130.122.339

1

76.100.42.339

1

185.920.1.554

1

185.130.x.x

1

185.920.x.x

1

190.130.x.x

1

76.100.x.x

1

44.920.x.x

2

200

1

302

1

301

1

500

1

404

1

401

1

0

3

1

3

GET

1

POST

1

PROPFIND

1

HEAD

1

PUT

1

-

1

  12. Basic example for Map[Map](?path=%2FMap)

Use Ctrl + scroll to zoom map

Use two fingers to move the map

2000 km

  13. Basic example for Markdown[Markdown](?path=%2FMarkdown)

# Heading level 1

## Heading level 2

### Heading level 3

**bold text** _italic text_

[link here](http://example.com/)

> quote

horizontal line:

* * *

`small code section`


         // large code section
         import React from 'react';
         import Markdown from '@splunk/visualizations/Markdown';

     * first bullet item
     * second bullet item
     1. first item
     2. second item

  14. Basic example for MarkerGauge[MarkerGauge](?path=%2FMarkerGauge)

02040608010020

  15. Basic example for ParallelCoordinates[ParallelCoordinates](?path=%2FParallelCoordinates)

000055551010101015151515202020202525252530303030353535354040404045454545economy
(mpg)3.033.033.53.53.53.54.044.044.54.54.54.55.055.055.55.55.55.56.066.066.56.56.56.57.077.077.57.57.57.58.088.08cylinders100100100100150150150150200200200200250250250250300300300300350350350350400400400400450450450450displacement
(cc)000020202020404040406060606080808080100100100100120120120120140140140140160160160160180180180180200200200200220220220220power
(hp)2,00020002,00020002,50025002,50025003,00030003,00030003,50035003,50035004,00040004,00040004,50045004,50045005,00050005,0005000weight
(lb)888810101010121212121414141416161616181818182020202022222222242424240-60
mph
(s)70707070717171717272727273737373747474747575757576767676777777777878787879797979808080808181818182828282yearnull

Clear filters406/406 lines selected

Note: Your data is currently truncated due to a high amount of categorical
values

  16. Basic example for Pie[Pie](?path=%2FPie)

### Chart

Pie chart with 10 slices.

Created with Highcharts
9.3.3AprilMayJuneJulyAugustSeptemberOctoberNovemberDecemberother (3)

End of interactive chart.

  17. Basic example for Punchcard[Punchcard](?path=%2FPunchcard)

121211223344556677889910101111mondaymondaytuesdaytuesdaywednesdaywednesdaythursdaythursdayfridayfridaysaturdaysaturdaysundaysunday315NullNull10207513052393623NullNull110266513357183842Null11122882109642534122Null182973119563430821Null3103266113583938111155NullNull61431474962161181NullNull4512246470

  18. Basic example for Rectangle[Rectangle](?path=%2FRectangle)

  19. Basic example for Sankey[Sankey](?path=%2FSankey)

OilFossil FuelsNatural GasCoalElectricityEnergy

  20. Basic example for Scatter[Scatter](?path=%2FScatter)

### Chart

Scatter chart with 4 data series.

The chart has 1 X axis displaying date_hour. Range: 0 to 24.

The chart has 1 Y axis displaying count. Range: 1000 to 2500.

Created with Highcharts
9.3.3date_hourcount4012014042000246810121416182022241.0K1.5K2.0K2.5K

     *      *      *      * End of interactive chart.

  21. Basic example for SingleValue[SingleValue](?path=%2FSingleValue)

1,320

Arrow Up

390

Source count over time sparkline trend

  22. Basic example for SingleValueIcon[SingleValueIcon](?path=%2FSingleValueIcon)

Question

1,320

Arrow Up

390

  23. Basic example for SingleValueRadial[SingleValueRadial](?path=%2FSingleValueRadial)

88

Arrow Up

25

  24. Basic example for Table[Table](?path=%2FTable)

* * *

foo|

* * *

bar
---|---
Tue Jan 21 2025| Mon Aug 25 2025
Sat May 31 2025| Wed Aug 20 2025
Sat Jan 04 2025| Sun Apr 20 2025
Sun Jul 06 2025| Fri Jan 03 2025
Thu Oct 03 2024| Thu Jan 09 2025

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev12345Next

  25. Basic example for Timeline[Timeline](?path=%2FTimeline)

Lane 1

Lane 2

Lane 3

Lane 4

Lane 5

Lane 6

Lane 7

---

# Utility Libraries {#utilities}

*Utility libraries for common functionality like time handling, formatting, etc.*

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `splunk-utils`

# @splunk/create

## What is @splunk/create?

`@splunk/create` generates code and scaffolding for a new Splunk application,
built with React, via CLI.

By using `@splunk/create`, you can quickly start developing with Splunk
provided packages such as [@splunk/react-ui](../react-ui/),
[@splunk/dashboard-core](../dashboard-docs/), and
[@splunk/visualizations](../visualizations/).

What will you create? Check out our [Examples
Gallery](../../toolkits/suit/examplesgallery) for inspiration.

### Requirements

  * Yarn >= 1.2
  * Node >= 22

## Prerequisites

To run your Splunk app locally you will need a local Splunk Enterprise
instance with `$SPLUNK_HOME` set.

For more information on getting a local instance, see the [Splunk Enterprise
downloads page](https://www.splunk.com/en_us/download/splunk-enterprise.html).

### Setting up $SPLUNK_HOME



    # Set SPLUNK_HOME to point to the top-level installation directory
    $ export SPLUNK_HOME=/opt/splunk

    # Add $SPLUNK_HOME/bin to the shell’s path.
    $ export PATH=$SPLUNK_HOME/bin:$PATH

## Getting started

To generate files for a Splunk app, run `npx @splunk/create` from an empty
project folder.



    $ mkdir project-folder
    $ cd project-folder
    $ npx @splunk/create
    #? What do you want to name your Splunk app?: MySplunkApp
    #? What do you want to name your new page?: MyPage
    #? What type of page would you like to create?: Add a Basic Page

Next, install project dependencies:



    $ yarn setup

You’ll now have two main directories, one for the created React page and one
for the created Splunk app.

  * packages/my-page
  * packages/my-splunk-app

### Splunk demo

Splunk demo will allow you to view your new app inside your local Splunk
instance:



    # navigate to your app folder
    $ cd packages/my-splunk-app

    # link the app to your local Splunk instance
    $ yarn link:app

    # check that the link is set (optional)
    $ ls -l $SPLUNK_HOME/etc/apps/my-splunk-app

    # restart Splunk (will start Splunk if not already started)
    $ splunk restart

    # navigate to the root project directory
    $ cd ../../

    # start the Splunk app
    $ yarn start

This will watch both your my-splunk-app and my-page folders for changes and
rebundle.

You should now see your app in the left hand menu of the Splunk Enterprise
home page, typically located at <https://localhost:8000>.

There is no hot-reloading within Splunk, you'll need to manually refresh the
page to see changes.

If you are not seeing your changes you can try:

  * hard reloading Shift+Command+R (Ctrl+Shift+R on Windows) in Google Chrome
  * [disabling Splunk asset cache](https://dev.splunk.com/enterprise/docs/developapps/manageknowledge/assetcaching/) (not recommended for production environments)
  * using <https://localhost:8000/en-US/_bump>

### Local React demo

Sometimes developing within Splunk is not the most efficient, which is why we
also provide a local development environment specifically for your React page.



    # navigate to the page directory
    $ cd packages/my-page

    # start the local development demo
    $ yarn run start:demo

Go to <http://localhost:8080/> to see your new React page in action.

Page files are located in packages/my-page/src. Make a change to a file to see
it update in the demo.

## What’s next

  * Check out our tutorials -> [Tutorial: Creating a todo list](/Packages/create//TodoList)
  * Learn about the dev tools available in your new project -> [Dev Tools](/Packages/create//DevTools)
  * Learn more about how your Splunk app is set up -> [Generated Splunk app code](/Packages/create//GeneratedCode)
  * Learn how to package your Splunk app -> [Packaging a @splunk/create app](/Packages/create//PackagingYourApp)
  * Check out examples for inspiration -> [Examples Gallery](../../toolkits/suit/examplesgallery)

---

## @splunk/time-range-utils - 3.0.1

**Package:** `time-range-utils` | **Component:** `Changelog`

# Changelog

## 3.0.1 (2022-11-17)

### Bug Fixes

  * Updated `presets.js` to filter presets with `disabled: true` (SUI-5129)

## 3.0.0 (2021-09-15)

### Bug Fixes

  * Updated dependency on `@splunk/react-ui` to fix a11y issues (SUI-2608)

### BREAKING CHANGES

  * Relicensed package to Apache-2.0

## [2.6.1] (2021-05-21)

### Changed

  * Redeploy the fix for `getISOWithTimeZone` to accept a timezone (PX-1363)

## [2.6.0] (2021-04-01)

### Changed

  * Update `getISOWithTimeZone` to accept a timezone (PX-1363)
  * Fixed `createRangeLabel` crashes when using unsupported locales (PX-1422)

## [2.5.0] (2021-02-18)

### Changed

  * Updated @splunk/moment to 0.6.0 (PX-918)

## [2.4.1] - 2021-02-17

### Fixed

  * Fixed `createRangeLabel` to output correct labels for date ranges spanning exactly a month or year (PX-1118)

## [2.4.0] - 2020-01-15

### Fixed

  * Released version with `getISOWithTimeZone` needed by `@splunk/react-time-range` (SCP-35898)

## [2.3.0] - 2020-07-24

### Changed

  * Updated date and time range labels to use en dash instead of "through" or "to" (PX-74)

## [2.2.0] - 2020-06-12

### Fixed

  * Fixed `createRangeLabel()` returning labels for date ranges spanning more than a month or year (SCP-27855)

## [2.1.0] - 2020-05-21

### Added

  * Added date and time conversion utils for RealTime and Relative times.

## [2.0.0] - 2020-03-24

### Added

  * Added type definitions for Typescript consumers (SCP-22772).

### Fixed

  * Fixing the string templates of relative time range section which was breaking the localization (APPLAT-2769).

## [1.2.0] - 2018-09-17

### Changed

  * Relicensed to `Splunk Software License Agreement`.

### Fixed

  * `createRelativeTimeLabel()` and `createRealTimeLabel()` now use sprintf to prevent localization issue (APPLAT-2269).

## [1.1.2] - 2018-06-26

### Fixed

  * `createRangeLabel()` now returns correct labels for through date ranges that end on the last day of a month (SUI-1480).
  * `createRangeLabel()` now returns correct labels for complex through date ranges (SUI-1482).

## [1.1.1] - 2018-05-24

### Added

  * `isWholeDay()` now accepts a moment instance.

### Fixed

  * `createRangeLabel()` now returns full labels for some ranges where times match but dates differ (SUI-1460).

## [1.1.0] - May 3, 2018-05-03

### Added

  * Added function: `formatDuration` (APPLAT-626)

## [1.0.2] - 2018-04-25

### Fixed

  * `@w7` is now supported (SUI-1453).
  * `parseTimeString` correctly parses `@w`.

## [1.0.1] - 2018-01-24

### Fixed

  * `isISO()` correctly returns false for years before 0000 or after 9999.

## [1.0.0] - 2018-01-04

### Changed

  * Version bump.

## [0.5.0] - 2017-11-20

### Added

  * `getUnitLabel()` converts a unit abbreviation, such as 's' or 'sec', into an unabbreviated form, such as 'second' or 'seconds'.

### Changed

  * `fetchISO()` renamed to `getISO()` and is no longer the default export from `timeParser`.
  * `fetchPresets()` renamed to `getPresets()` and is no longer the default export from `presets`.
  * `generateLabel()` renamed to `createRangeLabel()`.

## [0.4.0] - 2017-09-25

### Added

  * Time range AST util (SUI-980)

### Changed

  * `isValid` now returns `false` instead of `undefined`.

## [0.3.1] - 2017-09-01

### Fixed

  * `removeRealTime()` returns `'now'` instead of empty string to ensure correct processing by the time parser (SUI-1067).

## [0.3.0[] - 2017-07-24

### Changed

  * Improved support for multi-segment time strings (SUI-846).

## [0.2.0] - 2017-05-25

### Added

  * Initial release.

---

## @splunk/time-range-utils - 3.0.1

**Package:** `time-range-utils` | **Component:** `Presets`

# Presets Utils

Depends on splunkweb

This utility currently only has one function for fetching presets.



     import { getPresets } from '@splunk/time-range-utils/presets'


## getPresets

Fetches presets from splunkd with a browser fetch. When the promise is
resolved, an array of presets is returned in the format compatible with
@splunk/react-time-range components and sorted primarly by order and then
alphabetically.



     [
       { label: '30 second window', earliest: 'rt-30s', latest: 'rt' },
       { label: '1 hour window', earliest: 'rt-1h', latest: 'rt' },
       { label: 'All time (real-time)', earliest: 'rt', latest: 'rt' },
       { label: 'Today', earliest: '@d', latest: 'now' },
       { label: 'Year to date', earliest: '@y', latest: 'now' },
       { label: 'Previous year', earliest: '-1y@y', latest: '@y' },
       { label: 'All time', earliest: '0', latest: '' },
     ]


Example usage:



    getPresets()
        .then(data => {
            this.setState({
                presets: data,
            });
        })
        .catch(error => {
            console.log('Time presets could not be loaded from splunkweb.', error);
        });


Returns
**[promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)**

---

## @splunk/time-range-utils - 3.0.1

**Package:** `time-range-utils` | **Component:** `Time`

# Time Utils

Utilities for interpreting, parsing, and validating time ranges. Each function
can be imported separately.



     import { normalizeUnit, createRangeLabel } from '@splunk/time-range-utils/time'


## normalizeUnit

Normalizes units to it's shortest version, such as `s` for `sec` and `mon` for
`month`.

### Parameters

  * `unit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The unit, such as `s` or `quarter`.
  * `removeInvalid` **bool** When true, returns an empty string for invalid units, when false returns 's' for invalid units. (optional, default `true`)

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
Returns the normalized unit or empty string.

## normalizeSnapUnit

Normalizes snap units to it's shortest version, this is the same as
normalizeUnit, but also supports weekdays, such as `w5`.

### Parameters

  * `abbr`
  * `removeInvalid` **bool** When true, returns an empty string for invalid units, when false returns 's' for invalid units. (optional, default `true`)
  * `unit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The unit, such as `s`, `quarter` or `w0`.

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
Returns the normalized unit or empty string.

## getUnitLabel

Returns a label for a unit abbreviation, such as 'second' for 's' or 'sec'.

### Parameters

  * `unit` **[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)** The unit, such as `s`, `quarter` or `w0`.
  * `plural` **[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)** Whether the returned label should be plural. (optional, default `false`)

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## removeRealTime

Strips rt from the beginning of a time string when found. This makes a time
string compatible with the time parser. To ensure capability with the time
parser 'rt' returns 'now'.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `rt-2h@m`.

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
Returns the time string.

## removeISOTimezone

Removes the timezone from an iso time string

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## isEpoch

Validates that a string represents a unix epoch time.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns **bool**

## isISO

Validates that a string represents an ISO time.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns **bool**

## isAbsolute

Validates that a string represents an ISO or unix epoch time.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns **bool**

## getISOWithTimeZone

Adds timezone to ISO time.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as “2020-09-17T09:44:12.404”.
  * `momentTimeZoneName` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)?**

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
ISO with timezone “2020-09-17T16:44:12.404Z”

## parseTimeString

Parses a time string for inspection or form population.

Example parse for a relative time string:



    {
        string: '-3d@qtr+2hr',
        type: ['relative'], // 'relative', 'realTime', 'iso', or 'epoch'
        isFullyParsed: true,
        modifiers: [
            {
                string: '-3d@qtr',
                isParsed: true,
                unit: 'd',
                amount: -3,
                snap: 'q',
            },
            {
                string: '+2hr',
                isParsed: true,
                unit: 'h',
                amount: +2,
                snap: false,
            },
        ],
    }


Example parse for a epoch time:



    {
        string: '89451357',
        type: ['epoch'],
        isFullyParsed: true,
        modifiers: [],
    }


### Parameters

  * `timeString`
  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns
**[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)**

## isValidTime

Validates that a string is a valid time string.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **bool**

## isRealTime

Validates that a string represents a real-time search.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **bool**

## isWholeDay

Validates that a iso time string is a whole day.

### Parameters

  * `time` **([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | [object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))** A time string (such as `2008-09-15T15:53:00+05:00`) or a

Returns **bool**

## isEarliestEmpty

Validate that a time string acts is either empty or `0`.

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **bool**

## isLatestNow

Validate that a time string acts is either empty or now

### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **bool**

## isAllTime

Validate that a time range acts is equivalent to all-time.

### Parameters

  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.
  * `latest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **bool**

## timeRangesAreEquivalent

Validate that two time range are equivalent. This normalizes the two
comparisons using isEarliestEmpty() and isLatestNow().

### Parameters

  * `range1` **[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)** The time string range such as `{ earliest: '-1d', latest: 'now' }`.
  * `range2` **[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)** The time string range such as `{ earliest: '0', latest: '-1d' }`.

Returns **bool**

## findPresetLabel

Searches through an array of presets and returns any equivalent labels using
timeRangesAreEquivalent().

### Parameters

  * `presets` **[array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)** An array of presents such as: [ { label: '30 second window', earliest: 'rt-30s', latest: 'rt' }, { label: 'Today', earliest: '@d', latest: 'now' }, { label: 'Previous year', earliest: '-1y@y', latest: '@y' }, { label: 'Last 15 minutes', earliest: '-15m', latest: 'now' }, { label: 'All time', earliest: '0', latest: '' }, ]
  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.
  * `latest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.

Returns **([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | `false`)** The matched preset label.

## createRangeLabel

Creates an appropriate label for a time range, using a preset label if
available.

### Parameters

  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.
  * `latest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `rt` , `rtnow` or `-2h@m`.
  * `options` **[object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?** An array of presents such as: (optional, default `{}`)
    * `options.presets` **[array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)?** An array of presents such as: [ { label: '30 second window', earliest: 'rt-30s', latest: 'rt' }, { label: 'Today', earliest: '@d', latest: 'now' }, { label: 'Previous year', earliest: '-1y@y', latest: '@y' }, { label: 'Last 15 minutes', earliest: '-15m', latest: 'now' }, { label: 'All time', earliest: '0', latest: '' }, ]
    * `options.maxChars` **[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)?** If the generated label is too long, it will abbreviate to a more generic form, such as 'Between Date-times' instead of 'Feb 17, 2017 6:00 AM to Feb 18, 2017 12:20 AM'. `Infinity` and `0` allow labels of any length.
    * `options.locale` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** An array of presents such as: (optional, default `'en_US'`)

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
Returns `'Custom time'` if one cannot be made.

## formatDuration

Takes a duration in milliseconds and returns a string describing the duration
in terms of years, months, days, hours, minutes, seconds and milliseconds. If
a unit isn't needed it's omitted, e.g. durations less than a year won't
include '0 years'.

### Parameters

  * `ms` **([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | [number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))** The duration in milliseconds.

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
A formatted duration string, for example `27 days 16 hours 36 minutes 59
seconds`. Durations <= 0 return `null`.

## getFromNumber

Gets the number of units from the earliest string

### Parameters

  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

Returns
**[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)**

## getFromSnap

Returns true if the earliest string contains a snap unit

### Parameters

  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

Returns
**[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)**

## getFromUnit

Returns the time unit of the earliest string Defaults to seconds

### Parameters

  * `earliest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## getToSnap

Returns if the latest string has a snap unit

### Parameters

  * `latest` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## getRelativeEarliest

Returns the earliest time string in relative format

### Parameters

  * `fromNumber` **[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)**
  * `fromSnap` **[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)**
  * `fromUnit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## getRelativeLatest

Returns the latest time string in relative format

### Parameters

  * `fromUnit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
  * `toSnap` **[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)**

## getRealTimeEarliest

Returns the earliest time string in real time format

### Parameters

  * `fromNumber` **[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)**
  * `fromUnit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

Returns
**[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**

## getAcceleratedTimeRange

Returns the earliest and latest time range based on duration

### Parameters

  * `time`
  * `duration` **[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)**
  * `unit` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)**
  * `string` **time** (ISO format)

---

## @splunk/time-range-utils - 3.0.1

**Package:** `time-range-utils` | **Component:** `TimeParser`

# Time Parser Utils

Depends on splunkweb

This utility currently only has one function for parsing a time string on the
server.



     import { getISO } from '@splunk/time-range-utils/timeParser'


## getISO

Fetches the parsed time from splunkd with a browser fetch. When the promise is
resolved, a data object is returned with up to three properties:

  * time (the original time provided for for validation and identification purposes)
  * iso (the parsed time value)
  * error.

Example usage:



    getISO('-2d@h')
        .then(data => {
            this.setState({
                parseLatest: {error: data.error, iso: data.iso, time: data.time, },
            });
        })
        .catch(data => {
            this.setState({
                parseLatest: {error: data.error, iso: '', time: data.time, },
            });
        });


### Parameters

  * `time` **[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)** The time string such as `47165491` or `-2h@m`.

Returns
**[promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)**

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `ChangeLog`

# Change Log

## 1.10.0 - July 2, 2025

New Features:

  * Added `scrollIntoViewIfNeeded` method that scrolls an element’s offset parent to bring the element into view when it’s outside the visible area.

## 1.9.0 - June 3, 2025

API Changes:

  * Deprecate `keyboard`'s `keycode` function and use of `event.keyCode` (SUI-7352).

## 1.8.0 - February 14, 2025

New Features:

  * Added new functions `hexToRgb` and `isValidRgb`.

## 1.7.1 - August 26, 2024

Bug Fixes:

  * `getSortedTabbableElements` now works correctly in `jsdom` environments (SUI-6521).
  * `keycode` now correctly captures the key from `userEvent` in `testing-library` (SUI-6521).

## 1.7.0 - August 7, 2024

New Features:

  * Added `handleFocus` method which manages the focus for a group of elements (SUI-6268).

## 1.6.0 - May 2, 2023

New Features:

  * Added `options.ignoreTabIndex` to `getSortedTabbableElements`.

## 1.5.2 - December 6, 2022

Bug Fixes:

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 1.5.1 - October 5, 2022

Bug Fixes:

  * Upgraded lodash to non-vulnerable version 14.17.21 (SUI-3289).

## 1.5.0 - June 29, 2022

Notes:

  * `normalizeBoolean` has been deprecated in `ui-utils`. Use the new version introduced in `splunk-utils` instead.

## 1.4.0 - September 8, 2021

New Features:

  * New `isTabKey` focus utility.

## 1.3.0 - March 31, 2021

New Features:

  * `expandShortHandHex` converts three/four-digit hex colors to six/eight-digit hex colors.
  * `isValidHexColor` can be used to determine if the given string value is a 3, 4, 6, or 8-digit hex-color.
  * `isCSSColor` can be used to determine if the given value is considered of type `<color>` in CSS.
  * `extendedColorKeywords` is an array of the extended color keywords in CSS.

## 1.2.1 - February 4, 2021

Bug Fixes:

  * `getSortedTabbableElements` now treats radio groups as a single tab stop.

## 1.2.0 - August 31, 2020

New Features:

  * `isNumber` and `isDecimal` in the keyboard utils now support `locale` to define the decimal separator.

## 1.1.2 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 1.1.1 - June 11, 2019

Bug Fixes:

  * `handleTab` in `focus` now handles hidden elements better (SUI-1759).

## 1.1.0 - September 13, 2018

Bug Fixes:

  * `i18n` no longer throws an exception if `window` isn't available.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

## 1.0.1 - April 23, 2018

Bug Fixes:

  * `cookie` does not throw an exception in a sandboxed environment (SUI-1422).

## 1.0.0 - January 4, 2018

  * Version bump.

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Color`

# Color

A set of functions for Color.

### expandShortHandHex(value)

Converts shorthand hex color value to the equivalent six-digit hexadecimal
value.

value

Three-digit or four-digit shorthand hexadecimal value to be converted.

Type| string, null, undefined
---|---
Required| Yes

returns

value - If valid three or four-digit shorthand hexadecimal value, returns
converted six-digit or eight-digit code; original value otherwise.

Type| string, null, undefined
---|---

### isValidHexColor(value)

Returns true when `value` is a valid `<hex-color>`. `<hex-color>`s are strings
that can be 3, 4, 6, or 8 digits and must start with `#`.

value

Type| string
---|---
Required| Yes

returns

Type| boolean
---|---

### hexToRgb(hex)

Converts hex color to an array of rgb values.

hex

The 6 digit hex color. This doesn't accept hex colors of other digit lengths.

Type| string
---|---
Required| Yes

returns

Type| Array.<number>, null
---|---

### extendedColorKeywords

`Array` containing `string`s of the [named colors(Opens new
window)](https://www.w3.org/TR/css-color-4/#named-colors) from [CSS Color
Module 4(Opens new window)](https://www.w3.org/TR/css-color-4).

### isCSSColor(value)

Validates if the given string is a [<color> type(Opens new
window)](https://www.w3.org/TR/css-color-4/#color-type) in CSS.

Supports:

  * `<hex-color>`s 3, 4, 6 and 8 digit
  * `<named-color>`<https://www.w3.org/TR/css-color-4/#named-colors>[(Opens new window)](https://www.w3.org/TR/css-color-4/#named-colors)
  * `'currentColor'`
  * `'transparent'`

Does not support:

  * the color-functions: `<rgb()>`, `<rgba()>`, `<hsl()>`, `<hsla()>`, `<hwb()>`, `<lab()>`, `<lch()>`, and `<color()>`.
  * `<device-cmyk()>`
  * `<system-color>`

value

Type| string
---|---
Required| Yes

returns

Type| boolean
---|---

### isValidRgb(value)

Returns true when `value` is a valid `<rgb>`. `<rgb>`s are strings that have 3
comma separated numbers. This is not for validating `<rgba>`s. `<rgba>`s are
strings that have 4 comma separated numbers.

value

Type| string
---|---
Required| Yes

returns

Type| boolean
---|---

### extendedColorKeywordsToHex

`Object` containing `string`s of the [named colors(Opens new
window)](https://www.w3.org/TR/css-color-4/#named-colors) and their hex colors
from [CSS Color Module 4(Opens new window)](https://www.w3.org/TR/css-
color-4).

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Filter`

# Filter

A set of functions for filtering items, often menu items. For simple use
cases, use `filterByKeywords`. Use `stringToKeywords` and `testPhrase` when
more control of the filtering is necessary.

### stringToKeywords(filterPhrase)

Converts a string (filterPhrase) to an array of keyword tokens. Tokens are
usually words, but can be a multi-word phrase if quotes are used. The output
is suitable for the `testPhrase` function.

filterPhrase

The phrase to be broken into keywork tokens.

Type| String
---|---
Required| Yes

returns

Type| Array.<String>
---|---

### testPhrase(phrase, keywords)

Tests if a phrase matches a list of keywords. All keywords must be included in
the phrase for a match.

Examples:



    stringToKeywords('Named Bob'); // ['Named', 'Bob']
    stringToKeywords('"Named Bob"'); // ['Named Bob']
    stringToKeywords('A Street Cat "Named Bob"'); // ['A', 'Street', 'Cat', 'Named Bob']

phrase

The test phrase.

Type| String
---|---
Required| Yes

keywords

An array of keywords, as returned by `stringToKeywords`.

Type| Array.<String>
---|---
Required| Yes

returns

Type| Boolean
---|---

### keywordLocations(phrase, keywords)

Looks for keyword locations in a phrase and return portions of the string that
match one or more keywords. The return value can be used to highlight the
matched text.

phrase

The test phrase.

Type| String
---|---
Required| Yes

keywords

An array of keywords, as returned by `stringToKeywords`.

Type| Array.<String>
---|---
Required| Yes

returns

An array of location with start index and end index. Keyword ranges can
overlap. Example:



    [
        {
            start: 0,
            end: 8,
        },
        {
            start: 12,
            end: 17,
        },
    ]

Type| Array.<Object>, false
---|---

### filterByKeywords(items, filterPhrase, [valueGetter])

Filters an array of `items` against the `filterPhrase`.

items

An array of strings or objects to filter.

Type| Array
---|---
Required| Yes

filterPhrase

Type| String
---|---
Required| Yes

valueGetter

An optional function that returns the property of interest if filtering an
array of objects.

Type| function
---|---
Required| No

returns

A filtered list of items.

Type| Array
---|---

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Format`

# Format

Number and String format utilities.

### sprintf(fmt, values)

Returns a formatted string.



    const text = sprintf('%1$s %2$s a %3$s', 'Polly', 'wants', 'cracker') // 'Polly wants a cracker'

#### Format Specification

The placeholders in the format string are marked by `%` and are followed by
one or more of these elements, in this order:

  * An optional number followed by a `$` sign that selects which argument index to use for the value. If not specified, arguments are placed in the same order as the placeholders in the input string.
  * An optional `+` sign that forces to preceed the result with a plus or minus sign on numeric values. By default, only the `-` sign is used on negative numbers.
  * An optional padding specifier that says what character to use for padding, if specified. Possible values are `0` or any other character preceded by a (`'`) (single quote). The default is to pad with _spaces_.
  * An optional `-` sign that causes `sprintf` to left-align the result of this placeholder. The default is to right-align the result.
  * An optional number that says how many characters the result has. If the value to be returned is shorter than this number, the result is padded. When used with the `j` (JSON) type specifier, the padding length specifies the tab size used for indentation.
  * An optional precision modifier, consisting of a `.` (dot) followed by a number, that says how many digits are displayed for floating point numbers. When used with the `g` type specifier, it specifies the number of significant digits. When used on a string, it causes the result to be truncated.
  * A type specifier that can be any of the following:
    * `%` — yields a literal `%` character
    * `b` — yields an integer as a binary number
    * `c` — yields an integer as the character with that ASCII value
    * `d` or `i` — yields an integer as a signed decimal number
    * `e` — yields a float using scientific notation
    * `u` — yields an integer as an unsigned decimal number
    * `f` — yields a float as is; see notes on precision above
    * `g` — yields a float as is; see notes on precision above
    * `o` — yields an integer as an octal number
    * `s` — yields a string as is
    * `t` — yields `true` or `false`
    * `T` — yields the type of the argument<sup><a href="#fn-1" name="fn-ref-1">1</a></sup>
    * `v` — yields the primitive value of the specified argument
    * `x` — yields an integer as a hexadecimal number (lower-case)
    * `X` — yields an integer as a hexadecimal number (upper-case)
    * `j` — yields a JavaScript object or array as a JSON encoded string

This utility was adapted from [Alexandru's sprintf-js implementation(Opens new
window)](https://github.com/alexei/sprintf.js).

fmt

The string to format and insert values into.

Type| string
---|---
Required| Yes

values

The values to insert into the format string. See specification above.

Type| Any
---|---
Required| Yes

### abbreviateNumber(number, [locale])

Abbreviates a number by rounding to no more than three decimal places and by
appending a suffix: K/M/B. Additionally, the resulting number is formatted
using a given locale.

Examples:

  * `99549` returns `99.5K`
  * `1159000` returns `1.16M`
  * `9500`, `de-de` returns `9,5K`

number

The number to abbreviate.

Type| Number, String
---|---
Required| Yes

locale

Type| String
---|---
Default| 'en-us'
Required| No

returns

The abbreviated and localized number if `number` is positive. The localized
number if negative.

Type| String
---|---

### bytesToFileSize(bytes, [locale])

Abbreviates a number by rounding to no more than two decimal places and by
converting to binary prefixes (B/KB/MB/GB/TB). Additionally, the resulting
number is formatted using a given locale.

Examples:

  * `100` returns `100 B`
  * `1200` returns `1.17 KB`
  * `96619136`, `de-de` returns `92,14 MB`

bytes

The number of bytes to abbreviate.

Type| Number, String
---|---
Required| Yes

locale

Type| String
---|---
Default| 'en-us'
Required| No

throws

If `bytes` is less than zero.

Type| RangeError
---|---

returns

The abbreviated and localized number.

Type| String
---|---

### smartTrim(string, maxCharsFromString, [options])

Trim a String by replacing characters in the middle with an ellipsis.

Examples:

  * `1234567890`, `7` returns `123...7890`
  * `1234567890`, `10` returns `1234567890`
  * `1234567890`, `50` returns `1234567890`
  * `1234567890`, `2`, `{ precomposed: true }` returns `1…0`

string

The input string.

Type| String
---|---
Required| Yes

maxCharsFromString

How many characters to take from `string`.

Type| Number
---|---
Required| Yes

options

  * `precomposed`: Use one ellipsis character (…) instead of three periods. Defaults to `false`.

Type| Object
---|---
Required| No

returns

The trimmed result. Note that the total length might be up to three characters
more than `maxCharsFromString`. If `string` is falsy or if
`maxCharsFromString` is less than 1, `string` is returned.

Type| String
---|---

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Internationalization`

# Internationalization

Internationalization / translation utility. The exported `gettext` (and its
alias `_`) uses a shared translator function that's set to `window.gettext` by
default. If `window.gettext` isn't available, the identify function is used,
turning `gettext` and `_` into no-ops.

Caution is advised when using `setSharedTranslator` and
`resetSharedTranslator`. Always restore the translator after changing it, and
never assume that the translator hasn't been changed by external code during
long-running operations.

If used in combination with Splunk Enterprise, `window.gettext` is provided by
default. Using the `gettext` and `_` syntax ensures that messages can be
extracted, and a catalog file can be generated automatically.

### gettext(text)

Translates text using the shared translator. By default, this is
`window.gettext` if it's available. Otherwise, the identify function is used.

text

The text to translate.

Type| String
---|---
Required| Yes

returns

The translated text.

Type| String
---|---

### _(text)

This is an alias for `gettext`.

text

The text to translate.

Type| String
---|---
Required| Yes

returns

The translated text.

Type| String
---|---

### setSharedTranslator(newTranslator)

Sets the shared translator. It is used by all subsequent calls of `gettext`
and `_`.

newTranslator

A function that returns the translated string.

Type| function
---|---
Required| Yes

### resetSharedTranslator()

Resets the shared translator to `window.gettext` if available, and the
identify function otherwise. This function is invoked automatically during
module load.

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Keyboard`

# Keyboard

Utilities for handling keyboard events.

### keycode(event)

Warning

Deprecated

This function is deprecated and will be removed in a future major version. Use
`KeyboardEvent`'s `key` property for identifying key presses instead.

A utility for mapping key names with their numeric codes. This is an alias for
[the third-party library, keycode(Opens new
window)](https://github.com/timoxley/keycode).

event

A keyboard event.

Type| Event
---|---
Required| Yes

returns

Type| String
---|---

### isNumber(event)

Tests if the event key is a number.

event

Warning

Deprecated

Support for `keyCode` in this function is deprecated and will be removed in a
future major version.

A keyboard event that includes a `key`, a `keyCode`, or both.

Type| Event
---|---
Required| Yes

returns

Type| Boolean
---|---

### isDecimal(event, [options])

Tests if the event key is a decimal.

event

Warning

Deprecated

Support for `keyCode` in this function is deprecated and will be removed in a
future major version.

A keyboard event that includes a `key`, a `keyCode`, or both.

Type| Event
---|---
Required| Yes

options

Type| Object
---|---
Required| No

locale.string

The locale determines the decimal separator. Supported locale formats are:
`xx`, `xx-XX`, and `xx_XX`.

Type| String
---|---
Default| 'en-US'
Required| No

returns

Type| Boolean
---|---

### isMinus(event)

Tests if the event key is a minus sign.

event

Warning

Deprecated

Support for `keyCode` in this function is deprecated and will be removed in a
future major version.

A keyboard event that includes a `key`, a `keyCode`, or both.

Type| Event
---|---
Required| Yes

returns

Type| Boolean
---|---

### isNumeric(event, [options])

Tests if the event key is a numeric character (number, decimal, or minus).

event

Warning

Deprecated

Support for `keyCode` in this function is deprecated and will be removed in a
future major version.

A keyboard event that includes a `key`, a `keyCode`, or both.

Type| Event
---|---
Required| Yes

options

Type| Object
---|---
Required| No

locale.string

The locale determines the decimal separator. Supported locale formats are:
`xx`, `xx-XX`, and `xx_XX`.

Type| String
---|---
Default| 'en-US'
Required| No

returns

Type| Boolean
---|---

### addsCharacter(event)

Tests if the event key adds a character. Enter and Tab return false even
though they add characters in some situations. Caveat: Safari 9.0 and earlier
might return undefined as this cannot be practically determined.

event

A keyboard event that includes a key.

Type| Event
---|---
Required| Yes

returns

Type| Boolean, Undefined
---|---

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Math`

# Math

Math and floating point utilities.

### strictParseFloat(string)

A strict version of `parseFloat` that requires the entire input string to be
valid decimal or scientific format.

string

Type| String
---|---
Required| Yes

returns

Type| Number, NaN
---|---

### roundToDecimal(value, [exp])

Rounds a number to a specific exponent of base 10.

Examples:

  * `value` 125.678 and `exp` -2 rounds to 125.68
  * `value` 125.678 and `exp` -1 rounds to 125.7
  * `value` 125.678 and `exp` 0 rounds to 126
  * `value` 125.678 and `exp` 1 rounds to 130
  * `value` 125.678 and `exp` 2 rounds to 100

value

Type| Number
---|---
Required| Yes

exp

Exponent of base 10 of the decimal place to round to.

Type| Number
---|---
Default| 0
Required| No

returns

The rounded number or NaN if `value` is not a Number or `exp` isn't an
integer.

Type| Number, NaN
---|---

### floorPowerOfTen(number)

Returns the nearest whole power of ten less or equal to the given number.

Examples:

  * 10 returns 10
  * 11 returns 10
  * 99 returns 10
  * 100 returns 100

number

Type| Number
---|---
Required| Yes

returns

The result if `number` is positive, `0` if `number` is `0`, `NaN` if `number`
is negative.

Type| Number, NaN
---|---

### isLessThanMinSafeInt(number)

Determines if the given number is less than the minimum safe integer
(-9007199254740991).

number

Type| Number
---|---
Required| Yes

returns

`true` if the given number is less than the minimum safe integer, `false`
otherwise (or if `number` isn't a Number).

Type| Boolean
---|---

### isGreaterThanMaxSafeInt(number)

Determines if the given number is greater than the maximum safe integer
(9007199254740991).

number

Type| Number
---|---
Required| Yes

returns

`true` if the given number is greater than the maximum safe integer, `false`
otherwise (or if `number` isn't a Number).

Type| Boolean
---|---

---

## @splunk/ui-utils - 1.10.0

**Package:** `ui-utils` | **Component:** `Promise`

# Promise

### makeCancelable

Adds a cancel function on your promise to cancel future execution of then or
catch functions. `makeCancelable` also cancels all callbacks attached to new
promises returned by then or catch.

---

# Build Tools & Configuration {#build-tools}

*Build tools, configurations, and development utilities.*

## @splunk/babel-preset - 4.0.0

**Package:** `babel-preset` | **Component:** `ChangeLog`

# Change Log

## 4.0.0 - July 12, 2023

  * Replaced `@babel/preset-typescript` with `@babel/plugin-transform-typescript`
    * This addresses compatility issues between TypeScript `declare` fields and `@babel/plugin-proposal-class-properties`
    * `typescriptPresetOptions` (introduced in 3.0.0) continutes to function as normal for configuring TypeScript in `babel`

## 3.0.0 - May 1, 2020

  * `@babel/preset-typescript` is now enabled.
  * Supports passing options to the `typescript` preset using `typescriptPresetOptions`.
  * Added options `envPresetEnabled`, `reactPresetEnabled`, and `typescriptPresetEnabled`.

## 2.0.2 - March 15, 2020

  * Added missing peer dependency `@babel/core^7.0.0-0`.

## 2.0.1 - October 14, 2019

  * Relicensed to `Apache-2.0`.

## 2.0.0 - January 2, 2019

  * Babel 7 is supported and required (SUI-1612).
    * Migrating projects should update. For details see https://babeljs.io/docs/en/v7-migration.
  * Now supports passing options to the `env` and `react` presets (using `envPresetOptions` and `reactPresetOptions`).
  * Removed the `webpack` and `targets` options.
    * `webpack` is no longer necessary (requires `babel-loader@>=8`).
    * `targets` should be moved to `envPresetOptions`.

## 1.2.0 - September 13, 2018

  * Relicensed to `Splunk Software License Agreement`.

## 1.1.0 - March 2, 2018

  * Adds support for defining `targets`.

## 1.0.0 - January 4, 2018

  * Version bump.

---

## @splunk/babel-preset - 4.0.0

**Package:** `babel-preset` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/plugin-proposal-class-properties| 7.18.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-plugin-proposal-class-properties)|
<https://github.com/babel/babel.git>
@babel/plugin-proposal-object-rest-spread| 7.19.4| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-plugin-proposal-object-rest-
spread)| <https://github.com/babel/babel.git>
@babel/plugin-transform-typescript| 7.22.5| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-plugin-transform-typescript)|
<https://github.com/babel/babel.git>
@babel/preset-env| 7.19.4| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-preset-env)|
<https://github.com/babel/babel.git>
@babel/preset-react| 7.18.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-preset-react)|
<https://github.com/babel/babel.git>

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/cli| 7.10.1| MIT| [Sebastian McKenzie](https://babeljs.io/)|
<https://github.com/babel/babel.git>
@babel/core| 7.19.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@splunk/cicd-tools| 0.5.0| UNLICENSED| Splunk|
<https://git.splunk.com/scm/ui/workflow-components.git>
@splunk/eslint-config| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
babel-eslint| 10.1.0| MIT| [Sebastian
McKenzie](https://github.com/babel/babel-eslint)|
<https://github.com/babel/babel-eslint.git>
eslint| 7.14.0| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 18.2.1| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 6.15.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-plugin-import| 2.22.1| MIT| [Ben
Mosher](https://github.com/benmosher/eslint-plugin-import)|
<https://github.com/benmosher/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.4.1| MIT| Ethan Cohen|
<https://github.com/evcohen/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.21.5| MIT| [Yannick
Croissant](https://github.com/yannickcr/eslint-plugin-react)|
<https://github.com/yannickcr/eslint-plugin-react>
eslint-plugin-react-hooks| 4.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
webpack| 4.46.0| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 4.9.2| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 4.7.4| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server.git>
webpack-merge| 4.2.2| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `ChangeLog`

# Change Log

## 10.0.1 - September 4, 2025

Bug Fixes:

  * Resolved an issue where `yarn start` at the root of the generated monorepo would not write file changes to disk (SUI-8206).

## 10.0.0 - September 2, 2025

New Features:

  * Generated output code now uses Typescript `^5.8.3` (SUI-7550).
  * Generated output code now supports imports of packages using `css` files (SUI-8035).
  * Generated output code now uses prettier `^3.6.2` (SUI-7894).
  * Generated output code now uses eslint `^8.57.1` (SUI-7894).
  * Create now generates a new component when adding a page to an existing app (SUI-7999).
  * Name input validation is now more informative (SUI-7970).
  * Add Dashboard Page template (SUI-8083).

API Changes:

  * Removed Storybook as a template (SUI-8000).
  * Removed prompt options (SUI-8000):
    * A monorepo with a React component
    * Add a React component
    * Add a React Splunk app with a React component
    * Add a React Splunk app with an existing React component
  * Simplified prompt flow to (SUI-8000):
    * default to new Splunk app in empty folder
    * default to new page in existing create monorepo
  * Replaced Lerna with Yarn Workspaces for monorepo management (SUI-7951).
  * Node 22+ is now required (SUI-7990).

## 9.0.1 - August 5, 2025

API Changes:

  * Updated `fast-xml-parser` dependency.

## 9.0.0 - July 2, 2025

API Changes:

  * Removed `yeoman` dependency (SUI-7798).

## 8.0.0 - June 3, 2025

  * Includes all changes from `8.0.0-beta` and `8.0.0-rc` releases.

## 8.0.0-rc.2 - May 28, 2025

  * Release candidate 2.

## 8.0.0-rc.1 - May 14, 2025

  * Release candidate 1.

## 8.0.0-beta.2 - March 5, 2025

  * Public release of `8.0.0-beta.1`.

## 7.0.3 - March 4, 2025

Bug Fixes:

  * `splunk_create.spec.conf` is now correctly named `splunk_create.conf.spec` (SUI-5385).

## 8.0.0-beta.1 - February 20, 2025

  * `ReactComponent` template updated to remove usage of deprecated `backgroundColor` token (SUI-6656).

API Changes:

  * Generated packages now use `react@^18`.
  * `react` peer dependency of generated packages is now `"^16.8.0 || ^17.0.0 || ^18.0.0"`.

## 7.0.2 - May 14, 2024

Bug Fixes:

  * Fixed `yarn start:demo` not starting due to an invalid port on Windows (SUI-6224).

## 7.0.1 - April 2, 2024

Bug Fixes:

  * Fixed failing unit test for generated component (SUI-5811).
  * Fixed builds in Webpack 5 by adding missing dependency to `@splunk/splunk-utils` (SUI-6065).

## 7.0.0 - February 6, 2024

API Changes:

  * Generated packages now use `@splunk/splunk-utils@3.0.0` (SUI-5957).

## 6.4.1 - June 6, 2023

API Changes:

  * Added support for the latest `styled-components@5` (SUI-5467).

## 6.4.0 - January 25, 2023

  * Fixed a bug in the Splunk App template generator where `@splunk/react-page` wasn't receiving the proper theme (SUI-5302).
  * App.conf now specifies apps support both `light` and `dark` themes by default.
  * `@splunk/create` now generates a functional component (SUI-5267).

## 6.3.5 - December 6, 2022

  * Fix incorrect dependency on `@splunk/react-page` (SUI-5261).

## 6.3.4 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 6.3.3 - November 1, 2022

  * Fixed an issue where scripts would not run in a newly created component (SUI-5118).

## 6.3.2 - September 20, 2022

  * Fixed an issue with theming that caused generated apps to fail to load (SUI-5062).

## 6.3.1 - September 6, 2022

  * Fixed an issue where only the default app name would build (SUI-4277).
  * Fixed an incorrect version for `@splunk/react-ui` (SUI-4300).
  * Fixed missing `fast-xml-parser` dependency (SUI-4304).
  * Fixed an issue where pages could be created outside of splunk apps (SUI-3754).

## 6.3.0 - August 2, 2022

New Features:

  * Added cross platform compatibility for built application and component scripts.

## 6.2.0 - June 7, 2020

API Changes:

  * Added the ability to create a new React page in an existing Splunk app.

## 6.1.2 - April 5, 2022

API Changes:

  * Pinned `styled-components@5.1.1` to avoid breaking changes introduced in `styled-components@5.2.0`.

**`@splunk/create` is incompatible with styled-components version(s)
`^5.2.0`**.

`styled-components@5.2.0` changed how selectors like `& + &` are compiled;
[styled-components PR#3236](https://github.com/styled-components/styled-
components/pull/3236). This breaks styles that worked in previous versions of
styled-components; [styled-components issue #3265](https://github.com/styled-
components/styled-components/issues/3265).

**Until noted otherwise in a future release of`@splunk/create` do not use
`styled-components@^5.2.0` with` @splunk/create`**.

## 6.1.1 - February 23, 2022

  * Updated `yeoman-generator` to 4.4.0.

## 6.1.0 - October 4, 2021

New Features:

  * Splunk Apps created with `@splunk/create` now have a custom config file for recording internal metadata. This file should not be edited.

## 6.0.2 - September 8, 2021

  * Updated dependencies.
  * Hardcode mako template app path rather than using cherrypy path info (SPL-208341/CINC-37999).

## 6.0.1 - February 5, 2021

  * Correct dependencies versions in template for `@splunk/react-ui` and `@splunk/themes`.

## 6.0.0 - February 4, 2021

  * Theming in generated packages updated and now requires `@splunk/themes@^0.7`.

## 5.1.0 - August 31, 2020

  * Generated packages now use `eslint@^7` and updated linting packages.

## 5.0.0 - July 7, 2020

  * Generated packages now use `styled-components@^5`.
  * Generated packages now use `react@^16.8`.
  * Generated packages now use `@splunk/stylelint-config` 4.x.
  * `@splunk/react-ui` is no longer a peer dependency of generated component packages.

## 4.6.0 - May 1, 2020

  * Updated `@splunk/babel-preset`, `@splunk/eslint-config`, `@splunk/themes`, `@splunk/webpack-configs` in generated packages.

## 4.5.0 - March 15, 2020

  * Generated component and app packages now use `@splunk/stylelint-config` 4.x.
  * Generated app packages now use `@splunk/react-page` 3.x.

## 4.4.1 - October 14, 2019

  * Updated dependencies.
  * Relicensed to `Apache-2.0`.

## 4.4.0 - October 8, 2019

  * Updated dependencies.

## 4.3.0 - August 8, 2019

  * Generated component and app packages now use `@splunk/webpack-configs` 4.x.

## 4.2.0 - April 25, 2019

  * Generated packages now use `jest` for unit testing.

## 4.1.0 - February 22, 2019

  * Generated packages now use `styled-components@^4`.

## 4.0.0 - January 2, 2019

  * Generated packages now use Babel 7 and updated versions of `@splunk/babel-preset`, `@splunk/webpack-configs` (SUI-1612).

## 3.0.0 - September 13, 2018

  * Generated component and app packages now use `@splunk/react-ui` 2.x.
  * Generated component and app packages now use `styled-components`.
  * Relicensed to `Splunk Software License Agreement`.

## 2.1.2 - June 7, 2018

  * Generated component and app packages no longer include individual prettier-related tasks.

## 2.1.1 - May 24, 2018

  * Generated Splunk apps no longer fail intermittently on Safari (SUI-1472).

## 2.1.0 - April 23, 2018

  * Added Storybook as a template (APPLAT-759).

## 2.0.0 - March 2, 2018

  * Generated packages no longer include files inherited from the monorepo (SUI-1340).
  * Generated packages now include generic .npmignore files.
  * Generated packages now include CI tasks.
  * Removed non-monorepo generator options.
  * Updated dependencies.

## 1.0.0 - January 4, 2018

  * New visual design.

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `DevTools`

# Dev Tools

## Add another page

Use `@splunk/create` to add a page to your Splunk app:



    # navigate to project root
    $ cd /my-project

    # run @splunk/create
    $ npx @splunk/create

    # follow prompts
    #? What do you want to name your new page?: MySecondPage
    #? What type of page would you like to create?: Add a Basic Page

    # install the new pages package dependencies
    $ yarn setup

    # restart Splunk to see new page in Splunk instance
    $ splunk restart

    # start Splunk demo
    $ yarn start

## Code style

Your project has been bootstrapped with code style enforcement using
[prettier](https://github.com/prettier/prettier).



    # navigate to project root
    $ cd my-project

    # fix without confirming
    $ yarn run format

    # confirm before overwriting files
    $ yarn run format:verify

## Linting

Your project has been bootstrapped with linting using `eslint` and
`stylelint`.



    # navigate to project root
    $ cd my-project

    # run linter
    $ yarn run lint

## Unit testing for React page

Your React page has been bootstrapped with unit testing using
[Jest](https://jestjs.io/) and [testing-library](https://testing-
library.com/). We created an example test at `tests/my-page.unit.tsx`



    # navigate to the page directory
    $ cd packages/my-page

    # run tests once
    $ yarn run test

    # run tests in watch mode
    $ yarn run test:watch

## Available scripts

Project scripts (run from the project folder root)

React page scripts (run from the page folder: packages/my-page)

Splunk app scripts (run from the Spunk app folder: packages/my-splunk-app)

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `GeneratedCode`

# Generated Code

## Folder and files

### Splunk app

Within my-splunk-app/src/main you will find:

  * **resources/splunk** : Traditional Splunk app files. See [Anatomy of a Splunk app](https://dev.splunk.com/enterprise/docs/developapps/createapps/appanatomy/)
  * **webapp/pages** : Each sub folder is a different page in the app that loads React code

### React page

When creating a page using `@splunk/create`, the following Splunk app files
will be generated:

  * `src/main/resources/splunk/appserver/templates/<page-name>.html`
  * `src/main/resources/splunk/default/data/ui/views/<page-name>.xml`
  * `src/main/webapp/pages/<page-name>/index.jsx`
  * `src/main/webapp/pages/<page-name>/Styles.js`

In addition to these you will also have a React page specific folder in
/packages.

## JavaScript code

The entry point for your Splunk app is located at:

`my-splunk-app/src/main/webapp/pages/MyPage/index.tsx`

This code:

  * Imports the created React page
  * Imports styles from Styles.ts
  * Uses [@splunk/splunk-utils](../splunk-utils/) to detect users theme
  * Uses [@splunk/react-page](../react-page/) to display component in Splunk Enterprise layout

## Splunk XML views

Splunk uses .xml files within the data/ui/views directory to detect viewable
pages. The name of the .xml file corresponds to the URL path on the Splunk
server.

Note: The name of the .xml file needs to match the name of the page folder.
For example: MyPage.xml should have a webapp/pages/MyPage folder.

The .xml file contains a label and reference to an HTML template.



    <?xml version="1.0"?>
    <view template="<app-name>:/templates/MyPage.html" type="html">
        <label>My Page</label>
    </view>

## HTML view templates

The HTML view template contains code that will pull in the current pages
bundled JavaScript.



    <% page_path = "/static/app/my-splunk-app/pages/" + page + ".js" %>
    <script src="${make_url(page_path)}"></script>

## How code is bundled to the stage directory

When you run `yarn run build` from packages/my-splunk-app, it runs the webpack
configuration from packages/my-splunk-app/webpack.config.js to:

  * Treat the files in my-splunk-app/src/main/webapp/pages as entries
  * Output bundled JavaScript to my-splunk-app/stage/appserver/static/pages
  * Copy Splunk resources and put them in the stage folder

The result is a Splunk app that is readable and viewable within Splunk Web,
after the `yarn link:app` command is run.

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@inquirer/prompts| 7.5.3| MIT| [Simon
Boudrias](https://github.com/SBoudrias/Inquirer.js/blob/main/packages/prompts/README.md)|
<https://github.com/SBoudrias/Inquirer.js.git>
fast-xml-parser| 4.5.3| MIT| [Amit Gupta](https://solothought.com)|
<https://github.com/NaturalIntelligence/fast-xml-parser>
fs-extra| 11.3.0| MIT| [JP Richardson](https://github.com/jprichardson/node-
fs-extra)| <https://github.com/jprichardson/node-fs-extra>
glob| 7.2.3| ISC| [Isaac Z. Schlueter](http://blog.izs.me/)|
<git://github.com/isaacs/node-glob.git>
lodash-es| 4.17.21| MIT| [John-David Dalton](https://lodash.com/custom-
builds)| <https://github.com/lodash/lodash.git>
mem-fs| 4.1.2| MIT| Simon Boudrias| <https://github.com/SBoudrias/mem-fs.git>
mem-fs-editor| 11.1.4| MIT| Simon Boudrias| <https://github.com/SBoudrias/mem-
fs-editor.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@splunk/eslint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/react-ui| 5.3.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/stylelint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@vitest/coverage-v8| 3.2.4| MIT| [Anthony Fu](https://github.com/vitest-
dev/vitest/tree/main/packages/coverage-v8#readme)|
<git+https://github.com/vitest-dev/vitest.git>
eslint| 8.57.1| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 18.2.1| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 6.15.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-import-resolver-webpack| 0.13.7| MIT| [Ben
Mosher](https://github.com/import-js/eslint-plugin-
import/tree/HEAD/resolvers/webpack)| <git+https://github.com/import-js/eslint-
plugin-import.git>
eslint-plugin-import| 2.31.0| MIT| [Ben Mosher](https://github.com/import-
js/eslint-plugin-import)| <https://github.com/import-js/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.10.0| MIT| Ethan Cohen| <https://github.com/jsx-
eslint/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.37.1| MIT| [Yannick Croissant](https://github.com/jsx-
eslint/eslint-plugin-react)| <https://github.com/jsx-eslint/eslint-plugin-
react>
eslint-plugin-react-hooks| 4.6.2| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
memfs| 4.17.2| Apache-2.0| [streamich](https://github.com/streamich/memfs)|
<https://github.com/streamich/memfs.git>
request| 2.88.0| Apache-2.0| Mikeal Rogers|
<https://github.com/request/request.git>
stylelint| 15.11.0| MIT| [stylelint](https://stylelint.io/)|
<https://github.com/stylelint/stylelint.git>
tmp| 0.2.3| MIT| [KARASZI István](http://github.com/raszi/node-tmp)|
<https://github.com/raszi/node-tmp.git>
vitest| 3.2.4| MIT| [Anthony Fu](https://github.com/vitest-dev/vitest#readme)|
<git+https://github.com/vitest-dev/vitest.git>
wait-on| 8.0.3| MIT| Jeff Barczewski| <http://github.com/jeffbski/wait-on.git>
webpack| 5.91.0| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 5.1.4| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 5.2.2| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server>
webpack-merge| 5.9.0| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `PackagingYourApp`

# Packaging a @splunk/create app

To package your Splunk app, use the Splunk Enterprise package command `splunk
package app <appname>`



    $ cd $SPLUNK_HOME/bin
    $ splunk package app my-splunk-app

You can also use a built-in OS archive command similar to the one below



    $ cd $SPLUNK_HOME/etc/apps
    $ COPYFILE_DISABLE=true tar -zcvh --exclude='.gitignore' --exclude='.git' --exclude='local/' --exclude='stage/' --exclude='local.meta' --exclude='.DS_Store' -f <filename>.tar.gz <app-name>/

For more information see [Package apps for Splunk Cloud Platform or Splunk
Enterprise](https://dev.splunk.com/enterprise/docs/releaseapps/packageapps/).

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `PageTypes`

# Page types

## Basic Page

Basic Page is the default to get you started with a blank canvas.

## Dashboard Page

A Dashboard Page will get you started with the following packages
preinstalled:

  * @splunk/dashboard-context
  * @splunk/dashboard-core
  * @splunk/dashboard-definition
  * @splunk/dashboard-presets
  * @splunk/visualization-context

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `SplunkData`

# Tutorial: Using Splunk data

## Prerequisites

[Tutorial: Creating a todo list app](/Packages/create//TodoList)

## Use live data

**Scenario:** We have an administrator who regularly does quick audits for
every index. To make their task easier, the to-do app should automatically
populate a to-do list with all indexes.

1\. Add IndexList component

2\. Update the start page


And that's it! The application should now show a list of indexes, and clicking
a list item should toggle the checkmark.

## What is splunkd?

The prefix "splunkd/" is required in Splunk app API calls because
[splunkd](https://docs.splunk.com/Splexicon:Splunkd) is the core Splunk server
process responsible for handling indexing, searching, and management tasks.

It runs administration and management services on port 8089 with SSL/HTTPS
enabled by default and provides the REST interface through which API calls are
routed.

Prefixing API calls with "splunkd/" ensures that these calls are directed to
the correct internal service process that manages the core functionalities of
Splunk.

## What's next

Explore other endpoints, see [REST API Reference
Manual](https://docs.splunk.com/Documentation/Splunk/9.4.2/RESTREF/RESTlist)

---

## @splunk/create - 10.0.1

**Package:** `create` | **Component:** `TodoList`

# Tutorial: Creating a todo list

## Prerequisites

Use the [Getting started](./Overview) guide to scaffold a new project, use
these inputs when the CLI prompts you:



    #? What do you want to name your Splunk app?: MyTodoListApp
    #? What do you want to name your new page?: MyTodoListPage
    #? What type of page would you like to create?: Add a Basic Page

## Turn it into a to-do list

Now that we have everything up and running, let’s create our to-do list.

1\. Update React code in MyTodoListPage.tsx

2\. Update styles in MyTodoListPageStyles.ts


If you visit the demo page in your browser, a working to-do list should show
up, with three individually selectable items.

## What's next

In this tutorial, you generated a Splunk app using `@splunk/create` and
updated it with todo list functionality.

In the [next tutorial](./SplunkData), you'll populate your brand new to-do
list page with data from Splunk Enterprise.

---

## @splunk/dashboard-extension-webpack-plugin - 3.0.1

**Package:** `dashboard-extension-webpack-plugin` | **Component:** `ChangeLog`

# Change Log

## 3.0.1 - October 11, 2023

Bug Fixes:

  * This package should now load correctly in Webpack 4 environments (SUI-5802).

## 3.0.0 - October 4, 2023

API Changes:

  * The `webpack` peer dependency is now `^5` (SUI-5072).

## 2.0.1 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 2.0.0 - September 13, 2018

New Features:

  * Webpack 4 is now supported (SUI-1465).

API Changes:

  * The `webpack` peer dependency is now `^4`.
    * Migrating projects should update. For details see https://webpack.js.org/migrate/4/.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

## 1.0.0 - January 4, 2018

  * Upgrades dependencies.

---

## @splunk/dashboard-extension-webpack-plugin - 3.0.1

**Package:** `dashboard-extension-webpack-plugin` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/cli| 7.10.1| MIT| [Sebastian McKenzie](https://babeljs.io/)|
<https://github.com/babel/babel.git>
@babel/core| 7.19.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@splunk/babel-preset| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/eslint-config| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
babel-eslint| 10.1.0| MIT| [Sebastian
McKenzie](https://github.com/babel/babel-eslint)|
<https://github.com/babel/babel-eslint.git>
eslint| 7.14.0| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 18.2.1| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 6.15.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-plugin-import| 2.22.1| MIT| [Ben
Mosher](https://github.com/benmosher/eslint-plugin-import)|
<https://github.com/benmosher/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.4.1| MIT| Ethan Cohen|
<https://github.com/evcohen/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.21.5| MIT| [Yannick
Croissant](https://github.com/yannickcr/eslint-plugin-react)|
<https://github.com/yannickcr/eslint-plugin-react>
eslint-plugin-react-hooks| 4.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
webpack| 5.88.2| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 5.1.4| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 4.15.1| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server>
webpack-merge| 5.9.0| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

---

## @splunk/eslint-config - 5.0.0

**Package:** `eslint-config` | **Component:** `ChangeLog`

# Change Log

## 5.0.0 - November 8, 2024

  * Updated to work with `eslint@8` and the latest compatible config packages.
  * `babel-parser` is no longer supported and has been replaced with `@babel/eslint-parser`.
  * `prettier/react` is now included in `prettier` and should be removed from any `extends` in configs.
  * The following peer dependencies have changed:
    * `@babel/eslint-parser` has been added
    * `eslint` is now set to `^8`
    * `eslint-plugin-react-hooks` is now set to `^4`
  * `react/no-deprecated` has been set to `warn`.
  * `import/no-extraneous-dependencies` has been set to `error`.
  * The following default rules are now disabled in the base preset:
    * 'arrow-body-style'
    * 'no-restricted-exports'
    * 'import/no-relative-packages'
    * 'react/function-component-definition'

## 4.0.0 - August 31, 2020

  * Updated to work with `eslint` 7 and the latest config packages.
  * Now requires node.js 10.12 or newer.
  * The default rule set has changed.
    * Migrating projects should fix newly detected violations or disable individual rules.
  * The following peer dependencies have changed:
    * `eslint` is now set to `^7`.
    * `eslint-plugin-react-hooks` is now set to `^4`.

## 3.0.0 - May 1, 2020

  * Updated to work with `eslint` 6 and the latest config packages.
  * Now requires node.js 8.10 or newer.
  * The default rule set has changed.
    * Migrating projects should fix newly detected violations or disable individual rules.
  * `eslint-config-airbnb/hooks` is now enabled in the base preset.
  * The following default rules are now disabled in the base preset:
    * `react/static-property-placement`
    * `react/jsx-props-no-spreading`
  * The following default rules are now enabled in the base preset:
    * `no-return-assign`
  * The following peer dependencies have changed:
    * `eslint` is now set to `^6`.
    * `eslint-config-airbnb` is now set to `^18`.
    * `eslint-plugin-react-hooks@^2` was added.

## 2.0.1 - October 14, 2019

  * Relicensed to `Apache-2.0`.

## 2.0.0 - January 29, 2019

  * Updated to work with `eslint` 5 and the latest config packages.
  * The default rule set (`eslint-config-airbnb`) has changed significantly.
    * Migrating projects should fix newly detected violations or disable individual rules.
  * The following default rules are now disabled in the base preset:
    * `react/destructuring-assignment`
    * `react/forbid-foreign-prop-types`
  * The following peer dependencies have changed:
    * `babel-eslint` is now set to `^10`.
    * `eslint` is now set to `^5`.
    * `eslint-config-airbnb` is now set to `^17`.
    * `eslint-plugin-jsx-a11y` is now set to `^6`.
    * `eslint-plugin-react` is now set to `^7`.
    * `eslint-config-prettier` was removed.
      * The package is still required for projects using one of the `-prettier` configurations.

## 1.2.0 - September 13, 2018

  * Relicensed to `Splunk Software License Agreement`.

## 1.1.0 - April 23, 2018

  * `import/prefer-default-export` is now disabled.

## 1.0.0 - January 4, 2018

  * Version bump.

---

## @splunk/stylelint-config - 5.0.0

**Package:** `stylelint-config` | **Component:** `ChangeLog`

# Change Log

## 5.0.0 - August 7, 2024

New Features:

  * Updated to `stylelint@15` (SUI-6161).

API Changes:

  * `stylelint@^15` is now a peer dependency.
  * Now requires `nodejs@14` or newer.
  * Removed `stylelint-processor-styled-components` due to the removal of processors in `stylelint@15`.
    * Now using `postcss-styled-syntax` to support `styled-components`.

## 4.0.0 - March 15, 2020

New Features:

  * Updated to work with the latest stylelint and config packages.

API Changes:

  * `stylelint@^13` is now a peer dependency.
  * Updated the default rule set (`stylelint-config-standard`).
    * Migrating projects should fix newly detected violations or disable individual rules.
  * The default module changed from `postcss` to `styled`.
  * The `postcss` module was removed.
  * Now requires node.js 10 or newer.

## 3.0.1 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 3.0.0 - January 29, 2019

API Changes:

  * The `styled` configuration no longer disables `value-list-max-empty-line`.

## 2.0.0 - September 13, 2018

New Features:

  * Added support for linting `styled-components`.
    * Added new configuration to extend: `@splunk/stylelint-config/styled`.
  * Upgraded stylelint dependencies.

API Changes:

  * Due to the `stylelint-config-standard` dependency update additional violations might now be detected. Migrating projects should fix the violations or add disable statements if and where appropriate.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

---

# Other Packages {#other-packages}

*Additional packages and specialized functionality.*

## Splunk Design System

**Package:** `CRUD` | **Component:** `Create`

# Create Overview

Create is the starting point in a workflow where a user creates something new,
such as a dashboard, alert, or rule. The flow typically includes a trigger,
input, review, and feedback.

## 1\. Trigger

The trigger is the entry point into a create flow — often a Button labeled
with a clear action, like “Create dashboard” or “Add alert”. It should be easy
to find, aligned with nearby content, and clearly communicate what the user is
about to do.

## Must have

### Clearly label actions

Action clarity ensures all users, including those with cognitive or vision-
related disabilities, can easily understand what a trigger does before
interacting with it. Specific actions reduce ambiguity, helping users navigate
and complete tasks efficiently.

  * Identify the object or data you're trying to create
  * Use clear labels that start with verbs
  * Avoid words like “New” in “Create new”
  * Avoid articles like “a”, “an”, or “the”
  * “Plus” icon: Include an idiomatic indicator which reinforces the creation of something new

### Common verbs for triggers

  * **Create:** Use this when the user is making something that doesn’t yet exist. It is ideal for actions that require multiple steps, like creating API tokens
  * **Add:** Use this when the user is adding something that already exists, like adding a user to a group or permissions to an account
  * **Generate:** Use this when the action refers to an automated process with minimal user input, like generating tokens or custom reports

## Things to consider

### Placement & context

Effective placement uses both implicit and explicit groupings to create clear
structure and guide attention. Proximity and spacing (implicit) or hierarchy
and visual framing (explicit) help users quickly identify where actions belong
and where to focus.

  * **Implicit:** Place the action near related actions and content, aligned with the overall flow of the page.
  * **Explicit:** Use clear labeling, such as the data type (“route” or “roster”), so the user knows exactly what is being created.

#### Check out:

  * [Button](/Packages/react-ui/Button)
  * [Menu](/Packages/react-ui/Menu)

## 2\. Data entry

This step gathers the details needed to complete the task. It’s where the user
defines what they’re creating and provides the information required to move
the process forward.

## Must have

### For low-complexity tasks

Low-complexity tasks should be quick and repeatable, requiring minimal input
and offering simple ways to undo. Keeping them seamless within larger
workflows helps maintain momentum, especially when they’re nested inside more
complex interactions.

  * Keep tasks simple and in context: avoid breaking them into steps, and use inline inputs instead of modals or page transitions.
  * Enable quick correction: support undo, inline editing, or cancel/escape options.
  * Use consistent labels: include the object or data in the header, and keep button labels short and action-focused.

### For high-complexity tasks

High-complexity tasks involve more decisions, and potential for error. Without
structure and guidance, users may feel lost or make mistakes. Breaking tasks
into clear, manageable steps improves understanding, reduces errors, and
supports successful completion.

  * Use the right layout: a `Modal` with a `Step Bar` for linear, focused flows, or a full page for flexible, multi-section, or non-linear tasks.
  * Organize fields to reduce cognitive load: group related inputs, keep section headers consistent (all noun phrases or verb+noun), and use sentence case for labels and headers.
  * Clarify inputs: mark required fields with an asterisk and include a legend (“* indicates a required field”).

## Things to consider

### Preserve information

When users navigate backward or exit temporarily, it’s important to preserve
their input. This prevents frustration and allows them to continue where they
left off without losing progress.

  * Auto-save or cache entered information so it can be restored when the user returns.

#### Check out:

  * [Modal](/Packages/react-ui/Modal)
  * [Step Bar](/Packages/react-ui/Stepbar)
  * [Progress](/Packages/react-ui/Progress)
  * [Popover](/Packages/react-ui/Popover)

## 3\. Confirmation

Give users clarity and confidence at the end of a flow. Use this moment to
summarize what was created, provide a way to make changes if needed, and
confirm what happens next. The level of review and feedback should match the
complexity of the task.

## Must have

### For low-complexity tasks

For low-complexity tasks, feedback should be immediate, lightweight, and keep
users in flow. When effort matches task complexity, there's no need for page
changes, modals, or redundant summaries.

  * Clearly confirm that the task was completed
  * Show errors or partial outcomes with actionable messaging
  * Avoid disrupting flow — keep users in place and in context

### For high-complexity tasks

For high-complexity tasks, feedback should offer clarity, reassurance, and
control. When the effort required is higher, users benefit from structured
confirmation, persistent success states, and clear next steps. Messaging
should acknowledge what was completed, what’s in progress (if applicable), and
what actions are now available.

  * Provide a clear way to go back and make changes
  * Provide actionable guidance on what to do next, such as “View new contact” or “Edit route”
  * Summarize the key information the user provided with section headers that are consistent with step headers

## Things to consider

### Task reversibility

  * Let users act on the result right away (e.g. open the new contact, assign it, etc.)
  * Redirect after creation only if the user needs to act on or verify the result and it lives on a different page—otherwise, keep them in context

#### Check out:

  * [Message](/Packages/react-ui/Message)
  * [MessageBar](/Packages/react-ui/MessageBar)

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Actionmenu`

# Action Menu

The action menu is displayed on a selected or hovered visualization on the
dashboard. It allows users to perform customized actions like cloning or
deleting the visualization.

## How to Customize Action Menu

One can customize the buttons available in the action menu by using the
`actionMenus` prop on Dashboard and DashboardCore components. This prop
accepts an array of buttons. The code below demonstrates how to display the
full screen and delete buttons on the action menu:



    import React from 'react';
    import { DEFAULT_DEFINITION } from '@splunk/dashboard-definition'; // or use your own definition
    import { Dashboard } from '@splunk/dashboard';
    import { DashboardContextProvider } from '@splunk/dashboard-context';
    import { DeleteButton, FullscreenButton } from '@splunk/dashboard-action-buttons';
    import EnterprisePreset from '@splunk/dashboard-presets/EnterprisePreset';

    const actionMenus = [<FullscreenButton key="fullscreen" />, <DeleteButton key="delete" />];

    const App = () => (
        <DashboardContextProvider preset={EnterprisePreset} initialDefinition={DEFAULT_DEFINITION}>
            <Dashboard
                actionMenus={actionMenus}
                {/* ...other props...*/}
            />
        </DashboardContextProvider>
    );

**Note:** It is required to use a unique `key` prop for each button component
in the list to help React identify which items have changed and optimize
rendering of components (more in the [React
docs](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-
with-key))

Consumers can also customize which buttons are displayed in the menu depending
on `view` or `edit` mode. Create an object with `view` and `edit` keys, each
with an array of the buttons as the value. This object can be passed to the
Dashboard component using the `actionMenus` prop using `mode` from consuming
component's `state` or the `onModeChange` callback prop to get the latest
mode. The code below demonstrates how to do this for Dashboard component (can
be applied to DashboardCore):



    import React, { useState } from 'react';
    import { DEFAULT_DEFINITION } from '@splunk/dashboard-definition';
    import { Dashboard } from '@splunk/dashboard';
    import { CloneButton, DeleteButton, FullscreenButton, MoveButton } from '@splunk/dashboard-action-buttons';
    import EnterprisePreset from '@splunk/dashboard-presets/EnterprisePreset';

    const actionMenus = {
        view: [<FullscreenButton key="fullscreen" />],
        edit: [
            <MoveButton key="move" />,
            <CloneButton key="clone" />,
            <DeleteButton key="delete" />
            ],
    };

    const App = () => {
        const [mode, setMode] = useState('view');

        return (
            <DashboardContextProvider
                preset={EnterprisePreset}
                initialDefinition={DEFAULT_DEFINITION}
                initialMode={mode}
                onModeChange={setMode}
            >
                <Dashboard
                    actionMenus={actionMenus[mode]}
                    {/* ...other props...*/}
                />
            </DashboardContextProvider>
        );
    }

## What Buttons are Available

Dashboard team provides the following action buttons in the
`@splunk/dashboard-action-buttons` package.

Button| Description| Named import
---|---|---
Clone| Clones the item (also creates a copy of the datasource)| `CloneButton`
Delete| Deletes the item from the dashboard| `DeleteButton`
Export| Exports the visualization as a PNG or CSV| `ExportButton`
Fullscreen| Displays the visualization in full screen| `FullscreenButton`
Layer| Displays a menu to adjust the rendering order of the item|
`LayerButton`
Open in Search| Invokes the consumer defined `onOpenSearchClick` callback prop
which should open a search page with the datasource query| `OpenSearchButton`
Refresh| Re-runs search to retrieve latest data to display in the item|
`RefreshButton`

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

## How to Make Custom Buttons

To create custom buttons to display in the action menu, use the following
**optional** props provided in `BaseButton`.

Prop name| Type| Description
---|---|---
`itemId`| String| Visualization or input id
`dashboardApi`| Object| Dashboard API
`itemDefinition`| Object| Visualization or input definition
`dataSources`| Object| Associated datasource definitions

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Return `ActionButton` to ensure that button matches the styling of the other
buttons in the action menu. `ActionButton` has the following props:

Prop name| Type| Description
---|---|---
`icon` (**required**)| ReactElement| Icon for the button
`disabled`| Boolean| Whether button is enabled or disabled
`onClick`| Function| Callback to invoke when button is clicked

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Putting it together, below is the sample code:



    import React, { useCallback } from 'react';
    import {
        type BaseButtonProps,
        ActionButton,
    } from '@splunk/dashboard-action-buttons';
    import ArrowBroadBowRight from '@splunk/react-icons/ArrowBroadBowRight';
    // optional
    import { useTelemetryApi } from '@splunk/dashboard-telemetry';

    const ActionButtonIcon = <ArrowBroadBowRight />;

    const CustomButton = ({ dashboardApi }: BaseButtonProps) => {
        // If you plan to log any metrics, retrieve the telemetry api from the hook. Otherwise this is optional.
        const telemetry = useTelemetryApi();

        const handleOnClick = useCallback(() => {
            // handle clicks on this button, perhaps by calling a dashboardApi method
            // perhaps log events using metrics collector
        }, []);

        const disabled = false; // add logic to enable/disable button

        return (
            <ActionButton
                data-test="CustomButton" // for testing
                onClick={handleOnClick}
                icon={ActionButtonIcon} // icon for this button
                disabled={disabled}
            />
        );
    };

    export default CustomButton;

Add this to the array of buttons and pass it to `actionMenus` prop to the
Dashboard or DashboardCore components:

For Dashboard:



    import React from 'react';
    import { Dashboard } from '@splunk/dashboard';
    import { DEFAULT_DEFINITION } from '@splunk/dashboard-definition';
    import EnterprisePreset from '@splunk/dashboard-presets/EnterprisePreset';
    import { DashboardContextProvider } from '@splunk/dashboard-context';
    import CustomButton from './CustomButton';

    const actionMenus = [<CustomButton key="custom" />];

    const App = () => (
        <DashboardContextProvider preset={EnterprisePreset} initialDefinition={DEFAULT_DEFINITION}>
            <Dashboard
                actionMenus={actionMenus}
                {/* ...other props...*/}
            />
        </DashboardContextProvider>
    );

For DashboardCore:



    import React from 'react';
    import { DEFAULT_DEFINITION } from '@splunk/dashboard-definition';
    import EnterprisePreset from '@splunk/dashboard-presets/EnterprisePreset';
    import { DashboardContextProvider } from '@splunk/dashboard-context';
    import { DashboardCore } from '@splunk/dashboard-core';
    import CustomButton from './CustomButton';

    const actionMenus = [<CustomButton key="custom" />];

    const App = () => (
        <DashboardContextProvider preset={EnterprisePreset} initialDefinition={DEFAULT_DEFINITION}>
            <DashboardCore
                actionMenus={actionMenus}
                {/* ...other props...*/}
            />
        </DashboardContextProvider>
    );

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Cloudsearch`

# Cloud search

`CloudSearch` is a data source that can run searches on SCS.

Guide

Options

API

To run a basic search, provide **query** string and time range in the
definition. The timezone is GMT by default, you can specify **timezone**
together with **earliest** and **latest**.

## Search for data from last 24 hours



    {
     "type": "ds.search",
     "options": {
      "query": "from index:main | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now",
       "timezone": "America/Los_Angeles"
      }
     }
    }

Searches can be configured to automatically re-run, use **refresh** to specify
refresh interval, and use **refreshType** to control when you want the refresh
to happen.

## Rerun the search 30 seconds after the search completes



    {
     "type": "ds.search",
     "options": {
      "query": "from index:main | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now"
      },
      "refresh": "30s",
      "refreshType": "delay"
     }
    }

It would be useful to cache the search results in some cases. You can use the
**requiredFreshness** option to specify time period in seconds

## Use requiredFreshness



    {
     "type": "ds.search",
     "options": {
      "query": "from index:main | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now",
       "timezone": "America/Los_Angeles"
      },
      "requiredFreshness": 60
     }
    }

You can specify **module** to run the search in. The default module is used if
a module is not specified.

## Use module



    {
     "type": "ds.search",
     "options": {
      "query": "from index:main | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now",
       "timezone": "America/Los_Angeles"
      },
      "module": "my_module_name"
     }
    }

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Conditionalshowhide`

# Conditionally show or hide panels

Organize your dashboard or conceal empty panels by conditionally showing or
hiding panels based on data availability. For example, suppose a chart on your
dashboard is empty because it depends on a token setting from a different
visualization. In that case, you can hide the chart until the token is set and
data is available.

In both **Grid** and **Absolute** layout support conditionally showing or
hiding panels. The following elements support hiding panels conditionally:

Element| Grid layout| Absolute layout
---|---|---
Charts| X| X
Icons| n/a| X
Line shape| n/a| n/a
Rectangles| X| X
Ellipses| n/a| X
Dropdown input| X| X
Multiselect input| X| X

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

To conditionally hide a panel when its primary data source returns no data,
follow these steps:

  1. Select your visualization or input.
  2. Navigate to the Visibility section of the Configuration panel.
  3. Select "When data is unavailable, hide element" and a dotted blue line will surround your visualization or input.

To conditionally hide a panel using custom-defined conditions when the
**showConditionsEditor** feature flag is set to `true`, follow these steps:

  1. Select your visualization or input.
  2. Navigate to the Visibility section of the Configuration panel.
  3. Click "+ Set up condition".
  4. Click "+ Create condition".
  5. Using either the **Condition builder** or **JSONata source** , define the scenario in which the panel should visible.

By default, newly-configured conditions will be framed as "show when
[condition is met]", indicated by the Eye icon in the configuration panel next
to the condition's name. Clicking this icon will toggle its appearance between
an Eye and a Slashed Eye, reframing the condition between "show when
[condition is met]" and "hide when [condition is met]".

See [Conditions](?path=/Dashboard) for details on writing custom conditions.

## About the grid layout conditional visibility logic

If you hide a visualization in the grid layout, the dashboard balances the
composition of the remaining visualizations by adjusting their sizes. The grid
layout prioritizes filling any blank space within the canvas to achieve
compositional completeness.

When the grid layout resizes visualizations, it prioritizes adjusting the
visualizations neighboring a hidden element. The grid layout works across the
dashboard from left to right and top to bottom.

### Visualizations with equal proportions

The grid layout maintains the proportion of space used by the viewable
visualizations based on shared columns or rows. For example, you might have 4
visualizations in a row, each occupying 25% of the width of the dashboard
canvas, and you decide to hide 1 of the visualizations. The remaining 3
visualizations respond to the hidden visualization by adjusting their widths
to 33%.

### Visualizations with unequal proportions

If you intentionally create a dashboard visualization larger than its fellow
visualizations, the larger visualization stays proportionally more prominent
than the other visualizations throughout the resizing process. For example,
you might have 3 visualizations in a row. 1 visualization takes up 50% of the
dashboard, and the other 2 take up 25%. If you hide a small visualization, the
larger visualization will adjust to about 65%, and the remaining small
visualization will adjust to about 35%.

## Example of show or hide in the dashboard definition

You can control the condition of showing or hiding panels with the
`hideWhenNoData` option in the dashboard definition. The following example
shows the `hideWhenNoData` set to true, which activates the show or hide
feature.



    {
        "type": "splunk.singlevalue",
        "dataSources": {
            "primary": "ds_myDataSource"
        },
        "containerOptions": {
            "visibility": {
                "hideWhenNoData": true
            }
        }
    }

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Customdatasource`

# Custom data source

A `DataSource` is a javascript module that provides the data that powers a
dashboard. Any React component which extends the base `DataSource` class
exported from `@splunk/datasources` can be inserted into a dashboard
definition using a custom preset. See [Data source
overview](/Packages/dashboard-docs//?path=/Datasourcesoverview) for more
details about data sources.

## Quick example

This is a custom data source which repeatedly increments and returns a count.



    import { DataSet, DS_STATUS } from '@splunk/datasource-utils';
    import { DataSource } from '@splunk/datasources';

    export default class CustomDataSource extends DataSource {
        /**
         *
         * @param {Object} options.data static data set
         * @param {Number} options.delay
         * @param {*} context
         */
        constructor(options = {}, context = {}) {
            super(options, context);
            this.counter = 0;
        }

        request() {
            return (observer) => {
                const interval = setInterval(() => {
                    if (this.counter <= Number.MAX_SAFE_INTEGER) {
                        this.counter += 1;
                    } else {
                        this.counter = 0;
                    }

                    observer.next({
                        data: DataSet.fromJSONCols(
                            [
                                {
                                    name: 'count',
                                },
                            ],
                            [[this.counter]]
                        ),
                        meta: {
                            isRealTimeSearch: true,
                            totalCount: 1,
                            status: DS_STATUS.RUNNING,
                            lastUpdated: Date.now(),
                        },
                    });
                }, 2000);
                return () => {
                    clearInterval(interval);
                };
            };
        }
    }


## Using custom data sources

Show code

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

Count

Single Value

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Customeditors`

# Custom Editors

Custom Editors allow you to override the editing widgets used by the
Dashboard.

Different editor types may have a different interface but at minimum they
should all have the following props:



    interface CustomEditorProps {
        options: Record<string, unknown>;
        onOptionsChange: (options: Record<string, unknown>) => void;
    }

If the editor you want to override is using a DynamicEditor (e.g.
`layoutEditors` and `visualizationEditors`) and you just wanted to modify the
options layout instead of writing a custom editor you could use the
`DynamicEditorWrapper` provided by the `@splunk/dashboard-editors` package.

## Custom Layout Editor

Layout editors allow users to specify their own editors for layout options.

For instance if you were using the Absolute layout but wanted to use your own
components for the width/height options in the sidebar you would want to pass
in a custom `layoutEditors` that overrides the default AbsoluteLayoutEditor.



    type OnChange: (key: string; value: string) => void;
    const OptionValueEditor = (optionKey: string, optionValue: string, onChange: OnChange) => {
        const handleOptionsChange = useCallback((newValue: string) => {
            onChange(optionKey, newValue);
        }, [optionKey, onChange]);

        return (
            <div>
                <div>Option: {optionKey}</div>
                <input type="text" value={optionValue} />
                <button type="submit" onClick={handleOptionsChange}>
                    Update
                </button>
            </div>
        );
    }

    type CustomLayoutOptions = Record<string, string>;

    interface CustomLayoutEditorProps {
        options: CustomLayoutOptions;
        onOptionsChange: (options: CustomLayoutOptions) => void;
    }

    const CustomAbsoluteLayoutEditor = ({ options, onOptionsChange }: CustomLayoutEditorProps) => {
        const handleChange = useCallback((key, value) => {
            onOptionsChange({
                ...options,
                [key]: value,
            })
        }, [options, onOptionsChange]);

        return Object.entries(options).map(([key, value]) =>
            <OptionValueEditor optionKey={key} optionValue={value} key={key} onChange={handleChange} />
        );
    };

    return (
        <DashboardContextProvider initialDefinition={def}>
            <Dashboard
                layoutEditors={{
                    absolute: CustomAbsoluteLayoutEditor,
                }}
            />
        </DashboardContextProvider>
    );

## Custom DataSource Editor

Users can provide their own data source editing widget for custom data
sources.



    import { Dashboard } from '@splunk/dashboard';
    import { DashboardContextProvider } from '@splunk/dashboard-context';
    import { DataSourceEditors } from '@splunk/dashboard-editors';

    /**
     * DataSource Editor React Component
     */
    interface MyDataSourceEditorProps {
        /**
         * datasource meta node
         */
        meta: Record<string, unknown>;
        /**
         * datasource options
         */
        options: Record<string, unknown>;
        /**
         * a callback to update datasource options
         */
        onOptionsChange: (options: Record<string, unknown>) => void;
    }
    const MyDataSourceEditor = (props: MyDataSourceEditorProps) => {
        return <div>...</div>;
    };

    const App = () => (
        <DashboardContextProvider initialDefinition={def}>
            <Dashboard
                dataSourceEditors={{
                    // default datasource editors
                    ...DataSourceEditors,
                    'ds.myDataSource': MyDataSourceEditor,
                }}
            />
        </DashboardContextProvider>
    );

## Custom Visualization Editor

Users can provide their own visualization editing widgets.



    interface CustomEditorProps {
        options: Record<string, unknown>;
        onOptionsChange: (options: Record<string, unknown>) => void;
    }
    const CustomEditor = (props: CustomEditorProps) => <span>Custom</span>;

    const App = () => (
        <DashboardContextProvider initialDefinition={def}>
            <Dashboard
                visualizationEditors={{
                    'splunk.singlevalue': CustomEditor,
                }}
            />
        </DashboardContextProvider>
    );

## Dynamic Editor

For editors that use a dynamic editor you can make runtime modifications of
their layout by using a dynamic editor wrapper that transforms the editor
layout based on your conditions:



    import React from 'react';
    import { DynamicEditorWrapper } from '@splunk/dashboard-editors';

    /**
     * @param {Array} layout Contains the complete editor config for the component
     */
    const transformLayout = ({ layout }) => {
        if (/* some condition */) {
            // Mutate the layout
            delete layout[1];
        }

        return layout;
    };

    const CustomEditorWrapper = props => <DynamicEditorWrapper {...props} transformLayout={transformLayout} />;

    export default CustomEditorWrapper;

In the client `Dashboard` pass in the prop to use your custom wrapper:



    const App = () => (
        <DashboardContextProvider initialDefinition={def}>
            <Dashboard
                visualizationEditors={{
                    `viz.my_custom_viz`: CustomEditorWrapper
                }}
            />
        </DashboardContextProvider>
    );

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Custominteractions`

# Custom interactions

An Event Handler is a javascript module that handles dispatched action events.
Developers can provide their own Event Handler via custom preset.

## Events are triggered by visualizations

Visualizations can create action events at the dashboard runtime via the
`onEventTrigger` callback.



        onEventTrigger({
            type: 'myViz.click',
            originalEvent: e,
            payload: {
                ...
            }
        });

  * **type** \- unique event type.
  * **originalEvent** \- DOM event or React SyntheticEvent.
  * **payload** \- plain javascript object that contains arbitrary information about the event, e.g. field name and value(s) associated with the clicked data point

## Implementing an Event Handler

`EventHandler` is a javascript object with the following two functions.

  * **canHandle(event)** \- Returns a boolean value. A value of 'true' indicates that the current handler is capable of handling the current action event, while 'false' indicates that it is not.
  * **handle(event)** \- Handles an action event and returns a list of actions. The returned actions will be executed by the dashboard one after the other.

Example of a table cell click handler:



    class TableClickHandler {
        constructor(options) {
            this.options = options;
        }

        canHandle(event) {
            // only handle table cell.click event on particular field
            return (
                event.type === 'cell.click' &&
                event.payload.fieldValue === this.options.field
            );
        }

        handle(event) {
            return [
                {
                    type: 'setToken',
                    payload: {
                        tokens: {
                            title: `Click on field ${this.options.field} cell value: ${event.payload.cellValue}`,
                        },
                    },
                },
            ];
        }
    }

    export default TableClickHandler;


### Use it in dashboard

## Table Event handler for 'bar' column

Show code

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

$title$

* * *

foo|

* * *

bar
---|---
1| 1
2| 2
3| 3
4| 4
5| 5
6| 6
7| 7
8| 8

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Customlayout`

# Custom layouts

A layout is a React component which positions visualizations and in-canvas
inputs in a dashboard. Custom layouts receive from Dashboard Framework props
matching the type `BaseLayoutProps`, exported from `@splunk/dashboard-types`.

## Custom layout example

Show code

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

Viewing Item: table

Table

* * *

foo|

* * *

bar
---|---
1| 1
2| 2
3| 3
4| 4
5| 5
6| 6
7| 7
8| 8

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Prev. Item

Panel 1 of 3 _Auto-scroll set to 10 second(s)_

Next Item

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

## The `renderLayoutItem` prop

The `renderLayoutItem` prop is how a layout component requests that Dashboard
Framework generate a JSX element to be rendered. This item is specified by its
**itemId** , can be a visualization or an input - denoted by a provided `type`
argument - and is rendered at the provided dimensions. The signature of this
function, `RenderLayoutItem`, can be imported from the `@splunk/dashboard-
types` package.

## Layout options and structure

A layout is identified by its **type** , and has two optional properties:
**options** and **structure**. The `LayoutDefinitionItem` type exported by
`@splunk/dashboard-types` can be used to create this typedef:



    import type {
        LayoutDefinitionItem,
        StructureItemType,
    } from '@splunk/dashboard-types';

    /** Each entry in the layout's structure array will have a `type` and an `item` property */
    type MyLayoutStructure = {
        type: StructureItemType;
        item: string;
    }[];

    /** The layout will have an optional numeric configuration, `autoScroll` */
    type MyLayoutOptions = {
        autoScroll?: number;
    };

    /** The type of an object representing the layout definition can be generated using the structure and options types */
    type MyLayoutDefinition = LayoutDefinitionItem<
        MyLayoutStructure,
        MyLayoutOptions
    >;

While the `DashboardCore` module will not validate or assume any structure
format, the `DashboardValidator` will assert the structure . Instead, the
Layout component renders its own options and structure. The
`DashboardValidator` module, however, will validate and assume the structure
format of a provided layout.

## Layout APIs

A layout API is how Dashboard Framework interacts with layouts. Layout APIs
must implement the `LayoutApi` interface, exported from the
`@splunk/dashboard-types` package; for convenience an abstract base class
`BaseLayoutApi` is provided in the `@splunk/dashboard-layouts` package. The
core methods provided by a layout API are `addLayoutItems`,
`cloneLayoutItems`, `removeLayoutItems`, `getLayoutItems`, and `snapshot`.

  * `addLayoutItems` is responsible for generating a proposed structure which includes the items to be added
  * `cloneLayoutItems` is responsible for generating a proposed structure which includes clones of the items specified by the item IDs
  * `removeLayoutItems` is responsible for generating a proposed structure which omits the specified items
  * `getLayoutItems` normalizes a custom layout's structure into a format which can be used by Dashboard Framework
  * `snapshot` returns a deep clone of the layout's options, with any external resources resolved

Layouts which do not provide a static `config.layoutApi` property can still
render, but will have limited functionality.

## Custom layout API

Show code

Unnamed tab

Active tab: undefined

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

Add a tab

Viewing Item: table

Table

* * *

foo|

* * *

bar
---|---
1| 1
2| 2
3| 3
4| 4
5| 5
6| 6
7| 7
8| 8

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Clone

Delete

Prev. Item

Panel 1 of 3

Next Item

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

## Supporting code

The custom layout example imported a component named `ScrollStatus`. For
completeness, the source for this component is provided. The `ResetButton` is
not provided, as its purpose is only to reset the example in the event all
visualizations are removed.



    import React from 'react';
    import styled from 'styled-components';
    import { sprintf } from '@splunk/ui-utils/format';
    import { _ } from '@splunk/ui-utils/i18n';

    const InfoContainer = styled.div`
        display: flex;
        flex-direction: column;
        align-items: center;
    `;

    export const ScrollStatus = ({
        id,
        length,
        autoScroll,
    }: {
        id: number;
        length: number;
        autoScroll?: number;
    }) => (
        <InfoContainer>
            <span>
                Panel {id} of {length}
            </span>
            {!!autoScroll && <em>Auto-scroll set to {autoScroll} second(s)</em>}
        </InfoContainer>
    );

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `DashboardCoreAPI`

# Dashboard Core API

A set of methods for controlling an instance of the `DashboardCore` component

Guide

API

## Retrieving an API Reference

To retrieve a reference to the API for a mounted `DashboardCore` component you
can use the `dashboardCoreApiRef` prop



    import * as React from 'react';
    import { DashboardCore } from '@splunk/dashboard-core';
    import { DashboardContextProvider } from '@splunk/dashboard-context';
    import type { DashboardCoreApi } from '@splunk/dashboard-types';

    export default function MyDashboard() {
        const dashboardCoreApi = React.useRef<DashboardCoreApi>();
        const setDashboardCoreApi = React.useCallback((api: DashboardCoreApi) => {
            dashboardCoreApi.current = api;
        }, []);

        return (
            <DashboardContextProvider>
                <DashboardCore dashboardCoreApiRef={setDashboardCoreApi} />
            </DashboardContextProvider>
        );
    }

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Dataset`

# DataSet

`DataSet` is a representation of 2-dimensional data which includes utilities
for pagination, field retrieval, column retrieval, and conversion to and from
JSON structures.

Guide

API

A common use-case for **DataSet** is to convert JSON data to a structure which
can be used by dashboard framework and passed to visualizations.

## Converting a JSON array to a DataSet



    import DataSet from '@splunk/datasource-utils';

    DataSet.fromJSONArray(null, [
        { x: 'a', y: 4, z: 70 },
        { x: 'b', y: 5, z: 80 },
        { x: 'c', y: 6, z: 90 },
    ]);

    // > fields: [{ name: 'x' }, { name: 'y' }, { name: 'z' }]
    // > columns: [['a', 'b', 'c'], [4, 5, 6], [70, 80, 90]]


To specify the order, arity, or additional properties of the fields in the
data, the **fields** argument can be given a non-null value.

## Converting a JSON array to a DataSet with field information



    import DataSet from '@splunk/datasource-utils';

    DataSet.fromJSONArray(
        [{ name: 'x', groupby_key: 0 }, { name: 'z' }],
        [{ x: 'a', y: 4, z: 70 }, { x: 'b', y: 5 }, { z: 90 }]
    );

    // > fields: [{ name: 'x', groupby_key: 0 }, { name: 'z' }]
    // > columns: [['a', 'b', null], [70, null, 90]]

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Gridlayout`

# Grid Layout

A layout system that allows users to create non-overlapping, perfectly aligned
visualizations in a quick-and-easy way.

Guide

Options

API

## Grid layout example

Show code

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

Bar Chart

Chart

Bar chart with 8 bars.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 9.

Created with Highcharts 9.3.3foobarbar123456780123456789

  *

End of interactive chart.

Table

* * *

foo|

* * *

bar
---|---
1| 1
2| 2
3| 3
4| 4
5| 5
6| 6
7| 7
8| 8

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Column Chart

Chart

Bar chart with 8 bars.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 10.

Created with Highcharts 9.3.3foobarbar123456780246810

  *

End of interactive chart.

Line Chart

Chart

Line chart with 8 data points.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 10.

Created with Highcharts 9.3.3foobarbar123456780246810

  *

End of interactive chart.

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

## Grid Layout Behaviors

  1. The Height and Width of the Canvas dynamically change depending on the contents in the Layout
  2. If there is one or more Visualizations in the Layout, the Full Width of the Canvas will always be Filled Up with no empty space
  3. There are edges placed in between Visualizations
  4. Any change being made in the Layout will follow the rule of Least Disturbance - meaning the least disruption will be made to the overall layout

### Concept of Edges

  1. Edges exist between Visualizations and has two main functionalities:
  2. Resize the bordering Items by clicking and dragging the Edge
  3. Drag and drop an Item on top of an Edge

### Moving Visualizations

Moving Visualizations is centered around the behavior of a user selecting a
Visualization Item and dragging it around to drop it in a different area on
the Canvas. The traditional Absolute Layout allows a User to drag and drop a
Visualization located anywhere on or even outside the Canvas but the Grid
Layout is intended to keep all User behavior within the Canvas. This results
in the concept of Drop Targets, which of there are two types:

  1. A Drop Target can be on a Visualization Item
  2. A Drop Target can be on an Edge

### Creating a Grid Layout without using the UI

In order to create grid layouts programmatically or directly via source, the
following concepts must be followed:

  1. First, let's assume the width of the canvas is 1200 px.
  2. The height of the canvas will be calculated dynamically based on the visualizations present on the dashboard
  3. There is no empty space on the dashboard
     * no gaps between visualizations. If "viz1" starts at x=0 and ends at x=400, the next "viz2" MUST start at x=400. The same concept applies in the vertical direction.
     * no gaps between visualizations and the edges of the canvas. If the last viz to the right starts at x=800 it must end at x=1200 (ie. width of 400) in order to perfectly cover the 1200 px of canvas width. Another important application of this concept is that the first visualization must start at (0,0).
  4. Visualizations must not exceed canvas bounds
  5. Visualizations must not overlap

## Dealing with Invalid Grid Layout Definitions

### Possible Errors:

  1. Empty space between visualizations
  2. Empty space between edges of the canvas and visualizations
  3. Visualizations are outside of canvas bounds

In order to enable seeing these errors in edit mode, set feature flag
`enableGridLayoutErrors` to true.

## Invalid Grid Layout Example

Show code

New tab

Active tab: New tab

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

Add a tab

Bar Chart

#### Chart

Bar chart with 8 bars.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 10.

Created with Highcharts 9.3.3foobarbar123456780246810

  *

End of interactive chart.

Alert

Viz panel incorrectly configured.

"bar" expected a viz or canvas edge directly to its right at x=400

Table

* * *

foo|

* * *

bar
---|---
1| 1
2| 2
3| 3
4| 4
5| 5
6| 6
7| 7
8| 8

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

Alert

Viz panel incorrectly configured.

"table" expected a viz or canvas edge directly to its left at x=420

"table" expected a viz or canvas edge directly to its right at x=1120

Column Chart

#### Chart

Bar chart with 8 bars.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 10.

Created with Highcharts 9.3.3foobarbar123456780246810

  *

End of interactive chart.

Line Chart

#### Chart

Line chart with 8 data points.

The chart has 1 X axis displaying foo.

The chart has 1 Y axis displaying bar. Range: 0 to 10.

Created with Highcharts 9.3.3foobarbar123456780246810

  *

End of interactive chart.

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

The above example illustrates a key part of Grid Layout: there is no empty
space allowed. More specifically, every visualization lives adjacent to other
visualizations or the edge of the canvas. In the example, the visualization
"bar" starts at `x = 0` and has `width = 400`. Thus, it expects there to be
another visualization (or the edge of the canvas) at `x = 400`. Similarly, the
visualization "table" starts at `x = 420` and has `width = 700`. Thus, it
expects there to be an adjacent visualization to its left at `x = 420` AND an
adjacent visualization/canvas edge to its right at `x = 1120` (420 + 700).

In order to fix this layout, the user must fill any empty space by either
adding a visualization in the space or by resizing existing ones to fill that
space. In this example, a simple fix would be:

  1. change width of "bar" to `420` \- this ensures "bar" and "table" are directly adjacent
  2. change width of "table" to `780` \- this brings the right edge of "table" to the edge of the canvas

The following changes can be made through source mode or by dragging the
edges. However, positioning must be pixel perfect.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Introduction`

# Introduction

## What is Dashboard Framework?

Dashboard Framework is a set of UI components that render a dashboard. A
dashboard is one or more visualizations that connect to one or more
datasources. Dashboard Framework displays these visualizations with
datasources and lays them out on the page as designated by the layout. The
layout and relationship between visualizations and datasources is specified by
a JSON object called Dashboard Definition.

## Glossary

Term| Meaning
---|---
[Dashboard Definition](?path=/Dashboarddefinition)| A JSON object that
describes the structure of the dashboard.
Visualization| A React component that renders data into a DOM element.
Layout| A React component that positions visualizations on a dashboard.
Datasource| A JavaScript module that provides data.
[Input](?path=/Inputsoverview)| A React component that takes user input.
[Token](?path=/Tokens)| A variable that can be used to pass a runtime value
within and between dashboard visualizations.
[EventHandler](?path=/Custominteractions)| A JavaScript module that handles
events triggered by visualizations or inputs.
[Preset](?path=/Dashboardpreset)| A JavaScript module that bundles prebuilt
DataSource, Visualization, Layout, Input and EventHandler components and
modules for out of the box use.

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

## Dashboard vs DashboardCore

Dashboard Framework provides `Dashboard` and `DashboardCore` as 2 major
components. `DashboardCore` component provides a static view of the dashboard
and does not have UI editing capabilities. `Dashboard` component has UI
editing capabilities and is built on `DashboardCore`.

For more information, see our [Integration Guide](?path=/IntegrationGuide).

## High Level Architecture

The following diagram gives a high level overview of Dashboard Framework:

### DashboardContextProvider

The `DashboardContextProvider` component is the top level component which
provides state management, feature flag preferences, artifact providers, and
search orchestration for Dashboard Framework. The component props for
`DashboardContextProvider` are how most Dashboard Framework configurations can
be supplied by application authors. Only one `DashboardContextProvider` should
exist on a given page.

### Dashboard

The `Dashboard` component provides both viewing and editing experiences to an
application. It creates a `DashboardApi` instance which exposes methods to
create, update, and delete visualizations, inputs, and datasources. This
component also defines functions to render the toolbar, header, sidebar and
`DashboardCore`.

### Toolbar

The `Toolbar` component renders mode-specific buttons provided by the
application author. A collection of buttons which cover common use cases are
provided in the `@splunk/dashboard-toolbar` package.

### Sidebar

This component is only displayed in `edit` mode. By default, it displays UI
controls to edit dashboard height, width, background color, etc. When a
visualization or input is selected, it displays UI controls specific to that
item. The sidebar is also used for displaying and editing information about
other dashboard elements like datasources.

### DashboardCore

`DashboardCore` is a controlled component which renders the dashboard
definition set by the wrapping `DashboardContextProvider`. `DashboardCore`
also creates a `DashboardCoreApi` instance which provides methods to create,
update, and delete visualizations, inputs, and datasources (several methods
from `DashboardApi` internally call `DashboardCoreApi` methods). The rendered
dashboard is comprised of a global input container, if any global inputs
exist, and the layout canvas which contains visualizations and in-canvas
inputs.

### DashboardSourceEditor

`DashboardSourceEditor` is an optional editor which can be rendered as a child
of `DashboardContextProvider`; it provides a Monaco Editor instance for
viewing and editing a full dashboard definition.

# Contact us

  * **Slack** : [#webplatform](https://splunkcommunity.slack.com/archives/C01CYF27FSS)

  * **Email** : [[dashboards@splunk.com](mailto:dashboards@splunk.com)](mailto:dashboards@splunk.com)

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Keyboardlistener`

# Keyboard Listener

Guide

API

**KeyboardListener** enables keyboard shortcuts for editing dashboards. The
default keyboard listener works well in most cases, so you do not need to
provide one on your own.

The default shortcuts are:

Shortcut| Usage
---|---
ctrl/cmd + a| Select all visualizations
ctrl/cmd + shift + a| Unselect all visualizations
esc| Unselect
ctrl + alt/command + =| Increase dashboard zoom
ctrl + alt/command + -| Decrease dashboard zoom
ctrl + alt/command + 0| Zoom dashboard to fit browser width
ctrl/cmd + x| Cut the selected visualization
ctrl/cmd + c| Copy the selected visualization
ctrl/cmd + v| Paste the selected visualization
ctrl/cmd + d| Duplicate the selected visualization
backspace/delete| Delete the selected visualization
ctrl/cmd + z| Undo
ctrl/cmd + shift + z| Redo
left| Move the selected viz to the left and snap to the grid
right| Move the selected viz to the right and snap to the grid
up| Move the selected viz up and snap to the grid
down| Move the selected viz down and snap to the grid
shift + left| Move the selected viz to the left without snapping to the grid
shift + right| Move the selected viz to the right without snapping to the grid
shift + up| Move the selected viz up without snapping to the grid
shift + down| Move the selected viz down without snapping to the grid

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

If you do want to customize shortcuts, here is an example:

## Add new shortcut



    import React from 'react';
    import {
        KeyboardListener,
        DEFAULT_KEYMAP,
        DashboardContextProvider,
    } from '@splunk/dashboard-context';
    import { DashboardCore } from '@splunk/dashboard-core';

    // this will enable ctrl/cmd+p shortcut to paste visualization, in addition to the default ctrl/cmd+v shortcut.
    const customKeyMaps = [
        { event: 'paste', keys: 'meta+p', when: 'mac' },
        { event: 'paste', keys: 'ctrl+p', when: '!mac' },
    ];

    const keyMaps = [...DEFAULT_KEYMAP, ...customKeyMaps];

    const keyboardListener = new KeyboardListener(keyMaps);

    const MyApp = () => {
        return (
            <DashboardContextProvider keyboardListener={keyboardListener}>
                <DashboardCore />
            </DashboardContextProvider>
        );
    };

    export default MyApp;


It is also possible to create shortcuts for new events, which requires extra
work to wire up the event handlers. Please let the dashboard team know if you
need to create a shortcut for a new event.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Resettokens`

## ResetTokens interaction

`ResetTokens` is included in default presets provided by the dashboard
framework. This event handler allows a user to reset a specific token(s), all
tokens in a namespace, or all tokens back to their default values. Note, that
this configuration is mutually exclusive, but you can set up multiple reset
token handlers to reset all tokens for one namespace, and one token in
another. ResetToken can not be used to reset read-only tokens like smart
sources and environment tokens.

### Reset specific token(s)

Reset token can be configured to reset one or more specific tokens in any
namespace. A fully qualified token name is needed for tokens in a non-default
namespace, e.g. `namespace:token_name`.



    "eventHandlers": [
        {
            "type": "drilldown.resetTokens",
            "options": {
                tokens: ['namespace:token_name', 'a_default_token'],
            }
        }
    ],

### Reset all tokens in a namespace

Reset token can be configured to reset all tokens in a token namespace.



    "eventHandlers": [
        {
            "type": "drilldown.resetTokens",
            "options": {
                tokenNamespaces: ['custom_namespace', 'default'],
            }
        }
    ],

### Reset all tokens

Reset all tokens to their default values



    "eventHandlers": [
        {
            "type": "drilldown.resetTokens",
            "options": {}
        }
    ],

### Valid events

`ResetTokens` will only trigger for event types fired by its target which end
in `.click` or are typed as `range.select`. It does not support the `events`
or `fields` options supported by other event handlers. This interaction may
not be available on every visualization type.

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Sourceeditor`

# Dashboard Source Editor

Guide

`DashboardSourceEditor` enables users to edit the dashboard definition
directly as text. It is a React component based on [Monaco
Editor](https://microsoft.github.io/monaco-editor/).

`DashboardSourceEditor` is **not** integrated into `Dashboard` or
`DashboardCore` components, so you will need to render it separately in order
to use.

## Handling state

The `DashboardSourceEditor` component must be rendered as a child of
`DashboardContextProvider`. The component manages its own state directly from
the context, and then updates that state when exiting the component. This
component is meant to be used alongside a dashboard component like `Dashboard`
or `DashboardCore`, which will automatically pick up definition changes on
exit of the `DashboardSourceEditor` component.

## Validation

Validation of the source in `DashboardSourceEditor` happens only on exit of
the component. If the feature flag `enableSourceModeValidation` is enabled, it
provides out of the box dashboard validation. For custom validation, use the
prop `validateDefinition`. This function should return an array of errors if
there are errors OR an empty array if there are no validation errors. The
errors should follow the same format as existing errors. The internal
validation will return errors in the format of: `ValidationErrors =
Partial<ErrorObject>[];` where `ErrorObject` is ajv's definition of it:
<https://ajv.js.org/api.html#error-objects>.

If there are errors in the definition, it does not call `onExit`, instead
calling the `onValidationError` callback.

## Integrate `DashboardSourceEditor`

### Props

Prop Name| Description| Type| Default
---|---|---|---
title| Title to display| `string`|
width| Source editor width| `string \| number`| Required
height| Source editor height| `string \| number`| Required
onSourceChange| A callback for when the content of the source editor changes|
`Function`| noop
onExit| A callback for when the source editor is closed| `Function`| noop
onParse| Allow for custom JSON parsing functions to be passed in| `Function`|
`JSON.parse`
onValidationError| A callback for custom handling of errors| `Function`|
`console.error`
validateDefinition| A custom validation function that gets run before
attempting to save the source| `Function`| noop
metadata| Metadata to add to telemetry events| `Object`|
displayToolbar| Show or hide the title and back button| `boolean`| true

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

##

Show code

### Dashboard Title

Copy

* * *

CloseApply

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

{

    "title": "Dashboard Title",

    "visualizations": {

        "table": {

            "title": "Table",

            "type": "splunk.table",

            "dataSources": {

                "primary": "search1"

            }

        },

        "bar": {

            "title": "Bar Chart",

            "type": "splunk.bar",

            "dataSources": {

                "primary": "search1"

            }

        },

        "column": {

            "title": "Column Chart",

            "type": "splunk.column",

            "dataSources": {

                "primary": "search1"

            }

        },

        "line": {

            "title": "Line Chart",

            "type": "splunk.line",

            "dataSources": {

                "primary": "search1"

            }

To pick up a draggable item, press the space bar. While dragging, use the
arrow keys to move the item. Press space again to drop the item in its new
position, or press escape to cancel.

There are many additional props available, please check the API tab.

### Add monaco-editor-webpack-plugin

 _**This step is required in order to make the editor work!**_

Monaco requires complex setup, which is handled by the monaco-editor-webpack-
plugin. Here's an example of the `webpack.config.js` file:



    const MonacoWebpackPlugin = require('monaco-editor-webpack-plugin');

    module.exports = {
        // ... your other webpack settings ...
        module: {
            rules: [
                {
                    test: /\.css$/,
                    use: ['style-loader', 'css-loader'],
                },
                {
                    test: /\.ttf$/,
                    use: ['file-loader'],
                },
            ],
        },
        plugins: [new MonacoWebpackPlugin()],
    };

Here are some helpful references if you run into issues:

  * [monaco-editor-webpack-plugin(Opens new window)](https://github.com/Microsoft/monaco-editor-webpack-plugin)
  * [monaco-editor(Opens new window)](https://github.com/microsoft/monaco-editor)
  * [react-monaco-editor(Opens new window)](https://github.com/react-monaco-editor/react-monaco-editor)

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Splunksavedsearch`

# Splunk saved search

`SplunkSavedSearch` is a data source that can run saved searches on Splunk
Enterprise.

Guide

Options

API

To call a report or saved search you must use the **ref** property. When using
**ref** you must reference a saved search or report by its exact name.

## Calling a report or saved search with the ref property



    {
     "type": "ds.savedSearch",
     "options": {
      "ref": "Top 100 sourcetypes in the last 24 hours"
     }
    }

Reports from other apps can be called using the **app** property. Additionally
**refresh** and **refreshType** can be used for searches that are not
scheduled searches

## ds.savedSearch options



    {
     "type": "ds.savedSearch",
     "options": {
      "ref": "Current Time",
      "app": "my-app",
      "refresh": "5s",
      "refreshType": "interval"
     }
    }

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Splunksearch`

# Splunk search

`SplunkSearch` is a data source that can run searches on Splunk Enterprise.

Guide

Options

API

To run a basic search, provide **query** string and time range in the
definition.

## Search for data from last 24 hours



    {
     "type": "ds.search",
     "options": {
      "query": "index=_internal | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now"
      }
     }
    }

Searches can be configured to automatically re-run, use **refresh** to specify
refresh interval, and use **refreshType** to control when you want the refresh
to happen.

## Rerun the search 30 seconds after the search completes



    {
     "type": "ds.search",
     "options": {
      "query": "index=_internal | stats count()",
      "queryParameters": {
       "earliest": "-24h",
       "latest": "now"
      },
      "refresh": "30s",
      "refreshType": "delay"
     }
    }

---

## @splunk/dashboard-docs - 29.1.0

**Package:** `dashboard-docs` | **Component:** `Switchtotab`

## SwitchToTab interaction

`SwitchToTab` is included in default presets provided by the dashboard
framework. This event handler allows a user to change to another active tab
when a click event occurs.

Example:



    "eventHandlers": [
        {
            "type": "drilldown.switchToTab",
            "options": {
                "tabId": "layout_1234"
            }
        }
    ],

### Valid events

`SwitchToTab` will only trigger for event types fired by its target which end
in `.click`. The set of events that will trigger switching tabs can be further
filtered using an `events` array, a `fields` array, or both in the event
handler options. For example, to trigger only when clicking on the
`sourcetype` or `count` fields in the visualization legend, use the following.
Please see the visualization documentation for more information about the set
of events fired by visualizations.



    "eventHandlers": [
        {
            "type": "drilldown.switchToTab",
            "options": {
                "events": ["legend.click"],
                "fields": ["sourcetype", "count"],
                "tabId": "layout_1234"
            }
        }
    ],

---

## @splunk/moment - 0.7.0

**Package:** `moment` | **Component:** `ChangeLog`

# Change Log

## 0.7.0 - February 6, 2024

  * Upgrade `splunk-utils` dependency to `^3.0.0`.

## 0.6.1 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 0.6.0 - February 4, 2021

  * Upgrade `splunk-utils` dependency to `^2.0.0`.

## 0.5.2 - February 5, 2020

  * Fixed a bug when parsing some timezones from Windows servers (SUI-2030).

## 0.5.1 - October 14, 2019

  * Relicensed to `Apache-2.0`.

## 0.5.0 - August 19, 2019

New Features:

  * Support for moment's `strict` mode in `newSplunkTime` (SUI-1874).

## 0.4.0 - September 13, 2018

  * Relicensed to `Splunk Software License Agreement`.

---

## @splunk/moment - 0.7.0

**Package:** `moment` | **Component:** `Convert`

# Moment Plugins

Depends on splunkweb

A utility for converting a Splunk Serialized Timezone to Moment's [Unpacked
Timezone Format](http://momentjs.com/timezone/docs/#/data-formats/unpacked-
format/).



    import convertSplunkTimezone from '@splunk/moment/convertSplunkTimezone';


### convertSplunkTimezone(timezone, name)

This function has no dependecies on Moment, so it's possible to use Moment's
Unpacked Format as a more easily read and more portable alternative to
Splunk's Serialized Timezone Format.

timezone

A timezone in Splunk's Serialized Timezone Format 1.0.

Type| string
---|---
Required| Yes

name

An identifier for the time zone, such as America/Los_Angeles or +6:00, but may
be set to a guid or most any other string that does not contain a slash.

Type| string
---|---
Required| Yes

returns

A timezone in Moment's [Unpacked
Format](http://momentjs.com/timezone/docs/#/data-formats/unpacked-format/).

Type| object
---|---

---

## @splunk/moment - 0.7.0

**Package:** `moment` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@splunk/splunk-utils| 3.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/ui-utils| 1.6.0| Apache-2.0| Splunk Inc.| Unknown
lodash| 4.17.21| MIT| [John-David Dalton](https://lodash.com/)|
<https://github.com/lodash/lodash.git>

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/cli| 7.10.1| MIT| [Sebastian McKenzie](https://babeljs.io/)|
<https://github.com/babel/babel.git>
@babel/core| 7.19.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@splunk/babel-preset| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/eslint-config| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/webpack-configs| 7.0.2| Apache-2.0| Splunk Inc.| Unknown
babel-eslint| 10.1.0| MIT| [Sebastian
McKenzie](https://github.com/babel/babel-eslint)|
<https://github.com/babel/babel-eslint.git>
babel-loader| 8.3.0| MIT| [Luis Couto](https://github.com/babel/babel-loader)|
<https://github.com/babel/babel-loader.git>
babel-plugin-transform-imports| 2.0.0| ISC| [AMC
Theatres](https://bitbucket.org/amctheatres/babel-transform-imports)|
<https://bitbucket.org/amctheatres/babel-transform-imports.git>
chai| 3.5.0| MIT| [Jake Luer](http://chaijs.com/)|
<https://github.com/chaijs/chai>
cross-env| 6.0.3| MIT| [Kent C. Dodds](https://github.com/kentcdodds/cross-
env#readme)| <https://github.com/kentcdodds/cross-env.git>
eslint| 7.14.0| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 18.2.1| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 6.15.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-plugin-import| 2.22.1| MIT| [Ben
Mosher](https://github.com/benmosher/eslint-plugin-import)|
<https://github.com/benmosher/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.4.1| MIT| Ethan Cohen|
<https://github.com/evcohen/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.21.5| MIT| [Yannick
Croissant](https://github.com/yannickcr/eslint-plugin-react)|
<https://github.com/yannickcr/eslint-plugin-react>
eslint-plugin-react-hooks| 4.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
jest| 26.6.3| MIT| [Unknown](https://jestjs.io/)|
<https://github.com/facebook/jest>
jest-junit| 10.0.0| Apache-2.0| Jason Palmer| <https://github.com/jest-
community/jest-junit>
moment| 2.29.4| MIT| [Iskren Ivov Chernev](https://momentjs.com/)|
<https://github.com/moment/moment.git>
moment-timezone| 0.5.28| MIT| [Tim Wood](http://momentjs.com/timezone/)|
<https://github.com/moment/moment-timezone.git>
webpack| 5.88.2| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 5.1.4| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 4.15.1| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server>
webpack-merge| 5.9.0| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

---

## @splunk/moment - 0.7.0

**Package:** `moment` | **Component:** `Usage`

# Moment Plugins

Depends on splunkweb

### moment#splunkFormat(format)

This works similarly to moment().format(), but adds several new formats with
seconds and milliseconds. Other formats are passed through to
moment().format();



    moment.newSplunkTime().splunkFormat('LTMS'); // 1:43:06.132 PM
    moment.newSplunkTime().splunkFormat('ls');   // 8/9/2017 1:43:06 PM',
    moment.newSplunkTime().splunkFormat('lms');  // 8/9/2017 1:43:06.132 PM',
    moment.newSplunkTime().splunkFormat('lls');  // Aug 9, 2017 1:43:06 PM',
    moment.newSplunkTime().splunkFormat('llms'); // Aug 9, 2017 1:43:06.132 PM',
    moment.newSplunkTime().splunkFormat('LLS');  // August 9, 2017 1:43:06 PM',
    moment.newSplunkTime().splunkFormat('LLMS'); // August 9, 2017 1:43:06.132 PM',


Only Splunk Enterprise server locales are supported:



    de_DE, en_GB, en_US, fr_FR, it_IT, ja_JP, ko_KR, zh_CN, zh_TW


format

Type| string
---|---
Required| Yes

returns

The formatted time.

Type| string
---|---

### moment.newSplunkTime([options])

A shortcut for creating moment instances with the Splunk Enterprise locale and
timezone. Either window.$C must be set on the page, or
moment.setDefaultSplunkTimezone() must have been called.



    // now in server timezone and locale
    moment.newSplunkTime();
    // epoch in server timezone and locale
    moment.newSplunkTime({time: 1490500800});
    // parse date using the short date format for the current locale
    moment.newSplunkTime({time: '10/10/2017', format: 'l'});
    // parse date using the short date format for Germany
    moment.newSplunkTime({time: '10/10/2017', format: 'l', locale: 'de_DE'});
    // parse date using strict mode which results in an invalid date
    moment.newSplunkTime({time: '10/10/2017', format: 'YYYY/MM/DD', strict: true})
    // parse date without strict mode which results in a valid date
    moment.newSplunkTime({time: '10/10/2017', format: 'MM/DD/YYYY'})


options

An object to configure date creation and parsing properties.

Type| Object
---|---
Required| No

options.time

The date information passed to moment.

Type| String, Number, Array.<Number>, Object, Date, Moment
---|---
Required| No

options.format

Date formats passed to moment.

Type| String, Array.<String>
---|---
Required| No

options.locale

Defaults to the server locale when available. Otherwise, defaults to moment's
default locale.

Type| String
---|---
Required| No

options.strict

Controls moment's strict mode.

Type| Boolean
---|---
Default| false
Required| No

returns

A `moment` instance with the locale and timezone set.

Type| Object
---|---

### moment.addSplunkTimezone(timezone, [name])

Add a timezone using Splunk's Serialized Timezone Format 1.0.

timezone

A timezone in Splunk's Serialized Timezone Format 1.0.

Type| string
---|---
Required| Yes

name

Defaults to a generated guid to avoid name conflicts.

Type| string
---|---
Required| No

returns

The `name` parameter or the generated guid.

Type| string
---|---

### moment.setDefaultSplunkTimezone(timezone)

Sets the default timezone for newSplunkTime() and return's the name of the
time zone. This function is memoized, so it is safe to call multiple times
with the same timezone data.

timezone

A timezone in Splunk's Serialized Timezone Format 1.0.

Type| string
---|---
Required| Yes

returns

The name of the server timezone. Since this information is not available, the
function generates a guid which is returned as the name, which can be useful
for later use with moment-timezone.

Type| string
---|---

### moment.getDefaultSplunkTimezone()

Get the default timezone name. This may be useful should you need to convert
one timezone to another.

returns

The name of the server timezone.

Type| string
---|---

---

## @splunk/react-events-viewer - 28.1.0

**Package:** `react-events-viewer` | **Component:** `EventsViewer`

# EventsViewer

This is a re-implementation of the EventsViewer from Splunk Enterprise as a
React Component

[Examples](?section=examples)[API](?section=develop)[Test
Hooks](?section=test)

#### Element Selectors

#### EventsViewer

workflow-components:EventsViewer

The root of the EventsViewer component.

Example:| [data-test="workflow-components:EventsViewer"]
---|---
Attribute:| data-test
Value:| workflow-components:EventsViewer
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

#### ConfigurationPanel

workflow-components:ConfigurationPanel

The root of the ConfigurationPanel component.

Example:| [data-test="workflow-components:ConfigurationPanel"]
---|---
Attribute:| data-test
Value:| workflow-components:ConfigurationPanel
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

table-style-selector-button

The toggle for the table style selector dropdown.

Example:| [data-test="table-style-selector-button"]
---|---
Attribute:| data-test
Value:| table-style-selector-button
Scope Describes where to look for the element.:| In the root of the
`ConfigurationPanel`

table-style-selector-dropdown

The dropdown for selecting a table style.

Example:| [data-test="table-style-selector-dropdown"]
---|---
Attribute:| data-test
Value:| table-style-selector-dropdown
Scope Describes where to look for the element.:|

#### PageLengthSelector

workflow-components:PageLengthSelector

The root of the PageLengthSelector component

Example:| [data-test="workflow-components:PageLengthSelector"]
---|---
Attribute:| data-test
Value:| workflow-components:PageLengthSelector
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

pagination-dropdown

The dropdown for selecting page lengths

Example:| [data-test="pagination-dropdown"]
---|---
Attribute:| data-test
Value:| pagination-dropdown
Scope Describes where to look for the element.:| Child of the
PageLengthSelector

#### List

workflow-components:List

The root of the List component

Example:| [data-test="workflow-components:List"]
---|---
Attribute:| data-test
Value:| workflow-components:List
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

#### Raw

workflow-components:Raw

The root of the Raw component

Example:| [data-test="workflow-components:Raw"]
---|---
Attribute:| data-test
Value:| workflow-components:Raw
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

#### RowExpander

workflow-components:RowExpander

Root of the RowExpander

Example:| [data-test="workflow-components:RowExpander"]
---|---
Attribute:| data-test
Value:| workflow-components:RowExpander
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

event-actions-dropdown

Event action dropdown inside an expanded row

Example:| [data-test="event-actions-dropdown"]
---|---
Attribute:| data-test
Value:| event-actions-dropdown
Scope Describes where to look for the element.:| Child of the RowExpander

#### Table Cell Syntax Highlighting

highlight-syntax-button

Highlight syntax as Json button

Example:| [data-test="highlight-syntax-button"]
---|---
Attribute:| data-test
Value:| highlight-syntax-button
Scope Describes where to look for the element.:| Child of a Cell

show-raw-text-button

Show raw text button

Example:| [data-test="show-raw-text-button"]
---|---
Attribute:| data-test
Value:| show-raw-text-button
Scope Describes where to look for the element.:| Child of a Cell

#### Format

table-formatter-button

Format button

Example:| [data-test="table-formatter-button"]
---|---
Attribute:| data-test
Value:| table-formatter-button
Scope Describes where to look for the element.:| This is the root element of
the component. This selector should be used to scope selectors for elements
within the component and to access the state attributes. The root selector can
be overriden, and often should be, to uniquely identify a component.

table-format-menu

Menu for the formatting options

Example:| [data-test="table-format-menu"]
---|---
Attribute:| data-test
Value:| table-format-menu
Scope Describes where to look for the element.:| Child of the Format popover

rowNumbers

Checkbox for the Row Numbers menu option

Example:| [data-test="table-format-menu"] [data-test="rowNumbers"]
---|---
Attribute:| data-test
Value:| rowNumbers
Scope Describes where to look for the element.:| Child of the format menu

wrapResults

Checkbox for the Wrap Results menu option

Example:| [data-test="table-format-menu"] [data-test="wrapResults"]
---|---
Attribute:| data-test
Value:| wrapResults
Scope Describes where to look for the element.:| Child of the format menu

---

## @splunk/react-icons - 5.3.0

**Package:** `react-icons` | **Component:** `ChangeLog`

# Change Log

## 5.3.0 - September 2, 2025

New Features:

  * Added new icons (SUI-8152):
    * ArrowsDoubleLeftRight
    * ArrowsFourRightLeftUpDown
    * ShoppingCart
    * WallBricks

Bug Fixes:

  * Fixes `Calculation` icon size in filled variant (SUI-8152).

## 5.2.0 - August 5, 2025

New Features:

  * Added new icons (SUI-8027):
    * ChartColumnIcicle
    * ChartColumnMagnifier
    * CursorArrowClicking
    * FingerPointClicking
    * NodeBranchCog
    * NotePortrait
    * ReportDouble

Bug Fixes:

  * Renamed `Index` icon name to `SingleIndex` to avoid naming conflicts with Typescript declaration files (SUI-8046).

## 5.1.0 - July 2, 2025

New Features:

  * Added new icons (SUI-7923):
    * AsteriskCircle
    * CrossHexagon
    * DotsThreeCircle
    * InformationSerifSquare
    * TildeCircle

## 5.0.0 - June 3, 2025

  * Includes all changes from `5.0.0-beta` and `5.0.0-rc` releases.

New Features:

  * Added new icons (SUI-7824):
    * MonitorArrowInwardRight
    * NodeSplitHorizontal

## 5.0.0-rc.2 - May 28, 2025

  * Release candidate 2.

## 5.0.0-rc.1 - May 14, 2025

  * Release candidate 1.

## 5.0.0-beta.5 - May 7, 2025

  * Includes changes from `4.14.0`.

## 4.14.0 - May 6, 2025

New Features:

  * Added new icons (SUI-7721):
    * Certification
    * ChartGaugeLevelMarker
    * License
    * LicenseCog
    * MonitorArrowUp
    * NewSquare
    * ServerLicense

## 5.0.0-beta.4 - April 22, 2025

API Changes:

  * `typescript` version is now `^5.8.3` (SUI-7601).

## 5.0.0-beta.3 - April 2, 2025

  * Includes changes from `4.13.0`.

## 4.13.0 - April 1, 2025

New Features:

  * Added new icons (SUI-7516):
    * DonutPie
    * DonutPie25
    * DonutPie50
    * DonutPie75
    * LevelGauge14
    * LevelGauge24
    * LevelGauge34
    * LevelGauge44
    * MonitorArrow
    * PipeS
    * SignalAntenna
    * SignalColumns14
    * SignalColumns24
    * SignalColumns34
    * SignalColumns44
    * TokenKey
    * WiFiSignal
    * WiFiSignalSlash

## 5.0.0-beta.2 - March 5, 2025

  * Public release of `5.0.0-beta.1` with changes from `4.12.0`

## 4.12.0 - March 4, 2025

New Features:

  * Added new icons (SUI-7298):
    * ArrowDownCircle
    * ArrowLeftCircle
    * ArrowRightCircle
    * ArrowUpCircle
    * CircleTiny
    * CounterCumulative
    * FileRipped
    * LayersDoubleTransparent
    * ListIndentedSquare

## 5.0.0-beta.1 - February 20, 2025

API Changes:

  * `react` and `react-dom` peer dependencies are now `"^16.8.0 || ^17.0.0 || ^18.0.0"`.

## 4.11.0 - February 5, 2025

New Features:

  * Added new `Keyboard` icon (SUI-7065)

## 4.10.0 - January 7, 2025

New Features:

  * Added new icons (SUI-6957):
    * ListToken
    * Token

## 4.9.0 - December 3, 2024

New Features:

  * Added new icons (SUI-6884):
    * CalendarClock
    * CylinderIndexTable
    * DriveIndexTable
    * Index
    * NodesCentered
    * TableIndex

Bug Fixes:

  * Fixes `DriveArrowOutside` icon default variant: now defaults to "outlined" instead of "filled" (SUI-6884).

## 4.8.0 - October 1, 2024

New Features:

  * Added new icons (SUI-6652):
    * ArrowBroadLeftRight
    * ArrowLeftRight
    * BatteryCharging
    * ButtonPulldown
    * CalendarArrowsLeftRight
    * ChartFlame
    * ChartIcicle
    * ChevronBroadRight
    * ChevronBroadRightDashed
    * CircleDashed
    * CylinderDashed
    * Drive
    * DriveArrowInside
    * DriveArrowOutside
    * Earth
    * Fire
    * GamePad
    * MapUS
    * Odometer
    * PacketLoss
    * ParallelDotsHorizontal
    * PhoneReceiverAngled
    * PhoneReceiverAngledExclamationTriangle
    * PhoneReceiverAngledHourglass
    * PhoneReceiverAngledSlashed
    * PingPongPaddleRacket
    * RobotArm
    * ShieldKeyhole
    * ShieldSeparated
    * SpeakerSlashed
    * SpeakerSound
    * Stamp
    * StarEightPoints
    * StopwatchArrowRightLatency
    * SwordsCross
    * TerminalConsole
    * TrophyCup

## 4.7.0 - August 20, 2024

New Features:

  * Added new icons (SUI-6478):
    * ButtonsPulldown
    * EyeCheckmark
    * GiftBox
    * Scope
    * WeightingScale

## 4.6.0 - July 8, 2024

New Features:

  * Added new icons (SUI-6323):
    * ListNumbered
    * QuotationDouble
    * TextBBold
    * TextH
    * TextIItalic
    * TextSStrikethrough
    * TextUUnderline

## 4.5.0 - June 4, 2024

New Features:

  * Added new icons (SUI-6270):
    * Calculation
    * Calculator
    * CylinderWaves
    * DeviceEdgeHub
    * ExclamationTriangleDown
    * FileChevronRight
    * Shield
    * TextAlignBottom
    * TextAlignCenter
    * TextAlignLeft
    * TextAlignRight
    * TextAlignTop
    * TextAlignVerticalCenter
    * TriangleDown
    * WindowGlobe

## 4.4.0 - April 2, 2024

New Features:

  * Added new icons (SUI-6001):
    * ChainSlashed
    * CircleSmall
    * ControlFastForward
    * ControlNext
    * ControlPrevious
    * ControlRewind
    * ControlStopCircle

## 4.3.0 - Feb 21, 2024

New Features:

  * Added new icons (SUI-6001):
    * FileChevrons
    * FileZipped
    * PlusSquare
    * TagMarkerRight

## 4.2.0 - Dec 5, 2023

New Features:

  * Added the `StarSparklesDouble` icon (SUI-5904)

## 4.1.0 - Nov 7, 2023

New Features:

  * Added new icons:
    * BoxCardboard
    * BullsEye
    * CalendarArrowDownFilled
    * Cube
    * CylinderSquareCorners
    * IdentityCard
    * Observatory
    * RobotAgentMagnifier
    * Snowflake
    * TriangleRuler

## 4.0.2 - September 5, 2023

Bug Fixes:

  * Fixes `ChartScatter` icon name typo: renamed "ChartScatters" to "ChartScatter" (SUI-5602).

## 4.0.1 - June 6, 2023

Bug Fixes:

  * Corrected misspelling for `PunchCard`, updated `CylinderPie` to have filled and outlined styles, removed incorrectly added `FillFalse` and `FillTrue` icons (SUI-5528).
  * Icons no longer receive focus when clicked (SUI-5573).
  * Icon styling specificity reduced to allow for easier overriding of the `fill` attribute.

API Changes:

  * Added support for the latest `styled-components@5` (SUI-5467).

## 4.0.0 - May 10, 2023

New Features:

  * Added 400+ new icons designed for Prisma themes
  * Simplified icon API - most custom props have been removed and icons can be styled using standard `svg` attributes.

API Changes:

  * Many API changes have been made in this major version. See MIGRATION.md for details on how to migrate.
  * All Enterprise icons were moved from the package root to the `enterprise` directory.
    * Migrating projects should replace all `@splunk/react-icons/[...]` imports with `@splunk/react-icons/enterprise/[...]`, with the exception of `@splunk/react-icons/SVG` (see below).
    * Projects that use the Prisma design system can optionally switch to the newly added Prisma icons.
    * Note: Not every Enterprise icon has a Prisma equivalent, and icon names differ between themes.
  * The `SVG` component has updated to support the new API.
    * The previous `SVG` component has been renamed to `SVGEnterprise`.
    * Migrating projects should replace all `import SVG from @splunk/react-icons/SVG` with `import SVGEnterprise from @splunk/react-icons/SVGEnterprise`.
  * Icons now have a `tabIndex="-1"` by default and are properly `aria-hidden` in the accessibility tree.
  * Added `IconProvider` component with an experimental feature for boosting performance of multiple icon renders of the same icon component and variant.

## 3.3.1 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 3.3.0 - November 1, 2022

New Features:

  * Added `Monitor`, `NetworkDevice`, `Target` and `ZoomReset` icons.

## 3.2.0 - April 5, 2022

New Features:

  * Added `DistributionStream` and `Tool` icons.

API Changes:

  * Pinned `styled-components@5.1.1` to avoid breaking changes introduced in `styled-components@5.2.0`.

**`@splunk/react-icons` is incompatible with styled-components version(s)
`^5.2.0`**.

`styled-components@5.2.0` changed how selectors like `& + &` are compiled;
[styled-components PR#3236](https://github.com/styled-components/styled-
components/pull/3236). This breaks styles that worked in previous versions of
styled-components; [styled-components issue #3265](https://github.com/styled-
components/styled-components/issues/3265).

**Until noted otherwise in a future release of`@splunk/react-icons` do not use
`styled-components@^5.2.0` with` @splunk/react-icons`**.

## 3.1.0 - May 6, 2021

New Features:

  * Support for Typescript.

## 3.0.1 - August 31, 2020

Bug Fixes:

  * Improved accessibility when `hideDefaultTooltip` is enabled (SUI-2105).

## 3.0.0 - July 7, 2020

New Features:

  * Support for `styled-components@^5`.

Bug Fixes:

  * Fixed a visual issue on Safari (SUI-1587).

API Changes:

  * The `react` and `react-dom` peer dependencies are now `^16.8`.
  * The `styled-components` peer dependency is now `^5.1`.

## 2.6.2 - May 1, 2020

Bug Fixes:

  * Removed implicit dependency on `@splunk/react-ui`.

## 2.6.1 - October 14, 2019

  * Relicensed to `Apache-2.0`.

## 2.6.0 - October 8, 2019

New Features:

  * New component `SVG` for creating icons with the same interface as this library.

## 2.5.0 - February 22, 2019

New Features:

  * Support for `styled-components@^4`.

## 2.4.0 - January 29, 2019

  * Added `Rollup` icon.

## 2.3.0 - January 2, 2019

  * Icons now support a `hideDefaultTooltip` prop (SUI-1570).
  * Added `Filter`, `RefreshLight`, `RotateCounterLight`, `RotateLight`, `FullscreenLight`, `FullscreenExitLight`, `TextLight`, `Connection`, `DataSource`, `Inputs`, `Line`, `Shapes` and `ChartBasic` icons (APPLAT-4153).

## 2.2.0 - December 6, 2018

  * Added `MinusCircle` icon (SUI-1513).

## 2.1.0 - November 15, 2018

  * Added `Images`, `Icons` icons (APPLAT-3395).
  * Added `FitToView`, `GearUnfilled`, `MultiShare`, `Pan`, `Save`, `Select`, `ZoomIn`, `ZoomOut` icons (APPLAT-3487).

## 2.0.0 - September 13, 2018

  * `styled-components` is now a peer dependency.
  * Relicensed to `Splunk Software License Agreement`.

## 1.3.0 - June 30, 2018

  * Added `SplitBy` icon (SUI-1394).

## 1.2.0 - March 20, 2018

  * Added `Globe`, `Tree` and `Upload` icons (SUI-1369).

## 1.1.0 - February 5, 2018

New Features:

  * Added `More` and `More Vertical` icons (SUI-1346).

## 1.0.0 - January 4, 2018

  * Modified `Info`, `InfoCircle`, `Warning`, `Error`, `Sort`, `SortUp` and `SortedDown` icons (SUI-1298).

---

## @splunk/react-icons - 5.3.0

**Package:** `react-icons` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@splunk/ui-utils| 1.10.0| Apache-2.0| Splunk Inc.| Unknown
lodash| 4.17.21| MIT| [John-David Dalton](https://lodash.com/)|
<https://github.com/lodash/lodash.git>
prop-types| 15.8.1| MIT| [Unknown](https://facebook.github.io/react/)|
<https://github.com/facebook/prop-types.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/core| 7.28.0| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@babel/plugin-transform-runtime| 7.28.0| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-plugin-transform-runtime)|
<https://github.com/babel/babel.git>
@splunk/babel-preset| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/eslint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/stylelint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/webpack-configs| 7.0.2| Apache-2.0| Splunk Inc.| Unknown
@storybook/csf-tools| 7.6.20| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/lib/csf-
tools)| <https://github.com/storybookjs/storybook.git>
@storybook/manager-api| 7.6.20| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/lib/manager-
api)| <https://github.com/storybookjs/storybook.git>
@storybook/react-webpack5| 7.6.20| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/frameworks/react-
webpack5)| <https://github.com/storybookjs/storybook.git>
@storybook/test-runner| 0.16.0| MIT| shilman|
<https://github.com/storybookjs/test-runner>
@testing-library/user-event| 14.6.1| MIT| [Giorgio
Polvara](https://github.com/testing-library/user-event#readme)|
<https://github.com/testing-library/user-event>
@types/fs-extra| 9.0.13| MIT|
[Unknown](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/fs-
extra)| <https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@types/jest| 29.5.14| MIT|
[Unknown](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest)|
<https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@types/lodash| 4.17.16| MIT|
[Unknown](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/lodash)|
<https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@types/react| 18.2.14| MIT|
[Unknown](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react)|
<https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@types/react-dom| 18.2.6| MIT|
[Unknown](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react-
dom)| <https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@types/styled-components| 5.1.0| MIT| Unknown|
<https://github.com/DefinitelyTyped/DefinitelyTyped.git>
@typescript-eslint/eslint-plugin| 8.29.1| MIT| [Unknown](https://typescript-
eslint.io/packages/eslint-plugin)| <https://github.com/typescript-
eslint/typescript-eslint.git>
@typescript-eslint/parser| 8.29.1| MIT| [Unknown](https://typescript-
eslint.io/packages/parser)| <https://github.com/typescript-eslint/typescript-
eslint.git>
babel-loader| 8.3.0| MIT| [Luis Couto](https://github.com/babel/babel-loader)|
<https://github.com/babel/babel-loader.git>
babel-plugin-styled-components| 1.10.7| MIT| Unknown|
<https://github.com/styled-components/babel-plugin-styled-components.git>
babel-plugin-transform-imports| 2.0.0| ISC| [AMC
Theatres](https://bitbucket.org/amctheatres/babel-transform-imports)|
<https://bitbucket.org/amctheatres/babel-transform-imports.git>
babel-plugin-transform-require-context| 0.1.1| MIT| Aliaksei Sapach|
<https://github.com/asapach/babel-plugin-transform-require-context.git>
cross-env| 6.0.3| MIT| [Kent C. Dodds](https://github.com/kentcdodds/cross-
env#readme)| <https://github.com/kentcdodds/cross-env.git>
eslint| 8.57.1| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 19.0.4| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 9.1.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-import-resolver-webpack| 0.13.7| MIT| [Ben
Mosher](https://github.com/import-js/eslint-plugin-
import/tree/HEAD/resolvers/webpack)| <git+https://github.com/import-js/eslint-
plugin-import.git>
eslint-plugin-import| 2.31.0| MIT| [Ben Mosher](https://github.com/import-
js/eslint-plugin-import)| <https://github.com/import-js/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.10.0| MIT| Ethan Cohen| <https://github.com/jsx-
eslint/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.37.1| MIT| [Yannick Croissant](https://github.com/jsx-
eslint/eslint-plugin-react)| <https://github.com/jsx-eslint/eslint-plugin-
react>
eslint-plugin-react-hooks| 4.6.2| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
figma-js| 1.16.1-0| MIT| Unknown| <https://github.com/jemgold/figma-js>
jest| 29.7.0| MIT| [Unknown](https://jestjs.io/)|
<https://github.com/jestjs/jest.git>
jest-environment-jsdom| 29.7.0| MIT| Unknown|
<https://github.com/jestjs/jest.git>
jest-image-snapshot| 5.1.0| Apache-2.0| [Andres
Escobar](https://github.com/anescobar1991)|
<https://github.com/americanexpress/jest-image-snapshot.git>
jest-stare| 2.4.1| MIT| dan kelosky| <https://github.com/dkelosky/jest-stare>
playwright| 1.46.0| Apache-2.0| [Microsoft
Corporation](https://playwright.dev/)|
<git+https://github.com/microsoft/playwright.git>
react| 18.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
react-dom| 18.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
regenerator-runtime| 0.13.11| MIT| Ben Newman|
<https://github.com/facebook/regenerator/tree/main/packages/runtime>
storybook| 7.6.20| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/lib/cli)|
<https://github.com/storybookjs/storybook.git>
styled-components| 5.3.10| MIT| [Glen Maddern](https://styled-
components.com/)| <git+https://github.com/styled-components/styled-
components.git>
stylelint| 15.11.0| MIT| [stylelint](https://stylelint.io/)|
<https://github.com/stylelint/stylelint.git>
svgo| 3.0.2| MIT| [Kir Belevich](https://github.com/svg/svgo)|
<git://github.com/svg/svgo.git>
typescript| 5.8.3| Apache-2.0| [Microsoft
Corp.](https://www.typescriptlang.org/)|
<https://github.com/microsoft/TypeScript.git>
webpack| 5.91.0| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 5.1.4| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 5.2.2| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server>
webpack-merge| 5.9.0| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

---

## @splunk/react-icons - 5.3.0

**Package:** `react-icons` | **Component:** `Migration`

# Migration

This document lists migration guidance for new features and breaking changes.

## v3 to v4

`@splunk/react-icons@4.0.0` brings new outline and fill modes, improved
accessibility, and more than 400 newly designed icons. Check out the docs to
explore these new features and the redesigned icon library page.

When migrating from `@splunk/react-icons@3.x` to `@splunk/react-icons@4.0.0`
there are two options: continue to use the Enterprise icons or migrate to the
new icons.

### Enterprise icons

To continue using the Enterprise icons the only thing that has changed is the
icons’ import location which is now from an `enterprise` directory.

The following code in 3.x:



    import External from ‘@splunk/react-icons/External’;

should be changed to:



    import External from’@splunk/react-icons/enterprise/External’;

And that’s it! The API of these icons have remained unchanged, so although
this is a major version upgrade, it is backwards compatible, and you can
continue to use icons in the same way after updating the import path.

In most cases, you may be able to safely find and replace ’@splunk/react-
icons/’ with ‘@splunk/react-icons/enterprise/’

### Migrating to the new Icons

When adopting new icons, there are a few changes to the API that must be
considered.

#### Accessibility

In version 3.x icons had default labels and enabled the browser tooltip. This
meant there were icons that were visually the same but shipped as a separate
icon to have a different label: e.g. Close and Cancel.

In version 4.x icons are now decorative by default; meaning they do not have
labels or interactivity. Migrating will require deciding if the icon is
functional or decorative so the correct accessibility attributes can be used.
See below how to migrate a Button in both of these scenarios or check the docs
for examples on how to use icons in an accessible way.

##### Migrating a decorative icon

If previously you had a react-ui Button with a decorative icon it may have
looked like:



    import Button from '@splunk/react-ui/Button';
    import Print from '@splunk/react-icons/Print';

    const MyButton = () => {
    return (<Button icon={<Print screenReaderText={null} />} label="Print" />);
    }

In v4 there is no default accessible name added to the icon. The
screenReaderText prop has been removed for this reason. Migrated code should
look like this:



    import Button from '@splunk/react-ui/Button';
    import Printer from '@splunk/react-icons/Printer';

    const MyButton = () => {
        return (
            <Button icon={<Printer />} label="Print" />
        );
    }

##### Migrating a functional icon

If the icon instead is functional and needs an accessible name it may have
looked like:



    import Button from '@splunk/react-ui/Button';
    import Print from '@splunk/react-icons/Print';

    const MyButton = () => {
        return (
            <Button icon={<Print />} />
        );
    }

This relied on the icon to provide the accessible name by default. Now that
icons are decorative by default the migrated could should look like this:



    import Button from '@splunk/react-ui/Button';
    import Printer from '@splunk/react-icons/Printer';

    const MyButton = () => {
        return (
            <Button icon={<Printer />} aria-label="Print" />
        );
    }

#### API

The API of icons and the underlying SVG component has been significantly
reduced in favor of passing through native SVG attributes.

The following attributes have been removed from the API but are passed through
as SVG attributes if needed: width, height, viewBox, and preserveAspectRatio.
If you relied on these attributes previously note that the behavior may have
changed as it is determined according to browser implementation.

##### `screenReaderText`

This prop has been removed in favor of native aria-* attributes or using
`ScreenReaderContent` from `@splunk/react-ui`

In v3 the prop may have been used like this:



    <External screenReaderText={'Open in new tab'} />

Which should be migrated to one of these options:



    // using aria-label
    <ArrowSquareTopRight aria-label="Open in new tab" aria-hidden="false" />


    // or a sibling ScreenReaderContent component
    <>
        <ArrowSquareTopRight />
        <ScreenReaderContent>(Opens new window)</ScreenReaderContent>
    </>

##### `size`

This prop has been removed. Instead pass width and height or use styled-
components to set the dimensions via CSS.

##### `hideDefaultTooltip`

This behavior has been removed. Browser tooltips are not added by default and
the icons source no longer contains `<title>` elements with text. Using a
Tooltip from react-ui is preferred to give a label on hover. In cases where
the native tooltip is still desired, Icons accept children elements that are
inserted as nodes within the svg element:



    import ArrowSquareTopRightIcon from '@splunk/react-icons/ArrowSquareTopRight;

    <ArrowSquareTopRightIcon>
     <title>Open in window</title>
    </ArrowSquareTopRightIcon>

#### Mapping

Here are the mappings for commonly used icons from v3 to the new icon set in
v4:



    | react-icons v3 | react-icons v4            |
    |----------------|---------------------------|
    | Cancel         | Cross                     |
    | Close          | Cross                     |
    | Clear          | Cross                     |
    | Plus           | Plus                      |
    | Error          | ExclamationSquare, filled |
    | InfoCircle     | InformationCircle         |
    | ChevronRight   | ChevronRight              |
    | Success        | CheckCircle               |
    | Trash          | TrashCanCross             |
    | Warning        | ExclamationTriangle       |
    | ChevronDown    | ChevronDown               |
    | Pencil         | Pencil                    |
    | ChevronLeft    | ChevronLeft               |
    | Refresh        | ArrowsCircularDouble      |
    | MoreVertical   | DotsThreeVertical         |
    | Remove         | Cross                     |
    | Search         | Magnifier                 |

---

## @splunk/react-search - 7.0.1

**Package:** `react-search` | **Component:** `Bar`

# Search Bar

Search Bar is a react component that allows creating a search.

[Examples](?section=examples)[API](?section=develop)[Test
Hooks](?section=test)

#### Element Selectors

workflow-components:Search

Search component

Example:| [data-test="workflow-components:Search"]
---|---
Attribute:| data-test
Value:| workflow-components:Search
Scope Describes where to look for the element.:| The root search component div

search-button

Search button

Example:| [data-test="workflow-components:Search"] [data-test="search-button"]
---|---
Attribute:| data-test
Value:| search-button
Scope Describes where to look for the element.:| The search button

---

## @splunk/react-search - 7.0.1

**Package:** `react-search` | **Component:** `Changelog`

# Change Log

All notable changes to this project will be documented in this file. See
[Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## [7.0.1](https://cd.splunkdev.com/devplat/react-
search/compare/v7.0.0...v7.0.1) (2025-06-06)

**Note:** Version bump only for package @splunk/react-search

# 7.0.0 (2025-06-05)

Increased support range for React 16, 17, and 18. Updated to use SUI 5.

### Bug Fixes

  * **A11Y-302:** Add a way of overriding ARIA labels ([cd21445](https://cd.splunkdev.com/devplat/react-search/commits/cd214458c27ce44f821adbace2756560a7302c79))
  * **A11Y-302:** Fix missing default messages ([24748fb](https://cd.splunkdev.com/devplat/react-search/commits/24748fbe66dc66044b3c2bc25496c14185efb3a1))
  * **A11Y-302:** Improve way that ARIA attributes are handled ([a9b87e3](https://cd.splunkdev.com/devplat/react-search/commits/a9b87e3f75e4471b5f151ffc1b289369fb51233f))

### Features

  * **DEPS:** update to SUI 5 GA ([d54b2f3](https://cd.splunkdev.com/devplat/react-search/commits/d54b2f3eff8800058c92fa5bd8a1ae8984826249))
  * enable exposing typescript types for barrel rollup ([04bc29b](https://cd.splunkdev.com/devplat/react-search/commits/04bc29b2ceadb0c6c1c943b96b8e81c0fcbc12c9))

### Breaking changes

  * Uses SUI ^5.0.0
  * Requires @types/react as a peer dependency

## [6.0.0] - (2025-03-07)

No api changes in this release but given the rewrite to convert components to
Typescript the major version has been bumped out of an abundance of caution.

### Bug Fixes

  * **A11Y-302:** Add a way of overriding ARIA labels

### Features

  * Enable exposing typescript types for barrel rollup

## [5.0.0] - 2023-08-31

### Changed

  * Updated @splunk/react-ui to 4.19.0
  * Updated @splunk/themes to 0.16.1
  * Updated styled-components peerDependency to ^5.3.10
  * Upgraded ace-builds to 1.17.0 and enabled `enableKeyboardAccessibility` to allow tabbing over the ace-editor and escaping the editor's focus trap
  * [Breaking] The textareas in `Bar` and `Input` no longer receive focus when they mount onto the DOM
  * [Breaking] Pressing the `esc` key when the `Bar` and `Input` components have focus will escape the focus trap of the editor in addition to executing the `onEsc` callback
  * [Breaking] The value of the textarea for `Bar` and `Input` will always be the empty string until they receive focus

## [4.0.1] - 2021-10-06

### Changed

  * Updated `@splunk/react-time-range` component to 8.0.0

## [4.0.0] - 2021-09-21

### Changed

  * [Breaking] Relicensed to Apache-2.0

## [3.0.0] - 2021-02-19

### Changed

  * Upgraded to SUI 4.0 (PX-918)
  * [Breaking] Moved react-ui, react-icons and themes to direct dependencies
  * [Breaking] Removed the themes module
  * [Breaking] IE11 is no longer supported.

## [2.0.0] - 2020-07-24

### Changed

  * Updated following peer dependencies (SCP-25802)
  * [Breaking] react-ui: ^3
  * [Breaking] styled-components: ^5.1

### Fixed

  * Added missing dependency on `prop-types`

## [1.6.0] - 2020-06-12

### Changed

  * Updated `@splunk/react-time-range` component to 5.2.0

## [1.5.0] - 2020-06-09

### Changed

  * Updated `@splunk/react-time-range` component to 5.1.0

## [1.4.1] - 2020-06-04

### Changed

  * Updated `@splunk/react-time-range` component to 5.0.1

## [1.4.0] - 2020-05-27

### Fixed

  * Fixed exception when using advanced time in Bar (SCP-27128)

## [1.3.0] - 2020-05-21

### Changed

  * Updated `@splunk/react-time-range` component to v5.

## [1.2.0] - 2020-05-11

### Fixed

  * Changed the `Bar` component's use of `react-search/Dropdown` to use the default `appearance` (SCP-26766)

## [1.1.0] - 2020-04-08

### Changed

  * Moved the themes import to be consistent with other components so the import is now: `import { themes } from '@splunk/react-search/themes;`
  * Made the search bar have consistent border radiuses (SCP-25631)

## [1.0.0] - 2020-03-24

### Added

  * Added type definitions for Typescript consumers (SCP-22515)

### Changed

  * Updated react peer dependency to a minimum of 16.8 (SCP-24568)
  * Removed the need for a `theme` prop on the components by switching to use styled-components for theming (SCP-24571)

### Fixed

  * Marked user facing messages for localization (SCP-24092)

## [0.1.3] - 2019-10-07

### Fixed

  * Box sizing fix for `Search input bar`

## [0.1.2] – 2019-08-22

### Fixed

  * Placeholder bug for `Search input bar`

## [0.1.0] – 2018-09-20

### Changed

  * The `@splunk/react-ui` peer dependency is now `^2`.
  * The `react` and `react-dom` peer dependencies are now `^16.3`.
  * `styled-components` is now a peer dependency.
  * Relicensed to `Splunk Software License Agreement`.

## [0.0.1] – 2018-06-21

### Added

  * Search input bar
  * Timerange picker
  * Search button
  * Allow custom syntax in JSON formatted file
  * PropTypes to conform to the base viz api

---

## @splunk/react-search - 7.0.1

**Package:** `react-search` | **Component:** `Input`

# Input

Input is a react component that allows entering a search string.

[Examples](?section=examples)[API](?section=develop)[Test
Hooks](?section=test)

## Input

Show code



    1

    enter search here...





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    1

    enter search here...





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    1

    enter search here...





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    enter search here...





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    1

    enter search here...





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    1

    hello





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    1

    index=_audit | stats count() by host





    הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

---

## @splunk/react-search - 7.0.1

**Package:** `react-search` | **Component:** `Theming`

# Theming

The `@splunk/react-search` package supports theming via
[@splunk/themes](https://splunkui.splunk.com/Packages/themes/Overview) and
`styled-components`.

Themes are configured for your application by importing and configuring the
[SplunkThemeProvider](https://splunkui.splunk.com/Packages/themes/SplunkThemeProvider)
from `@splunk/themes`.

---

## @splunk/react-sparkline - 0.6.3

**Package:** `react-sparkline` | **Component:** `ChangeLog`

# Change Log

## 0.6.3 - June 6, 2023

API Changes:

  * Added support for the latest `styled-components@5` (SUI-5467).

## 0.6.2 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 0.6.1 - April 5, 2022

API Changes:

  * Pinned `styled-components@5.1.1` to avoid breaking changes introduced in `styled-components@5.2.0`.

**`@splunk/react-sparkline` is incompatible with styled-components version(s)
`^5.2.0`**.

`styled-components@5.2.0` changed how selectors like `& + &` are compiled;
[styled-components PR#3236](https://github.com/styled-components/styled-
components/pull/3236). This breaks styles that worked in previous versions of
styled-components; [styled-components issue #3265](https://github.com/styled-
components/styled-components/issues/3265).

**Until noted otherwise in a future release of`@splunk/react-sparkline` do not
use `styled-components@^5.2.0` with`@splunk/react-sparkline`**.

## 0.6.0 - February 4, 2021

API Changes:

  * Upgrade `react-ui` dependency to `^4.0.0`.

## 0.5.0 - July 7, 2020

New Features:

  * Support for `styled-components@^5`.
  * The `elementRef` prop now supports object refs (SUI-1910).

API Changes:

  * The `react` and `react-dom` peer dependencies are now `^16.8`.
  * The `styled-components` peer dependency is now `^5.1`.
  * `@splunk/react-ui` is no longer a peer dependency.

## 0.4.1 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 0.4.0 - February 22, 2019

New Features:

  * Support for `styled-components@^4`.

## 0.3.2 - N/A

Bug Fixes:

  * Fixed the `elementRef` prop.

Notes:

  * Was not published.

## 0.3.1 - October 29, 2018

Bug Fixes:

  * Now displays gaps in the data when data is `null` and `acceptNull` is false (APPLAT-2587).

## 0.3.0 - September 13, 2018

New Features:

  * Added ability to configure the length of the sparkline (by number of data points), and number of end dots to render.

API Changes:

  * `@splunk/react-ui` is now a peer dependency.
  * `styled-components` is now a peer dependency.
  * The `react` peer dependency is now `^16.3`.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

---

## @splunk/react-sparkline - 0.6.3

**Package:** `react-sparkline` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@splunk/react-ui| 4.17.1| Apache-2.0| Splunk Inc.| Unknown
@splunk/ui-utils| 1.6.0| Apache-2.0| Splunk Inc.| Unknown
lodash| 4.17.21| MIT| [John-David Dalton](https://lodash.com/)|
<https://github.com/lodash/lodash.git>
prop-types| 15.7.2| MIT| [Unknown](https://facebook.github.io/react/)|
<https://github.com/facebook/prop-types.git>

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/core| 7.19.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@cypress/react| 5.12.4| MIT| [Gleb Bahmutov](https://github.com/cypress-
io/cypress/blob/master/npm/react/#readme)| <https://github.com/cypress-
io/cypress.git>
@cypress/webpack-dev-server| 1.8.2| MIT| [Unknown](https://github.com/cypress-
io/cypress/tree/master/npm/webpack-dev-server#readme)|
<https://github.com/cypress-io/cypress.git>
@splunk/babel-preset| 3.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/cicd-tools| 0.5.0| UNLICENSED| Splunk|
<https://git.splunk.com/scm/ui/workflow-components.git>
@splunk/eslint-config| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/stylelint-config| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/webpack-configs| 6.0.0| Apache-2.0| Splunk Inc.| Unknown
@storybook/addon-a11y| 6.5.9| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/main/addons/a11y)|
<https://github.com/storybookjs/storybook.git>
@storybook/addon-essentials| 6.5.9| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/main/addons/essentials)|
<https://github.com/storybookjs/storybook.git>
@storybook/addon-interactions| 6.5.9| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/main/addons/interactions)|
<https://github.com/storybookjs/storybook.git>
@storybook/csf| 0.0.1| MIT| [Unknown](https://github.com/storybookjs/csf)|
<https://github.com/storybookjs/csf.git>
@storybook/react| 6.5.9| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/main/app/react)|
<https://github.com/storybookjs/storybook.git>
@storybook/testing-react| 1.3.0| MIT| yannbf@gmail.com|
<https://github.com/storybookjs/testing-react>
@testing-library/jest-dom| 5.16.1| MIT| [Ernesto
Garcia](https://github.com/testing-library/jest-dom#readme)|
<https://github.com/testing-library/jest-dom>
@testing-library/react| 12.1.2| MIT| [Kent C.
Dodds](https://github.com/testing-library/react-testing-library#readme)|
<https://github.com/testing-library/react-testing-library>
babel-eslint| 10.1.0| MIT| [Sebastian
McKenzie](https://github.com/babel/babel-eslint)|
<https://github.com/babel/babel-eslint.git>
babel-loader| 8.2.5| MIT| [Luis Couto](https://github.com/babel/babel-loader)|
<https://github.com/babel/babel-loader.git>
babel-plugin-istanbul| 5.2.0| BSD-3-Clause| [Thai Pangsakulyanont
@dtinth](https://github.com/istanbuljs/babel-plugin-istanbul#readme)|
<git+https://github.com/istanbuljs/babel-plugin-istanbul.git>
babel-plugin-transform-imports| 2.0.0| ISC| [AMC
Theatres](https://bitbucket.org/amctheatres/babel-transform-imports)|
<https://bitbucket.org/amctheatres/babel-transform-imports.git>
core-js| 3.12.1| MIT| Unknown| <https://github.com/zloirock/core-js.git>
cross-env| 6.0.3| MIT| [Kent C. Dodds](https://github.com/kentcdodds/cross-
env#readme)| <https://github.com/kentcdodds/cross-env.git>
cypress| 9.5.1| MIT| [Unknown](https://github.com/cypress-io/cypress)|
<https://github.com/cypress-io/cypress.git>
cypress-real-events| 1.7.0| MIT| Dmitriy Kovalenko|
<https://github.com/dmtrKovalenko/cypress-real-events.git>
eslint| 7.14.0| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 18.2.1| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 6.15.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-import-resolver-webpack| 0.13.0| MIT| [Ben
Mosher](https://github.com/benmosher/eslint-plugin-
import/tree/master/resolvers/webpack)|
<git+https://github.com/benmosher/eslint-plugin-import.git>
eslint-plugin-cypress| 2.12.1| MIT| [Chris
Breiding](https://github.com/cypress-io/eslint-plugin-cypress#readme)|
<git+https://github.com/cypress-io/eslint-plugin-cypress.git>
eslint-plugin-import| 2.22.1| MIT| [Ben
Mosher](https://github.com/benmosher/eslint-plugin-import)|
<https://github.com/benmosher/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.4.1| MIT| Ethan Cohen|
<https://github.com/evcohen/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.21.5| MIT| [Yannick
Croissant](https://github.com/yannickcr/eslint-plugin-react)|
<https://github.com/yannickcr/eslint-plugin-react>
eslint-plugin-react-hooks| 4.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
fs-readdir-recursive| 1.1.0| MIT| [Jonathan Ong](http://jongleberry.com)|
<https://github.com/fs-utils/fs-readdir-recursive.git>
html-webpack-plugin| 3.2.0| MIT| [Charles
Blaxland](https://github.com/jantimon/html-webpack-plugin)|
<https://github.com/jantimon/html-webpack-plugin.git>
jest| 25.5.2| MIT| [Unknown](https://jestjs.io/)|
<https://github.com/facebook/jest>
jest-junit| 10.0.0| Apache-2.0| Jason Palmer| <https://github.com/jest-
community/jest-junit>
react| 16.13.1| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
react-dom| 16.13.1| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
react-test-renderer| 16.14.0| MIT| [Unknown](https://reactjs.org/)|
<git+https://github.com/facebook/react.git>
styled-components| 5.3.10| MIT| [Glen Maddern](https://styled-
components.com/)| <git+https://github.com/styled-components/styled-
components.git>
stylelint| 13.3.3| MIT| [stylelint](https://stylelint.io/)|
<https://github.com/stylelint/stylelint.git>
webpack| 4.46.0| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 4.9.2| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 4.7.4| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server.git>
webpack-merge| 4.2.2| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

---

## @splunk/react-sparkline - 0.6.3

**Package:** `react-sparkline` | **Component:** `Line`

# Line

Use `Line` for showing data trend.

[Examples](?section=examples "Examples")[API](?section=develop "API")[Test
Hooks](?section=test "Test Hooks")

### Line

CodeShow Code

0

### Area

CodeShow Code

0

### Area with null values

CodeShow Code

Accept Null Values

0

### Area in table

CodeShow Code

#### General

Show Tooltip

Show as Area

Height

IncrementDecrement

Width

IncrementDecrement

#### Line

Line Color

#65a637

Line Width

IncrementDecrement

Line Length

IncrementDecrement

#### Area

Fill Color

#65a637

Fill Opacity

IncrementDecrement

#### End Dot

Show end dot

Radius

IncrementDecrement

Fill Color

white

Stroke Color

black

Stroke Width

IncrementDecrement

End Dot Count

IncrementDecrement

#### Cursor

Stroke Color

#5184af

Stroke Width

IncrementDecrement

Stroke Linecap

Square

Stroke Dasharray

Name| Fisical Year| Revenue
---|---|---
DATA| 06 - 17|
GOOG| 02 - 16|
AMZN| 08 - 17|
TEAM| 12 - 16|
OKTA| 15 - 17|
CHGX| 00 - 17|
BABA| 00 - 17|

### YScale

CodeShow Code

Y Min

IncrementDecrement

Y Max

IncrementDecrement

Height

IncrementDecrement

Width

IncrementDecrement

0

0

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `ChangeLog`

# Change Log

## 0.12.0 - June 3, 2025

  * Includes all changes from `0.12.0-beta` and `0.12.0-rc` releases.

## 0.12.0-rc.2 - May 28, 2025

API Changes:

  * `Toast` now uses `KeyboardEvent`'s `key` property instead of deprecated `keyCode` property (SUI-7352).

## 0.12.0-rc.1 - May 14, 2025

  * Release candidate 1

## 0.12.0-beta.1.v5.2 - March 5, 2025

  * Public release of `0.12.0-beta.1.v5`

## 0.12.0-beta.1.v5 - February 20, 2025

API Changes:

  * `react` peer dependency is now `"^16.8.0 || ^17.0.0 || ^18.0.0"`.

## 0.11.3 - Dec 5, 2023

Bug Fixes:

  * Adds styling support for title prop in Enterprise themes (SUI-5890)
  * Align visual styling of title between Enterprise and Prisma themes

## 0.11.2 - June 6, 2023

API Changes:

  * Added support for the latest `styled-components@5` (SUI-5467).

## 0.11.1 - December 6, 2022

  * Optimizes bundle sizes of consumers by reducing footprint of "lodash" (SUI-5090).

## 0.11.0 - May 20, 2022

New Features:

  * `Toast` now supports a `title` property (SUI-3569).

## 0.10.1 - April 5, 2022

API Changes:

  * Pinned `styled-components@5.1.1` to avoid breaking changes introduced in `styled-components@5.2.0`.

**`@splunk/react-toast-notifications` is incompatible with styled-components
version(s) `^5.2.0`**.

`styled-components@5.2.0` changed how selectors like `& + &` are compiled;
[styled-components PR#3236](https://github.com/styled-components/styled-
components/pull/3236). This breaks styles that worked in previous versions of
styled-components; [styled-components issue #3265](https://github.com/styled-
components/styled-components/issues/3265).

**Until noted otherwise in a future release of`@splunk/react-toast-
notifications` do not use `styled-components@^5.2.0` with` @splunk/react-
toast-notifications`**.

## 0.10.0 - May 6, 2021

New Features:

  * `Toast` action labels can now be of type `node` (SUI-2562).
  * `Toast` action now supports a `props` object to supply/override any of the action's props (SUI-2562).

Bug Fixes:

  * Fixed console error: "Unknown event handler property `onRequestHide`" (SUI-2397).

## 0.9.0 - February 4, 2021

New Features:

  * Prisma theme family now supported (SUI-2262).

API Changes:

  * IE11 is no longer a supported browser.
  * Theming updated and now requires `@splunk/themes@^0.7`.
  * `themes` are no longer exported.
  * `getToastTypeColor` no longer exported.

## 0.8.0 - July 7, 2020

New Features:

  * Support for `styled-components@^5`.

API Changes:

  * The `react` and `react-dom` peer dependencies are now `^16.8`.
  * The `styled-components` peer dependency is now `^5.1`.
  * `@splunk/react-ui` is no longer a peer dependency.

## 0.7.0 - March 15, 2020

API Changes:

  * The `@splunk/react-ui` peer dependency is now `^2.16`.

## 0.6.2 - October 14, 2019

Notes:

  * Relicensed to `Apache-2.0`.

## 0.6.1 - August 8, 2019

Bug Fixes:

  * Added support for `otherProps` to the `Toast` component (SUI-1839).

## 0.6.0 - June 11, 2019

New Features:

  * Added `theme` module which supports Enterprise (Dark) and Light themes.

Bug Fixes:

  * Fixed `Toaster` action button borders on IE11 (MAW-2616).

## 0.5.0 - February 22, 2019

New Features:

  * Support for `styled-components@^4`.

## 0.4.0 - September 13, 2018

API Changes:

  * `styled-components` is now a peer dependency.
  * The `@splunk/react-ui` peer dependency is now `^2`.
  * The `react` peer dependency is now `^16.3`.

Notes:

  * Relicensed to `Splunk Software License Agreement`.

## 0.3.1 - Not released

Bug fixes:

  * `Toaster` will now hold a queue of messages that are shown after `ToastMessages` is mounted.

## 0.3.0 - July 27, 2018

New Features:

  * `ToastMessages` now supports a `position` prop to change the container position.

Bug Fixes:

  * Moved `react-flip-move` to dependencies.

## 0.2.0 - June 30, 2018

  * Initial release

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `Licenses`

# Licenses

This package is licensed: Apache-2.0.

The following list contains the third-party dependencies used during
development, building, testing, publishing, and execution of this package.
Their source code and their output might be reproduced in parts or in full in
the published artifacts of this package. The list of dependencies is not
guaranteed to be complete. Each dependency might have additional dependencies
of its own. Refer to each dependency's source code and documentation for
details. The dependency versions listed are the versions used up until and
including the publishing stage. Due to the nature of semantic version ranges,
newer releases of each dependency might be used during execution.

We would like to thank the contributors to those projects.

## Production

Name| Version| License| Vendor| Repository
---|---|---|---|---
@splunk/react-icons| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/react-ui| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/themes| 1.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/ui-utils| 1.9.0| Apache-2.0| Splunk Inc.| Unknown
lodash| 4.17.21| MIT| [John-David Dalton](https://lodash.com/)|
<https://github.com/lodash/lodash.git>
prop-types| 15.8.1| MIT| [Unknown](https://facebook.github.io/react/)|
<https://github.com/facebook/prop-types.git>
react-flip-move| 3.0.4| MIT| Joshua Comeau|
<https://github.com/joshwcomeau/react-flip-move.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

## Development

Name| Version| License| Vendor| Repository
---|---|---|---|---
@babel/core| 7.25.8| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-core)|
<https://github.com/babel/babel.git>
@babel/eslint-parser| 7.25.8| MIT| [The Babel Team](https://babel.dev/)|
<https://github.com/babel/babel.git>
@babel/plugin-transform-runtime| 7.18.6| MIT| [The Babel
Team](https://babel.dev/docs/en/next/babel-plugin-transform-runtime)|
<https://github.com/babel/babel.git>
@splunk/babel-preset| 4.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/eslint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/stylelint-config| 5.0.0| Apache-2.0| Splunk Inc.| Unknown
@splunk/webpack-configs| 7.0.2| Apache-2.0| Splunk Inc.| Unknown
@storybook/addon-a11y| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/addons/a11y)|
<https://github.com/storybookjs/storybook.git>
@storybook/addon-essentials| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/addons/essentials)|
<https://github.com/storybookjs/storybook.git>
@storybook/addon-interactions| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/addons/interactions)|
<https://github.com/storybookjs/storybook.git>
@storybook/csf| 0.0.1| MIT| [Unknown](https://github.com/storybookjs/csf)|
<https://github.com/storybookjs/csf.git>
@storybook/manager-api| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/lib/manager-
api)| <https://github.com/storybookjs/storybook.git>
@storybook/react-webpack5| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/frameworks/react-
webpack5)| <https://github.com/storybookjs/storybook.git>
@storybook/test-runner| 0.16.0| MIT| shilman|
<https://github.com/storybookjs/test-runner>
@testing-library/dom| 10.4.0| MIT| [Kent C. Dodds](https://github.com/testing-
library/dom-testing-library#readme)| <https://github.com/testing-library/dom-
testing-library>
@testing-library/jest-dom| 6.6.3| MIT| [Ernesto
Garcia](https://github.com/testing-library/jest-dom#readme)|
<https://github.com/testing-library/jest-dom>
@testing-library/react| 16.3.0| MIT| [Kent C.
Dodds](https://github.com/testing-library/react-testing-library#readme)|
<https://github.com/testing-library/react-testing-library>
babel-loader| 8.3.0| MIT| [Luis Couto](https://github.com/babel/babel-loader)|
<https://github.com/babel/babel-loader.git>
babel-plugin-transform-imports| 2.0.0| ISC| [AMC
Theatres](https://bitbucket.org/amctheatres/babel-transform-imports)|
<https://bitbucket.org/amctheatres/babel-transform-imports.git>
cross-env| 6.0.3| MIT| [Kent C. Dodds](https://github.com/kentcdodds/cross-
env#readme)| <https://github.com/kentcdodds/cross-env.git>
cypress| 13.17.0| MIT| [Unknown](https://cypress.io/)|
<https://github.com/cypress-io/cypress.git>
cypress-real-events| 1.9.1| MIT| Dmitriy Kovalenko|
<https://github.com/dmtrKovalenko/cypress-real-events.git>
eslint| 8.57.1| MIT| [Nicholas C. Zakas](https://eslint.org/)|
<https://github.com/eslint/eslint.git>
eslint-config-airbnb| 19.0.4| MIT| [Jake Teton-
Landis](https://github.com/airbnb/javascript)|
<https://github.com/airbnb/javascript>
eslint-config-prettier| 9.1.0| MIT| Simon Lydell|
<https://github.com/prettier/eslint-config-prettier.git>
eslint-import-resolver-webpack| 0.13.7| MIT| [Ben
Mosher](https://github.com/import-js/eslint-plugin-
import/tree/HEAD/resolvers/webpack)| <git+https://github.com/import-js/eslint-
plugin-import.git>
eslint-plugin-import| 2.31.0| MIT| [Ben Mosher](https://github.com/import-
js/eslint-plugin-import)| <https://github.com/import-js/eslint-plugin-import>
eslint-plugin-jsx-a11y| 6.10.0| MIT| Ethan Cohen| <https://github.com/jsx-
eslint/eslint-plugin-jsx-a11y>
eslint-plugin-react| 7.37.1| MIT| [Yannick Croissant](https://github.com/jsx-
eslint/eslint-plugin-react)| <https://github.com/jsx-eslint/eslint-plugin-
react>
eslint-plugin-react-hooks| 4.6.2| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
identity-obj-proxy| 3.0.0| MIT| [Keyan
Zhang](https://github.com/keyanzhang/identity-obj-proxy#readme)|
<git+https://github.com/keyanzhang/identity-obj-proxy.git>
jest| 29.7.0| MIT| [Unknown](https://jestjs.io/)|
<https://github.com/jestjs/jest.git>
jest-environment-jsdom| 29.7.0| MIT| Unknown|
<https://github.com/jestjs/jest.git>
jest-junit| 10.0.0| Apache-2.0| Jason Palmer| <https://github.com/jest-
community/jest-junit>
react| 18.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
react-dom| 18.2.0| MIT| [Unknown](https://reactjs.org/)|
<https://github.com/facebook/react.git>
react-test-renderer| 16.14.0| MIT| [Unknown](https://reactjs.org/)|
<git+https://github.com/facebook/react.git>
storybook| 7.6.17| MIT|
[Unknown](https://github.com/storybookjs/storybook/tree/next/code/lib/cli)|
<https://github.com/storybookjs/storybook.git>
styled-components| 5.3.10| MIT| [Glen Maddern](https://styled-
components.com/)| <git+https://github.com/styled-components/styled-
components.git>
stylelint| 15.11.0| MIT| [stylelint](https://stylelint.io/)|
<https://github.com/stylelint/stylelint.git>
webpack| 5.91.0| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack)|
<https://github.com/webpack/webpack.git>
webpack-cli| 5.1.4| MIT| [Unknown](https://github.com/webpack/webpack-
cli/tree/master/packages/webpack-cli)| <https://github.com/webpack/webpack-
cli.git>
webpack-dev-server| 4.15.1| MIT| [Tobias Koppers
@sokra](https://github.com/webpack/webpack-dev-server#readme)|
<https://github.com/webpack/webpack-dev-server>
webpack-merge| 5.9.0| MIT| [Juho
Vepsalainen](https://github.com/survivejs/webpack-merge)|
<https://github.com/survivejs/webpack-merge.git>

To pick up a sortable column, press space or enter. Use the left and right
arrow keys to update the position of the column. Press space or enter again to
drop the column in its new position, or press escape to cancel.

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `Toaster`

# Toaster

A Toaster is a singleton responsible for posting toast messages that are
received by a ToastMessages container.

[Examples](?section=examples)[API](?section=develop)

### Toaster API

The Toaster component leverages the function returned from
`makeCreateToast(Toaster)` which we refer to as `createToast`. This function
expects a set of props as parameters which are defined as follows:

#### Props

action

An actionable button that has a required label and callback function. `props`
can optionally be added to pass any additional props to the button.

PropType:| shape({label: oneOfType(string, node), callback: func, props:
object})
---|---
Required:| no

autoDismiss

Whether the toast message should automatically dismiss after 5 seconds.

PropType:| bool
---|---
Default:| true
Required:| no

dismissOnActionClick

Whether the toast message should automatically dismiss after an action is
clicked.

PropType:| bool
---|---
Default:| true
Required:| no

message

The message to be shown in the toast.

PropType:| string
---|---
Required:| yes

title

The message title to be shown in the toast.

PropType:| string
---|---
Default:| ''
Required:| no

type

The type of toast. These types are pre-defined in `ToastConstants.js` as
`TOAST_TYPES`. If an unknown toast type is sent to `ToastMessages`, it will
default to `TOAST_TYPES.INFO` and show warnings to the developer. We do not
enforce `TOAST_TYPES` in props because if multiple apps use the same
`ToastMessages` container where one of these versions have a newer version
`Toaster` with perhaps new types, we do not want to show nothing, but rather
show the message and default to `TOAST_TYPES.INFO`.

PropType:| string
---|---
Required:| yes

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `ToastMessages`

# Toast Messages

A ToastMessages container is a singleton that is responsible for displaying
posted toast notifications from a Toaster.

[Examples](?section=examples)[API](?section=develop)

### ToastMessages API

This component is a singleton that is responsible for displaying posted toast
notifications. Because it is a singleton, only create one instance within an
app.

#### Props

position

The static position on the screen that toasts will display.

PropType:| oneOf('top-left', 'top-center', 'top-right', 'bottom-left',
'bottom-center', 'bottom-right')
---|---
Default:| 'top-center'
Required:| no

---

## @splunk/react-toast-notifications - 0.12.0

**Package:** `react-toast-notifications` | **Component:** `Usage`

# Usage

**Important:** Any component (or any of it's descendants) that is (or ever
might be) consumed by another app should not import anything from react-toast-
notifications aside from `@splunk/react-toast-notifications/ToastConstants`.
This is because we do not want conflicting versioned dependencies.

## 1\. Create a Toast Messages container

A ToastMessages container is a singleton that is responsible for displaying
posted toast notifications.

Referencing the important note, we suggest that you wrap the root of your app
(whether it is exported or not) by a component that is only used when running
internally. This internal component should include a ToastMessages container.

As an example, the Analysis Workspace wraps it's exposed Workspace component
in a WorkspaceInternal component that is used only when running the app
internally.



    import React from 'react';
    import ToastMessages from '@splunk/react-toast-notifications/ToastMessages'
    import { Workspace } from './metrics';

    const WorkspaceInternal = props => (
        <div>
            <Workspace {...props} />
            <ToastMessages />
        </div>
    );

    export default WorkspaceInternal;

## 2\. Create a Toaster

A Toaster is a singleton responsible for posting toast messages.

In order to create toasts, you must add an additional function prop to the
root of your app (as a convention let's use createToast).

Using the Analysis Workspace as an example again, this is done like so:



    import Toaster, { makeCreateToast } from '@splunk/react-toast-notifications/Toaster';

    const props = {
        createToast: makeCreateToast(Toaster),
        ...
    };

The above will bind a Toaster instance to the create function which can then
be passed props as parameters to create toasts.

Like ToastMessages, if you are running internally, it is safe to pass a
createToast prop created from Toaster. However, if this component (ex.
Workspace) is exposed for consumption, it should be on the consumer to create
a Toaster and ToastMessages container and pass this prop to the component so
the exposed app has no dependencies on react-toast-notifications.

## 3\. Create toasts

Now that you have a ToastMessages component and createToast prop passed to
your app, you will be able to post messages using createToast. How you pass
this function throughout your app is up to you.

Here is an example of a toast message:



    import { TOAST_TYPES } from '@splunk/react-toast-notifications/ToastConstants';

    const toastProps = {
        message: `Toast created created successfully.`,
        type: TOAST_TYPES.SUCCESS,
        action: {
            label: 'Show Alert',
            callback: () => {
                // do something
            },
        },
    };
    this.props.actions.createToast(toastProps);

For details on the supported props for toasts, please see the API section.

---

## Splunk Design System

**Package:** `SUIT` | **Component:** `Backbone`

# Working with Splunk UI and CoreJS

One of the reasons we choose React over other framework libraries is that it
plays well with other framework libraries on the page. React is simply a view
layer and can be used in conjunction with other view layers, and any data
layer. This document will discuss using Backbone with React, but many of the
same principles would apply to any other framework library you might want to
use with React.

When working with React and Backbone, it is essential to minimize the touch
points between the two libraries. Use a single module as the "glue" layer
between code that uses Backbone and code that uses React. Only this one module
should be aware of both libraries.

Although there are a variety of libraries on npm and the web in general that
provide support for using React and Backbone together, most should be avoided.
They often deeply intertwine the two libraries and result in code that is
deeply dependent on both. Changes become difficult and larger refactors nearly
impossible.

Below are three common scenarios where Backbone and React code meet.

## Rendering React Components from Backbone Views

Here's the base view from Core which is used to wrap a React Component in a
Backbone View.



    import BaseView from 'views/Base';
    import ReactDOM from 'react-dom';
    import React from 'react';

    const ReactAdapterBaseView = BaseView.extend({
        getComponent() {
            throw new Error('getComponent() not implemented');
        },
        render() {
            ReactDOM.render(this.getComponent(), this.el);
            return this;
        },
        remove() {
            ReactDOM.unmountComponentAtNode(this.el);
            return BaseView.prototype.remove.call(this);
        },
    }, {
        wrapComponent(Component) {
            return ReactAdapterBaseView.extend({
                getComponent() {
                    return React.createElement(Component);
                },
            });
        },
    });

    export default ReactAdapterBaseView;

## Rendering Backbone Components (View or Modal) from React Views

Here's the base view from Core which is used to wrap a Backbone Component in a
React View.



    import React, { Component } from 'react';

    class BackboneAdapterBase extends Component {
        componentDidMount() {
            this.backboneView = this.getView();
            // If dealing with a View
            this.backboneView.render().$el.appendTo(this.container);
            // OR
            // If dealing with a Modal
            this.backboneView.render().show();
        }

        shouldComponentUpdate() {
            return false;
        }

        componentWillUnmount() {
            if (this.backboneView) {
                this.backboneView.remove();
            }
        }

        getView() { // eslint-disable-line class-methods-use-this
            throw new Error('getView() not implemented');
        }

        getContainerProps() {
            // subclass can override this method to return a subset of props.
            // by default it will just pass through all props.
            return this.props;
        }

        render() {
            return (
                <div
                    {...this.getContainerProps()}
                    ref={c => (this.container = c)}
                />
            );
        }
    }

    export default BackboneAdapterBase;

## Using Backbone Models to manage data for React Components

When using Backbone Models to manage data for React Components use the
[Controller-View Architecture](https://facebook.github.io/flux/docs/in-depth-
overview/#views-and-controller-views). Although this example is using Flux for
the data layer, the same principles apply. The Controller-View is the only
React Component that is aware of the data layer and is solely responsible for
managing that data and passing it to a top-level Component that actually
handles the rendering logic. The Controller-View passes the Component vanilla
JavaScript. Nothing below the Controller-View has any knowledge of the library
used to manage the data.

Sometimes a Controller-View is called a "Smart Component" and the rest of the
views "Dumb Components". But, the principles are the same. The "Smart
Component" is responsible for data management and the "Dumb Components" are
responsible for rendering logic.

Large and complex applications may have multiple Controller-Views on a single
page. In general, a Controller-View should own an entire domain and be able to
stand on its own, plugged in where needed with minimal impact on the rest of
the applications code.

## Rendering Backbone Views in React Components

Rendering Backbone Views into a React tree is relatively straight forward.
Again, it is important to isolate the two libraries. Create a React Component
that wraps the Backbone View, translating the Backbone API to a React API.

Generally, the wrapper component's render function will simply return div or
container element with a ref on it. Then, the Backbone View is rendered into
the container el in the component's `componentDidMount` and/or
`componentDidUpdate` lifecycle methods.

When wrapping a view, expose a React style API. The internal Backbone view
should be controlled by props. Never expose imperative Backbone View methods
through the React wrapper.

---

## Splunk Design System

**Package:** `SUIT` | **Component:** `ExamplesGallery`

# Examples Gallery

Filter by Tag Or Category

Filter…

## App workflows

Interacting with the KV Store

[](https://github.com/splunk/SUIT-example-for-kv-store)View on GitHub

View Larger Image

The KV Store allows developers to store, retrieve and update important data in
their instance. This example shows a simple CRUD workflow with a provided KV
Store collection, and also allows you to view the records in other collections
in your instance.

Splunk REST API

Login pages

[](https://github.com/splunk/SUIT-example-for-logins)View on GitHub

View Larger Image

For apps outside of Splunk Web, a simple login page can be used to
authenticate users into Splunk. This example shows a login interface made with
@splunk/react-ui components.

Splunk REST API

Setup Pages

[](https://github.com/splunk/SUIT-setup-page-example)View on GitHub

View Larger Image

This example shows the common workflow of having a setup page asking for user
input to configure apps. Use @splunk/react-ui components to capture user input
and use @splunk/splunk-utils to effectively store secrets.

Splunk REST API

Visualizations with Splunk UI

[](https://github.com/splunk/SUIT-example-for-visualizations)View on GitHub

View Larger Image

With Splunk UI Toolkit, there are many ways to display data with your Splunk
searches. This example shows how to leverage the @splunk/search-job package to
run searches to display data to both third party and @splunk/visualizations
charts.

Third-party visualizations

Splunk searches

Searching Outside Splunk Web

[](https://github.com/splunk/react_search_example)View on GitHub

View Larger Image

Leverage the Splunk UI Toolkit to run searches outside of Splunk Web, and
dynamically add more visualizations by running post-process searches with the
click of a button!

Splunk REST API

Analytics for Packages

[](https://github.com/splunk/analytics-for-packages)View on GitHub

View Larger Image

Reqest data from a Third Party API and display it on Splunk Visualizations.
This example captures user input to search metrics for publicly available
packages across platforms.

## Custom dashboards and visualizations

Custom inputs for Splunk Dashboard Framework

[](https://github.com/splunk/splunk-dashboard-framework-custom-inputs)View on
GitHub

View Larger Image

Go to the next level with your dashboards by creating your own custom input
interface for your users by extending the Splunk Dashboard Framework. This
example builds a custom widget that maps multiple inputs into tokens that can
filter your data sources and displays results on a third party calendar
visualization

Third-party visualizations

Dashboard with a simple table component

[](https://github.com/splunk/dashboard-simple-table-component)View on GitHub

View Larger Image

A simple introduction to custom development with the Splunk Dashboard
Framework. Create a simple Splunk app and integrate a customized table as a
visualization in your dashboard.

Dashboard with custom interactivity - click to open a modal

[](https://github.com/splunk/dashboard-interactivity-modal)View on GitHub

View Larger Image

Integrate custom workflows, including click actions to open modals with Splunk
Dashboard Framework. This example provides a starting point for workflows with
dashboards that are not supported natively by the framework.

Dashboard with custom Google Maps components

[](https://github.com/splunk/dashboard-react-google-maps)View on GitHub

View Larger Image

If you want to use an open source React component, or have developed one
yourself that you would like to use, this example shows how to do so with an
open source map package that allows you to render an interactive map as a
React component.

Third-party visualizations

Supply chain tracking

[](https://github.com/splunk/supply-chain-tracking)View on GitHub

View Larger Image

This contributed project showcases how to integrate additional Google Maps
functionality by creating marks on the map itself and attaching click events
that open mini-dashboards.

Third-party visualizations

## Apps showcase

Slack alerts

[](https://github.com/splunk/slack-alerts)View on GitHub

View Larger Image

This app adds a new custom alert action to your Splunk instance which allows
you to send a message to a Slack channel. This app contains a setup page
created with @splunk/react-ui.

AppInspect UI

[](https://github.com/splunk/appinspect-ui)View on GitHub

View Larger Image

For avid Splunk app developers, the AppInspect UI app provides an easy way for
validating apps against selected AppInspect checks. Made with Nextron and
Splunk UI, elevate your app delivery workflow with this easy-to-use app.

SPL-ing Bee

Actions

View Larger Image

Do you know how to SPL? These Github Repositories are the apps you need to
replicate the SPL-ing Bee from .conf 2022. This fun game includes a contestant
app and a moderator app for your Splunk environments. You'll be able to use
the moderator app to run a live multiple round, SPL challenge game.
Contestants can use the contestant app to participate. Results will be
Splunk'd in real time and will be judged based on search efficiency, quickest
to answer, and correctness. Come join the fun!

Splunk REST API

Timelapse inputs for dashboards

[](https://github.com/splunk/timelapse-vis)View on GitHub

View Larger Image

The timelapse input serves as a way for users to analyze changes to their
dashboard over time rapidly. Built with Splunk UI and the Splunk REST API,
this app is designed to plug-and-play with all your current Dashboard Studio
dashboards.

Third-party component

Splunk REST API

Splunk searches

---

## Splunk Design System

**Package:** `toolkits` | **Component:** `suit`

# Page not found

The page you are trying to view does not seem to exist.

---

