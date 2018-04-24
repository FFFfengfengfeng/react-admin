import React, { Component } from 'react';
import ReactDom from 'react-dom';
import { 
    BrowserRouter as Router,
    Route,
    Link,
    Redirect,
    NavLink
} from 'react-router-dom';

/**
 * 
 * 
 * @class Profile
 * @extends {Component}
 */
class Profile extends Component {
    constructor() {
        super();
    }
    render() {
        return (
            <div>
                <p>个人中心</p>
                <Link to='/'>返回</Link>
            </div>
        );
    }
}

export default Profile;