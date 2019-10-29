<!DOCTYPE HTML>
<html xmlns=“http://www.w3.org/1999/xhtml”>
<head>
	<link rel="stylesheet" type="text/css" href="styles.css"> 
	<meta charset="utf-8" />
	<title> IT 207 Final Grade Determiner</title>
<head>
<body>
	
<div class= "page">		
	<div class="sidebar1">
		<?php $sidebar1 = 'sidebar1.inc';
		readfile($sidebar1)
		?>	
	</div>
	<div class="header">
		<?php $header = 'header.php';
		include ($header)
		?>
	</div>
	<div class="maincontent">
		<form action="finalgrade.php" method="post">
			<h3>Participation</h3>
			
			Earned: <input type="text" name="earnedParticipation" />
			Max: <input type="text" name="maxParticipation" />
			Weight (percentage): <input type="text" name="weightParticipation" />
			<h3>Quizzes</h3>
			
			Earned: <input type="text" name="earnedQuiz" />
			Max: <input type="text" name="maxQuiz" />
			Weight (percentage): <input type="text" name="weightQuiz" />
			<h3>Lab Assignments</h3>
			
			Earned: <input type="text" name="earnedLab" />
			Max: <input type="text" name="maxLab" />
			Weight (percentage): <input type="text" name="weightLab" />
			<h3>Practica</h3>
			
			Earned: <input type="text" name="earnedPracticum" />
			Max: <input type="text" name="maxPracticum" />
			Weight (percentage): <input type="text" name="weightPracticum" />
			<br /><br />
			<input type="submit" />
		</form>
	</div>
	<div class="footer">
		<?php $footer = 'footer.inc';
		readfile ($footer)?>
	</div>
</div>
</body>
</html>