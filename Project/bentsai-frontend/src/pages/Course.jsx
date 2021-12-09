import React from "react";
import { useNavigate } from "react-router-dom";

const Course = () => {
	let navigate = useNavigate();

	async function handleSubmit(event) {
		event.preventDefault();
		navigate("../assignment");
	}

	return (
		<>
			<div class="card text-white bg-primary rounded-3" style={{ height: 200 }}>
				<div class="card-body">
					<h5 class="card-title">STAT 107 - Data Science Discovery</h5>
					<h6 class="card-subtitle mb-2">
						<span class="badge rounded-pill bg-dark">Canvas</span>
					</h6>
					<p class="card-text">
						Fall 2021
						<br />
						ON1
					</p>
				</div>
			</div>
			<br />
			<div class="container">
				<div class="card text-white bg-danger" onClick={handleSubmit}>
					<div class="card-body">
						<h5 class="card-title">Assignment 1</h5>
						<h6 class="card-subtitle mb-2">
							Due: <span class="badge rounded-pill bg-dark">Sep 9, 2021</span>
						</h6>
					</div>
				</div>
				<br />
				<div class="card text-white bg-danger">
					<div class="card-body">
						<h5 class="card-title">Assignment 2</h5>
						<h6 class="card-subtitle mb-2">
							Due: <span class="badge rounded-pill bg-dark">Sep 27, 2021</span>
						</h6>
					</div>
				</div>
			</div>
			<br />
		</>
	);
};

export default Course;
