import React, { Component } from 'react';

class Hello extends Component {
    constructor(pros) {
        super(pros);
        this.state = {
            color: 'blue'
        }
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick() {
        this.setState({
            color: 'red'
        });
    }
    render() {
        let style = {
            color: this.state.color
        };
        return(
            <div>
                <h1 style={style}>Hello World {this.props.name}</h1>
                <a href="javascript:;" onClick={this.handleClick}>修改</a>
            </div>
        );
    }
}

export default Hello;