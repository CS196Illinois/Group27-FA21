import React from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
	let navigate = useNavigate();

	async function handleSubmit(event) {
		event.preventDefault();
		navigate("courses");
	}

	return (
		<>
			<div class="card text-white bg-dark rounded-3" style={{ height: 100 }}>
				<div class="card-body">
					<h1 class="card-title">Login</h1>
				</div>
			</div>
			<br />
			<div class="container">
				<form onSubmit={handleSubmit}>
					<h2>
						You must log in to <strong>iCourse</strong> to continue.
					</h2>
					<p />
					<div class="mb-3">
						<label for="exampleInputEmail1" class="form-label">
							Enter your <b>NetID</b>
						</label>
						<input class="form-control" />
					</div>
					<div class="mb-3">
						<label for="exampleInputPassword1" class="form-label">
							Enter your <b>password</b>
						</label>
						<input type="password" class="form-control" />
					</div>
					<button type="submit" class="btn btn-dark">
						Login
					</button>
					<p />
					<div class="mb-3 form-check">
						<input
							type="checkbox"
							class="form-check-input"
							id="exampleCheck1"
						/>
						<label class="form-check-label" for="exampleCheck1">
							Clear previous selection for automatically sharing my information
							with this service
						</label>
					</div>
				</form>
				<br />
				<h3>Forgot your password?</h3>
				<p>
					To change or reset your password, go to the{" "}
					<a href="http://go.illinois.edu/password">Password Manager</a>.
				</p>
				<h3>Need to select a different campus?</h3>
				<p>
					<a href="https://discovery.illinois.edu/discovery/DS">
						Clear your remembered campus
					</a>
					and log in again.
				</p>
			</div>
			<br />
		</>
	);
};

export default Login;
