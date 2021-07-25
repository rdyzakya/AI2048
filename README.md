# AI2048
Repositori ini berisikan source code AI 2048 menggunakan algoritma minimax dan expectimax.

https://user-images.githubusercontent.com/56197074/126901674-7b8ebd42-c755-4f4d-9e8f-d7bb0e46b765.mp4

## How To Use
Berikut adalah cara untuk menggunakan source code AI 2048:

1. Pastikan Python telah tersedia (diharapkan versi 3.7 ke atas, program ini dibuat di Python 3.8.5)
2. Pastikan tersedia library numpy dan IPython.display (digunakan untuk merender gamenya di notebook)
3. Siapkan file ipynb agar dapat melihat gamenya dengan lebih nyaman
4. Lakukan import source code

```python
from src import ai2048
```

5. Panggil fungsi play jika ingin melihat 1 kali run sebuah ai pada game

```python
game_record, point = ai2048.play(depth=5,how='minimax',render=True)
```
```
Parameters:
depth : int (kedalaman algoritma minimax atau expectimax pada ai)
how : {'minimax', 'expectimax'}, default='minimax' (algoritma yang dipakai ai)
render : boolean, default=False (jika ingin melihat ai bermain secara langsung)

return record (list of board, bisa dimainkan menggunakan play_record), max_point(perolehan tile tertinggi)
```

5. Jika parameter render bernilai False, bisa gunakan fungsi play_record untuk memperlihatkan alur permainan yang sudah diselesaikan

```python
ai2048.play_record(game_record)
```

6. Jika ingin melakukan run dengan jumlah yang banyak dan mengharapkan permainan dirun sebanyak yang diinginkan maka gunakan fungsi train

```python
score_data, nice_record = ai2048.train(run=100,val=1024,render=True)
```
```
Parameters:
run : int (jumlah run permainan)
val : int, default=1024 (tentukan permainan dengan max_point berapa yang dimasukan ke dalam list of records)
render : boolean, default=False (jika ingin melihat ai bermain secara langsung)

return score_data (list of max_point dari seluruh run), nice_record (list of records yang menempuh max_point sebesar val)
```
