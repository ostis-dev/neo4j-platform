
import * as React from 'react';

import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { createTheme, MuiThemeProvider } from '@material-ui/core';

import * as store from './store';

import { Loader } from './ui/loader';

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

    render() {

        return (
            <MuiThemeProvider theme={theme}>
                <Loader msg="Loading..."></Loader>
            </MuiThemeProvider>);
    }
}

export const AppContainer = withRouter(
    connect(mapStateToProps)(AppContainerImpl) as any);