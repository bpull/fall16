;Brandon Pullig 175148
(define (sqr x) (* x x))

;Problem 1
(define (root-info L)
  (let ((discrim (- (sqr (cadr L)) (* 4 (* (car L) (caddr L))))))
      (cond ((< discrim 0)
             0)
            ((= discrim 0)
             1)
            ((> discrim 0)
             2))
    )
  )

;Problem 2
;fold-help is a tail recursive help function to fold
(define (fold-help A B L)
  (if (null? A)
      (if (null? B)
          L
          (append L B))
      (if (null? B)
          (append L A)
          (fold-help (cdr A) (cdr B) (append L (cons (car A) (cons (car B) '()))))
          )
      )
  )
(define (fold A B) (fold-help A B '()))

;Problem 3
(define (total-length LoL)
  (apply + (map length LoL)))

;Problem 4
(define (mkpiece f g x0)
  (lambda (x)
    (cond ((> x x0)
           (g x))
          (else (f x))
          )
    )
  )

;Problem 5
;sumpos-help is the tail-recursive helper function
(define (sumpos-help args accum)
  (if (null? (cdr args))
      (if (> (car args) 0)
          (+ accum (car args))
          accum)
      (if (> (car args) 0)
           (sumpos-help (cdr args) (+ accum (car args)))
           (sumpos-help (cdr args) accum))
  ))
(define (sumpos x . args)
  (let ((v (append (list x) args)))
    (sumpos-help v 0))
  )

;Problem 6
(define (compose f g)
  (lambda (x)
    (f (g x)))
  )

;Problem 7
(define (make-rebooter start)
  (let ((last start))
    (let ((day (+ start 86400)))
      (lambda (time)
        (cond ((< time last)
               (display "bad time")
               (newline))
              ((> time last)
               (cond ((< time day)
                      (set! last time))
                     ((> time day)
                      (begin (display "reboot")
                             (newline)
                             (set! last time)
                             (set! day (+ time 86400)))
                      )
                     )
               )
              )
        ))))