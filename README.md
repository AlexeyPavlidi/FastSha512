# FastSha512
SHA512 accelerated encryption

How to use it.
1. Place the DLL file (myDLL2_7.dll) to the directory where the Python program/script is located.
it can be placed in other directories, if they are in the %Path system variable.
2. Python Script named -( mainSHADLL_v2_6_7.py <--> myDLL2_7.dll) l this is a Demo showing how to call from the C function from Python. .
Input parameter .- string (in the demo - original_string).
+ Lng - calculated length of the string, which is considered Hash - SHA512.
Output parameter .
the hash is returned as 8 64-bits.global variables(Hs0..hs7) from which the Hash tuple is assembled.
Then it can be converted to an array of bytes or whatever else is required.
3. C code ( MainSHADLLv2_7. c + main.h) - source code for the DLL. Compiled under CodeBloks + GCC. just in case, the compilation keys are given in the comments.
