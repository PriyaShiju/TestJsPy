<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<script type="text/php">
		<?php function response( $input ) {
	 //Insert your code here 
	 $response = [];
	for ($i=1; $i<=$input; $i++) {
	  if ($i%3==0 && $i%5==0) {
		  array_push($response, 'FizzBuzz');
	  }else if($i%3==0){
		  array_push($response, 'Fizz');
	  }else if($i%5==0){
		  array_push($response, 'Buzz');
	  }else{
		  array_push($response, $i);
	  }
	}
	return $response;
}
 ?>
 
	</script>
</body>
</html>
<?php function response( $input ) {
	 //Insert your code here 
	 $response = [];
	for ($i=1; $i<=$input; $i++) {
	  if ($i%3==0 && $i%5==0) {
		  array_push($response, 'FizzBuzz');
	  }else if($i%3==0){
		  array_push($response, 'Fizz');
	  }else if($i%5==0){
		  array_push($response, 'Buzz');
	  }else{
		  array_push($response, $i);
	  }
	}
	return $response;
}
 ?>
 