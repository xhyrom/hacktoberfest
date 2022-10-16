// Program to convert temperature taken Celsius and transform into Fahrenheit.



#include<iostream>

using namespace std;

float temp_Conv(float x){
    return (9/5.0)*x + 32.0;
}

int main(){
    float celsius;
    cout<<"Enter the Temperature in Celsius : ";
    cin>>celsius;
    cout<<"Temperature in Fahrenheit is "<<temp_Conv(celsius)<<endl;
    return 0;
}