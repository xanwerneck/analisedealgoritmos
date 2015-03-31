#include <stdio.h>


float valor_unitario(int quantidade, int tipo_entrega)
{
	float valor_cobrado;

	if (tipo_entrega == 1)
	{
		/* tipo de entrega igual a 1 */
		if (quantidade <= 1000){
			valor_cobrado = 11.10 * quantidade;
		}else if(quantidade > 1000 && quantidade <= 5000){
			valor_cobrado = 10.00 * quantidade;
		}else if(quantidade > 5000 && quantidade <= 10000){
			valor_cobrado = 6.40 * quantidade;
		}else{
			valor_cobrado = 3.30 * quantidade;
		}
	}
	else
	{
		/* tipo de entrega igual a 2 */
		if (quantidade <= 1000){
			valor_cobrado = 11.10 * quantidade;
		}else if(quantidade > 1000 && quantidade <= 5000){
			valor_cobrado = 10.00 * quantidade;
		}else if(quantidade > 5000 && quantidade <= 10000){
			valor_cobrado = 6.40 * quantidade;
		}else{
			valor_cobrado = 3.30 * quantidade;
		}

	}
	return valor_cobrado;
}

int main(void)
{
	int quantidade;
	int tipo = 0;
	int n;
	float total = 0.0;
	float valor = 0.0;
	int qtosdescontos = 0;
	int jafiz = 0;

	//scanf("Informe a quantidade de clientes: %d" , &n);

	printf("Digite um numero: ");
    scanf("%d", &n);

	while( jafiz < n ){
		printf("Informe a quantidade de unidades: ");
	    scanf("%d", &quantidade);

	    printf("Informe o tipo de entrega: ");
	    scanf("%d", &tipo);

		valor = valor_unitario(quantidade, tipo);
		if ( (tipo == 1) && (valor > 4000.00) )
		{
			valor = valor - (valor * 0.30);
			qtosdescontos = qtosdescontos + 1;
		}	
		total = total + valor;

		jafiz = jafiz + 1;
	}

	printf("Valor total vendido: %.2f \n" , total);
	printf("Quantos descontos: %d \n" , qtosdescontos);
	
	return 0;
}
