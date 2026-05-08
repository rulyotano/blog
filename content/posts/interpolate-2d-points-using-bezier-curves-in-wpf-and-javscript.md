---
title: Interpolate 2D Points Using Bezier Curves in WPF (and Javscript)
date: '2024-10-02T18:45:59+00:00'
draft: false
tags:
- Blog
- WPF
- Algorithm
- C#
url: /blog/article/wpf-bezier-interpolation
cover:
  image: /images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/interpolation-bezier-curves.gif
  alt: Interpolate 2D Points Using Bezier Curves in WPF (and Javscript)
  relative: false
---

* [**[Original Article]**](https://main.codeproject.com/articles/Interpolate-2D-Points-Using-Bezier-Curves-in-WPF)
* [**Sample on GitHub (WPF)**](https://github.com/rulyotano/WPF-Bezier-Interpolation/tree/master)
* [**Sample on Github (JavaScript)**](https://github.com/rulyotano/rulyotano.crosscutting.js/tree/main/src/rulyotano.math.interpolation.bezier)
* [**Live example in JavaScript (ReactJs)**](https://rulyotano.com/demos/bezier)

## Introduction

Interpolating points sometimes is hard mathematical work, even more, if the points are ordered. The solution is to create a function using the points and using an extra parameter `t` that represents the time dimension. This often is called a parametric representation of the curve. This article shows a simple way of interpolating a set of points using Bezier curves in WPF.

## Background

The idea of this solution comes after asking [this question in](http://stackoverflow.com/questions/13312834/how-to-interpolate-n-points-that-do-not-describe-a-function) Stack Overflow. The accepted answer makes references to a simple and interesting method proposed by Maxim Shemanarev, where the control points are calculated from the original points (called anchor points).

Here, we create a WPF `UserControl` that draws the curve from any collection of points. This control can be used with the pattern MVVM. If any point's coordinate changes, the curve also will change automatically. For instance, it can be used for a draw application, where you can drag & drop the points for changing the drawing, or curve.

## The Algorithm Behind

Due to the original [antigrain site](http://www.antigrain.com/research/bezier_interpolation/index.html) being down (I can find that Sourceforge is still supporting this library and we can find the original [article over here!](https://agg.sourceforge.net/antigrain.com/research/bezier_interpolation/index.html#PAGE_BEZIER_INTERPOLATION)), I'm going to explain what is the algorithm proposed by [Maxim Shemanarev](https://en.wikipedia.org/wiki/Anti-Grain_Geometry).

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/AP1GczMf0rclISZvatzGQR9cWCEfUhRTqb-aBcCFt1ePA17jaiRzoWsDr7trnlN3fHcYF81yS2nVeGWK2FV99DeP7Fn5J1TaJuzvxTOgEJX1rE8pgs1ODVJrELpmPvqToG87gHcliVlehlkw7oSQnAA7zGz_cg=w267-h224-s-no-gm)

A Bezier curve has two anchor points (begin and end) and two control ones (CP) that determine its shape. Our anchor points are given, they are pair of vertices of the polygon. The question is, how to calculate the control points? It is obvious that the control points of two adjacent edges form one straight line along with the vertex between them.

The solution found is a very simple method that does not require any complicated math. First, we take the polygon and calculate the middle points Ai of its edges.

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/AP1GczMvDff_nieypyRNnJwMH31SQljwYJnTWsOfptMGu5u-lmcHYXqdAKMyqRvgUmTgbqrMWWt9_bgB71NEzrkyag7JqmLVJ0sTvvZaWisO0HjrYtHYLRyL8BEThNFlRWHIqYl7GjKeIdBQ7ws3RzjXz27gag=w242-h223-s-no-gm)

Here, we have line segments Ci that connect two points Ai of the adjacent segments. Then, we should calculate points Bi as shown in this picture.

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/AP1GczOu6RdEoaqxynUgSqjX7T3dz8gFfkknsAsUB_fL0VQyxHt5exY9H5iOcuZz1I7nikk-XQ0KQka7PyHQ043edc1QJNPyh1mCJmyFvtqI4IJcIDDGCKfbPZte4tVhRbOaF3_rVzxz5futrlN70DUA2NUbHg=w252-h249-s-no-gm)

The third step is final. We simply move the line segments Ci in such a way that their points Bi coincide with the respective vertices. That's it, we calculated the control points for our Bezier curve and the result looks good.

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/AP1GczPYy-vrePpjPFYKmKhhHhnGLgvxdXGOqcPOEfxZVsVkodOHeEdmv9qs1678zjjgJV1wJcPN6vXE98xQWMaZ__8Awt_X4NOHYRyENU-CgNyH57cLAXNI61JTMy9kH59e7jYYN4JDtIUUlx1gO7AvRF2FjA=w284-h279-s-no-gm)

One little improvement. Since we have a straight line that determines the place of our control points, we can move them as we want, changing the shape of the resulting curve. I used a simple coefficient K that moves the points along with the line relative to the initial distance between vertices and control points. The closer the control points to the vertices are, the sharper figure will be obtained.

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/AP1GczPdduKZRywxfag8UUVpAiHfguArf5y07vq4_ym4z98C6S2BhMRxhrNQPTY4ppIIGtCofRuUo9_YpjqFOQMuJromese7yrU7RpfDyGJxC4IswpRO9omFZzNK1ZRKQ7EcxSVx1Wp8P2XxI2YMLfxB_yH-9Q=w273-h259-s-no-gm)

The method works quite well with self-intersecting polygons. The examples below show that the result is pretty interesting.

## The Class for Calculation

Below is the class that makes the calculation of the spline segments, based on the algorithm, exposed above. This class is named `InterpolationUtils`, it has a `static` method (named `InterpolatePointWithBezierCurves`) that returns a list of `BezierCurveSegment`, that will be the solution to our problem.

The class `BezierCurveSegment` has the four properties that define a spline segment: `StartPoint`, `EndPoint`, `FirstControlPoint`, and the `SecondControlPoint`.

As the above algorithm was originally implemented for closed curves, and it is desired that it can be applied for open curves too, a little change is needed. For this reason, the `InterpolatePointWithBezierCurves` method receives a second parameter, a boolean variable named `isClosedCurve`, which determines if the algorithm will return an open or closed curve. Since we take four points (x1 = *the current point*, x2 = *the next point*, but also are required two more points for creating the three edges. x0 = *the current's previous point* and x3 = *the next's next point*), the x0 and x3 points selection will be like this:

* If it is a closed curve if x1 is the first point, then x0 is going to be the latest point (in this implementation, it is the latest but one because the latest point is the same as the first one), and if x2 is the latest point, then x3 is going to be the first point (in a similar way, in this implementation, is going to be the second point).
* If it is an open curve, then x0 = x1 and x3 = x2 for the previous cases.

## The User Control

The user control that we propose is very simple to use, and it works with the MVVM pattern.

The `LandMarkControl` has only two dependency properties, one for the points, and another for the color of the curve. The most important property is the `Points` attached property. It is of `IEnumerable` type, and it assumes that each item has an `X` and `Y` properties.

In case the collection of points implements the `INotifyCollectionChanged` interface, the control will register to the `CollectionChanged` event, and if each point implements the `INotifyPropertyChanged` interface, the control also will register to the `PropertyChanged` event. In this way, every time any point is added or removed, or any point's coordinates changed, the control will be refreshed.

This is the complete user control code behind:

And this is the XAML code:

## Examples of Usage

Using the control for creating the data template for the `LandMarkViewModel`:

Now everywhere a `LandMarkViewModel` is displayed, this data template will show the item as a `LandMarkControl`. It needs to be rendered on a `Canvas`:

This is a final image example:

![](/images/interpolate-2d-points-using-bezier-curves-in-wpf-and-javscript/interpolation-bezier-curves.gif)

## References

* [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Constructing_B.C3.A9zier_curves)
* [De Casteljau's algorithm](https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm#Geometric_interpretation)
* [Interpolation By Bezier Curves](https://agg.sourceforge.net/antigrain.com/research/bezier_interpolation/index.html#PAGE_BEZIER_INTERPOLATION)
