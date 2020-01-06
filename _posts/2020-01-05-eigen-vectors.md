---
title: "Eigen Vectors"
date: 2020-01-05 00:26:00 +0800
categories: [Eigen Vectors]
tags: [Eigen]
---

The Eigen Vector equation is:

$$
(A - \lambda I_n)\vec{x} = 0 \\ - eq 1
$$


Where $$A$$ is the matrix we want to find out the Eigen vectors for and $$\vec{x}$$ is the eigen vector of $$A$$. So how to interpret this physically or graphically? Let's discuss!

Usually when you say A.B what does it mean? A would be a transform. Consider it as f(x). Now Assume B will also result in a transform, we call it g(x). A.B means f(g(x)). That's why A.B $$\neq$$ B.A. Because f(g(x)) $$\neq$$ g(f(x)). Now the equation-1 can be rewritten as

$$
A\vec{x} = \lambda I_n \vec{x} \\ - eq 2
$$

See this? The eigen vector doesn't care about the transform. It will make f(x) look like an interpolator function, which it actually isn't all times. Isn't that cool?

So if you take Matrix A's eigen vector , plot in on graph the points representing the eigen vector just interpolate when the function f(x) is applied. That's what the eigen vector means graphically. For more illustration checkout this great video.


[![Eigen Vectors 3Blue1Brown](https://www.youtube.com/watch?v=PFDu9oVAE-g&t=761s)
