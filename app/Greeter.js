/**
 * 定义返回问候信息的html元素函数
 * 依据CommonJS规范导出这个函数为一个模块
 */
import React, {Component} from 'react';
import config from './config.json';
import styles from './Greeter.css';

class Greeter extends Component{
    render() {
        return (
            <div className={styles.root}>
                {config.greetText}
            </div>
        )
    }
}

export default Greeter