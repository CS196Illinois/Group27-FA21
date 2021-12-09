import { Routes, Route, Link, useNavigate } from "react-router-dom";
import Login from "./pages/Login";
import Courses from "./pages/Courses";
import Course from "./pages/Course"
import Assignment from "./pages/Assignment";
import Profile from "./pages/Profile"

function App() {
	let navigate = useNavigate();

	async function handleSubmit(event) {
		event.preventDefault();
		navigate("../profile");
	}

	return (
		<div className="App">
			<div class="container">
				<header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
					<a
						href="/"
						class="d-flex align-items-center mb-md-0 me-md-auto text-dark text-decoration-none"
					>
						<img
							src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/University_of_Illinois_at_Urbana%E2%80%93Champaign_logo.svg/2560px-University_of_Illinois_at_Urbana%E2%80%93Champaign_logo.svg.png"
							height="40"
							onClick={handleSubmit}
						/>
					</a>
				</header>
			</div>
			<Routes>
				<Route path="/" element={<Login />} />
				<Route path="courses" element={<Courses />} />
				<Route path="course" element={<Course />} />
				<Route path="assignment" element={<Assignment />} />
				<Route path="profile" element={<Profile />} />
			</Routes>
		</div>
	);
}

export default App;
