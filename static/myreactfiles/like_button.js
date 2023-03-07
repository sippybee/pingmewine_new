"use strict";
const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false, years: [] };
  }

//   componentDidMount() {
//     axios.get(`http://128.199.5.86/api/market/ford/mustang/`).then((res) => {
//       console.log(res);
//       const years = res.data;
//       this.setState({ years });
//     });
//   }

  render() {
    if (this.state.liked) {
      return (
        <div><h2 class="title">Huy sobachi</h2></div>
        );
    }

    return (
        <div><h2 class="title" onClick={() => this.setState({ liked: true })}>Empowering businesses with SaaS technology</h2></div>
    );
  }
}


const domContainer = document.querySelector("#like_button_container");
ReactDOM.render(e(LikeButton), domContainer);
