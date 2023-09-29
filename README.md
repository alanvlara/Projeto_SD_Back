# DesporPato - Documentação Técnica Backend

## Sumário

1. [Introdução](#Introdução)
2. [Configuração](#Configuração)
3. [Aplicativos](#Aplicativos)
    - [Usuario](#Usuario)
    - [Eventos](#Eventos)
    - [Atividades](#Atividades)
4. [Utils](#Utils)
    - [Custom_serializer_register](#Custom_serializer_register)
    - [Custom_serializer](#Custom_serializer)
    - [Custom_view_register](#Custom_view_register)
    - [Exportar_excel_view](#Exportar_excel_view)
    - [Gerar_certificado_view](#Gerar_certificado_view)
    - [Permissions](#Permissions)
    - [Storages](#Storages)
    - [Validators](#Validators)



## Introdução

*DesporPato* é um webapp desenvolvido usando o framework Django no backend para gerenciar eventos esportivos na cidade de Pato Branco. O sistema permite o registro de eventos esportivos, participação de usuários, e oferece funcionalidades para os organizadores, como criação de eventos e controle de participantes.

- *Registro e Autenticação*: Utiliza a biblioteca Django Rest Auth e Rest Framework para autenticação. Os usuários podem se registrar, fazer login e atualizar seus perfis.
- *Gerenciamento de Eventos*: Os organizadores podem criar eventos esportivos, definindo detalhes como título, esporte, data e local.
- *Participação de Usuários*: Os usuários podem visualizar eventos futuros e passados, e acessar informações detalhadas sobre cada evento. Os usuários podem baixar certificados de participação nos eventos.
- *Controle de Participantes*: Os organizadores podem ver a lista de participantes inscritos em seus eventos, gerando QR Codes para controle de entrada.

## Configuração

- *Banco de Dados*: Utiliza um banco de dados SQL no RDS da AWS para armazenar informações sobre eventos, usuários e atividades.
- *Armazenamento de Imagens*: As imagens associadas aos eventos são armazenadas no S3 da AWS.
- *Servidor*: O backend do aplicativo atualmente está rodando apenas localmente.
- *Autenticação*: Implementa autenticação com token para garantir a segurança das APIs.

## Aplicativos e seus principais modelos/serializadores/viewsets

### Usuário

#### Modelos

- *Usuario*: Modelo personalizado que representa um usuário. Ele estende o modelo de usuário padrão do Django (AbstractUser) e inclui campos adicionais como esporte preferido, CPF, CEP, endereço, cidade, estado, foto, total de eventos, indicação de desejo de criar eventos (quer_criar), indicação de criador (criador) e representação.

#### Serializadores e Views

- *UsuarioWriteSerializer*: Este serializador é usado para criar e atualizar informações de usuário. Ele define campos que podem ser alterados, como esporte preferido, foto e total de eventos. Também implementa lógica personalizada para atualizar o total de eventos com base no esporte preferido do usuário.

- *UsuarioReadSerializer*: Este serializador é usado para ler informações de usuário. Ele inclui campos como nome, sobrenome, nome de usuário, esporte preferido, total de eventos e foto. Ele também controla quais campos podem ser lidos por diferentes usuários, permitindo o acesso total ao próprio usuário e acesso limitado a outros.

- *UsuarioView*: Esta view define como os perfis de usuário são manipulados na API. Ela inclui operações como listagem e atualização de informações de perfil. A criação de usuários é tratada por meio de um endpoint de registro separado e a exclusão não é permitida, apenas a inativação.

### Eventos

#### Modelos

- *Evento*: Modelo que representa um evento esportivo. Ele inclui campos como título, link, data, esporte e outras informações associadas ao evento.

#### Serializadores e Views

- *EventosWriteSerializer*: Este serializador é usado para criar e atualizar eventos. Ele define campos como título, link, data e esporte, bem como regras de validação para a criação de eventos.

- *EventosReadSerializer*: Este serializador é usado para ler eventos. Ele inclui campos como título, link, data, esporte e também o URL do código QR associado ao evento.

- *EventoView*: Esta view define como os eventos são manipulados na API. Ela inclui operações como listagem, criação, atualização e exclusão de eventos. Também implementa permissões para garantir que apenas os usuários autorizados possam criar ou editar eventos.

### Atividades

#### Modelos

- *Atividade*: Modelo que representa uma atividade registrada por um usuário em um evento. Ele inclui campos como data, foto e uma referência ao evento e usuário relacionados.

#### Serializadores e Views

- *AtividadeWriteSerializer*: Este serializador é usado para criar e atualizar atividades. Ele define campos como data, evento e foto, bem como regras de validação para a criação de atividades.

- *AtividadeReadSerializer*: Este serializador é usado para ler atividades. Ele inclui campos como data, evento e foto, e também fornece informações detalhadas sobre o usuário associado e o evento relacionado.

- *AtividadeView*: Esta view define como as atividades são manipuladas na API. Ela inclui operações como listagem, criação, atualização e exclusão de atividades. Também implementa permissões para garantir que apenas os usuários autorizados possam criar ou editar atividades.


## Utils
A pasta `Utils` contém diversos módulos auxiliares e utilitários que são utilizados em diferentes partes do sistema.

#### Custom_serializer_register

O módulo `Custom_serializer_register` contém uma classe personalizada chamada `CustomRegisterSerializer`. Esta classe é usada para estender o processo de registro de usuários e coletar informações adicionais durante o registro. As informações adicionais incluem campos como primeiro nome, último nome, esporte preferido, CPF, CEP, endereço, cidade, estado, indicação de criador (criador) e representação.

A classe `CustomRegisterSerializer` inclui validações personalizadas para o CPF e o estado, garantindo que esses campos sejam preenchidos corretamente. Ela também possui um método `custom_signup` que é usado para salvar as informações adicionais no perfil do usuário após o registro.

Além disso, a classe `CustomRegisterSerializer` substitui o método `get_cleaned_data` para incluir os campos adicionais no conjunto de dados limpos durante o processo de registro.

Esta classe personalizada é integrada ao processo de registro do Django Rest Auth e é usada para coletar informações extras durante o registro de um novo usuário.

#### Custom_serializer

O módulo `Custom_serializer` contém uma classe personalizada chamada `CustomUserDetailsSerializer`. Esta classe é usada para estender o serializador de detalhes de usuário do Django Rest Auth, permitindo a inclusão de campos extras no perfil do usuário.

A classe `CustomUserDetailsSerializer` inclui os seguintes campos extras:

- `esportePreferido`: Permite que os usuários definam seu esporte preferido.
- `cpf`: Permite que os usuários insiram seu número de CPF.
- `cep`: Permite que os usuários insiram seu CEP.
- `endereco`: Permite que os usuários insiram seu endereço.
- `cidade`: Permite que os usuários insiram sua cidade.
- `estado`: Permite que os usuários insiram seu estado.
- `foto`: Permite que os usuários façam o upload de uma foto de perfil.
- `totalEventos`: Registra o total de eventos em que o usuário participou.
- `criador`: Indica se o usuário é um criador de eventos.
- `representa`: Permite que os usuários indiquem uma representação.
- `quer_criar`: Indica se o usuário deseja criar eventos.

Esses campos extras são opcionais e não são necessários durante o registro, mas podem ser atualizados pelo usuário posteriormente.

A classe `CustomUserDetailsSerializer` estende a classe `UserDetailsSerializer` do Django Rest Auth e inclui os campos extras no conjunto de campos permitidos. Ela garante que esses campos sejam incluídos nos detalhes do usuário quando necessário.

Esta classe personalizada é usada para estender as informações disponíveis no perfil do usuário, permitindo que os usuários adicionem detalhes extras ao seu perfil.

#### Custom_view_register

O módulo `Custom_view_register` inclui a classe `CustomUserDetailsView`, que é uma visualização personalizada usada para estender a funcionalidade de detalhes de usuário oferecida pelo Django Rest Auth.

A classe `CustomUserDetailsView` é usada para exibir e atualizar os detalhes do perfil do usuário. Ela substitui o serializador padrão usado para detalhes de usuário pelo `CustomUserDetailsSerializer`, que inclui campos extras no perfil do usuário, como esporte preferido, CPF, CEP, foto, total de eventos, criador, representa e desejo de criar eventos.

A classe `CustomUserDetailsView` também define os seguintes comportamentos:

- `parser_classes`: Aceita vários formatos de dados, incluindo JSON e formulários multipartes, tornando-a versátil para receber atualizações de perfil.
- `renderer_classes`: Define os formatos em que os dados de resposta são renderizados, incluindo JSON e renderização multipartes.

Essa visualização personalizada permite que os usuários vejam e atualizem os detalhes do perfil, incluindo os campos extras adicionados ao perfil do usuário.

#### Exportar_excel_view

O módulo `Exportar_excel_view` inclui a classe `ExportarDadosParaExcel`, que é uma APIView personalizada usada para exportar dados relacionados a participantes de um evento específico para um arquivo Excel.

A classe `ExportarDadosParaExcel` define a seguinte funcionalidade:

- Método `get`: Este método é chamado quando uma solicitação GET é feita para a API. Ele recebe um parâmetro `evento_id`, que identifica o evento do qual deseja exportar dados de participantes.

  O método executa as seguintes etapas:
  
  - Recupera todas as atividades relacionadas ao evento específico com base no `evento_id`.
  - Coleta as cidades dos usuários que participaram dessas atividades.
  - Cria um DataFrame do Pandas com os dados coletados.
  - Usa o Pandas para contar o número de ocorrências de cada cidade.
  - Escreve os dados no DataFrame em um arquivo Excel.
  - Retorna o arquivo Excel como resposta HTTP para download.

O resultado final é um arquivo Excel que contém informações sobre as cidades dos participantes do evento, juntamente com a contagem de participantes em cada cidade.

#### Gerar_certificado_view

O módulo `Gerar_certificado_view` inclui a função `gerar_certificado`, que gera certificados de participação em formato PDF para os participantes de um evento.

A função `gerar_certificado` executa as seguintes etapas:

- Recebe um parâmetro `atividade_id` para identificar a atividade da qual deseja gerar o certificado.
- Obtém os dados da atividade com base no `atividade_id`.
- Cria um PDF usando a biblioteca ReportLab.
- Baixa uma imagem de fundo do Amazon S3 para o certificado.
- Desenha a imagem baixada no PDF e adiciona informações personalizadas, como o nome do participante, data do evento e assinatura do diretor do evento.
- Retorna o certificado em formato PDF como uma resposta HTTP para download.

Os certificados gerados contêm informações personalizadas com base nos dados da atividade e do evento. Cada certificado é único para o participante.

#### Permissions

O módulo `Permissions` define permissões personalizadas que controlam o acesso às diferentes partes da API com base nas regras de negócios da aplicação.

##### `IsOwnerOrReadOnly`

A classe `IsOwnerOrReadOnly` é uma permissão personalizada que permite que apenas os proprietários de um objeto visualizem ou editem o objeto. Ela é usada em partes da API relacionadas a atividades. As principais funcionalidades incluem:

- Permite solicitações de leitura (como GET) para qualquer usuário.
- Apenas permite solicitações de gravação (como POST, PUT, DELETE) para o proprietário da atividade.
- Garante que somente o usuário que criou a atividade possa modificá-la.

##### `IsOwnerOrReadOnlyUser`

A classe `IsOwnerOrReadOnlyUser` é outra permissão personalizada usada para garantir que apenas os proprietários de um objeto possam visualizá-lo ou editá-lo. No entanto, esta permissão é aplicada a objetos relacionados a usuários. As principais funcionalidades incluem:

- Permite solicitações de leitura (como GET) para qualquer usuário.
- Apenas permite solicitações de gravação (como POST, PUT, DELETE) para o proprietário do objeto.
- Garante que somente o usuário autenticado possa modificar seu próprio perfil de usuário.

Essas permissões personalizadas são essenciais para garantir a segurança e o controle de acesso adequados em várias partes da API do DesporPato.

#### Storages

O módulo `Storages` contém configurações para armazenamento de arquivos estáticos e mídia, incluindo configurações específicas para o Amazon S3.

##### `StaticStorage`

`StaticStorage` é uma classe que herda de `S3Boto3Storage` e é usada para o armazenamento de arquivos estáticos, como arquivos CSS, JavaScript e imagens que fazem parte do design da aplicação. Principais configurações:

- `location`: Define a pasta no bucket S3 onde os arquivos estáticos são armazenados.
- `default_acl`: Define as permissões de acesso padrão para esses arquivos, permitindo que sejam lidos publicamente.

##### `PublicMediaStorage`

`PublicMediaStorage` é outra classe que herda de `S3Boto3Storage`, mas é usada para o armazenamento de arquivos de mídia públicos, como imagens de perfil de usuário ou imagens associadas a eventos. Principais configurações:

- `location`: Define a pasta no bucket S3 onde os arquivos de mídia públicos são armazenados.
- `default_acl`: Define as permissões de acesso padrão para esses arquivos, permitindo que sejam lidos publicamente.
- `file_overwrite`: Evita a substituição de arquivos existentes, garantindo que os nomes de arquivo sejam únicos.

##### `PrivateMediaStorage`

`PrivateMediaStorage` é outra classe derivada de `S3Boto3Storage` e é usada para o armazenamento de arquivos de mídia privados, que podem incluir informações sensíveis ou restritas. Principais configurações:

- `location`: Define a pasta no bucket S3 onde os arquivos de mídia privados são armazenados.
- `default_acl`: Define as permissões de acesso padrão para esses arquivos, restringindo o acesso apenas a usuários autorizados.
- `file_overwrite`: Evita a substituição de arquivos existentes, garantindo que os nomes de arquivo sejam únicos.
- `custom_domain`: Desativa o uso de um domínio personalizado para acesso aos arquivos, mantendo-os restritos ao Amazon S3.

Essas configurações de armazenamento são fundamentais para garantir que os arquivos estáticos e de mídia sejam gerenciados e acessados de acordo com as necessidades de privacidade e segurança do DesporPato.

#### Validators

O módulo `Validators` contém funções personalizadas para validação de dados, incluindo validação de CPF, esporte e estado.

##### `valida_cpf`

A função `valida_cpf(cpf)` verifica se um número de CPF fornecido é válido. Ela realiza a validação de acordo com as regras do CPF, verificando os dígitos verificadores. Se o CPF for inválido, a função retorna `False`.

##### `mascara_cpf`

A função `mascara_cpf(cpf)` formata um número de CPF válido em uma string formatada com a máscara de CPF com pontos e traço. Se o CPF não for válido, a função retorna `None`.

##### `valida_esporte`

A função `valida_esporte(esporte)` verifica se uma string representando um esporte está presente na lista de esportes válidos. Se o esporte não estiver na lista, a função retorna `False`.

##### `valida_estado`

A função `valida_estado(estado)` verifica se uma sigla de estado está presente na lista de estados válidos no Brasil. Se o estado não estiver na lista, a função retorna `False`.

Essas funções personalizadas de validação são usadas em várias partes do código para garantir que os dados inseridos atendam aos critérios de validade. Se um dado não for válido de acordo com essas funções, as operações correspondentes podem gerar uma exceção de validação.















