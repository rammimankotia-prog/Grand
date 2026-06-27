<?php
header('Content-Type: application/json');
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type, Accept");

// --- SMTP Configuration ---
// Set SMTP_ENABLED to true to send emails via SMTP.
// Set to false to use the standard PHP mail() function.
define('SMTP_ENABLED', true);
define('SMTP_HOST', 'smtp.godwinhotels.com');
define('SMTP_PORT', 587); // 587 (TLS), 465 (SSL), or 25
define('SMTP_USER', 'tours@godwinhotels.com');
define('SMTP_PASS', 'YOUR_SMTP_PASSWORD'); // <-- REPLACE WITH YOUR EMAIL PASSWORD
define('SMTP_SECURE', 'tls'); // 'tls', 'ssl', or ''

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = json_decode(file_get_contents('php://input'), true);
    if (empty($data)) {
        $data = $_POST;
    }

    $email = filter_var(trim($data["email"] ?? ''), FILTER_SANITIZE_EMAIL);
    $tourName = strip_tags(trim($data["_subject"] ?? $data["tourName"] ?? 'Grand Holidays Query'));
    
    // Check if it's a newsletter subscription
    $isNewsletter = (stripos($tourName, 'Newsletter') !== false);

    $to = "tours@godwinhotels.com";

    if ($isNewsletter) {
        if (empty($email)) {
            http_response_code(400);
            echo json_encode(["success" => false, "message" => "Please enter a valid email address."]);
            exit;
        }

        $subject = "New Newsletter Subscription";
        $email_content = "Hello Team,\n\nYou have a new newsletter subscriber:\nEmail: $email\n\nBest Regards,\nWebsite System";
        
        $headers = [];
        $headers["From"] = "Grand Holidays Website <" . (SMTP_ENABLED ? SMTP_USER : "webmaster@" . ($_SERVER['HTTP_HOST'] ?? 'grandholidaytours.com')) . ">";
        $headers["Reply-To"] = $email;
        $headers["MIME-Version"] = "1.0";
        $headers["Content-Type"] = "text/plain; charset=UTF-8";

        $success = send_email($to, $subject, $email_content, $headers);

        if ($success) {
            http_response_code(200);
            echo json_encode(["success" => true, "message" => "Successfully subscribed."]);
        } else {
            http_response_code(500);
            echo json_encode(["success" => false, "message" => "Server error. Could not process subscription."]);
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

    if (empty($name) || empty($email) || empty($phone) || empty($date)) {
        http_response_code(400);
        echo json_encode(["success" => false, "message" => "Please fill all required fields: Name, Email, Mobile Number, and Preferred Date."]);
        exit;
    }

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

    $headers = [];
    $headers["From"] = "Grand Holidays <" . (SMTP_ENABLED ? SMTP_USER : "bookings@" . ($_SERVER['HTTP_HOST'] ?? 'grandholidaytours.com')) . ">";
    $headers["Reply-To"] = $email;
    $headers["Cc"] = $email; // Send a copy to the customer
    $headers["MIME-Version"] = "1.0";
    $headers["Content-Type"] = "text/plain; charset=UTF-8";

    $success = send_email($to, $subject, $email_content, $headers);

    if ($success) {
        http_response_code(200);
        echo json_encode(["success" => true, "message" => "Thank you! Your booking request has been sent."]);
    } else {
        http_response_code(500);
        echo json_encode(["success" => false, "message" => "Oops! Something went wrong and we couldn't send your request. Please try contacting us directly."]);
    }
} else if ($_SERVER["REQUEST_METHOD"] == "OPTIONS") {
    http_response_code(200);
    exit;
} else {
    http_response_code(403);
    echo json_encode(["success" => false, "message" => "There was a problem with your submission, please try again."]);
}

// Mail Dispatcher Helper
function send_email($to, $subject, $message, $headers_arr) {
    if (SMTP_ENABLED) {
        try {
            return send_smtp_email($to, $subject, $message, $headers_arr);
        } catch (Exception $e) {
            // Fallback to PHP mail() if SMTP fails
            error_log("SMTP failed: " . $e->getMessage() . ". Falling back to PHP mail().");
            return send_php_mail($to, $subject, $message, $headers_arr);
        }
    } else {
        return send_php_mail($to, $subject, $message, $headers_arr);
    }
}

// PHP mail() Fallback
function send_php_mail($to, $subject, $message, $headers_arr) {
    $headers = "";
    foreach ($headers_arr as $key => $val) {
        $headers .= "$key: $val\r\n";
    }
    return mail($to, $subject, $message, $headers);
}

// SMTP Client Implementation
function send_smtp_email($to, $subject, $message, $headers_arr) {
    $host = SMTP_HOST;
    if (SMTP_SECURE === 'ssl') {
        $host = "ssl://" . SMTP_HOST;
    }
    
    $smtp_conn = @fsockopen($host, SMTP_PORT, $errno, $errstr, 15);
    if (!$smtp_conn) {
        throw new Exception("Could not connect to SMTP host: $errstr ($errno)");
    }
    
    $response = fgets($smtp_conn, 512);
    
    fwrite($smtp_conn, "EHLO " . ($_SERVER['HTTP_HOST'] ?? 'localhost') . "\r\n");
    $response = fgets($smtp_conn, 512);
    while (substr($response, 3, 1) === '-') {
        $response = fgets($smtp_conn, 512);
    }
    
    if (SMTP_SECURE === 'tls') {
        fwrite($smtp_conn, "STARTTLS\r\n");
        $response = fgets($smtp_conn, 512);
        if (substr($response, 0, 3) !== '220') {
            fclose($smtp_conn);
            throw new Exception("STARTTLS failed: " . $response);
        }
        if (!stream_socket_enable_crypto($smtp_conn, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
            fclose($smtp_conn);
            throw new Exception("Failed to start TLS encryption");
        }
        // Resend EHLO after starting TLS
        fwrite($smtp_conn, "EHLO " . ($_SERVER['HTTP_HOST'] ?? 'localhost') . "\r\n");
        $response = fgets($smtp_conn, 512);
        while (substr($response, 3, 1) === '-') {
            $response = fgets($smtp_conn, 512);
        }
    }
    
    if (SMTP_USER !== '' && SMTP_PASS !== 'YOUR_SMTP_PASSWORD' && SMTP_PASS !== '') {
        fwrite($smtp_conn, "AUTH LOGIN\r\n");
        $response = fgets($smtp_conn, 512);
        if (substr($response, 0, 3) !== '334') {
            fclose($smtp_conn);
            throw new Exception("AUTH LOGIN failed: " . $response);
        }
        
        fwrite($smtp_conn, base64_encode(SMTP_USER) . "\r\n");
        $response = fgets($smtp_conn, 512);
        if (substr($response, 0, 3) !== '334') {
            fclose($smtp_conn);
            throw new Exception("SMTP username rejected: " . $response);
        }
        
        fwrite($smtp_conn, base64_encode(SMTP_PASS) . "\r\n");
        $response = fgets($smtp_conn, 512);
        if (substr($response, 0, 3) !== '235') {
            fclose($smtp_conn);
            throw new Exception("SMTP password rejected: " . $response);
        }
    }
    
    // Sender
    $from_email = SMTP_USER !== '' ? SMTP_USER : "bookings@" . ($_SERVER['HTTP_HOST'] ?? 'grandholidaytours.com');
    fwrite($smtp_conn, "MAIL FROM:<" . $from_email . ">\r\n");
    $response = fgets($smtp_conn, 512);
    if (substr($response, 0, 3) !== '250') {
        fclose($smtp_conn);
        throw new Exception("MAIL FROM failed: " . $response);
    }
    
    // Recipients
    $recipients = [$to];
    if (isset($headers_arr["Cc"])) {
        $recipients[] = $headers_arr["Cc"];
    }
    if (isset($headers_arr["Bcc"])) {
        $recipients[] = $headers_arr["Bcc"];
    }
    
    foreach ($recipients as $rcpt) {
        // Extract email if in "Name <email>" format
        if (preg_match('/<([^>]+)>/', $rcpt, $matches)) {
            $rcpt_email = $matches[1];
        } else {
            $rcpt_email = trim($rcpt);
        }
        if (!empty($rcpt_email)) {
            fwrite($smtp_conn, "RCPT TO:<" . $rcpt_email . ">\r\n");
            $response = fgets($smtp_conn, 512);
            if (substr($response, 0, 3) !== '250') {
                fclose($smtp_conn);
                throw new Exception("RCPT TO failed for $rcpt_email: " . $response);
            }
        }
    }
    
    // Data
    fwrite($smtp_conn, "DATA\r\n");
    $response = fgets($smtp_conn, 512);
    if (substr($response, 0, 3) !== '354') {
        fclose($smtp_conn);
        throw new Exception("DATA command failed: " . $response);
    }
    
    // Build SMTP payload
    $headers = "";
    foreach ($headers_arr as $key => $val) {
        $headers .= "$key: $val\r\n";
    }
    $headers .= "To: $to\r\n";
    $headers .= "Subject: =?UTF-8?B?" . base64_encode($subject) . "?=\r\n";
    
    $body = $headers . "\r\n" . $message;
    $body = str_replace("\r\n.", "\r\n..", $body);
    
    fwrite($smtp_conn, $body . "\r\n.\r\n");
    $response = fgets($smtp_conn, 512);
    if (substr($response, 0, 3) !== '250') {
        fclose($smtp_conn);
        throw new Exception("Sending message body failed: " . $response);
    }
    
    // Quit
    fwrite($smtp_conn, "QUIT\r\n");
    fclose($smtp_conn);
    return true;
}
?>
