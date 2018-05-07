import React, { Component } from 'react';
import {
    NavLink
} from 'react-router-dom';

class Sidebar extends Component {
    render() {
        return (
            <div className='sidebar'>
                <ul className='menu'>
                    <li><h3>FFF后台管理</h3></li>
                    <li><NavLink exact activeClassName='active' to="/">数据统计</NavLink></li>
                    <li><NavLink activeClassName='active' to="/article">文章管理</NavLink></li>
                </ul>
            </div>
        );
    }
}

export default Sidebar;