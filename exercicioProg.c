#include <stdio.h>

int main(void)
{

	int litragem;
	printf("Digite um número:");
	scanf("%d" , &litragem);

	int totalsuco     = litragem + (litragem * 2);
	int totalrefresco = litragem + (litragem * 4);

	printf("Podem ser produzidos %d litros de suco \n", totalsuco);
	printf("Podem ser produzidos %d litros de refresco \n", totalrefresco);

	int qtosCoposSucos    = totalsuco * 10;
	int qtosCoposRefresco = totalrefresco * 10;

	float rendimentoSucos     = 2 * qtosCoposSucos;
	float rendimentoRefrescos = qtosCoposRefresco;
	float totalRendimentos    = rendimentoSucos + rendimentoRefrescos;
	
	printf("Rendimento total = %f ( %f + %f ) \n", totalRendimentos , rendimentoSucos, rendimentoRefrescos);	

	return 0;
}