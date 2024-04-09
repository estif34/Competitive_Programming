<?php class Solution {
/**
 * @param Integer $n
 * @return String[]
 */
function fizzBuzz($n) {
    $solution = array();
    for($i=1; $i<=$n; $i++){

    if ($i%3==0 && $i%5==0){
        $solution[]="FizzBuzz";
    }
    else if($i%3==0){
        $solution[]="Fizz";
    }
    else if($i%5==0){
        $solution[]= "Buzz";
    }
    else{$solution[]= "$i";
    }
    }
    return $solution;
}
}
?>