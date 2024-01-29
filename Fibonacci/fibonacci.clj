(loop [n 30 a 0 b 1]
	(println a)
	(if (> n 0)
		(recur (dec n) b (+ a b))
		n
	)
)
