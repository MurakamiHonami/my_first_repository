// // N番目のリュカ数を求める


#include <bits/stdc++.h>
using namespace std;

int main() {
    int64_t N;
    scanf("%ld",&N);
    int64_t cnt=0,l=0;
    vector<int64_t> L;
    while(N>=cnt){
        if(cnt==0){
            L.push_back(2);
            cnt++;
        }
        else if(cnt==1){
            L.push_back(1);
            cnt++;
        }
        else if(cnt==2){
            L.push_back(3);
            cnt++;
        }
        else{
            l=L.at(cnt-1)+L.at(cnt-2);
            L.push_back(l);
            cnt++;
        }
    }
    printf("%ld\n",L.at(N));
    return 0;
}
