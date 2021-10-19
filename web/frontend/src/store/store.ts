import { User, _initUser } from './interfaces/user';

export interface Store {
    user: User,
}

export const storeInitialState: Store = {
    user: _initUser,
}