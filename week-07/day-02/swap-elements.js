'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`


var abc = ["Arthur", "Boe", "Chloe"]

var temporary = abc[2]
abc[2] = abc[0]
abc[0] = temporary

console.log(abc);