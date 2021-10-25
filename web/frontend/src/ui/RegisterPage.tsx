import {NavLink, useHistory} from "react-router-dom";
import {Box, Button, Container, TextField, Typography} from "@material-ui/core";
import * as React from "react";
import {connect} from "react-redux";
import * as store from "../store";

interface RegisterErrors {
    login: string,
    password: string,
    firstName: string,
    lastName: string
}

export interface RegisterProps {
    services: store.services.Services,
    login: string,
    password: string,
    firstName: string,
    secondName: string,
    online: boolean,
    errors: RegisterErrors,
}

function mapStateToProps(state: store.Store): RegisterProps {
    return {
        services: state.services,
        login: state.user.login,
        password: state.user.password,
        firstName: state.user.firstName,
        secondName: state.user.lastName,
        online: state.user.online,
        errors: {
            login: state.errors.erLoginMsg,
            password: state.errors.erPasswordMsg,
            firstName: state.errors.erFirstNameMsg,
            lastName: state.errors.erLastNameMsg
        }
    };
}

const RegisterImpl: React.FC<RegisterProps> = (props: RegisterProps) => {
    const history = useHistory();
    const {services} = props
    const login = props.login
    const firstName = props.firstName
    const lastName = props.secondName
    const password = props.password
    const errors = props.errors

    async function postRequest(data: object) {
        const url: string = "http://127.0.0.1:5000/users/register"
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
                return Promise.reject("A user with that login already exists")
            }
        }

        doPost().then((response) => {
            if (response["message"] === undefined) {
                services.authService.updateUser({
                    // id: response['id'],
                    access_token: response['access_token'],
                    online: true,
                })
                history.push('/loader');
            }
        }).catch((e) => {
            services.authService.updateErrors({
                erLoginMsg: e
            })
        })
    }

    const handleSubmit = (event) => {
        postRequest({
            'username': login,
            'password': password,
            'full_name': firstName + ' ' + lastName,
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
        } else if (event.target.name == "firstName") {
            services.authService.validateFirstName(event.target.value)
            services.authService.updateUser({
                firstName: event.target.value
            })
        } else if (event.target.name == "lastName") {
            services.authService.validateLastName(event.target.value)
            services.authService.updateUser({
                lastName: event.target.value
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
                <form onSubmit={handleSubmit}>
                    <Box sx={{mb: 3}}>
                        <Typography
                            color="textPrimary"
                            variant="h2"
                        >
                            Create new account
                        </Typography>
                    </Box>
                    <TextField
                        error={Boolean(errors.firstName)}
                        fullWidth
                        helperText={errors.firstName}
                        label="First name"
                        margin="normal"
                        name="firstName"
                        onChange={handleChange}
                        value={firstName}
                        variant="outlined"
                    />
                    <TextField
                        error={Boolean(errors.lastName)}
                        fullWidth
                        helperText={errors.lastName}
                        label="Last name"
                        margin="normal"
                        name="lastName"
                        onChange={handleChange}
                        value={lastName}
                        variant="outlined"
                    />
                    <TextField
                        error={Boolean(errors.login)}
                        fullWidth
                        helperText={errors.login}
                        label="Login"
                        margin="normal"
                        name="login"
                        onChange={handleChange}
                        type="login"
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
                            Sign up
                        </Button>
                    </Box>
                    <Typography
                        color="textSecondary"
                        variant="body1"
                    >
                        Have an account?
                        {' '}
                        <NavLink to="/login" variant="h6" underline="hover" onClick={() => {
                            services.authService.updateUser({
                                firstName: "",
                                lastName: "",
                                login: "",
                                password: "",
                                online: false,
                            })
                        }}>
                            Sign in
                        </NavLink>
                    </Typography>
                </form>
            </Container>
        </Box>
    );
};

export const Register = connect(mapStateToProps)(RegisterImpl);
