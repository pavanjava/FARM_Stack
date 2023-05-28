import * as Actiontypes from '../types/nobelPrizeActionTypes';
import {nobelPrize} from '../apis/NobelPrizeApis';
import axios from 'axios';

export const fetchAllNobelPrize = () => async (dispatch: Function) => {
    dispatch(dataLoading(true));

    const response = await axios.get(nobelPrize);

    dispatch({
        type: Actiontypes.FETCH_ALL,
        payload: response.data.data
    });

    dispatch(dataLoading(false));
}

export const dataLoading = (isLoading: boolean) => ({
    type: Actiontypes.LOADING,
    payload: isLoading
});