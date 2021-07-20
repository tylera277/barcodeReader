# barcodeReader
Program which reads barcodes that are in the form of screenshot's taken from the web.
--Later in the program, I employed a simple one-dimensional clustering algorithm in order to more effectively and accurately read and interpret the stripes of the barcode.


7/20/2021: I have gotten the program to read most barcodes on the left-hand side for right now, I next need to get my program to work for the part of the barcode on the right-hand side of the middle guard.

Below is an example of the output of the program, with the barcode being read and the output written from the program.
<img width="362" alt="barcode_being_read" src="https://user-images.githubusercontent.com/37377528/126339277-4fced5fd-0ecf-4663-83b1-0898a6a4c9f9.png">

<img width="504" alt="barcode_reader_output" src="https://user-images.githubusercontent.com/37377528/126339305-586a34a1-dd59-4cea-9059-976b78f44ab7.png">

This chart is kind of complicated to explain but all thats needed to be known about it is if the four peaks on it are relatively sharp and concentrated, the better my program will run in its current state.
<img width="599" alt="plot" src="https://user-images.githubusercontent.com/37377528/126339331-192a0553-c1eb-4ec6-b87c-8dee667526dc.png">
