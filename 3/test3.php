<?php

// Generate an array of 10 random numbers
$numbers = [];
for ($i = 0; $i < 10; $i++) {
    $numbers[] = rand(1, 10000);
}

// Find the largest number in the array
$largestNumber = max($numbers);

// Output the result
echo "Random array is created: [".implode(", ", $numbers)."]\n";
echo "The greatest number is: ".$largestNumber."\n";

?>