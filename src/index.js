import React from 'react';
import ReactDOM from 'react-dom';
import Routes from '../src/routes/index';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Routes />, document.getElementById('root'));
registerServiceWorker();
