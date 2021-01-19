let option_sum a b = match (a, b) with
  | (None, x) | (x, None) -> None
  | (Some x, Some y) -> Some(x + y)

let twostep_map f g h x =
  let (a, b) = f x in
  (g a, h b)

let function_repeat f xs = 
  let rec aux acc xs = match xs with
    | [] -> acc
    | x :: rest ->
      let n = f x in
      let rec repeat x n list = match n with
        | a when a <= 0 -> list
        | _ -> repeat x (n - 1) (x :: list)
      in aux (repeat x n acc) rest
    in List.rev (aux [] xs)

let rec iterate f stop z = 
  if stop z then z 
  else iterate f stop (f z)

(* Druga naloga *)

type 'a improved_list = 
  | Empty
  | Node of 'a array * 'a improved_list

let test = Node([|1;2;20|],Node([|17;19;20;30|],Node([|100|], Empty)))
let test2 = Node([|1;3;5|],Node([|7;11;16;33|],Node([|100|],Empty)))

(* A naloga *)

let rec count sez = match sez with
  | Empty -> 0
  | Node (x, y) -> Array.length x + count y
(* B naloga *)

let rec nth sez i = match sez with
  | Empty -> None
  | Node (x, y) -> (
    let l = Array.length x in
    if i > l - 1 then nth y (i - l)
    else Some x.(i)
  )

(* C naloga *)

let rec urejen a i =
  if i = 0 then true
  else if a.(i) >= a.(i - 1) then urejen a (i - 1)
  else false

let is_sorted arr = 
  let rec aux zadnji arr = match arr with
    | Empty -> true
    | Node (x, y) -> 
      if x.(0) < zadnji then false
      else
        let l = Array.length x - 1 in
        if urejen x l then aux x.(l) y
        else false
      in
      aux (-1000) arr

(* D naloga *)

let rec update arr i n = match arr with
  | Empty -> Empty
  | Node (x, y) ->
    let l = Array.length x in
    if i > l then Node (x, update y (i - l) n)
    else
      let rec zamenjaj a j acc =
        if j > l - 1 then acc
        else if j != i then zamenjaj a (j + 1) (Array.append acc [|a.(j)|])
        else zamenjaj a (j + 1) (Array.append acc [|n|])
      in
      Node (zamenjaj x 0 [||], y)