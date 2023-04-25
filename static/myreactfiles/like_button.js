"use strict";
const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { phone: "", sent: false, error: false };
  }
  handleInputChange = (event) => {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value,
    });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("https://sippybee.com/ping/api/create/", {
        phone_number: this.state.phone,
      })
      .then((response) => {
        console.log(response);
        this.setState({
          sent: true,
        });
      })
      .catch((error) => {
        console.log(error);
        this.setState({
          error: true,
        });
        setTimeout(() => {
          window.location.reload();
        }, 5000);
      });
  };

  render() {
    if (this.state.sent) {
      return (
        <div>
          <h5
            className="wow animated fadeInLeft"
            data-wow-duration="1.5s"
            data-wow-delay="0.4s"
          >
            We got your number!
          </h5>
        </div>
      );
    }
    return (
      <form onSubmit={this.handleSubmit} className="comment-form" method="POST">
        <div className="col-md-12">
          {this.state.error ? (
            <h6 className="subtitle wow  fadeInLeft animated">
              Something went wrong, use 5062345678 format, we will reload the page
            </h6>
          
          ) : (
            <h6></h6>
          )}
          <div className="single-input-inner">
            <input
              value={this.state.phone}
              onChange={this.handleInputChange}
              type="text"
              name="phone"
              placeholder="Enter Phone Number e.g. 5062345678"
              id="phone"
              className="my-input"
            />
          </div>
        </div>
        <div className="buttons">
          <a><button
            className="btn btn-border-base wow animated fadeInLeft"
            data-wow-duration="1.5s"
            data-wow-delay="0.6s"
            type="submit"
            onClick={() => {
              if (this.state.error) {
                this.setState({  error: false });
              }
            }}
          >
            Sign me up! I'm 21+
          </button></a>
          <div
            className="d-inline-block align-self-center wow animated fadeInLeft"
            data-wow-duration="1.5s"
            data-wow-delay="0.7s"
          >
          </div>
        </div>
      </form>
    );
  }
}

const domContainer = document.querySelector("#like_button_container");
ReactDOM.render(e(LikeButton), domContainer);
