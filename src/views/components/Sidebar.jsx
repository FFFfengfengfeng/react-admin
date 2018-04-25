import React, { Component } from 'react';
import ReactDom from 'react-dom';
import {
    BrowserRouter as Router,
    Route,
    Link,
    Redirect,
    NavLink,
    Switch
} from 'react-router-dom';

class Sidebar extends Component {
    constructor() {
        super();
    }

    render() {
        return (
            <div className='sidebar'>
                <ul className='menu'>
                    <li><Link to="/user">用户管理</Link></li>
                    <li><Link to="/user">用户管理</Link></li>
                </ul>
            </div>
        );
    }
}

export default Sidebar;