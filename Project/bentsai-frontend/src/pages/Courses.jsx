import React from "react";
import { useNavigate } from "react-router-dom";

const Grades = () => {
	let navigate = useNavigate();

	async function handleSubmit(event) {
		event.preventDefault();
		navigate("../course");
	}

	return (
		<>
			<div class="container">
				<div
					class="card text-white bg-primary rounded-3"
					style={{ height: 180 }}
					onClick={handleSubmit}
				>
					<div class="card-body d-flex flex-column">
						<h5 class="card-title">STAT 107 - Data Science Discovery</h5>
						<p class="card-text">Section AL1</p>
						<h6 class="card-subtitle mb-2">
							<span class="badge rounded-pill bg-dark">Canvas</span>
						</h6>
						<p class="align-self-end card-text">
							Fall 2021: <b>85.74%</b>
						</p>
					</div>
				</div>
			</div>
			<br />
			<div class="container">
				<div class="card text-white bg-danger" style={{ height: 180 }}>
					<div class="card-body d-flex flex-column">
						<h5 class="card-title">IS 101 - Intro to Information Sciences</h5>
						<p class="card-text">Section AD2</p>
						<h6 class="card-subtitle mb-2">
							<span class="badge rounded-pill bg-dark">Moodle</span>
						</h6>
						<p class="align-self-end card-text">
							Fall 2021: <b>33.33%</b>
						</p>
					</div>
				</div>
			</div>
			<br />
			<div class="container">
				<div class="card text-white bg-success" style={{ height: 180 }}>
					<div class="card-body d-flex flex-column">
						<h5 class="card-title">RST 242 - Nature and American Culture</h5>
						<p class="card-text">Section ONB</p>
						<h6 class="card-subtitle mb-2">
							<span class="badge rounded-pill bg-dark">Compass 2G</span>
						</h6>
						<p class="align-self-end card-text">
							Fall 2021: <b>97.39%</b>
						</p>
					</div>
				</div>
			</div>
		</>
	);
};

export default Grades;
