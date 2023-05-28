
import {Action} from '../types/genericActionTypes'
import {FETCH_ALL, FETCH_ONE, SAVE_ONE, LOADING} from '../types/nobelPrizeActionTypes';

const initialState = [{
    'year': '',
    'category': '',
    'laureates': [
        {
            'firstname':'',
            'surname':'',
            'motivation':'',
            'share':''
        }
    ],
    'isLoading': false,
    'isAPIError': false
}]

export const nobelPrizeReducer = (state=initialState, action: Action) => {
    switch(action.type){
        case FETCH_ALL:
            return {...state, ...action.payload};
        case FETCH_ONE:
            return;
        case SAVE_ONE:
            return;
        case LOADING:
            return {...state, 'isLoading': action.payload}
        default:
            return state;
    }
}