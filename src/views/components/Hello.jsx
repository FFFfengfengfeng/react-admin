import React, { Component } from 'react';

class Hello extends Component {
    constructor(pros) {
        super(pros);
        this.state = {
            color: 'blue',
            clickCount: 0
        }
        this.setStateClick = this.setStateClick.bind(this);
    }
    setStateClick() {
        this.setState({
            color: 'yellow'
        });
    }
    render() {
        let style = {
            color: this.state.color
        };
        return(
            <div>
                <h1 style={style}>Hello World {this.props.name}</h1>
                <p>{this.state.clickCount}</p>
                <a href="javascript:;" onClick={this.setStateClick}>setState</a><br/>
            </div>
        );
    }
}

export default Hello;