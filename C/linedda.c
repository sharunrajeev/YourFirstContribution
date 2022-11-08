#include <graphics.h>
#include <stdio.h>
#include <conio.h>
int main() 
{
    int gd=detect,gm;
    float x,y1,x2,y2,dx,dy,i1,x,y,i2,d,xend,m;
    int($gd,$gm,"");
    printf("\n Enter the value of x1,y1,and x2,y2");
    scanf("%f%f%f%f"&x1,&y1,&x2,&y2);
    clrscr();
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    m=dy/dx;
    if(m<1)
    {
        i1=2*dy;
        i2=2*(dy-dx);
        d=i1-dx;
        if(dx<0)
        {
            x=x2;
            y-y2;
            xend=x1;
        }
        else
        {
            x=x1;
            y=y1;
            xend=x2;
        }
    
    }
    while (x<xend)
    {
        putpixel(x,y,red);
        if(d<0)
        {
        d=d+i1;
        }
        else
        {
            d=d+i2;
            y=y+1;
        }
    }
    x=x+1;
    else
    {
        i1=2*dx;
        i2=2*(dx-dy);
        d=i1-dy;
    }
    if (dy<0)
    {
        x=x1;
        y=y1;
        xend=y1;
    }
    else
    {
        x=x1;
        y=y1;
        xend=y2;

    }
    while (y<xend)
    {
        putpixel(x,y,red);
        if (d<0)
        {
            d=d+12;
        }
        else
        {
            d=d+i2;
            x=x+1;
        }
        y=y+1;
    }
    get ch()
    close graph()
    return 0;
}




































