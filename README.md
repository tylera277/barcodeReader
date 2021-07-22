# barcodeReader
Program which reads barcodes that are in the form of screenshot's taken from the web.
--Later in the program, I employed a simple one-dimensional clustering algorithm in order to more effectively and accurately read and interpret the stripes of the barcode.

7/21/2021: I have gotten the right side of the middle guard to being read with decently high accuracy, some barcodes are capable
of completely making my system go haywire. I am not sure if they are poorly produced barcodes or what not, but most of them do indeed work with my program.

Below is an example of the output of the program, with the barcode being read and the output written from the program.
<img width="769" alt="barcode_being_read" src="https://user-images.githubusercontent.com/37377528/126395619-21a3459d-def3-4412-9878-672718a9b438.png">


<img width="850" alt="barcode_reader_output" src="https://user-images.githubusercontent.com/37377528/126395651-d79d870b-fc86-44c4-a070-103db6c6c1cf.png">


This chart is kind of complicated to explain but all thats needed to be known about it is if the four peaks on it are relatively sharp and concentrated, the better my program will run in its current state.
<img width="627" alt="plot_barcode" src="https://user-images.githubusercontent.com/37377528/126395676-ac77bb12-3432-4488-bb96-ab351a4455c9.png">


