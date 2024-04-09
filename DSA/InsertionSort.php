<?php

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1($n, $arr) {
    // Write your code here
    $t = $arr[($n-1)];
    for($i=($n-2); $i>=0; $i--){
        if($t<$arr[$i]){
        $arr[$i+1] = $arr[$i];
        }
        else{
        $arr[$i+1]= $t;
        }
        $result = "";
        for($j=0; $j<$n; $j++){
            $result = $result.$arr[$j]." ";
        }
        echo $result . "\n";
    }

}

$n = intval(trim(fgets(STDIN)));

$arr_temp = rtrim(fgets(STDIN));

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

insertionSort1($n, $arr);

?>