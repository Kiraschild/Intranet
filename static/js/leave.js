function applyfornewleave() {
    // Get the form element
    var leaveForm = document.getElementById('leaveFormContent');
    
    // Display the form
    leaveForm.style.display = 'block';
    
    function generateRandomLeaveId() {
        // Generate a random number between 100000 and 999999
        return Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000;
    }

    var leaveIdLabel = document.getElementById('leave_id');
    
    // Generate a random 6-digit leave ID and set it in the leave ID label
    var randomLeaveId = generateRandomLeaveId();
    leaveIdLabel.textContent = `Leave ID: ${randomLeaveId}`;

    var element = document.getElementById("leave_id");
    // Store the leave ID in a data attribute for use when submitting the form
    element.dataset.leaveId = randomLeaveId;

}

function submitleaveform(event){

    event.preventDefault(); // Prevent the form from submitting in the default way
    // Retrieve form data
    var element = document.getElementById("leave_id");
    var leaveId = element.dataset.leaveId
    var leavestartDate = document.getElementById("leave_Startdate").value;
    var leaveenddate = document.getElementById("leave_Enddate").value;
    var subject = document.getElementById("subject").value;
    var status = "Pending";

    var startDate = new Date(leavestartDate);
    var endDate = new Date(leaveenddate);

    // Calculate the time difference in milliseconds
    var timeDifference = endDate - startDate;

    // Convert the time difference from milliseconds to days
    var totalDays = timeDifference / (1000 * 60 * 60 * 24);

    
    // Add a new row to the table
    addLeaveRecordToTable(leaveId, leavestartDate, leaveenddate, totalDays, subject, status);
    
    var leaveForm = document.getElementById('leaveFormContent');
    leaveForm.style.display = 'none';
    document.getElementById("leave_Startdate").value = "";
    document.getElementById("leave_Enddate").value = "";
    document.getElementById("subject").value = "";

    hideForm();
    
    
}
function addLeaveRecordToTable(leaveId, leavestartDate, leaveenddate, totalDays, subject, status) {
    // Get the table body element
    var tableBody = document.getElementById('leaveRecordsTable').getElementsByTagName('tbody')[0];
    
    // Create a new row as an HTML string
    var newRowHTML = `
        <tr>
            <td>${leaveId}</td>
            <td>${leavestartDate}</td>
            <td>${leaveenddate}</td>
            <td>${totalDays}</td>
            <td>${subject}</td>
            <td>${status}</td>
        </tr>
    `;
    
    // Append the new row to the table body using innerHTML
    tableBody.innerHTML += newRowHTML;

}

function showForm() {
    document.getElementById('overlayForm').style.display = 'block';
    document.getElementById('leaveFormContent').style.display = 'block';
    applyfornewleave(); // Call the function to generate leave ID and display the form
}


// function confirmLogout() {
//     window.location.href = '/logout';
// }

function cancelButton() {
    hideForm();
}

function hideForm() {
    document.getElementById('overlayForm').style.display = 'none';
    document.getElementById('leaveFormContent').style.display = 'none';
}