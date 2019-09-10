#include <stdio.h>
#include <stdlib.h>

//==================================================================
typedef unsigned char uchar;
typedef struct _image {
  int rows, cols, maxval;
  uchar *data, type; 	      // pixels de la imagen
   } image; 

//===================================================================


image *carga(char *f) { 
  int rows, cols, maxval;
  FILE *fd;
  fd = fopen(f, "rb");
  image *r;
  char line[100];
  r = (image *)malloc(sizeof(image));
  fgets(line, sizeof(line), fd);
  fscanf(fd, "%d %d %d\n", &rows, &cols, &maxval);
  r->rows = rows;r->cols = cols;
  r->maxval = maxval;
  r->data = (uchar *)malloc(r->rows * r->cols * sizeof(uchar));
  fread(r->data, sizeof(uchar), r->rows * r->cols, fd);
  return r;
}
//---------------------------------------------------------------------

image *procesa(image *r) {
    for (int i=0; i< r->rows * r->cols; i++)
     if (r->data[i] > 150) r->data[i]=255;
    return r;
}
//---------------------------------------------------------------------

void salva(image *r)
{ FILE *si = fopen("result.pgm", "wb");
  fprintf(si, "P5\n%u %u 255\n", r->rows, r->cols);
  fwrite(r->data, 1, r->rows * r->cols * sizeof(uchar), si);
  fclose(si);
}
//----------------------------------------------------------------------


int main(int argc, char *argv[])
{ image *nimg = carga(argv[1]);
  nimg = procesa(nimg); 
  salva(nimg);
}


// gcc taller1.c  -o taller1

// sudo apt install g++

// g++  taller1.cpp  -o taller1
// ./taller1 mdb155.pgm 
//  g++  barracuda2_09042019.cpp -o barracuda2











/* 

#define pix(Im,x,y)  *(Im->data + (x) * Im->cols + (y))


int M[1024][1024];

for (i = 0; i < r->rows; i++)
     for (j = 0; j < r->cols; j++) {
       M[i][j] = r->data[k];

       pix(r,i,j)=255;

       k++;
    };
*/ 
