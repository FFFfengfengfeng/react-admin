import React, { Component } from 'react';
import { 
    Link
} from 'react-router-dom';

/**
 * 
 * 
 * @class Article
 * @extends {Component}
 */
class Article extends Component {
    constructor() {
        super();
    }
    render() {
        return (
            <div className='main'>
                <div className='warpper'>
                    <table className='table'>
                        <thead>
                            <tr>
                                <th>
                                    <input type="checkbox"/>
                                </th>
                                <th>id</th>
                                <th>标题</th>
                                <th>浏览</th>
                                <th>评论</th>
                                <th>日期</th>
                                <th>操作</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <input type="checkbox"/>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                                <td>
                                    <p>1</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div className='page'>
                        <a href="" className='active'>1</a>
                        <a href="">2</a>
                        <a href="">3</a>
                        <a href="">4</a>
                        <a href="">6</a>
                    </div>
                </div>
            </div>
        );
    }
}

export default Article;