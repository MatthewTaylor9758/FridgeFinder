import './App.css';
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { useSelector } from 'react-redux';
import SplashPage from './pages/SplashPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';
import ProfilePage from './pages/ProfilePage';

function App() {
  /*
  Will be making my own proxy in Flask when I get there, but for now I am using the
  one I have listed on the line 10(cors-anywhere.herokuapp.com)
  */
  // const makeRequest = async () => {
  //   let res = await fetch('https://cors-anywhere.herokuapp.com/http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3', {
  //     method: 'get',
  //     // mode: '*cors',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //   })
  //   let response = await res.json();
  //   console.log(response);
  // }

  return (
    <BrowserRouter>
      <Switch>
        <Route exact path='/login' component={LoginPage}></Route>
        <Route exact path='/signup' component={SignUpPage}></Route>
        <Route path='/myfridge/:id' component={ProfilePage}></Route>
        <Route path='/' component={SplashPage}></Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
