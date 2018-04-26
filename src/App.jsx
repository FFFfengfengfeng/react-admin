import React, { Component } from 'react';
// import ReactDom from 'react-dom';
import { 
    BrowserRouter as Router,
    Route,
    Switch
} from 'react-router-dom';

//引入组件
import Article from './views/Article';
import Static from './views/Static';
import Header from './views/components/Header';
import Sidebar from './views/components/Sidebar';

class App extends Component {
    /**
     * @class App
     * @extends {Component}
     */
    constructor() {
        super();
    }
    render() {
        let activeStyle = {
            color: 'red'
        }
        return (
            <Router>
                <div className='container'>
                    <Header></Header>
                    <Sidebar></Sidebar>
                    <Route path="/article" component={ Article }/>
                    <Route exact path="/" component={ Static }/>
                </div>
            </Router>
        );
    }
}

export default App;