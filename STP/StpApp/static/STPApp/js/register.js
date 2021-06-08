const form = document.getElementById('form');
const name = document.getElementById('name');
const email = document.getElementById('email');
const aadhar = document.getElementById('aadhar');
const mobile = document.getElementById('mobile');
const address = document.getElementById('address');
const fname = document.getElementById('fname');
const occupation = document.getElementById('occupation');
const institute = document.getElementById('institute');
const percentage = document.getElementById('percentage');
const cgpa = document.getElementById('cgpa');
const sem = document.getElementById('sem');

form.addEventListener('submit', e => {
	e.preventDefault();

	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces
	const nameValue = name.value.trim();
	const emailValue = email.value.trim();
	const aadharValue = aadhar.value.trim();
	const mobileValue = mobile.value.trim();
	const addressValue = address.value.trim();
	const fnameValue = fname.value.trim();
	const instituteValue = institute.value.trim();
	const semValue = sem.value.trim();
	const percentageValue = percentage.value.trim();
	const cgpaValue = cgpa.value.trim();
	const occupationValue = occupation.value.trim();

	if (nameValue === '') {
		setErrorFor(name, 'Name cannot be blank');
	} else {
		setSuccessFor(name);
	}
	if (fnameValue === '') {
		setErrorFor(fname, 'Father\'s Name cannot be blank');
	} else {
		setSuccessFor(fname);
	}
	if (semValue === '') {
		setErrorFor(sem, 'Semester/Year cannot be blank');
	} else {
		setSuccessFor(sem);
	}
	if (instituteValue === '') {
		setErrorFor(institute, 'Institute Name cannot be blank');
	} else {
		setSuccessFor(institute);
	}
	if (percentageValue === '') {
		setErrorFor(percentage, 'Percentage Name cannot be blank');
	} else {
		setSuccessFor(percentage);
	}
	if (cgpaValue === '') {
		setErrorFor(cgpa, 'Percentage Name cannot be blank');
	} else {
		setSuccessFor(cgpa);
	}

	if (occupationValue === '') {
		setErrorFor(occupation, 'Occupation cannot be blank');
	} else {
		setSuccessFor(occupation);
	}

	if (addressValue === '') {
		setErrorFor(address, 'Address cannot be blank');
	} else {
		setSuccessFor(address);
	}
	if (emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	} else {
		setSuccessFor(email);
	}

	if (aadharValue === '') {
		setErrorFor(aadhar, 'Aadhar Number cannot be blank');
	} else if (!isAadhar(aadharValue)) {
		setErrorFor(aadhar, 'Not a valid aadhar number');
	}
	else {
		setSuccessFor(aadhar);
	}

	if (mobileValue === '') {
		setErrorFor(mobile, 'Mobile Number cannot be blank');
	} else if (!isMobile(mobileValue)) {
		setErrorFor(mobile, 'Not a valid mobile number or not in prescribed format');
	} else {
		setSuccessFor(mobile);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
	alert("Congrats! Form Submitted!");
	$('.alert').alert();
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function isMobile(mobile) {
	return /^\+?([9][1])\)?[- ]?([0-9]{10})$/.test(mobile);
}

function isAadhar(aadhar) {
	return /^\(?([0-9]{4})\)?[- ]?([0-9]{4})[- ]?([0-9]{4})$/.test(aadhar);
}
function photoValidation(ph) {
	var fileInput = document.getElementById(ph);
	var filePath = fileInput.value;
	var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
	if (!allowedExtensions.exec(filePath)) {
		alert("Please uplaod file having extensions .jpg/ .jpeg/ .png only");
		fileInput.value = '';
		return false;
	}
}
function fileValidation(ty) {
	var fileInput = document.getElementById(ty);
	var filePath = fileInput.value;
	var allowedExtensions = /(\.pdf)$/i;
	if (!allowedExtensions.exec(filePath)) {
		alert("Please uplaod file having extension pdf only");
		fileInput.value = '';
		return false;
	}
}
