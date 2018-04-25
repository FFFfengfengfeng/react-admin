import React, { Component } from 'react';
import { 
    Link
} from 'react-router-dom';

/**
 * 
 * 
 * @class User
 * @extends {Component}
 */
class User extends Component {
    constructor() {
        super();
    }
    render() {
        return (
            <div>
                <p>用户管理</p>
                <Link to='/'>返回</Link>
            </div>
        );
    }
}

export default User;