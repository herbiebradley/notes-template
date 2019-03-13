---
title: "A Hypercube-Based Encoding for Evolving Large-Scale Neural Networks"
short_title: "HyperNEAT"
authors: ['Kenneth Stanley', 'David D'Ambrosio', 'Jason Gauci']
journal: "Artificial Life"
year: 2009
url: "https://www.mitpressjournals.org/doi/10.1162/artl.2009.15.2.15202"
added_date: 2019-03-07
---

# [A Hypercube-Based Encoding for Evolving Large-Scale Neural Networks (HyperNEAT)][HyperNEAT]

## TLDR


### Motivation

NEAT used a direct encoding for its network structure. This was so that networks could be incrementally evolved by adding nodes and connections one at a time. This is fine for small networks like the ones used back in 2002, but in order to evolve large networks you need a much faster method of evolution.

If you look at the brain, you see a network with billions of nodes and trillions of connections. The brain uses repetition of structure, so a mapping of the same gene is used to generate the same physical structure multiple times. The brain also exploits physical properties of the world: symmetry and locality.

Normal neural nets do not have any of these properties. NEAT does not have a way of generating the same structure multiple times, and backprop/NEAT are invariant to locality.

[HyperNEAT]: https://www.mitpressjournals.org/doi/10.1162/artl.2009.15.2.15202
