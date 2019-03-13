---
title: "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks"
short_title: "CycleGAN"
authors: ['Jun-Yan Zhu', 'Taesung Park', 'Phillip Isola', 'Alexei A. Efros']
journal: "ICCV"
year: 2017
arxiv_id: "1703.10593"
url: "https://arxiv.org/abs/1703.10593"
added_date: 2018-12-29
---

# [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks (CycleGAN)][CycleGAN]

#### Reminders
1. What previous research and ideas were cited that this paper is building off of? (introduction)
2. Reasoning for performing this research? (introduction)
3. Clearly list the objectives of the study
4. Was any equipment/software used? (methods)
5. What variables were measured during experimentation? (methods)
6. Were any statistical tests used? What were their results? (methods/results)
7. What are the main findings? (results)
8. How do these results fit into the context of other research in the field? (discussion)
9. Explain each figure and discuss their significance.
10. Can the results be reproduced and is there any code available?
11. Are any of the authors familiar, do you know their previous work?
12. What key terms and concepts do I not know and need to look up in a dictionary, textbook, or ask someone?
13. What are your thoughts on the results? Do they seem valid?

## TLDR

GAN architecture for general image-to-image translation, using two generators and two discriminators. Key insight is the cycle-consistency term in the generator loss, which is an L1 distance between the original image and the image passed through both A->B and B->A generators. This term reduces the space of possible mapping functions, making it much easier to learn a good mapping.

#### Key Points

- The generator uses an architecture from [Johnson et al., 2016](https://arxiv.org/abs/1603.08155), consisting of several downsampling layers followed by a number of residual blocks with skip connections, followed by several fractionally strided convolution layers to upsample.


#### Notes/Questions

- Using fractionally strided convolutions to upsample can risk checkerboard artifacts due to

[CycleGAN]: https://arxiv.org/abs/1703.10593
