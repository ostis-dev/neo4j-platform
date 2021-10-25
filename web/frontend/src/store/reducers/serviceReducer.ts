import * as services from '../interfaces/services';
import { Action } from '../actions/baseAction';
import * as serviceAction from '../actions/serviceActions';

export function reducer(state: services.Services = services._initServices, action: Action<any>): any {
    switch (action.type) {
        case serviceAction.Type.Init:
            return action.payload;

        default:
            return state;
    }
}
