<?php 

function matriz($linha,$coluna, $procurado){

	# aqui monta apenas a matriz com complexidade quadratica
	$matriz='';
	$cont = 1;
	for ($i=1; $i <= $linha ; $i++) { 
		for ($j=1; $j <= $coluna; $j++) { 
			$matriz[$i][$j] = $cont;
			$cont++;
		}
	}

	# aqui comeca de fato o algoritmo
	$meio = $linha / 2;
	if ( ($linha % 2) > 0 ) {
		$meio = ( ($linha - 1) / 2) + 1;
	}
	if ($procurado == $matriz[$meio][$meio + 1]) {
		# achou o elemento
		echo $meio . $meio + 1;
	}
	else if ($procurado > $matriz[$meio][$meio + 1]) {
		# procura do meio da matriz para frente
		for ($i=$meio; $i <= $linha; $i++) { 
			for ($j=$meio+1; $j <= $coluna ; $j++) { 
				if ($procurado == $matriz[$i][$j]) {
					echo $i . $j;
				}
			}
		}
	}else{
		# procura do meio da matriz para tras
		for ($i=1; $i < $meio; $i++) { 
			for ($j=1; $j < $meio + 1 ; $j++) { 
				if ($procurado == $matriz[$i][$j]) {
					echo $i . $j;
				}
			}
		}
	}
	var_dump($matriz);
}

matriz(3,3,1);
?>