'use strict';

var promiseBuyApple = function (payment) {
    return new Promise(function (resolve, reject) {
        if (payment >= 150) {
            resolve(payment - 150);
        } else {
            reject('金額が足りません。');
        }
    });
}

//りんごをたくさん買う
promiseBuyApple(400).then(function (change) {
    console.log('おつりは' + change + '円です');
    return promiseBuyApple(change);
}).then(function (change) {
    console.log('おつりは' + change + '円です');
    return promiseBuyApple(change);
}).then(function (change) {
    console.log('おつりは' + change + '円です');
}).catch(function (error) {
    console.log('エラーが発生しました：' + error);
});


/*
var asyncBuyApple = function (payment, callback) {
    setTimeout(function () {
        if (payment >= 150) {
            callback(payment - 150, null);
        } else {
            callback(null, '金額が足りません。');
        }
    }, 1000);
}


//りんごをたくさん買う場合（コールバック地獄）
asyncBuyApple(500, function (change, error) {
    if (change !== null) {
        console.log('１回目のおつりは' + change + '円です。');
        asyncBuyApple(change, function (change, error) {
            if (change !== null) {
                console.log('２回目のおつりは' + change + '円です。');

                asyncBuyApple(change, function (change, error) {
                    if (change !== null) {
                        console.log('３回目のおつりは' + change + '円です。');
                    }
                    if (error !== null) {
                        console.log('３回目でエラーが発生しました：' + error);
                    }
                });
            }
            if (error !== null) {
                console.log('２回目でエラーが発生しました：' + error);
            }
        });
    }
    if (error !== null) {
        console.log('１回目でエラーが発生しました：' + error);
    }
});
*/

