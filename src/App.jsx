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

/**
 * 引入组件
 */
import User from './views/User';
import Profile from './views/Profile';
import Header from './views/components/Header';

/**
 * 
 * 
 * @class App
 * @extends {Component}
 */
class App extends Component {
    constructor() {
        super();
    }
    render() {
        let activeStyle = {
            color: 'red'
        }
        return (
            <Router>
                <div>
                    <Header></Header>
                    <ul>
                        <li><NavLink activeStyle={activeStyle} to="/user">用户管理</NavLink></li>
                        <li><NavLink activeStyle={activeStyle} to="/profile">个人中心</NavLink></li>
                        <Switch>
                            <Route path="/user" component={ User }/>
                            <Route path="/profile" component={ Profile }/>
                        </Switch>
                    </ul>
                </div>
            </Router>
        );
    }
}

export default App;