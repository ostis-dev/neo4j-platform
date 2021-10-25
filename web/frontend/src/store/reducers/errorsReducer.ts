import {Action} from '../actions/baseAction';
import * as errors from '../interfaces/errors'
import * as errorsAction from '../actions/errorsActions'

export function reducer(state: errors.Errors = errors._initErrors, action: Action<any>): any {
    switch (action.type) {
        case errorsAction.Type.UpdateErrors:
            return { ...state, ...action.payload };
        default:
            return state;
    }
}
