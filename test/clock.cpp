//C++入門　EX24 - 時計の実装
//正の数が入力されたら時計を進める
//負の数が入力されたら時計を戻す
#include <bits/stdc++.h>
using namespace std;

struct Clock{
    int hour;
    int minute;
    int second;
    void set(int h,int m,int s){
        hour=h;
        minute=m;
        second=s;
    }
    string to_str(){
      string h=to_string(hour);
      string m=to_string(minute);
      string s=to_string(second);
      if (h.size()==1){
        h="0"+h;
      }
      if (m.size()==1){
        m="0"+m;
      }
      if (s.size()==1){
        s="0"+s;
      }
      string time=h+":"+m+":"+s;
      return time;
    }
    void shift(int diff_second){
      if(diff_second>0){
        hour+=diff_second/3600;
        int minutes=diff_second%3600;
        minute+=minutes/60;
        second+=minutes%60;
        if(second>59){
          minute+=1;
          second-=60;
        }
        if(minute>59){
          hour+=1;
          minute-=60;
        }
        if(hour>23){
          hour-=24;
        }

      }
      else{
        hour+=diff_second/3600;
        int minutes=diff_second%3600;
        minute+=minutes/60;
        second+=minutes%60;
        if(second<0){
          minute-=1;
          second+=60;
        }
        if(minute<0){
          hour-=1;
          minute+=60;
        }
        if(hour<0){
          hour+=24;
        }
      }
    }
};
int main() {
  // 時刻入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  //加減算する秒数を受け取る
  int diff_second;
  cin >> diff_second;

  Clock clock;

  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;
}
