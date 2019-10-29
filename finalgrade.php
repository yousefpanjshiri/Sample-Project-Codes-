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
	<?php 
	function average($value1, $value2) {
		$Result=($value1/$value2)*100;
		return $Result;
	}
	?>
	<?php
	function weightedGrade($av,$value3) {
		$resultWeight=(($av*$value3)/100);
		return $resultWeight;
	}
	?>
	<div class="maincontent">
			<?php
			$participationEarn = $_POST['earnedParticipation'];
			$participationMax = $_POST['maxParticipation'];
			$participationWeight = $_POST['weightParticipation'];
			
			$avgPart = average($participationEarn,$participationMax);
			$weightPart = weightedGrade($avgPart,$participationWeight);
			
			echo "You earned a <b>$avgPart</b>% for Participation, with a weighted value of <b>$weightPart</b> %.<?p>";
			echo "<br>";
			echo "<br>";
			echo "<br>";
			?>
			
			<?php
			$quizEarn = $_POST['earnedQuiz'];
			$quizMax = $_POST['maxQuiz'];
			$quizWeight = $_POST['weightQuiz'];
			
			$avgQuiz= average($quizEarn,$quizMax);
			$weightQuiz = weightedGrade($avgQuiz,$quizWeight);
			echo "You earned a <b>$avgQuiz</b>% for Quizzes, with a weighted value of <b>$weightQuiz</b> %.<?p>";
			echo "<br>";
			echo "<br>";
			echo "<br>";
			?>
		
			<?php
			$labEarn = $_POST['earnedLab'];
			$labMax = $_POST['maxLab'];
			$labWeight = $_POST['weightLab'];
			
			$avgLab = average($labEarn,$labMax);
			$weightLab = weightedGrade($avgLab,$labWeight);
			echo "You earned a <b>$avgLab</b>% for Lab Assignments, with a weighted value of <b>$weightLab</b> %.<?p>";
			echo "<br>";
			echo "<br>";
			echo "<br>";
			?>
		
			<?php
			$practicaEarn = $_POST['earnedPracticum'];
			$practicaMax = $_POST['maxPracticum'];
			$practicaWeight = $_POST['weightPracticum'];
			
			$avgPrac = average($practicaEarn,$practicaMax);
			$weightPrac = weightedGrade($avgPrac,$practicaWeight);
			echo "You earned a <b>$avgPrac</b>% for Practicums, with a weighted value of <b>$weightPrac</b> %.<?p>";
			echo "<br>";
			echo "<br>";
			?>
			<?php
			$gradeTotal = $weightPart + $weightQuiz + $weightLab + $weightPrac; 
			$Letter = ($gradeTotal>=96) ? "A+":"A";
			$Letter =($gradeTotal>=90 and $gradeTotal<=95) ? "A":"B+";
			$Letter =($gradeTotal>=86 and $gradeTotal<=89) ? "B+":"B";
			$Letter =($gradeTotal>=80 and $gradeTotal<=85) ? "B":"C+";
			$Letter =($gradeTotal>=75 and $gradeTotal<=79) ? "C+":"C";
			$Letter =($gradeTotal>=70 and $gradeTotal<=74) ? "C":"D";
			$Letter =($gradeTotal>=60 and $gradeTotal<=69) ? "D":"F";
			//($gradeTotal>=0 and gradeTotal<=60) ? "F":_;//
			echo "<br>";
			echo "<b>Your Final Grade is $gradeTotal % which is a $Letter.</b><?p>";
			?>
	</div>
	<div class="footer">
		<?php $footer = 'footer.inc';
		readfile ($footer)?>
	</div>
</div>
</body>
</html>