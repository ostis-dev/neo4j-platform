import { services, user , errors} from './interfaces';

export interface Store {
    user: user.User,
    services: services.Services,
    errors: errors.Errors
}

export const storeInitialState: Store = {
    user: user._initUser,
    services: services._initServices,
    errors: errors._initErrors
}