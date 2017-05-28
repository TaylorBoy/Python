#include <iostream>
#include <string>

using namespace std;

// 销售项目
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
    string isbn;  //书号
    unsigned units_sold;  //销售数量
    double revenue;  //总金额
};


//类   人
class Person
{

public:

    //:这样初始化好,速度快
    Person(const string &p_name, const string &p_address):name(p_name),address(p_address)
    {
        //name = p_name;
        //address = p_address;
    }

    string getName() const  //不修改数据成员
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







