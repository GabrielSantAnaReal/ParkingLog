# To-do

## [0.14]

**Limpeza e organização de funções**

- Separar as funções relacionadas as placas e manipulação de dados dos veículos das funções de registro e criação dos arquivos para o registro. Motivo: limpeza do código e melhorar a organização.


## [0.13] (Released in 2022-12-29)

**Pequenas correções e implementações**

- (Ok) Substituir a forma de salvar marca e modelo do veículo ("marca/modelo" para "marca;modelo");
- ~~Alterar formato de hora e data de "hh:mm:ss-dd/mm/aaaa" para "hh:mm:ss;dd/mm/aaaa", separando as duas informações;~~
Mudança cancelada. Motivo: programa está funcionando bem com o *datetime* nesse formato. A princípio, sem alterações.
- (Ok) Fazer a função "readplate" voltar a funcionar; (está dando o tempo parado novamente) (Origem do problema descoberta: só funciona se a placa for digitada em CAPSLOCK)
- (Ok) Permitir apagar saídas de até 10 minutos atrás somente;
- (Ok) Fazer com que todas as funções peguem a data antes de cada execução, e não no começo do programa.
