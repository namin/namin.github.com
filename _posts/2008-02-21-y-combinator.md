---
layout: post
title: Recursion and the Y Combinator
---

What are recursive definitions? Is it essential to be able to name a function in order to define it in terms of itself? Can we abstract away the idea of recursion by expressing it with just `lambda`'s?

Here is a recursive definition of the factorial function:

{% highlight scheme %}
    (define factorial
      (lambda (n)
        (if (= n 0)
            1
            (* n (factorial (- n 1))))))
{% endhighlight %}

We can think of a recursive definition as a tower of definitions, each one building on top of the previous one(s). In the case of factorial:

{% highlight scheme %}
    F0 = (lambda (n) (if (= n 0) 1 (* n (?? (- n 1)))))
    F1 = (lambda (n) (if (= n 0) 1 (* n (F0 (- n 1)))))
    F2 = (lambda (n) (if (= n 0) 1 (* n (F1 (- n 1)))))
    ...
    Fn = (lambda (n) (if (= n 0) 1 (* n (Fn-1 (- n 1)))))
{% endhighlight %}

Our factorial definition is then the limit of `Fn` as `n` goes to infinity.

Of course, in Scheme, we can define `Fn` as a `lambda` by expanding `Fn-1`, then `Fn-2`, ..., `F0`. However, let's go a step further and abstract away the idea of a finite tower of definitions. All these definitions are similar, except for the call to the previously defined function. So let's just pass the previous function as a parameter (for good measure, we'll use curried paramters).


{% highlight scheme %}
    (lambda (f)
      (lambda (n)
        (if (= n 0)
            1
            (* n (f (- n 1))))))
{% endhighlight %}

This lambda really abstracts away what the factorial is about. Now, how
do we get it started?

Well, for `F0`, we could simply call it like this:

{% highlight scheme %}
    F0 = ((lambda (f)
            (lambda (n)
              (if (= n 0)
                  1
                  (* n (f (- n 1))))))
          ??)
{% endhighlight %}

But let's instead name this pattern, and call it like this:

{% highlight scheme %}
    F0 = (let ((F (lambda (f)
                    (lambda (n)
                      (if (= n 0)
                          1
                          (* n (f (- n 1))))))))
           (F ??))
{% endhighlight %}

Remember that let is just syntactic sugar for `lambda`, so, here is an
equivalent definition of `F0`:

{% highlight scheme %}
    F0 = ((lambda (F)
            (F ??))
          (lambda (f)
            (lambda (n)
              (if (= n 0)
                  1
                  (* n (f (- n 1)))))))
{% endhighlight %}

Now, `F1` is just a matter of making one more call to `F`:

{% highlight scheme %}
    F1 = ((lambda (F)
            (F (F ??)))
          (lambda (f)
            (lambda (n)
              (if (= n 0)
                  1
                  (* n (f (- n 1)))))))
{% endhighlight %}

What we really want is to be able to call F an infinite number of times:

{% highlight scheme %}
    Factorial = ((lambda (F)
                   (F ... (F (F ??)))
                   (lambda (f)
                     (lambda (n)
                       (if (= n 0)
                           1
                           (* n (f (- n 1))))))))
{% endhighlight %}

In practice, the argument `n` being finite, we'll only need a finite tower
of definitions (e.g. we simply need to build up to `Fn` in order to
compute factorial of `n`).

So, instead of constructing the entire tower in advance (which would
never end, anyways), let's build it as we need it:

{% highlight scheme %}
    Factorial = ((lambda (F)
                   (F F))
                 (lambda (F)
                   (lambda (n)
                     (if (= n 0)
                         1
                         (* n ((F F) (- n 1)))))))
{% endhighlight %}

And that's it! We have a perfect definition of factorial without a
recursive define! It really works:

{% highlight scheme %}
    (((lambda (F)
        (F F))
      (lambda (F)
        (lambda (n)
          (if (= n 0)
              1
              (* n ((F F) (- n 1)))))))
      6)
    ;Value: 720
{% endhighlight %}

Let's go further, still. Remember that our goal is to abstract away the
idea of recursion. Right now, it is intermixed with our define-free
expression of factorial. In our factorial expression, factorial is
really just `(F F)`, so let's just be explicit about this:

{% highlight scheme %}
    ((lambda (F)
        (F F))
      (lambda (F)
        ((lambda (factorial)
           (lambda (n)
             (if (= n 0)
                 1
                 (* n (factorial (- n 1))))))
         (F F))))
{% endhighlight %}

Now, we have a problem: we're not building the definitions as needed
anymore, but an infinite tower upfront with the `(F F)` outside the
`if`. How can we be lazy about it? With a lambda, of course! So we wrap
our `(F F)` inside a lambda. And since our factorial function takes one
argument, our lambda will take one argument:

{% highlight scheme %}
    ((lambda (F)
        (F F))
      (lambda (F)
        ((lambda (factorial)
           (lambda (n)
             (if (= n 0)
                 1
                 (* n (factorial (- n 1))))))
         (lambda (x) ((F F) x)))))
{% endhighlight %}

Now, notice how the factorial pattern is totally independent of the rest
of the code. So we can move it out:

{% highlight scheme %}
    ((lambda (fun)
       ((lambda (F)
          (F F))
        (lambda (F)
          (fun (lambda (x) ((F F) x))))))
     (lambda (factorial)
       (lambda (n)
         (if (= n 0)
             1
             (* n (factorial (- n 1)))))))
{% endhighlight %}

Sanity check:

{% highlight scheme %}
    (((lambda (fun)
       ((lambda (F)
          (F F))
        (lambda (F)
          (fun (lambda (x) ((F F) x))))))
      (lambda (factorial)
        (lambda (n)
          (if (= n 0)
              1
              (* n (factorial (- n 1)))))))
     6)
    ;Value: 720
{% endhighlight %}

We've just derived the applicative-order Y combinator.

{% highlight scheme %}
    Y = (lambda (fun)
          ((lambda (F)
             (F F))
           (lambda (F)
             (fun (lambda (x) ((F F) x))))))
{% endhighlight %}

The Y combinator computes the fixed-point function of a function whose
argument is a function: `(Y fun) = (fun (Y fun))`. It abstracts away the
idea of recursion.

### Bibliography ###

* [The Little Schemer, Chapter 9](http://www.ccs.neu.edu/home/matthias/BTLS/)
* [Richard Gabriel, the Why of Y](http://www.dreamsongs.com/Files/WhyOfY.pdf)
