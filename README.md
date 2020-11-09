# hackathon-portal
Upload portal for the WDSSxWSS Hackathon

## Endpoints:
- / POST
	- Submit a .csv file as well as a .ipynb file
	- Passed along with JWT token/UID
	- Backend validates file extensions
	- Neither file can exceed sizes x and y, determined by Tim
	- Validate that user with UID didn't upload < 1 hour ago
	- Call evaluate with CSV file, which will evaluate against stored ground truth file
- / GET
	- Get the leaderboard, which is either stored or calculated in the backend
	- Pass to the frontend to display with a sidebar form to get the POST request
