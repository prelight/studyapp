'use strict';

var syncBuyApple = function (payment) {
    if (payment >= 150) {
        return { change: payment - 150, error: null };
    } else {
        return { change: null, error: 150 - payment + '円足りません。' };
    }
}

var result1 = syncBuyApple(500);
if (result1.change !== null) {
    console.log('1つ目のおつりは' + result1.change + '円です。');
}
if (result1.error !== null) {
    console.log('1つ目でエラーが発生しました：' + result1.error);
}
var result2 = syncBuyApple(result1.change);
if (result2.change !== null) {
    console.log('2つ目のおつりは' + result2.change + '円です。');
}
if (result2.error !== null) {
    console.log('2つ目でエラーが発生しました：' + result2.error);
}
var result3 = syncBuyApple(result2.change);
if (result3.change !== null) {
    console.log('3つ目のおつりは' + result3.change + '円です。');
}
if (result3.error !== null) {
    console.log('3つ目でエラーが発生しました：' + result3.error);
}
var result4 = syncBuyApple(result3.change);
if (result4.change !== null) {
    console.log('4つ目のおつりは' + result4.change + '円です。');
}
if (result4.error !== null) {
    console.log('4つ目でエラーが発生しました：' + result4.error);
}

