import React, { Component } from "react";
import Comment from "./Comment";

export class ChildrenComments extends Component {
  render() {
    return (
      <>
        {this.props.comments.map(comment => {
          return (
            <li className="list-group">
              <Comment key={comment.id} comment={comment} />
            </li>
          );
        })}
      </>
    );
  }
}

export default ChildrenComments;
