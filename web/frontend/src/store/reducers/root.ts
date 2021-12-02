import { combineReducers } from 'redux';
import * as user from './userReducer'
import * as services from './serviceReducer'
import * as errors from './errorsReducer'

export const rootReducer = combineReducers({
    user: user.reducer,
    services: services.reducer,
    errors: errors.reducer
});