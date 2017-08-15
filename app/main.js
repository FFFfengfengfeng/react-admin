/**
 * 把Greester模块返回的元素插入文档
 */
import React from 'react';
import {render} from 'react-dom';
import Greeter from './Greeter.js';

import './app.css';
import './app.less';

render(<Greeter />, document.getElementById('root'));