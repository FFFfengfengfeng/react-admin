import React, { Component } from 'react';
import axios from 'axios';
import { domin } from '../../util';
import { 
    Link,
} from 'react-router-dom';
import MarkDown from '../components/Markdown';
/**
 * 
 * 
 * @class Edit
 * @extends {Component}
 */
class Edit extends Component {
    constructor() {
        super();
        this.state = {
            // content: '',
            title: '',
        }
    }
    componentDidMount() {
        let _this = this, id = _this.props.match.params.id;
        _this.getDetail(id);
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
                <MarkDown handleChangeContent={this.handleChangeContent.bind(this)} content={this.state.content} id={this.props.match.params.id}></MarkDown>
                <div className='tool'>
                    <Link to='/article' className='btn fr'>返回</Link>
                    <a href='javascript:;' className='btn fr btn-save' onClick={this.handleSave.bind(this)}>保存</a>
                </div>
            </div>
        );
    }
    getDetail(id) {
        let _this = this;
        axios({
            method: 'post',
            url: domin + '/article/detail',
            data: {
                id: id
            }
        }).then(res => {
            if (res.data.status === '1') {
                // console.log(res.data.result.content);
                _this.setState({
                    content: res.data.result.content,
                    title: res.data.result.title
                });
            }
        });
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
    }
    handleSave() {
        let _this = this;
        axios({
            method: 'post',
            url: domin + '/article/edit',
            data: {
                id: _this.props.match.params.id,
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

export default Edit;