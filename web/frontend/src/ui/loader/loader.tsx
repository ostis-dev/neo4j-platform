require("./loader.css");


import * as React from 'react';

interface LoaderProps {
    msg: string,
}

export class LoaderImpl extends React.Component<LoaderProps, any> {

    render() {
        return (
            <div className='loader-container'>
                <div className='loader-vertical-center'>
                    <div className='loader'></div>
                    <div className='loader-text'>{this.props.msg}</div>
                </div>
            </div>
        );
    }
}

export const Loader = LoaderImpl;