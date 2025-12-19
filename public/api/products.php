<?php
require_once "../../config/db.php";

$limit = 12;
$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$start = ($page - 1) * $limit;

$sql = "SELECT SQL_CALC_FOUND_ROWS * FROM tvs ORDER BY id DESC LIMIT $start,$limit";
$res = $conn->query($sql);

$data = [];
while ($row = $res->fetch_assoc()) {
    $data[] = $row;
}

$total = $conn->query("SELECT FOUND_ROWS() total")->fetch_assoc()['total'];
$pages = ceil($total / $limit);

echo json_encode([
    "products" => $data,
    "pages" => $pages
]);
