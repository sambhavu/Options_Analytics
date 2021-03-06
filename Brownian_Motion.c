//Brownian Motion Simulation 

#include <math.h> 
#include <time.h> 
#include <stdlib.h> 
#include <GL/glub.h> 

#define POINTS 200 
#define WINDOWSIZE 400 
#if defined (_WIN32) 
  #define SEED srand
  #define RANDNUM random 
  #define RANDMAX (lu<<31) -1 
#endif 

typedef GLfloat point[2]; 
point points[POINTS]; 
int Arand, Nrand; 
double GaussAdd, GaussFac, winLimit; 

void InitGauss(int seed); 
double Gauss(); 
void gfxinit(void); 
void display(void); 

void main(int arc, char** argv)
{
  float displacement; 
  int i; 
  
  /* Begin by computing the vertices for the line as the sum of Gaussian 
   * random variables.
   */ 
   
    InitGauss((int) time(NULL)); 
    displacement = 0.0; 
    points[0][0] = points[0][1] = 0.0;
    for(i=1; i<POINTS; i++)
    { 
        displacement += Gauss(); 
        points[i][0] = (float)i; 
        points[i][1] = displacement; 
    } 
    
    winLimit = 2.0 * sqrt((double) POINTS); 
    
    /* set graphics window parameters.*/
    glutInit(&argc, argv);
    gluttInitWindowSize(WINDOWSIZE, WINDOWSIZE); 
    glutInitWindowPosition(200,200);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); 
    glutCreateWIndow("Brownian Motion"); 
    glutDisplayFunc(display); 
    gfxinit(); 
    glutMainLoop(); 
} 

void InitGauss (int seed) 
{
/* Routine for initializing the Gaussian random number generator 
 */ 
 
 Nrand = 4; 
 Arand = RANDMAX; 
 GaussAdd = sqrt(3.0 * (double)Nrand); 
 GaussFac = 2.0 * GaussAdd / ((double)Nrand * (double)Arand); 
 SEED(seed); 
} 

double Gauss()
/* Routine to generate a Gaussian random number
 */ 
 
 double sum; 
 int i;
 sum = 0.0; 
 for(i = 1; i <= Nrand; i++) sum += (double) RANDNUM(); 
 return (GaussFac * sum - GaussAdd); 
}

void gfxinit()
{

  /* This is the routine that generates the image to be displayed. */ 
  
  int i; 
  glMatrixMode(GL_PROJECTION); 
  glLoadIdentity(); 
  gluOrtho2D (0.0, (double) (POINTS-1), -winLimit, wimLimit); 
  glClearColor(1.0, 1.0, 1.0, 0.0); /*Make the background white*/ 
  glColor3f ( 0.0, 0.0, 0.0);     /* Draw in black. 
  glNewList ( 1, GL_COMPILE); 
      glBegin(GL_LINE_STRIP); 
          for(i=0; i<POINTS; i++) glVertex2fv(points[i]); 
      glEnd(); 
  glEndList(); 
} 

void display(void)
{
  /*callback function that gets executed every time the display needs
   *to be updated. 
   */ 
   
   glClear(GL_COLOR_BUFFER_BIT); 
   glCallList(1); 
   glFlush(); 
   
 } 


  
    
