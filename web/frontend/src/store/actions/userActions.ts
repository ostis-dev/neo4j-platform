import {Action} from "./baseAction";

export namespace Type {
    export const UpdateUser = 'USER_UPDATE';
}

export function UpdateUser(user: object): Action<object> {
    return {
        type: Type.UpdateUser,
        payload: user,
    };
}