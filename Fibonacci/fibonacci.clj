(def a (atom 0))
(def b (atom 1))
(dotimes [i 31]
	(println @a)
	(def c (+ @a @b))
	(reset! a @b)
	(reset! b c)
)
