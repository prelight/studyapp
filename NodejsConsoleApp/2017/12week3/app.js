'use strict';

var fetchSomething1 = function () {
    return new Promise(function (resolve, reject) {
        // API1にアクセス
        doAjaxStuff(someOptions, {
            success: function (data) { // 成功した場合
                resolve();
            },
            fail: function () { // 何かしらエラーが発生した場合
                reject({ message: 'APIにアクセスできませんでした' });
            }
        });
    });
};

fetchSomething1().then(function () {
    alert('API1よりデータを取得しました');
}, function (error) {
    alert('API1よりデータを取得できませんでした。エラーメッセージ: ' + error.message);
});

