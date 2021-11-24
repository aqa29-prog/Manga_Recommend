// const output_csv = document.getElementById('output_csv');

// function csv_data(dataPath) {
//     const request = new XMLHttpRequest(); // HTTPでファイルを読み込む
//     request.addEventListener('load', (event) => { // ロードさせ実行
//         const response = event.target.responseText; // 受け取ったテキストを返す
//         csv_array(response); //csv_arrayの関数を実行
//     });
//     request.open('GET', dataPath, true); // csvのパスを指定
//     request.send();
// }

// function csv_array(data) {
//     const dataArray = []; //配列を用意
//     const dataString = data.split('\n'); //改行で分割
//     console.log(dataString.length);
//     for (let i = 0; i < dataString.length; i++) { //あるだけループ
//         dataArray[i] = dataString[i].split(',');
//     }
//     let insertElement = ''; //テーブルタグに表示する用の変数
//     dataArray.forEach((element) => { //配列の中身を表示
//         insertElement += '<tr>';
//         element.forEach((childElement) => {
//             insertElement += `<td>${childElement}</td>`
//         });
//         insertElement += '</tr>';
//     });
//     output_csv.innerHTML = insertElement; // 表示
// }
// csv_data('ギャグ・コメディ漫画.csv'); // csvのパス

function getCsv(url) {
    //CSVファイルを文字列で取得。
    var txt = new XMLHttpRequest();
    txt.open('get', url, false);
    txt.send();

    //改行ごとに配列化
    var arr = txt.responseText.split('\n');

    //1次元配列を2次元配列に変換
    var res = [];
    for (var i = 0; i < arr.length; i++) {
        //空白行が出てきた時点で終了
        if (arr[i] == '') break;

        //","ごとに配列化
        res[i] = arr[i].split(',');

        for (var i2 = 0; i2 < res[i].length; i2++) {
            //数字の場合は「"」を削除
            if (res[i][i2].match(/\-?\d+(.\d+)?(e[\+\-]d+)?/)) {
                res[i][i2] = parseFloat(res[i][i2].replace('"', ''));
            }
            console.log(res[i][i2]);
        }
    }

    return res;
}

getCsv('ギャグ・コメディ漫画.csv');
