import {Action} from '../actions/baseAction';
import * as user from '../interfaces/user'
import * as userAction from '../actions/userActions'

export function reducer(state: user.User = user._initUser, action: Action<any>): any {
    switch (action.type) {
        case userAction.Type.UpdateUser:
            return { ...state, ...action.payload };

        default:
            return state;
    }
}
