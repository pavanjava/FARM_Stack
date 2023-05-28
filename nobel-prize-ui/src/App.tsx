import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { useSelector } from 'react-redux';
import { State } from './state/RootReducers';
import { useDispatch } from 'react-redux';
import { fetchAllNobelPrize } from './state/actionCreators/nobelPrizeActionCreator';
import { bindActionCreators } from 'redux';

const App = () => {

  const dispatch = useDispatch();
  const state: any = useSelector((state: State) => state.nobilePrizeState);
  const fetchAllNobelPrizeAction = bindActionCreators(fetchAllNobelPrize, dispatch);

  useEffect(() => {
       fetchAllNobelPrizeAction();
  }, []);

  console.log(state.isLoading);

  return (
    <div className="App">
        
    </div>
  );
}

export default App;
