;;;SI 413 Lab 1
;;;MIDN Pullig

;1
(define ex1 (+ 3.7 (* 4.7(- 34.453 47.728))))

;2
(define ex2 (max (sqrt 5) (+ (sin 1) (sin 2) (sin 3)) (/ 31 13)))

;3
(define ex3 (- (+ (- (* 2 (expt 2.451 3)) (expt 2.451 2)) (* 3 2.451)) 5))

;4
(define root2 (sqrt 2))

;5
(define (to-celsius f)
    (* (/ 5  9) (- f 32)))
(define (to-fahrenheit c)
    (+ 32 (* (/ 9 5) c)))

;6
(define (test-trig x)
    (+ (expt (sin x) 2) (* x (cos x))))

;7
(define (signed-inc x)
    (if (< x 0)
        (+ x -1)
        (+ x 1)))

;8
(define (signed-inc-better x)
    (if (< x 0)
        (+ x -1)
        (if (> x 0)
            (+ x 1)
            (+ x 0))))

;9
(define (middle x y z)
    (if (equal? x (max x y z))
        (if (> y z)
            (display y)
            (display z))
        (if (equal? y (max x y z))
            (if (> x z)
                (display x)
                (display z))
            (if (> x y)
                (display x)
                (display y))
            )
        )
    )

;10
(define (middle-better x y z)
    (cond ((equal? x (max x y z))
           (cond ((> y z) y)
                 (else z)))
          ((equal? y (max x y z))
           (cond ((> x z) x)
                 (else z)))
          (else (cond ((> x y) x)
                      (else y))
                )
          )
    )

;11
(define (factorial x)
    (if (= x 1)
        x
        (* x (factorial (- x 1)))))
;Java would not have given this answer because it would have overflown MAX_INT

;12 WRONG
#|(define (compound-month B r)
  (* B (+1 (/ r 1200))))
(define (accrue-months B r m)
    (if (= m 1)
        ;if
        B
        ;else
        (
         (let bal (* B (+ 1 (/ r 1200))))
         (accrue-months bal r (- m 1))
        )
      )
   )
|#
;13
(define (fib n)
    (cond ((< n 1) 0)
          ((= n 1) 1)
          ((= n 2) 1)
          (else (+ (fib (- n 1)) (fib (- n 2))))))

;14
