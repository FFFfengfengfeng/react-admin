import React, { Component } from 'react';
import BraftEditor from 'braft-editor';
import 'braft-editor/dist/braft.css';

/**
 * 
 * 
 * @class MarkDown
 * @extends {Component}
 */
class MarkDown extends Component {
    render() {
        let editorProps = {
            height: 500,
            contentFormat: 'html',
            initialContent: this.props.content,
            onChange: this.handleChange,
            onRawChange: this.handleRawChange,
            contentId: this.props.id
        }
      
        return (
            <div className="markdown">
              <BraftEditor {...editorProps}/>
            </div>
        )
    }
    handleChange = (content) => {
        this.props.handleChangeContent(content);
    }
    
    handleRawChange = (rawContent) => {
        // this.props.handleChange(rawContent);
    }
}

export default MarkDown;