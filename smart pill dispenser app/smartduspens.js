// Get references to HTML elements
const form = document.querySelector('form');
const medicationTable = document.querySelector('table');
const elements = document.querySelectorAll('.')

// Define an array to store medications
let medications = [];

// Define a function to render the medication table
function renderTable() {
  // Clear the table
  medicationTable.innerHTML = '';

  // Create table headers
  const headers = `
    <thead>
      <tr>
        <th>Name</th>
        <th>Dosage</th>
        <th>Schedule</th>
        <th>Actions</th>
      </tr>
    </thead>
  `;

  // Create table rows for each medication
  const rows = medications.map((medication, index) => `
    <tr>
      <td>${medication.name}</td>
      <td>${medication.dosage}</td>
      <td>${medication.schedule}</td>
      <td>
        <button onclick="dispenseMedication(${index})">Dispense</button>
        <button onclick="editMedication(${index})">Edit</button>
        <button onclick="deleteMedication(${index})">Delete</button>
      </td>
    </tr>
  `);

  // Combine headers and rows into a single HTML string
  const html = headers + '<tbody>' + rows.join('') + '</tbody>';

  // Set the HTML of the medication table
  medicationTable.innerHTML = html;
}

// Define a function to add a new medication
function addMedication(name, dosage, schedule) {
  // Create a new medication object
  const medication = { name, dosage, schedule };

  // Add the medication to the array
  medications.push(medication);

  // Render the updated medication table
  renderTable();
}

// Define a function to dispense a medication
function dispenseMedication(index) {
  // Remove the medication from the array
  medications.splice(index, 1);

  // Render the updated medication table
  renderTable();
}

// Define a function to edit a medication
function editMedication(index) {
  // Get the medication object from the array
  const medication = medications[index];

  // Set the form values to the medication values
  form.elements['name'].value = medication.name;
  form.elements['dosage'].value = medication.dosage;
  form.elements['schedule'].value = medication.schedule;

  // Remove the medication from the array
  medications.splice(index, 1);

  // Render the updated medication table
  renderTable();
}

// Define a function to delete a medication
function deleteMedication(index) {
  // Remove the medication from the array
  medications.splice(index, 1);

  // Render the updated medication table
  renderTable();
}

// Handle form submission
form.addEventListener('submit', event => {
  event.preventDefault();

  // Get form values
  const name = form.elements['name'].value;
  const dosage = form.elements['dosage'].value;
  const schedule = form.elements['schedule'].value;

  // Add the new medication
  addMedication(name, dosage, schedule);

  // Reset the form
  form.reset();
});
