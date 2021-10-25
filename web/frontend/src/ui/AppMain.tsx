import * as React from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router';
import { Route, Switch } from 'react-router-dom';
import { Login } from './LoginPage';
import {Register} from "./RegisterPage";
import {Loader} from "./loader";

class MainImpl extends React.Component {
    render() {
        return (
            <div className="main">
                <Switch>
                    <Route path="/" exact>
                        <Redirect to="/login" />
                    </Route>
                    <Route path="/login">
                        <Login />
                    </Route>
                    <Route path="/register">
                        <Register />
                    </Route>
                    <Route path="/loader">
                        <Loader msg='Loading...'/>
                    </Route>
                </Switch>
            </div>
        );
    }
}

export const AppMain = connect()(MainImpl);
