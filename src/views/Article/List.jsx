import React, { Component } from 'react';
import axios from 'axios';
import { domin } from '../../util';
import moment from 'moment';
import { 
    Link,
    Switch,
    Route
} from 'react-router-dom';

import Add from './Add';

/**
 * 
 * 
 * @class List
 * @extends {Component}
 */
class List extends Component {
    constructor() {
        super();
        this.state = {
            list: [],
            total: 0
        }
        // this.handleDelete = this.handleDelete.bind(this);
    }
    componentDidMount() {
        this.getList();
    }
    getList() {
        let _this = this;
        axios({
            method: 'post',
            url: 'http://127.0.0.1:7001/article/list',
            data: {
                size: 15,
                page: 1
            }
        }).then((res)=>{
            if (res.data.status === '1') {
                _this.setState({
                    list: res.data.list,
                    total: res.data.total
                });
            }
        });   
    }
    handleDelete(id) {
        let _this = this;
        axios({
            method: 'post',
            url: 'http://127.0.0.1:7001/article/delete',
            data: {
                id: id
            }
        }).then((res)=>{
            if (res.data.status === '1') {
                _this.getList();
            }
        });  
    }
    render() {
        let _this = this;
        return (
            <div className='main'>
                <div className='warpper'>
                    <div className='tool clear'>
                        <div className='search'>
                            <input type="text"/>
                            <a href="" className='btn'>搜索</a>
                        </div>
                        <Link className='btn fr' to='/article/add'>新建</Link>
                    </div>
                    <table className='table'>
                        <thead>
                            <tr>
                                <th>
                                    <input type="checkbox"/>
                                </th>
                                <th>id</th>
                                <th>标题</th>
                                <th>浏览</th>
                                {/* <th>评论</th> */}
                                <th>日期</th>
                                <th>操作</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                _this.state.list.map(function (item, index) {
                                    return  <tr key={ index }>
                                                <td>
                                                    <input type="checkbox"/>
                                                </td>
                                                <td>
                                                    <p>{ item.id }</p>
                                                </td>
                                                <td>
                                                    <p>{ item.title || '' }</p>
                                                </td>
                                                <td>
                                                    <p>{ item.view || 0 }</p>
                                                </td>
                                                <td>
                                                    <p>{ moment(item.created_at).format('YYYY-MM-DD HH:mm:ss') }</p>
                                                </td>
                                                <td className='operate'>
                                                    <Link to={'/article/edit/' + item.id}>编辑</Link>
                                                    <span></span>
                                                    <a href="javascript:;" onClick={_this.handleDelete.bind(item.id)}>删除</a>
                                                </td>
                                            </tr>
                                })
                            }
                        </tbody>
                    </table>
                    <div className='page'>
                        <a href="" className='active'>1</a>
                        <a href="">2</a>
                        <a href="">3</a>
                        <a href="">4</a>
                        <a href="">6</a>
                    </div>
                </div>
            </div>
        );
    }
}

export default List;