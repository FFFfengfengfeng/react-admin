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
                <p>文章管理</p>
            </div>
        );
    }
}

export default Article;