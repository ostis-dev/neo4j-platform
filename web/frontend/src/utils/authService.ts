import * as redux from 'redux'
import * as store from '../store'


export class AuthService {
    private _store: redux.Store<store.Store> = null;

    constructor(st: redux.Store<store.Store>) {
        this._store = st;
        this._store.dispatch(
            store.actions.services.Init({
                authService: this,
            }),
        );
    }

    public updateUser(user: object): void {
        this._store.dispatch(store.actions.user.UpdateUser(user))
    }

    public validateLogin(login: string): void {
        if (!login) {
            this.updateErrors({
                erLoginMsg: "Login is required"
            })
        } else if (!/^[a-z0-9_-]+$/i.test(login)) {
            this.updateErrors({
                erLoginMsg: "Login must contain only letters, numbers, -, _"
            })
        } else {
            this.updateErrors({
                erLoginMsg: ""
            })
        }
    }

    public validatePassword(password: string): void {
        if (!password) {
            this.updateErrors({
                erPasswordMsg: "Password is required"
            })
        } else if (!/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$/i.test(password)) {
            this.updateErrors({
                    erPasswordMsg: "Password must contain one letter and one number and must be longer than 8 characters"
                }
            )
        } else {
            this.updateErrors({
                erPasswordMsg: ""
            })
        }
    }

    public validateFirstName(first_name: string): void {
        if (!first_name) {
            this.updateErrors({
                erFirstNameMsg: "First name is required"
            })
        } else if (!/^[a-zA-Z ]+$/i.test(first_name)) {
            this.updateErrors({
                erFirstNameMsg: "First name must contain letters"
            })
        } else {
            this.updateErrors({
                erFirstNameMsg: ""
            })
        }
    }

    public validateLastName(second_name: string): void {
        if (!second_name) {
            this.updateErrors({
                erLastNameMsg: "Last name is required"
            })
        } else if (!/^[a-zA-Z ]+$/i.test(second_name)) {
            this.updateErrors({
                erLastNameMsg: "Last name must contain letters"
            })
        } else {
            this.updateErrors({
                erLastNameMsg: ""
            })
        }
    }

    public updateErrors(errors: object): void {
        this._store.dispatch(store.actions.errors.UpdateErrors(errors))
    }
}
