import React, { Component } from 'react';
import ReactDom from 'react-dom';
import BraftEditor from 'braft-editor';
import 'braft-editor/dist/braft.css';

/**
 * 
 * 
 * @class MarkDown
 * @extends {Component}
 */
class MarkDown extends Component {
    constructor() {
        super()
        // this.handleChange = this.handleChange.bind(this);
        // this.handleRawChange = this.handleRawChange.bind(this);
    }
    render() {
        const editorProps = {
            height: 500,
            contentFormat: 'html',
            initialContent: '<p>Hello World!</p>',
            onChange: this.handleChange,
            onRawChange: this.handleRawChange
        }
      
        return (
            <div className="markdown">
              <BraftEditor {...editorProps}/>
            </div>
        )
    }
    handleChange = (content) => {
        console.log(content)
    }
    
    handleRawChange = (rawContent) => {
        console.log(rawContent)
    }
}

export default MarkDown;