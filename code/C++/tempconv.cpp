// Program to convert temperature units.



#include<iostream>

using namespace std;

float Fahrenheit(float x){
    return (9/5.0)*x + 32.0;
}

float Celcius(float x){
    return (5.0/9)*(x-32);
}


int main(){
    float input;
    int type1,type2;
    cout<<"Temperature converter"<<endl;
    cout<<"Convert from (type, enter the respective) :\n";
    cout<<"From Celsius -> 1 \n";
    cout<<"From Fahrenheit -> 2 \n";
    cout<<"From Kelvin -> 3 \n";
    cin>>type1;
    cout<<"Convert to (type, enter the respective) :\n";
    cout<<"From Celsius -> 1 \n";
    cout<<"From Fahrenheit -> 2 \n";
    cout<<"From Kelvin -> 3 \n";
    cin>>type2;
    if(type1 == type2) 
    {
        cout<<"Wrong choice!!!"<<endl;
        return 0;
    }
    cout<<"Enter the temperature : ";
    cin>>input;
    if (type1 == 1 && type2 == 2) // Celsius to Fahrenheit
    {
        cout<<Fahrenheit(input);
    }
    if (type1 == 1 && type2 == 3) // Celsius to Kelvin
    {
        cout<<(input + 273.16);
    }
    if (type1 == 2 && type2 == 1) // Fahrenheit to Celcius
    {
        cout<<Celcius(input);
    }
    if (type1 == 2 && type2 == 3) // Fahrenheit to Kelvin
    {
        cout<<Celcius(input) + 273.16;
    }
    if (type1 == 3 && type2 == 1) // Kelvin to Celcius
    {
        cout<<input - 273.16;
    }
    if (type1 == 3 && type2 == 2) // Kelvin to Fahrenheit
    {
        cout<<Celcius(input) - 273.16;
    }
    cout<<"\n";
    return 0;

}