/**
 * 把Greester模块返回的元素插入文档
 */
const greeter = require('./Greeter');
document.querySelector('#root').appendChild(greeter());