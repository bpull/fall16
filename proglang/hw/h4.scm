(define (digits n) 
  (if (zero? n) 
      `()
    (append (digits (quotient n 10)) (list (remainder n 10)))))

(define ups 0)
(define (pushups x)
  (set! ups (+ ups x))
  ups)
(define (print-reverse L)
  (if (not (null? L))
      (begin (print-reverse (cdr L))
             (newline)
             (display (car L)))))

(define (split-inches i)
    (cond ((< i 12) (display (cons 0 i)))
          (else (display (cons (/ (- i (remainder i 12)) 12) (remainder i 12))))
    )
  )

#|(define (print-height inches)
    (cond ((< inches 12) 
                 (cond ((not (eq? inches 1))
                        (display 1 'inch))
                       (else (display inches 'inches))))
          ((eq? inches 12)(display 1 'foot))
          ((< inches 24)
                 (cond ((|#
                         
(define (display-feet f)
    (if (eq? f 1)
        (display "1 foot ")
        (if (eq? f 0)
            (display "")
            (begin (display f)
                   (display " feet ")))
        )
  )
(define (display-inches i)
    (if (eq? i 0)
        (display "")
        (if (eq? i 1)
            (begin (display i)
                   (display " inch"))
            (begin (display i)
                   (display " inches")))))
(define (print-height inches)
    (display-feet (/ (- inches (remainder inches 12)) 12))
    (display-inches (remainder inches 12)))

(define (bigger-num n)
  (max (round (/ n 10)) (remainder n 10)))

(define (bigdigit L)
  (if (null? L)
      0
      (max (bigdigit (cdr L)) (bigger-num (car L)))))

(define (bigdigitL L)
  (apply max (map (lambda (n) (max (round (/ n 10))(remainder n 10))) L)))