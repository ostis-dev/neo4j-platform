import * as React from 'react';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';
import {AppBar, Box, Button, Toolbar, Typography} from "@material-ui/core";

class HeaderImpl extends React.Component {
    render() {
        return (
            <Box sx={{ flexGrow: 1, height: '6%'}}>
                <AppBar position="relative">
                    <Toolbar>
                        <Typography variant="h6" component="div" style={{flex: 1}}>
                            OSTIS Neo4j Platform
                        </Typography>
                        <Button component={NavLink} to="/login" color="inherit">Login</Button>
                    </Toolbar>
                </AppBar>
            </Box>
        );
    }
}

export const AppHeader = connect()(HeaderImpl);
