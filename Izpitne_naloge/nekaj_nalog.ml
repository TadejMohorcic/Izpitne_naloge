let dot_prod (a1, a2, a3) (b1, b2, b3) = a1 * b1 + a2 * b2 + a3 * b3

let fix_second f b = 
  let (f1, f2) = f in
  (f1, b)

let combine_and_filter f xs ys =
  let rec combine_aux acc f xs ys =  