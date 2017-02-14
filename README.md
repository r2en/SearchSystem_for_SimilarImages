# SearchSystem_for_SimilarImages
## 前処理<br>
カラー画像、RGB(256,256,256) = 256^3 = 16,777,316通りに対し、<br>
RGB(0~3,0~3,0~3) = (4^3) = 64色(通り)の減色処理をする。<br>
64次元のデータを、4 * 4 * Red + 4 * Green + Blueの色量子化を行い<br>
ヒストグラムに割り当てる。<br>
<br>
## 類似度<br>
以下、i次元空間の点pと点q間の距離が近いものを類似度とする<br>
交差、ユークリッド距離、マンハッタン距離の三手法での検証を行う<br>
<br>
### 1. 交差 Intersection<br>
#### 式<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22911103/607ddbf6-f2a1-11e6-9446-6102e573cbba.png)
<br>
#### 実行速度<br>
0.1883742 sec
#### 実行結果<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22910204/b5609b28-f29b-11e6-8f54-f0c7f3547004.png)<br>

### 2. ユークリッド距離 Euclid<br>
#### 式<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22911058/39c8a8f6-f2a1-11e6-9d45-34393860d108.png)
<br>
#### 実行速度<br>
0.118295 sec
#### 実行結果<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22910040/edddcb52-f29a-11e6-813c-422a4efacebd.png)<br>
### 3. マンハッタン距離 Manhattan<br>
#### 式<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22911093/55393ec0-f2a1-11e6-98d5-f231205e1310.png)
<br>
#### 実行速度<br>
0.1154851 sec
#### 実行結果<br>
![image](https://cloud.githubusercontent.com/assets/17031124/22910090/1e5cfb0e-f29b-11e6-9c59-2417f7da7069.png)<br>

※ 実行速度は試行回数5の平均値<br>