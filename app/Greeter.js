/**
 * 定义返回问候信息的html元素函数
 * 依据CommonJS规范导出这个函数为一个模块
 */
module.exports = function() {
    let greet = document.createElement('div');
    greet.textContent = 'Hi there and greetings';
    return greet;
}