# slide-dev-prototype

## Overview

The goal here is to replace Marp with an easier to format and manage markdown to slides template. 

slidev.js was chosen because it uses the same markdown translation that our documentation does, therefore the markdown should theoretically be more familiar to individuals working with both. 


## How it works

It is a node.js plugin, and it builds html. 

To get it to build pdf's I added something locally. 

I will document that when I get to it. 

## How it differs from Marp

Marp delineates slides like this

```
---
<optional header content here>
---
```

slidev delineates slides like this

```
---
layout: cover
---
```

## Goals

If we use a markdown to slides tool it is in our interest that the actual typing to create a slide is not encumbered with having to include html elements. 

Hopefully this avoids that problem. 

How did our Marp slides get so crowded and complex? I think that leadership wanted a certain look that was hard to get in Marp. 

## Custom theme

It seems a custom them and layout elements are fairly straightforward to create. So far I have done some of that, I hope the rest is easy

## Documentation

https://sli.dev/guide/


## Contents

the slidev_built_in_demo was created by running

`pnpm create slidev`

And when prompted naming the project `slidev_built_in_demo`

In order to run that demo switch to the directory and run

`npm run dev`




## Foundations Course Directory

This is basically the same as pnpm create slidev with the following changes. 

Custom theme, 
Some changes to config to support the callout boxes on our website. 

The addition of an `assets` folder to hold images.

The addition of a `kurrent_2025` folder which holds our theme. 

Mainly for them we creat a layout in the layouts folder, and an associated style in the styles `layout.css`

## To enable emojis and to get the callout style 

pnpm install i markdown-it-emoji

pnpm install i markdown-it-container

Remove the line from package.json
  // "type": "module",
  

To run against another markdown file
`pnpm exec slidev -- --port 3030 <File Name>`

