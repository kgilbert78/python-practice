// explanation of this from example class component in react docs
// https://reactjs.org/docs/forms.html

class NameForm extends React.Component { // class NameForm(React.Component):
    constructor(props) { // def __init__(self, props):
        super(props); // super().__init__(props)
        this.state = { value: '' }; // self.state = { 'value': ''}

        // in functions "this" refers to the thing that called the function, so if you want "this" to refer to the state (like self in python) you have to "bind" it to itself for each function as below
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        // this.function means the "this" from that function, and (this) is passed to .bind as a parameter. all the thises are refering to the same thing.
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
        // self.setState({ 'value': event.target.value })
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value); // + self.state.value
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name:
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}