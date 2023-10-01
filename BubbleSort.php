<?php

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps($a) {
    // Write your code here
    $swapCount=0;
    $n = count($a);
    for ($i = 0; $i < $n; $i++) {
        for ($j = 0; $j < $n - 1; $j++) {
        // Swap adjacent elements if they are in decreasing order
        if ($a[$j] > $a[$j + 1]) {
            $t = $a[$j];
            $a[$j] = $a[$j+1];
            $a[$j+1] = $t;
            // swap($a[$j], $a[$j + 1]);
            $swapCount++;
            }
        }     
}
    $last = ($a[count($a) -1]);
    echo "Array is sorted in " .$swapCount . " swaps. \n";
    echo "First Element: " . $a[0] . "\n";
    echo "Last Element: ". $last . "\n";
}

$n = intval(trim(fgets(STDIN)));

$a_temp = rtrim(fgets(STDIN));

$a = array_map('intval', preg_split('/ /', $a_temp, -1, PREG_SPLIT_NO_EMPTY));

countSwaps($a);
