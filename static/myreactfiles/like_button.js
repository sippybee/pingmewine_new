"use strict";
const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { phone: "" };
  }
  handleInputChange = event => {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit = event => {
    event.preventDefault();
    console.log('Phone:', this.state.phone);
  }
//   componentDidMount() {
//     axios.get(`http://128.199.5.86/api/market/ford/mustang/`).then((res) => {
//       console.log(res);
//       const years = res.data;
//       this.setState({ years });
//     });
//   }

  render() {
    return (
        <form onSubmit={this.handleSubmit} className="comment-form" method="POST">
                        <div className="col-md-12">
                            <div className="single-input-inner">
                                <input value={this.state.phone}
            onChange={this.handleInputChange} type="text" name="phone" placeholder="Your Phone Number e.g. 5062345678" id="phone"/>
                            </div>
                        </div>
                        <div className="buttons">
                        <button className="btn btn-border-base wow animated fadeInLeft" data-wow-duration="1.5s" data-wow-delay="0.6s" type="submit">Sign me up! I'am 21+</button>
                        <div className="d-inline-block align-self-center wow animated fadeInLeft" data-wow-duration="1.5s" data-wow-delay="0.7s">
                            <a className="video-play-btn-hover" href="https://www.youtube.com/embed/Wimkqo8gDZ0"> <h6 className="d-inline-block">how we work</h6></a>
                        </div>
                        </div>
                    </form>
    );
  }
}


const domContainer = document.querySelector("#like_button_container");
ReactDOM.render(e(LikeButton), domContainer);
