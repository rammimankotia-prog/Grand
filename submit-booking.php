<?php
header('Content-Type: application/json');
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type, Accept");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = json_decode(file_get_contents('php://input'), true);
    if (empty($data)) {
        $data = $_POST;
    }

    $email = filter_var(trim($data["email"] ?? ''), FILTER_SANITIZE_EMAIL);
    $tourName = strip_tags(trim($data["_subject"] ?? $data["tourName"] ?? 'Grand Holidays Query'));
    
    // Check if it's a newsletter subscription
    $isNewsletter = (stripos($tourName, 'Newsletter') !== false);

    if ($isNewsletter) {
        if (empty($email)) {
            http_response_code(400);
            echo json_encode(["message" => "Please enter a valid email address."]);
            exit;
        }

        $to = "mail@godwinhotels.com";
        $subject = "New Newsletter Subscription";
        $email_content = "Hello Team,\n\nYou have a new newsletter subscriber:\nEmail: $email\n\nBest Regards,\nWebsite System";
        $headers = "From: webmaster@" . (isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : 'grandholidaytours.com') . "\r\n";
        
        if (mail($to, $subject, $email_content, $headers)) {
            http_response_code(200);
            echo json_encode(["message" => "Successfully subscribed."]);
        } else {
            http_response_code(500);
            echo json_encode(["message" => "Server error."]);
        }
        exit;
    }

    // Standard Tour Booking
    $name = strip_tags(trim($data["name"] ?? ''));
    $phone = strip_tags(trim($data["mobile"] ?? $data["phone"] ?? ''));
    $date = strip_tags(trim($data["preferredDate"] ?? $data["date"] ?? ''));
    $travelers = strip_tags(trim($data["guestsCount"] ?? $data["travelers"] ?? ''));
    $notes = strip_tags(trim($data["message"] ?? $data["notes"] ?? ''));
    $estimatedPrice = strip_tags(trim($data["estimatedPrice"] ?? ''));

    if (empty($name) || empty($email) || empty($phone)) {
        http_response_code(400);
        echo json_encode(["message" => "Please fill all required fields (Name, Email, Phone)."]);
        exit;
    }

    $to = "mail@godwinhotels.com";
    $subject = $tourName;

    $email_content = "Hello Team,\n\n";
    $email_content .= "A new tour booking request has been submitted on the website.\n\n";
    $email_content .= "Tour/Subject: $tourName\n";
    if (!empty($estimatedPrice)) {
        $email_content .= "Estimated Price: $estimatedPrice\n";
    }
    $email_content .= "Full Name: $name\n";
    $email_content .= "Email Address: $email\n";
    $email_content .= "Mobile Number: $phone\n";
    $email_content .= "Preferred Date: $date\n";
    $email_content .= "Number of Guests: $travelers\n\n";
    $email_content .= "Custom Requirements/Notes:\n$notes\n\n";
    $email_content .= "Best Regards,\nWebsite Booking System";

    $headers = "From: bookings@" . (isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : 'grandholidaytours.com') . "\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Cc: $email\r\n"; // Send a copy to the customer

    if (mail($to, $subject, $email_content, $headers)) {
        http_response_code(200);
        echo json_encode(["message" => "Thank you! Your booking request has been sent."]);
    } else {
        http_response_code(500);
        echo json_encode(["message" => "Oops! Something went wrong and we couldn't send your request. Please try contacting us directly."]);
    }
} else if ($_SERVER["REQUEST_METHOD"] == "OPTIONS") {
    http_response_code(200);
    exit;
} else {
    http_response_code(403);
    echo json_encode(["message" => "There was a problem with your submission, please try again."]);
}
?>
