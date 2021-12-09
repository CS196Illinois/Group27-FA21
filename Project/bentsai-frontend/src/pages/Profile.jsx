import React from "react";

const Profile = () => (
	<>
		<div class="container">
			<h3>Profile</h3>
			<center>
				<img
					src="https://www.pikpng.com/pngl/b/502-5028005_glen-circle-profile-gentleman-clipart.png"
					height="100"
				/>
				<br />
				<br />
				<h5>John Doe</h5>
				<h6 class="text-muted">johndoe2@illinois.edu</h6>
			</center>
			<br />
			<h5>University Services</h5>
			<div class="row">
				<div class="col">
					<center>
						<img
							src="https://pbs.twimg.com/profile_images/951539807527849989/HqfBUc5P_400x400.jpg"
							height="40"
						/>
						<br />
						<span class="text-muted">Self Service</span>
					</center>
				</div>
				<div class="col">
					<center>
						<img
							src="https://www.drought.gov/sites/default/files/hero/partners/university-of-illinois-logo.png"
							height="40"
						/>
						<br />
						<span class="text-muted">myIllini</span>
					</center>
				</div>
				<div class="col">
					<center>
						<img
							src="https://download.logo.wine/logo/Microsoft_Outlook/Microsoft_Outlook-Logo.wine.png"
							height="40"
						/>
						<br />
						<span class="text-muted">Outlook</span>
					</center>
				</div>
				<div class="col">
					<center>
						<img
							src="https://images-platform.99static.com//KlBLMX8dQrcq6hZGnxf5HSnG29I=/8x543:525x1060/fit-in/500x500/99designs-contests-attachments/123/123360/attachment_123360235"
							height="40"
						/>
						<br />
						<span class="text-muted">Course Explorer</span>
					</center>
				</div>
			</div>
			<br />
			<h5>Account & Support</h5>
			<ul class="list-group list-group-flush">
				<li class="list-group-item">⚙️ Settings</li>
				<li class="list-group-item">❓ Help</li>
				<li class="list-group-item">⬅️ Log Out</li>
			</ul>
		</div>
	</>
);

export default Profile;
