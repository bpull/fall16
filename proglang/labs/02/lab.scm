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

;7
(define (sum x)
    (if (null? x)
        0
        (+ (car x) (sum (cdr x)))))
(define (average x)
  (/ (sum x) (length x)))
(define (square x)
  (* x x))
(define (square-sum x ave)
  (if (null? x)
      0
      (+ (square (- (car x) ave)) (square-sum (cdr x) ave))))
(define (std-dev x)
  (let ((ave (average x)))
  (sqrt (/ (square-sum x ave) (- (length x) 1)))
    )
  )

;8
;PASS

;9
(define (test-sin x)
    (let ((sinx (+ (square (sin x)) 1)))
      (- (+ (/ 1 sinx) (sqrt sinx)) (square sinx))))

;10
(define (dist a b c d)
    (let ((L1 (+ (* a 12) b))
          (L2 (+ (* c 12) d)))
      (abs (- L1 L2))))

;11
(define (fd-at g n)
  (- (g (+ n 1)) (g n)))

;12
(define (sqrt-prod n)
  