import React, { Component } from "react";
import ChildrenComments from "./ChildrenComments";

export class Comment extends Component {
  render() {
    const comment = this.props.comment;
    return (
      <div className="list-group">
        <li href="#" className="list-group-item">
          {comment.comment}

          <ChildrenComments comments={comment.reply_set} />
        </li>
      </div>
    );
  }
}

export default Comment;
