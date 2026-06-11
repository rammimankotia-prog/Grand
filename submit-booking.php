<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get JSON input
    $data = json_decode(file_get_contents('php://input'), true);
    
    // If empty, try $_POST (fallback)
    if (empty($data)) {
        $data = $_POST;
    }

    $name = strip_tags(trim($data["name"] ?? ''));
    $email = filter_var(trim($data["email"] ?? ''), FILTER_SANITIZE_EMAIL);
    $phone = strip_tags(trim($data["phone"] ?? ''));
    $date = strip_tags(trim($data["date"] ?? ''));
    $travelers = strip_tags(trim($data["travelers"] ?? ''));
    $notes = strip_tags(trim($data["notes"] ?? ''));
    $tourName = strip_tags(trim($data["tourName"] ?? 'Grand Holidays Tour'));

    if (empty($name) || empty($email) || empty($phone)) {
        http_response_code(400);
        echo json_encode(["message" => "Please fill all required fields (Name, Email, Phone)."]);
        exit;
    }

    $to = "mail@godwinhotels.com";
    $subject = "New Booking Query: " . $tourName;

    $email_content = "Hello Team,\n\n";
    $email_content .= "A new tour booking request has been submitted on the website.\n\n";
    $email_content .= "Tour Requested: $tourName\n";
    $email_content .= "Full Name: $name\n";
    $email_content .= "Email Address: $email\n";
    $email_content .= "Mobile Number: $phone\n";
    $email_content .= "Preferred Date: $date\n";
    $email_content .= "Number of Guests: $travelers\n\n";
    $email_content .= "Custom Requirements/Notes:\n$notes\n\n";
    $email_content .= "Best Regards,\nWebsite Booking System";

    $headers = "From: bookings@" . $_SERVER['HTTP_HOST'] . "\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Cc: $email\r\n"; // Send a copy to the customer

    if (mail($to, $subject, $email_content, $headers)) {
        http_response_code(200);
        echo json_encode(["message" => "Thank you! Your booking request has been sent."]);
    } else {
        http_response_code(500);
        echo json_encode(["message" => "Oops! Something went wrong and we couldn't send your request. Please try contacting us directly."]);
    }
} else {
    http_response_code(403);
    echo json_encode(["message" => "There was a problem with your submission, please try again."]);
}
?>
