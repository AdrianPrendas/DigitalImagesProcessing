
import itertools
"""
    author: prendas.adrian@gmail.com
"""
import array

class PGMio:
    def __str__(self):
        return  """
                    input_file: str
                    header: { type, cols_rows, maxValue }
                    data: [int]
                    matrixForm :[[int]]
                    cols: int
                    rows: int
                    output_file: str
                    writeFile(output_file:str)
                """
    def __init__(self, input_file, mode="rb"):
        self.input_file = input_file
        
        f = open(input_file, mode)
        L = f.readlines()
        f.close()

        self.header = {
            "type": L[0].decode().rstrip(),
            "cols_rows":L[1].decode().rstrip(),
            "maxValue":L[2].decode().rstrip()
        }
        self.cols = int(self.header["cols_rows"].split(" ")[0])
        self.rows = int(self.header["cols_rows"].split(" ")[1])

        L3 = [L[i] for i in range(3,len(L))]
        L4 = [array.array('B', e).tolist() for e in L3 ]

        self.data = list(itertools.chain(*L4))
        self.matrixForm = [self.data[i*self.cols:(i+1)*self.cols] for i in range(0,self.cols)]
        
        matrixForm = list(itertools.chain(*self.matrixForm))
        data = self.data
        cols = self.cols
        rows = self.rows
        print("readed" if cols*rows == len(data) and len(data)==len(matrixForm)  else "fail")

    def writeFile(self, output_file, mode="wb"):
        self.output_file = output_file

        newFileByteArray = bytearray(self.data)

        f2 = open(output_file, mode)

        f2.write(str(self.header["type"]+"\n").encode()) # type
        f2.write(str(self.header["cols_rows"]+"\n").encode()) # matrix size; cols * rows
        f2.write(str(self.header["maxValue"]+"\n").encode()) # max value
        f2.write(newFileByteArray) # data

        f2.close()
        print(f"{output_file} was written")

if __name__ == "__main__":
    pgm = PGMio("./../mdb155.pgm")
    
    data = pgm.data

    o = map(lambda x: 0 if x>190 else x,data) 

    pgm.data = o

    pgm.writeFile("out.pgm")


