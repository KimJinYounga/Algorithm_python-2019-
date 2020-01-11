#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

typedef struct student {
	string name;
	int kor,eng,math;
}student;

bool compare(const student &s1, const student &s2){
	if(s1.kor>s2.kor)
		return true;
	else if(s1.kor==s2.kor){
		if( s1.eng < s2.eng)
			return true;
		if(s1.eng==s2.eng){
			return s1.math > s2.math;
			if(s1.math==s2.math){
				return s1.name < s2.name;
			}
		}
	}

}

int main()
{
    int n;
    cin>>n;
    
    vector<student> a(n);
    for (int i=0; i<n; i++) 
    {
        cin >> a[i].name >> a[i].kor >> a[i].eng >> a[i].math;
    }

	sort(a.begin(), a.end(), compare);
    for(int i=0; i<n; i++)
    {
        cout<<a[i].name<<'\n';
    }
 
    return 0;
}