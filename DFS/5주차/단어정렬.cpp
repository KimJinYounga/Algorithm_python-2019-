#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(void){
	int num;
	cin >> num;
	vector <pair<int,string>> words(num);
	for(int i=0;i<num;i++){
		cin >> words[i].second;
		words[i].first=words[i].second.length();
	}

	sort(words.begin(), words.end());

	for(int i=0;i<num-1;i++){
		if(words[i].second==words[i+1].second){
			words.erase(words.begin()+i);
			i--;
			num--;
		}
	}
	for(int i=0;i<num;i++){
		cout << words[i].second << '\n';
	}
}