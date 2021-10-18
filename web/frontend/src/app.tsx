
import * as React from 'react';

import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { createTheme, MuiThemeProvider } from '@material-ui/core';

import * as store from './store';

const css = require('./app.css');

const theme = createTheme({
    palette: {
        primary: {
            main: '#000000',
        },
        secondary: {
            main: '#f44336',
        },
    },
    props: {
        MuiButtonBase: {
            disableRipple: true
        }
    }
});

interface AppContainerProps {
    store?: store.Store
}

function mapStateToProps(state: store.Store): any {
    return {
        store: state
    };
}

export class AppContainerImpl extends React.Component<AppContainerProps, any> {

    private renderLoader(msg: string): React.ReactNode {
        return (
            <div className='loader-container'>
                <div className='loader-vertical-center'>
                    <div className='loader'></div>
                    <div className='loader-text'>{msg}</div>
                </div>
            </div>
        );
    }

    render() {

        return (
            <MuiThemeProvider theme={theme}>

            </MuiThemeProvider>);
    }
}

export const AppContainer = withRouter(
    connect(mapStateToProps)(AppContainerImpl) as any);