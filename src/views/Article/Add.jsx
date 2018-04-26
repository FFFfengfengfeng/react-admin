import React, { Component } from 'react';
import { 
    Link,
    Switch,
    Route
} from 'react-router-dom';
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
                <p>添加文章</p>
                <Link to='/article'>返回</Link>
            </div>
        );
    }
}

export default Add;