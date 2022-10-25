import java.util.Scanner;

public class Stackarray {
    int[] arr = new int[80];
    int top;

    Stackarray(int top){
        this.top = top;
    }

    void push(int d) {
        if (top == 80) {
            System.out.println("Stack overflow!");
            return;
        } else {
            arr[top] = d;
            top++;
        }
    }

    void pop() {
        if (top == 0) {
            System.out.println("Stsck underflow!");
            return;
        } else {
            top--;
            System.out.println("Item popped.");
        }
    }

    void display() {
        System.out.println("Stack is: ");
        for (int i = top - 1; i > -1; i--) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       
        int p = 50;
        System.out.println("Enter the number of elements: ");
        int top = sc.nextInt();
        Stackarray ob=new Stackarray(top);
        System.out.println("Enter the elements: ");
        for (int i = 0; i < top; i++) {
            ob.arr[i] = sc.nextInt();
        }

        while (p > 0) {
            System.out.println("\n1.Push\n2.Pop\n3.Display\n4.Exit");
            System.out.println("Enter your option: ");
            int ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.println("Enter the value to push:");
                    int d=sc.nextInt();
                    ob.push(d);
                    break;
                case 2:
                    ob.pop();;
                    break;
                case 3:
                    ob.display();;
                    break;
                case 4:
                    p = 0;
                    break;
                default:
                    System.out.println("Invalid option!!!");

            }
        }
    }

}
