#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
class account
{
    char cust_name[20], *acc_type;
    int acc_no;

protected:
    float acc_bal;

public:
    void create_acct(char *);
    void depo();
    void disp();
    void wdrwl();
};
class cur_acct : public account
{
    float min_bal;

public:
    void chk_minbal();
}; // checkbk,no intrst,min balace maintenance
class sav_acct : public account
{
public:
    void intrst();
}; // no checkbk,wdrwl,compound interest
int main()
{
    sav_acct sah1;
    cur_acct cah1;
    int a, b;
label:
    while (1)
    {
        cout << "\nenter type of account:\n1.saving\n2.current\n3.exit\nenter option:";
        cin >> b;
        switch (b)
        {
        case 2:
        {
            int c;
            while (1)
            {
                cout << "\n\nenter function to be done:(Create account before doing other functions)\n1.create account\n2.deposit\n3.display\n4.check minimum balance\n5.withdrawal\n6.Back to previous option\nenter option:";
                cin >> c;
                switch (c)
                {
                case 1:
                    cah1.create_acct("current account");
                    break;
                case 2:
                    cah1.depo();
                    break;
                case 3:
                    cah1.disp();
                    break;
                case 4:
                    cah1.chk_minbal();
                    break;
                case 5:
                    cah1.wdrwl();
                    break;
                case 6:
                    goto label;
                    break;
                default:
                    cout << "error input";
                    break;
                }
            }
        }
        break;
        case 1:
        {
            int d;
            while (1)
            {
                cout << "\n\nenter function to be done(Create account before doing other functions):\n1.create account\n2.deposit\n3.display\n4.interest\n5.withdrawal\n6.Back to previous option\nenter option:";
                cin >> d;
                switch (d)
                {
                case 1:
                    sah1.create_acct("savings account");
                    break;
                case 2:
                    sah1.depo();
                    break;
                case 3:
                    sah1.disp();
                    break;
                case 4:
                    sah1.intrst();
                    break;
                case 5:
                    sah1.wdrwl();
                    break;
                case 6:
                    goto label;
                    break;
                default:
                    cout << "\nerror input\n";
                }
            }
        }
        break;
        case 3:
            exit(0);
            break;
        default:
            cout << "error input";
            break;
        }
    }
    return 0;
}
void account::create_acct(char *s)
{
    cout << "\nenter customer name:";
    cin >> cust_name;
    acc_type = s;
    cout << "enter account no.:";
    cin >> acc_no;
    acc_bal = 0.0;
}
void account::depo()
{
    float amt;
    cout << "\nenter amount to be deposited:";
    cin >> amt;
    acc_bal += amt;
}
void account::disp()
{
    cout << "\ncustomer name: " << cust_name;
    cout << "\ncustomer account type: " << acc_type;
    cout << "\naccount number: " << acc_no;
    cout << "\naccount balance: " << acc_bal;
}
void cur_acct::chk_minbal()
{
    min_bal = 1000;
    if (acc_bal < min_bal)
    {
        acc_bal -= acc_bal * 0.01;
        cout << "\nmin balance maintenance charge reduced from account!";
    }
}
void sav_acct::intrst()
{
    float rate = 0.02, y;
    cout << "enter no. of years:";
    cin >> y;
    acc_bal += acc_bal * pow(1 + (rate / y), y);
    cout << "\ninterest added";
}
void account::wdrwl()
{
    float amt;
    cout << "\nenter amount for withdrawal:";
    cin >> amt;
    if (acc_bal > amt)
        acc_bal -= amt;
    else
        cout << "no sufiicient amount in account to withdraw";
}