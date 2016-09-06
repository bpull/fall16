;1
(define (to-usdollar amt cur)
    (cond ((eqv? cur 'euro)
            (/ amt .76))
          ((eqv? cur 'yen)
           (/ amt 98.18))
          ((eqv? cur 'won)
            (/ amt 1109.85))
          ((eqv? cur 'usd)
            (/ amt 1))
        )
  )

;2
(define (from-usdollar amt cur)
    (cond ((eqv? cur 'euro)
            (* amt .76))
          ((eqv? cur 'yen)
            (* amt 98.18))
          ((eqv? cur 'won)
           (* amt 1109.85)))
        )

;3
(define (convert amt fromCur toCur)
    (from-usdollar (to-usdollar amt fromCur) toCur))

;4
(define (squares i j)
    (if (> i j)
       '()
       (cons (* i i) (squares (+ i 1) j))
       )
    )

;5
(define (longer? L1 L2)
    (cond ((null? L1)
           (display #f))
          ((null? L2)
           (display #t))
          (else (longer? (cdr L1) (cdr L2)))
    ))

;6
(define (sum-cash L)
    (if (null? L)
        0
      (+ (to-usdollar (caar L) (cdar L)) (sum-cash (cdr L)))
        )
    )