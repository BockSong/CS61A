; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (if (null? s)
     nil
     (car (cdr s)))
)

(define (caddr s)
  (if (null? s)
     nil
     (cadr (cdr s)))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0))
)

(define (ordered? s)
  (if (null? (cdr s))
      True
      (if (> (car s) (cadr s))
          False
          (ordered? (cdr s))))
)

(define (nodots s)
  (define (dothelper s) (and (pair? s)
                             (not (pair? (cdr s)))
                             (not (null? (cdr s)))
                             ))
  (cond
    ((null? s) s)
    ((dothelper s) (cons (nodots (car s)) (cons (nodots (cdr s)) nil)))
    ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
    (else s))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((= (car s) v) True)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (addhelper s v lst)
  (cond ((null? s) (append lst (cons v nil)))
        ((> (car s) v) (append lst (cons v s)))
        (else (addhelper (cdr s) v (append lst (cons (car s) nil))))
  ))

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          (else (addhelper s v nil))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((> (car s) (car t)) (intersect s (cdr t)))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (cons (car s) (intersect (cdr s) (cdr t))))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (else (union (cdr s) (add t (car s))))
          ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (helper b n total)
    (if (= n 0)
      total
      (helper b (- n 1) (* b total))))
  (helper b n 1)
)

(define (filter pred lst)
  (define (helper pred lst prelst)
    (if (null? lst)
      prelst
      (if (pred (car lst))
        (helper
          pred
          (cdr lst)
          (append prelst (cons (car lst) nil)))
        (helper
          pred
          (cdr lst)
          prelst))))
  (helper pred lst nil)
)
