;; Scheme ;;

; Q1
(define (over-or-under x y)
  (cond
    ((> y x) -1)
    ((< y x) 1)
    (else 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q3
(define lst
  (cons
    (cons 1 nil)
    (cons
        2
        (cons
            (cons 3 4)
            (cons
                5
                nil))))
)

; Q4
(define (filter f lst)
  (if (null? lst)
      nil
      (if (f (car lst))
          (cons
            (car lst)
            (filter f (cdr lst)))
          (filter f (cdr lst))))
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q5
(define (make-adder num)
  (lambda (x) (+ x num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13
