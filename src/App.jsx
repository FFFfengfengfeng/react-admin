import React, { Component } from 'react';
// import ReactDom from 'react-dom';
import { 
    BrowserRouter as Router,
    Route,
    Switch
} from 'react-router-dom';

//引入组件
import User from './views/User';
import Profile from './views/Profile';
import Header from './views/components/Header';
import Sidebar from './views/components/Sidebar';

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
                    <Sidebar></Sidebar>
                    <Switch>
                        <Route path="/user" component={ User }/>
                        <Route path="/profile" component={ Profile }/>
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default App;