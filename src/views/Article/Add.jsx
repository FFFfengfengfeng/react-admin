import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { domin } from '../../util';
import { 
    Link,
    Switch,
    Route
} from 'react-router-dom';
import MarkDown from '../components/Markdown';
/**
 * 
 * 
 * @class Add
 * @extends {Component}
 */
class Add extends Component {
    constructor() {
        super();
        this.state = {
            content: '',
            title: '',
        }
    }
    render() {
        return(
            <div className='main'>
                <div className='warpper'>
                    <div className='form'>
                        <span>标题:</span>
                        <input type="text" value={this.state.title} onChange={this.handleChangeTitle.bind(this)}/>
                    </div>
                    {/* <div className='form'>
                        <span>标签:</span>
                        <input type="text"/>
                    </div> */}
                </div>
                <MarkDown handleChangeContent={this.handleChangeContent.bind(this)}></MarkDown>
                <div className='tool'>
                    <Link to='/article' className='btn fr'>返回</Link>
                    <a href='javascript:;' className='btn fr btn-save' onClick={this.handleClick.bind(this)}>保存</a>
                </div>
            </div>
        );
    }
    handleChangeTitle(e) {
        this.setState({
            title: e.target.value
        })
    }
    handleChangeContent(content) {
        this.setState({
            content: content
        })
        // console.log(content);
    }
    handleClick() {
        let _this = this;
        axios({
            method: 'post',
            url: 'http://127.0.0.1:7001/article/add',
            data: {
                title: _this.state.title,
                content: _this.state.content
            }
        }).then((res)=>{
            if (res.data.status === '1') {
                _this.props.history.push('/article');
            }
        });
    }
}

export default Add;