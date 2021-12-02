import { Action } from './baseAction';
import * as services from '../interfaces/services';

export namespace Type {
    export const Init = 'SERVICES_INIT';
}

export function Init(services: services.Services): Action<services.Services> {
    return {
        type: Type.Init,
        payload: services,
    };
}
