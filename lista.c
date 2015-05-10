
typedef struct tagElemLista {

      int pValor;
      struct tagElemLista * pProx;
      bool bVisited;

} tpElemLista ;


typedef struct LIS_tagLista {

      tpElemLista * pOrigemLista ;
      tpElemLista * pFimLista ;
      tpElemLista * pElemCorr ;
      int numElem ;

} LIS_tpLista ;

typedef struct MAT_Lista {

      int pValor;
      bool bVisited;   

} MAT_tpLista ;