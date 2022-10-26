/*
C++ Program on Ceasor Cipher (Cryptography)
In Ceasor Cipher technique, We substitute each character of the message 
with another character where both characters are related with a key.
The key is a  fixed number so that character can be substitute by fixed number
of positions down in the alphabet.

For example: 
message = "ABCDEFGHI"
key = 2
Encrypted Message = "CDEFGHIJK";
where A->C, B->D, and so on.

Encryption function:
E(x) = (x+key)mod26;
*/

#include<iostream>

using namespace std;

string encrypter(string msg, int shift){
	string en_msg = ""; // storing encrypted message.
	
	for(int i = 0; i < msg.length(); i++){
		
		if(isupper(msg[i])){
			//  Encryption Function
			en_msg += char(int(msg[i] + shift -65 )%26 + 65);
			}
			else{
				en_msg += char(int(msg[i] + shift -97 )%26 + 97);	
				}
		}
		return en_msg;
	}

int main()
{
	string message = "HelloWorld!";
	int shift = 3;
	cout<<"Encrypted Message : "<<encrypter(message,shift)<<endl;
	return 0;
}