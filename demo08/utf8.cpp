#include <iostream>
#include <string>
#include <cstring>
using namespace std;

/*
 * 深复制和浅复制
 *
 */

class CppDemo
{
public :
    CppDemo(int pa, char *cpp_str)
    {
        this->a = pa;
        this->str = new char[1024];
        strcpy(this->str, cpp_str);
    }

    // C++默认写一个复制构造函数
    // 深复制: 指针复制, 指正所指向的对象也复制
    // 浅复制: 指针复制, 指正所指向的对象没复制, 指向了同一对象

    // 深复制:
    CppDemo(CppDemo &c)
    {
        this->a = c.a;
        this->str = new char[1024];
        if (this->str)
        {
            strcpy(this->str, c.str);
        }
    }


    // 浅复制:
/*    CppDemo(CppDemo &c)
    {
        this->a = c.a;
        this->str = c.str;
    }
*/
    ~CppDemo()
    {
        delete str;
    }

public :
    int a ;
    char *str;

};


int main()
{
    CppDemo c(10, "World");
    CppDemo c1 = c;

    cout << c.a << ", " << c.str << endl;

    //变量a不同, str指向了同一对象.
    c.a = 7;
    strcpy(c.str, "Hello");
    cout << c.a << ", " << c.str << endl;
    cout << c1.a << ", " << c1.str << endl;


    return 0;
}
