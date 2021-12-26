<?php

$json = file_get_contents("php://input");
$data = json_decode($json, true);

session_start();

if("POST" == $_SERVER["REQUEST_METHOD"]) {

  $json = file_get_contents("php://input");
  $data = json_decode($json, true);

  if($data["data"]["attributes"]["email"] !== "sample@email.com"
    || $data["data"]["attributes"]["password"] !== "p@ssw0rd") {

    http_response_code("403");
    return;
  }

  $_SESSION["login"] = true;
}

if("GET" == $_SERVER["REQUEST_METHOD"]) {

  if(!$_SESSION["login"]) {
    http_response_code("403");
    return;
  }

  echo json_encode(array(
    "data" => array(
      "attributes" => array(
        "email" => "sample@email.com",
        "password" => "p@ssw0rd"
      )
    )
  ));
}

