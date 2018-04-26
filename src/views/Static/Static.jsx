import React, { Component } from 'react';
import ReactDom from 'react-dom';
import { 
    Link,
} from 'react-router-dom';

/**
 * 
 * 
 * @class Static
 * @extends {Component}
 */
class Static extends Component {
    constructor() {
        super();
    }
    render() {
        return (
            <div className='main'>
                <p>数据统计</p>
            </div>
        );
    }
}

export default Static;