import React, { Component, Fragment } from "react";
import axios from "axios";
import Comment from "./Comment";

export class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      comments: []
    };
  }
  componentDidMount() {
    let fetchData = async () => {
      let post_resp = await axios.get("/api/posts/");
      let comment_resp = await axios.get("/api/comments/");

      this.setState({
        posts: post_resp.data,
        comments: comment_resp.data
      });
    };
    fetchData();
  }
  render() {
    const { posts, comments } = this.state;
    return (
      <div className="container">
        <div className="just-padding">
          <div className="list-group list-group-root well">
            {posts.map((post, index) => {
              const postComments = comments.filter(
                item => item.from_post === post.id && item.parent === null
              );
              console.log(postComments);
              return (
                <Fragment>
                  <li href="#" className="list-group-item">
                    <h3>Post {index + 1}</h3>
                    <p>{post.post}</p>
                  </li>
                  {postComments.map((comment, index) => (
                    <Comment comment={comment} />
                  ))}
                </Fragment>
              );
            })}
          </div>
        </div>
      </div>
    );
  }
}

export default Dashboard;
