export interface User {
    id: string,
    firstName: string,
    lastName: string,
    login: string,
    password: string,
    online: boolean,
    access_token: string,
}

export const _initUser: User = {
    id: '',
    firstName: '',
    lastName: '',
    login: '',
    password: '',
    online: false,
    access_token: null,
}