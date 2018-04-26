import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { 
    Link,
    Switch,
    Route
} from 'react-router-dom';
import MarkDown from '../components/Markdown';
/**
 * 
 * 
 * @class Add
 * @extends {Component}
 */
class Add extends Component {
    constructor() {
        super();
    }
    render() {
        return(
            <div className='main'>
                <div className='warpper'>
                    <div className='form'>
                        <span>标题:</span>
                        <input type="text"/>
                    </div>
                </div>
                <MarkDown></MarkDown>
                <div className='tool'>
                    <Link to='/article' className='btn fr'>返回</Link>
                    <Link to='/article' className='btn fr btn-save'>保存</Link>
                </div>
            </div>
        );
    }
}

export default Add;