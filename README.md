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


