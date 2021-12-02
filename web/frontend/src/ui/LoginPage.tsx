import {NavLink, useHistory} from "react-router-dom";
import {Box, Button, Container, TextField, Typography} from "@material-ui/core";
import * as React from "react";
import {connect} from "react-redux";
import * as store from '../store';

interface LoginErrors {
    login: string,
    password: string
}

export interface LoginProps {
    services: store.services.Services,
    login: string;
    password: string;
    online: boolean;
    errors: LoginErrors
}

function mapStateToProps(state: store.Store): LoginProps {
    return {
        services: state.services,
        login: state.user.login,
        password: state.user.password,
        online: state.user.online,
        errors: {login: state.errors.erLoginMsg, password: state.errors.erPasswordMsg}
    };
}

const LoginImpl: React.FC<LoginProps> = (props: LoginProps) => {
    const history = useHistory()
    const login = props.login
    const password = props.password
    const services = props.services
    const errors = props.errors


    async function postRequest(data: object) {
        const url: string = "http://127.0.0.1:5000/users/login"
        const doPost = async () => {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Authorization": "Bearer dev",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            if (response.ok) {
                return Promise.resolve(response.json())
            } else {
                return Promise.reject("Bad login or password")
            }
        }

        doPost().then((response) => {
            if (response["message"] === undefined) {
                services.authService.updateUser(
                    {
                        // id: response['id'],
                        // firstName: response['first_name'],
                        // lastName: response['last_name'],
                        access_token: response['access_token'],
                        online: true,
                    }
                )
                history.push('/loader');
            }
        }).catch((e) => {
            services.authService.updateErrors({
                erLoginMsg: e,
                erPasswordMsg: e
            })
        })
    }

    const handleSubmit = (event) => {
        postRequest({
            'username': login,
            'password': password
        })
        event.preventDefault()
    }

    const handleChange = (event) => {
        if (event.target.name == "login") {
            services.authService.validateLogin(event.target.value)
            services.authService.updateUser({
                login: event.target.value
            })
        } else if (event.target.name == "password") {
            services.authService.validatePassword(event.target.value)
            services.authService.updateUser({
                password: event.target.value
            })
        }
    }

    return (
        <Box
            sx={{
                backgroundColor: 'background.default',
                display: 'flex',
                flexDirection: 'column',
                height: '94%',
                justifyContent: 'center'
            } as React.CSSProperties}
        >
            <Container maxWidth="sm">
                <form onSubmit={handleSubmit} autoComplete='off'>
                    <Box sx={{mb: 3}}>
                        <Typography
                            color="textPrimary"
                            variant="h2"
                        >
                            Sign in
                        </Typography>
                    </Box>
                    <TextField
                        error={Boolean(errors.login)}
                        fullWidth
                        helperText={errors.login}
                        label="Login"
                        margin="normal"
                        name="login"
                        onChange={handleChange}
                        value={login}
                        variant="outlined"
                    />
                    <TextField
                        error={Boolean(errors.password)}
                        fullWidth
                        helperText={errors.password}
                        label="Password"
                        margin="normal"
                        name="password"
                        onChange={handleChange}
                        type="password"
                        value={password}
                        variant="outlined"
                    />
                    <Box sx={{py: 2}}>
                        <Button
                            color="primary"
                            fullWidth
                            size="large"
                            type="submit"
                            variant="contained"
                        >
                            Sign in
                        </Button>
                    </Box>
                    <Typography
                        color="textSecondary"
                        variant="body1"
                    >
                        Don&apos;t have an account?
                        {' '}
                        <NavLink to="/register" variant="h6" underline="hover" onClick={() => {
                            services.authService.updateUser({
                                firstName: "",
                                lastName: "",
                                login: "",
                                password: "",
                                online: false,
                            })
                        }}>
                            Sign up
                        </NavLink>
                    </Typography>
                </form>
            </Container>
        </Box>
    );
};

export const Login = connect(mapStateToProps)(LoginImpl);