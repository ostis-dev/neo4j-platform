import {Action} from "./baseAction";

export namespace Type {
    export const ChangeErFirstNameMsg = 'ERRORS_CHANGE_FIRST_NAME';
    export const ChangeErLastNameMsg = 'ERRORS_CHANGE_LAST_NAME';
    export const ChangeErLoginMsg = 'ERRORS_CHANGE_LOGIN';
    export const ChangeErPasswordMsg = 'ERRORS_CHANGE_PASSWORD';
    export const UpdateErrors = 'ERRORS_UPDATE'
}

export function UpdateErrors(errors: object): Action<object> {
    return {
        type: Type.UpdateErrors,
        payload: errors,
    };
}
