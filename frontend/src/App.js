import React, { Component, Fragment } from "react";
import Header from "./components/layout/Header";
import "./App.css";
import Dashboard from "./components/blog_post/Dashboard";

export class App extends Component {
  componentDidMount() {
    console.log("Compoenent mounted.");
  }

  render() {
    return (
      <Fragment>
        <Header />
        <Dashboard />
      </Fragment>
    );
  }
}

export default App;
