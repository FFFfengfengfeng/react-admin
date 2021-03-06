﻿import React, { Component } from 'react';
// import ReactDom from 'react-dom';
import { 
    BrowserRouter as Router,
    Route,
    Switch,
} from 'react-router-dom';
import './App.css';

//引入组件
import ArticleList from './views/Article/List';
import ArticleAdd from './views/Article/Add';
import ArticleEdit from './views/Article/Edit';
import Static from './views/Static/Static';
import Header from './views/components/Header';
import Sidebar from './views/components/Sidebar';

class App extends Component {
    /**
     * @class App
     * @extends {Component}
     */
    render() {
        return (
            <Router>
                <div className='container'>
                    <Header></Header>
                    <Sidebar></Sidebar>
                    <Route exact path="/" component={ Static }/>
                    <Switch>
                        <Route exact path="/article" component={ ArticleList }/>
                        <Route path="/article/add" component={ ArticleAdd }/>
                        <Route path="/article/edit/:id" component={ ArticleEdit }/>
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default App;