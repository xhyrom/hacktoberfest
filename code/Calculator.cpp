# include <iostream>
using namespace std;

int main() {

  char op;
  float a1, a2;

  cout << "Enter operator: +, -, *, /: ";
  cin >> op;

  cout << "Enter two operands: ";
  cin >> a1 >> a2;

  switch(op) {

    case '+':
      cout << a1 << " + " << a2 << " = " << a1 + a2;
      break;

    case '-':
      cout << a1 << " - " << a2 << " = " << a1 - a2;
      break;

    case '*':
      cout << a1 << " * " << a2 << " = " << a1 * a2;
      break;

    case '/':
      cout << a1 << " / " << a2 << " = " << a1 / a2;
      break;

    default:
      // If the operator is other than +, -, * or /, error message is shown
      cout << "Error! operator is not correct";
      break;
  }

  return 0;
}
