import React, { Component } from 'react';
class Tool extends Component {
    /**
     * 
     * 
     * @class Tool
     * @extends {Component}
     */
    constructor() {
        super();
    }
    render() {
        return(
            <div className='tool clear'>
                <div className='search'>
                    <input type="text"/>
                    <a href="" className='btn'>搜索</a>
                </div>
                <a href="" className='btn fr'>新建</a>
            </div>
        );
    }
}

export default Tool;