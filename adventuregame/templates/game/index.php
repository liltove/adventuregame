{% load staticfiles %}

<!DOCTYPE html>
<html>
<head>
<title>Frontier</title>
<link rel="stylesheet" type="text/css" href="{% static 'game/main.css' %}" />
</head>

<body>

<div id="welcomeBar">
	<h1>Welcome to The Frontier,
	Frontier Fracas,
	Lock, Stock, and Two Smoking Frontiers (... wtf does that even mean),
	Guess who’s coming to … the frontier!,
	Space, The Penultimate Frontier!</h1>
</div>
<div id ="main">
	<div id="nav">
		<?php include "/static/game/nav.php"; ?>
		<?php echo "{% static 'game/nav.php' %}"; ?>
		<?php $stat="{% static 'game/nav.php' %}"; ?>
		<?php echo "$stat";?>
	</div>
	<div id="win"
		<p>More to come soon.</p>
	</div>
</div>
</body>
</html>