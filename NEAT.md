---
title: "Evolving Neural Networks through Augmenting Topologies"
short_title: "NEAT"
authors: ['Kenneth Stanley', 'Risto Miikkulainen']
journal: "Evolutionary Computation"
year: 2002
url: "http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf"
added_date: 2019-03-02
---

# [Evolving Neural Networks through Augmenting Topologies (NEAT)][NEAT]

### TLDR

How to evolve the topology of neural networks properly as well as just the weights.

### Motivation

To set the scene, at the time NEAT came out the approach of evolving the weights of neural networks had shown promise for benchmarks such as pole balancing. These days such tasks are usually solved using non evolutionary deep reinforcement learning methods that can achieve good results simply by using a massive amount of computation. Before NEAT, several papers had tried evolving the topology of networks but were not able to outperform a fixed network. NEAT was the first algorithm to do so, which is why it is frequently used and very well known.

Research questions:
Can we get good results on benchmarks by evolving the topology of neural networks as well as the weights?

The authors identified 3 key problems to solve to achieve this:
1. How should we represent network architectures to allow for crossover between topologies?
2. If we have an evolved topology that needs several generations to optimise, how do we stop it disappearing from the population?
3. How can we minimise the complexity of topologies throughout evolution?

### Genetic encoding

The question of encoding comes from the question of how do we wish to represent individuals genetically in our algorithm. Any encoding will fall into one of two categories, direct or indirect. A direct encoding will explicitly specify everything about an individual. If it represents a neural network this means that each gene will directly be linked to some node or connection of the network. An indirect encoding tends to specify rules or parameters of processes for creating an individual. As a result, they are more compact, but can introduce a bias in the search space depending on how the encoding works.

The main issue with encoding neural networks as genes is the competing conventions problem: having more than one way to represent the same network. When two genomes representing the same network structure do not have the same encoding, crossover is likely to produce damaged offspring. The key insight in NEAT's encoding is that two genes with the same historical origin represent the same structure. This solves the problem, and we can achieve this by including a global innovation number for each edge (or gene) in the network graph, essentially a version number for each edge.

The NEAT encoding scheme is designed to allow corresponding genes to be easily matched up during crossover.  Each genome is a list of connection genes representing edges in the graph, each of which refers to two node genes. The connection genes specify the in node, out node, weight of the edge, whether or not the edge is in the graph, and the innovation number. So the genome (or genotype) is the list of connection genes and node genes, and the phenotype is the neural network diagram.

There are two possible mutations to a genome: adding a node or adding a connection. When any connection is added, the global innovation number is incremented and assigned to that gene. So the innovation numbers represent a history of every gene in the system.

### Protecting innovation

In a topology evolving network, adding new structure usually causes the fitness of a network to decrease, since for example, adding a new connection causes the fitness to reduce temporarily before the connection's weight has a chance to optimise. Several generations may be required to optimise new structure and make use of it. NEAT solves this by dividing the population into species based on topological similarity, so individuals compete with others in their own species and have a chance to optimise before they have to compete with the overall population.

NEAT uses the innovation numbers to determine topological similarity, by calculating a compatibility distance between two genomes. This is based on the number of connection genes with different innovation numbers in each genome, along with the average weight difference between connection genes that share the same innovation number. This distance measure allows us to divide the population of genomes into species using a threshold. Genomes are tested sequentially - if a genome's distance to a randomly chosen member of a species is less than the threshold then it is placed into this species. This ensures species do not overlap.

As a reproduction mechanism, NEAT uses fitness sharing, where all organisms in the same species share their fitness. The original fitness is then adjusted by dividing by the number of individuals in the species. Species then grow or shrink depending on how high their average adjusted fitness is. Species reproduce by first eliminating the lowest performing members, then the entire population is replaced by the offspring of the remaining organisms in each species.

### Minimizing dimensionality

Typically, topology evolving networks start with an initial population of random topologies. However, a random population has a large amount of network structure that has not been evaluated for fitness and may be completely unnecessary. Therefore with random initialisation the algorithm may waste effort by optimising unnecessarily complex structures. NEAT's solution to this is to start with a uniform population of networks with zero hidden nodes. New structure is introduced incrementally with mutations, and the only structures that survive are found to be useful via fitness evaluations.

Hence NEAT minimises the complexity of not only the final network, but all intermediate networks along the way. This significantly reduces the number of generations needed to find a solution.

### Architecture Summary

To summarise, the design principles of NEAT are:
- Historical marking with innovation numbers. This allows
- Dividing the population into species based on topological similarity. This allows
- Starting minimally and allowing for growth of more complex structures. This allows

### Results & Experiments

NEAT was first evaluated on the XOR problem, which is not linearly separable, to test if the algorithm could solve a basic problem and evolve structure properly. The algorithm found a solution in every run, averaging 32 generations.

NEAT was also tested on double pole balancing tasks - a benchmark in which two poles are connected to a moving cart by a hinge. The objective is to apply force to the cart to keep both poles upright. NEAT was tested against two rival algorithms, Cellular Encoding, which evolves network structure, and Enforced Subpopulations, which only evolves weights. NEAT was tested on two versions of this task - allowing the network to see the cart velocity and hiding this information, and in both tasks NEAT proved to be much more efficient than the rival algorithms. In the harder task with velocity hidden, NEAT used 25 times fewer evaluations to reach a solution than Cellular Encoding, 5 times fewer evaluations than Enforced Subpopulations, and never needed to restart. Hence NEAT has a significant performance advantage over previous neuroevolutionary algorithms.

NEAT was finally evaluated with an ablation study - a study in which different components of the system are removed in turn to see which components are critically important. These experiments were evaluated on a simplified pole balancing task, and tested NEAT with no growth of the topology, a random initial population rather than starting from a population with no hidden units, and a version without species. All showed worse results than the full version of NEAT, proving that all components of the algorithm are important for its performance.

### Discussion

Key insight: it is not the ultimate structure of the solution that really matters, but rather the structure of all the intermediate solutions along the way to finding the solution. The connectivity of every intermediate solution represents a parameter space that evolution must optimize, and the more connections there are, the more parameters need to be optimized. Therefore, if the amount of structure can be minimized throughout evolution, so can the dimensionality of the spaces being explored, leading to significant performance gains.

NEAT strengthens the analogy between GAs and natural evolution by adding a complexifying function, allowing the networks to become incrementally more complex as they become more optimal. Each increase in complexity resulting from new structure leads to a promising part of a higher dimensional space because most of the existing structure is already optimized.

Another benefit of evolving topology is the ability to escape local optima. Adding new structure can alter the fitness landscape, allowing the algorithm to find a path away from the local optima.

[NEAT]: http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf
