#include <iostream>
#include <string>

using namespace std;

// ������Ŀ
class Sales_item
{
public:
    Sales_item(string &book, unsigned units, double amount)
        : isbn(book), units_sold(units), revenue(amount)
    { }

    double avg_price() const
    {
        if (units_sold )
        {
            return revenue / units_sold;
        }
        else
        {
            return 0;
        }
    }

private:
    string isbn;  //���
    unsigned units_sold;  //��������
    double revenue;  //�ܽ��
};


//��   ��
class Person
{

public:

    //:������ʼ����,�ٶȿ�
    Person(const string &p_name, const string &p_address):name(p_name),address(p_address)
    {
        //name = p_name;
        //address = p_address;
    }

    string getName() const  //���޸����ݳ�Ա
    {
        return name;
    }

    string getAddress() const
    {
        return address;
    }


private:
    string name;
    string address;

};

int main()
{
    Person p("douBi", "FuJian");

    cout << p.getName() << endl;
    cout << p.getAddress() << endl;

    return 0;
}







