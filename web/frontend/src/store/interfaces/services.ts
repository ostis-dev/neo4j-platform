import {AuthService} from '../../utils/authService'

export interface Services {
    authService: AuthService,
}

export const _initServices: Services = {
    authService: null
};
