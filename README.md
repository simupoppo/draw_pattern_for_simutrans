# draw_pattern_for_simutrans

## about me
このプログラムは、Simutransのアドオン開発向けに、画像の選択された色のドットを、別の指定した、ばらつきのある色に塗り替えるプログラムです。

Simutransのアドオン開発向けにすこし工夫がされております。ご使用の際はご注意ください。

## インストール方法
1. draw_pattern_for_simutrans.exeをダウンロードします。  
2. ダブルクリックまたはターミナルで ./draw_pattern_for_simutrans.exe と入力し起動します。
## 使い方
1. inputする画像を選択します。  
2. 置換するマスの色をRGBの3色で指定します。マスは左から順にR,G,Bです。  
3. 置換するマスの置換後の色をRGBの3色で指定します。入力方法は2.と同じです。  
4. 色の揺らぎを指定します。  
5. 2.-4.が終わったら「色を追加」を押します。置換する色の組み合わせの入力は2.-5.を繰り返してください。
6. 色の追加が終わったら、色の揺らぎ方を指定します。  
7. 「変換を実行」を押し、出力する画像名を指定すると、画像の生成が始まります。

2.-5.の操作は「CSVから変換する色を選択」を押してCSVファイルを指定することで代替できます。その場合、最初の3列が置換前の色(R,G,B)、次の3列が置換後の色(R,G,B)、最後の3行が色の揺らぎ(R,G,B)と入力してください。空欄の行がある場合正しく読み込まれない場合があります。

なお、コマンド引数に以下のように入力することで一括での変換にも対応しています。

./draw_pattern_for_simutrans.exe (input画像とoutput画像を書いたcsvファイル名) (色を指定したcsvファイル名) [gaussian/linear] [3d/1d]


## 注意点
色の指定は必ずR,G,Bの3色について、0-255の整数値を入力してください。

置換前の色に[231,255,255](simutransの透明色)は指定できません(あらかじめほかの色に塗り替えてください)。また、置換後の色に発光色等予約色を指定した場合、予約色以外の色に代替されます(予期せぬ発光等を防ぐためです。)。

入出力する画像のフォーマットはRGB8bitまたはRGBA8bitに対応しています。ただし、塗り替え前の色は透過色が255でない場合塗り替えられず、塗り替え後の色の透過色は255しか出力できません。

## 免責
本プログラムを使用し作成した一切の著作物について、使用・公開に制限はございません。ご自由にお使いください。

本プログラムを閲覧、ダウンロード、起動、使用したことにより発生したいかなる損害について、作者は一切の責任を負いません。

本プログラムの使用に関して気が付いたことがある場合は、twitter(@simu__poppo)までご連絡をお願いします。



## 更新履歴

2023.05.13 V1.00 公開  
2023.06.15 V2.00 同時複数ファイルの変換に対応(不具合あり)  
2023.06.15 V2.10 同時複数ファイル変換に正式に対応  
2025.01.06 V4.00 選択済みの色の削除に関する微修正  

