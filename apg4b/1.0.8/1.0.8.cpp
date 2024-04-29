#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int p;
  string text;
  int price;
  int N;
 
  // パターン入力
  cin >> p;

  // パターン1
  if (p == 1) {
    cin >> price;
    cin >> N;
    cout << price * N << endl;
  }
 
  // パターン2
  if (p == 2) {
    cin >> text >> price;
    cin >> N;

    cout << text << "!" << endl;
    cout << price * N << endl;
  } 
}