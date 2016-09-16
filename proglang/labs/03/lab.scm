(#%require racket/base)

;1
;TAIL RECURSIVE
(define (which-sin L minnum)
  (if (not (null? L))
      (if (= (sin (car L)) minnum)
          (car L)
          (which-sin (cdr L) minnum))
      #t
      )
  )
(define (min-sin x . args)
    (let ((minnum (apply min x (map sin args))))
      (if (eq? minnum (sin x))
          x
          (which-sin args minnum))))


;2
(define (take-n L n)
    (if (null? L)
        '()
        (if (= 0 n)
            '()
            (cons (car L) (take-n (cdr L) (- n 1)))
            )
        )
    )
(define (remove-n L n)
  (if (null? L)
      '()
      (if (= 0 n)
          L
          (remove-n (cdr L) (- n 1)))))
(define (group n x . args)
  (if (not (null? args))
      ((let ((L (append (list x) args)))
         (if (not (null? L))
             (cons (take-n L n) (group n (remove-n L n)))
            '())
         ))
      ((if (not (null? x))
             (cons (take-n x n) (group n (remove-n x n)))
            '())
         )
      )
    )

;3
(define (power n)
  (lambda (x)
    (expt x n)))


;4 recieved help from sijing qiu
;TAIL RECURSIVE
(define (call_c*rs L y)
  (if (null? L)
      y
      (cond ((eqv? (car L) 'a) (call_c*rs (cdr L) (car y)))
            ((eqv? (car L) 'd) (call_c*rs (cdr L) (cdr y)))
            )
      )
  )
      
(define (make-cXr x . args)
  (let (( L (reverse (cons x args))))
    (lambda (y) (call_c*rs L y))))

;5
(define (make-stack) 
  (let ((L '())) 
    (lambda (command . data)
      (cond ((eqv? command 'size) 
             (length L))
            ((eqv? command 'pop) 
             (display (car L))
             (newline)
             (set! L (cdr L)))
            ((eqv? command 'push)
             (set! L (append data L)))
      )
    )
  ))

;6
(define (make-set) 
  (let ((L '())) 
    (lambda (command . data)
      (cond ((eqv? command 'get) 
             L)
            ((eqv? command 'set!) 
             (set! L (car data)))
            ((eqv? command 'size)
             (length L))
      )
    )
  ))

;7
(define (contains? L data)
  (if (null? L)
      #f
      (if (< data (car L))
           (contains? (cdr L) data)
           (if (= data (car L))
               #t
               #f
               )
           )
      )
  )
(define (insert-help L data)
  (if (not (null? (cdr data)))
      (if (not (contains? L data))
           ((append L data)(sort L <)(insert-help L (cdr data))))
      )
      L
  )
(define (make-set) 
  (let ((L '())) 
    (lambda (command . data)
      (cond ((eqv? command 'get) 
             L)
            ((eqv? command 'set!) 
             (set! L (car data)))
            ((eqv? command 'size)
             (length L))
            ((eqv? command 'insert!)
             (set! L (insert-help L data))
             (set! L (sort L <)))
            ((eqv? command 'contains?)
             (contains? L data))
      )
    )
  ))