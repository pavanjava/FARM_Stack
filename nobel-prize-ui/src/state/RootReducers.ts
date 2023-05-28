import {combineReducers} from 'redux';
import {nobelPrizeReducer} from './reducers/nobelPrizeReducer';

export const rootReducer = combineReducers({
    nobilePrizeState: nobelPrizeReducer
});

export type State = ReturnType<typeof rootReducer>