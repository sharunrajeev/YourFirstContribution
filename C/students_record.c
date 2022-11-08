#include <stdio.h>
#include <stdlib.h>
typedef struct student{
    int rno;
    char name[20];
    struct subject{
        int scode;
        char sname[20];
        int mark;
    }sub[3];
    int total;
    float per;
}student;

void create(){
    student *s;
    FILE *fp;
    int n,i,j;
    printf("Enter the number of students : ");
    scanf("%d",&n);
    s = (student*)calloc(n,sizeof(student));
    fp = fopen("myStudents.txt","w");


    for(i=0;i<n;i++){
        s[i].total=0;
        s[i].per=0;
        printf("Enter RollNo : ");
        scanf("%d",&s[i]);
        fflush(stdin);
        printf("Enter Name   : ");
        scanf("%[^\n]%*c",s[i].name);
        for(j=0;j<3;j++)
        {
            printf("Enter Marks of Subject%d : ",j+1);
            scanf("%d",&s[i].sub[j].mark);
            s[i].total+=s[i].sub[j].mark;
        }
        s[i].per = s[i].total/3.0;
        fwrite(&s[i],sizeof(student),1,fp);
    }
    fclose(fp);
}
void display(){
    student s1;
    FILE *fp;
    int j;
    fp = fopen("myStudents.txt","r");
    while(fread(&s1,sizeof(student),1,fp))
    {
        printf("\n%-5d%-20s",s1.rno,s1.name);
        for(j=0;j<3;j++){
            printf("%4d",s1.sub[j].mark);
        }
        printf("%5d%7.2f",s1.total,s1.per);
    }

    fclose(fp);

}
void append(){
     student *s;
    FILE *fp;
    int n,i,j;
    printf("Enter the number of students : ");
    scanf("%d",&n);
    s = (student*)calloc(n,sizeof(student));
    fp = fopen("myStudents.txt","a");


    for(i=0;i<n;i++){
        s[i].total=0;
        s[i].per=0;
        printf("Enter RollNo : ");
        scanf("%d",&s[i]);
        fflush(stdin);
        printf("Enter Name   : ");
        scanf("%[^\n]%*c",s[i].name);
        for(j=0;j<3;j++)
        {
            printf("Enter Marks of Subject%d : ",j+1);
            scanf("%d",&s[i].sub[j].mark);
            s[i].total+=s[i].sub[j].mark;
        }
        s[i].per = s[i].total/3.0;
        fwrite(&s[i],sizeof(student),1,fp);
    }
    fclose(fp);


}

void noofrec(){
    student s1;
    FILE *fp;
    fp = fopen("myStudents.txt","r");
    fseek(fp,0,SEEK_END);
    int n=ftell(fp)/sizeof(student);
    printf("\n\nNo of Records = %d",n);
    fclose(fp);
}
void search(){
    student s1;
    int rno;
    int found=0;
    FILE *fp;
    int j;
    fp = fopen("myStudents.txt","r");
    printf("Enter RollNO to Search : ");
    scanf("%d",&rno);
    while(fread(&s1,sizeof(student),1,fp))
    {
        if(s1.rno == rno){
            found = 1;
            printf("\n%-5d%-20s",s1.rno,s1.name);
            for(j=0;j<3;j++){
            printf("%4d",s1.sub[j].mark);
        }
        printf("%5d%7.2f",s1.total,s1.per);

        }

    }
    if(!found)
        printf("\nRecord Not Found\n");

    fclose(fp);

}

void update(){
    student s1;
    int i;
    int rno;
    int found=0;
    FILE *fp ,*fp1;
    int j;
    fp = fopen("myStudents.txt","r");
    fp1 = fopen("temp.txt","w");
    printf("Enter RollNO to Update : ");
    scanf("%d",&rno);
    while(fread(&s1,sizeof(student),1,fp))
    {
        if(s1.rno == rno){
            s1.total=0;
            s1.per=0;
            found = 1;
            fflush(stdin);
            printf("Enter New Name   : ");
            scanf("%[^\n]%*c",s1.name);
            for(j=0;j<3;j++)
            {
                printf("Enter New Marks of Subject%d : ",j+1);
                scanf("%d",&s1.sub[j].mark);
                s1.total+=s1.sub[j].mark;
            }
            s1.per = s1.total/3.0;

            }
            fwrite(&s1,sizeof(student),1,fp1);

    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1 = fopen("temp.txt","r");
        fp  = fopen("myStudents.txt","w");

        while(fread(&s1,sizeof(student),1,fp1)){
            fwrite(&s1,sizeof(student),1,fp);
        }

        fclose(fp);
        fclose(fp1);

    }

    else
        printf("\nRecord Not Found\n");

    fclose(fp);

}

void delete_rec(){
    student s1;
    int i;
    int rno;
    int found=0;
    FILE *fp ,*fp1;
    int j;
    fp = fopen("myStudents.txt","r");
    fp1 = fopen("temp.txt","w");
    printf("Enter RollNO to Delete : ");
    scanf("%d",&rno);
    while(fread(&s1,sizeof(student),1,fp))
    {
        if(s1.rno == rno){
            found=1;
            }
        else
            fwrite(&s1,sizeof(student),1,fp1);

    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1 = fopen("temp.txt","r");
        fp  = fopen("myStudents.txt","w");

        while(fread(&s1,sizeof(student),1,fp1)){
            fwrite(&s1,sizeof(student),1,fp);
        }

        fclose(fp);
        fclose(fp1);

    }

    else
        printf("\nRecord Not Found\n");

    fclose(fp);

}
void sort_total_on_screen(){
    student *s,s1;
    int i,j;
    FILE *fp;
    fp=fopen("myStudents.txt","r");
    fseek(fp,0,SEEK_END);
    int n = ftell(fp)/sizeof(student);
    s = (student*)calloc(n,sizeof(student));

    rewind(fp);
    for( i=0;i<n;i++)
    {
        fread(&s[i],sizeof(student),1,fp);
    }
    fclose(fp);

    for(i=0;i<n;i++)
    {
        for( j=i+1;j<n;j++)
        {
            if(s[i].rno>s[j].rno)
            {
                s1 = s[i];
                s[i]=s[j];
                s[j]=s1;

            }
        }
    }
    fp = fopen("myStudents.txt","w");

    for(i=0;i<n;i++)
    {
        printf("\n%-5d%-20s",s[i].rno,s[i].name);
        for(j=0;j<3;j++){
        printf("%4d",s[i].sub[j].mark);
        }
        printf("%5d%7.2f",s[i].total,s[i].per);
        fwrite(&s[i],sizeof(student),1,fp);


    }


    fclose(fp);



}
void sort_rollno_in_file(){}

int main(){
    int ch;
    do{
        printf("\n1.CREATE");
        printf("\n2.DISPALY");
        printf("\n3.APPEND");
        printf("\n4.NO OF RECORDS");
        printf("\n5.SEARCH");
        printf("\n6.UPDATE");
        printf("\n7.DELETE");
        printf("\n8.SORT BY ROLLNO");
        printf("\n0.EXIT");

        printf("\nEnter your choice : ");
        scanf("%d",&ch);

        switch(ch){
        case 1:
            create();
        break;
        case 2:
            display();
        break;
        case 3:
            append();
        break;
        case 4:
            noofrec();
        break;
        case 5:
            search();
        break;
        case 6:
            update();
        break;
        case 7:
            delete_rec();
        break;
        case 8:
            sort_total_on_screen();
        break;

        }


    }while(ch!=0);




    return 0;
}
