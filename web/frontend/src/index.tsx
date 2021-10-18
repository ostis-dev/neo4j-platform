import * as ReactDOM from 'react-dom';
import * as redux from 'redux';

import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

import { configureStore, Store } from './store';
import { AppContainer } from './app';

const store: redux.Store<Store> = configureStore();

ReactDOM.render(
    <Provider store={store}>
        <BrowserRouter>
            <AppContainer />
        </BrowserRouter>
    </Provider>,
    document.getElementById("content")
)