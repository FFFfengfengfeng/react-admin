import React from 'react';
import { 
    BrowserRouter as Router,
    Route,
    Link,
    Redirect 
} from 'react-router-dom';

/*views*/
import Home from '../Home';
import About from '../About';

const Routes = () => {
    return (
        <Router>
            <Route path="/" component={ Home }>
                <Route path="/about" component={ About }/>
            </Route>   
        </Router>
    );
};

export default Routes;