"# DesporPato - Documentação Técnica Backend

## Sumário

1. [Introdução](#introdução)
2. [Configuração](#configuração)
3. [Aplicativos](#aplicativos)
    - [user_data](#user_data)
    - [eventos](#eventos)
    - [atividades](#atividades)

## Introdução

*DesporPato* é um webapp desenvolvido usando o framework Django para gerenciar eventos esportivos na cidade de Pato Branco. O sistema permite o registro de eventos esportivos, participação de usuários, e oferece funcionalidades para os organizadores, como criação de eventos e controle de participantes.

- *Registro e Autenticação*: Utiliza a biblioteca Django Rest Auth e Rest Framework para autenticação. Os usuários podem se registrar, fazer login e atualizar seus perfis.
- *Gerenciamento de Eventos*: Os organizadores podem criar eventos esportivos, definindo detalhes como título, esporte, data e local.
- *Participação de Usuários*: Os usuários podem se inscrever em eventos, visualizar eventos futuros e passados, e acessar informações detalhadas sobre cada evento.
- *Controle de Participantes*: Os organizadores podem ver a lista de participantes inscritos em seus eventos, gerando QR Codes para controle de entrada.
- *Histórico de Ações*: Registra o histórico de ações dos usuários, como inscrições em eventos e participações.

## Configuração

- *Banco de Dados*: Utiliza um banco de dados SQL para armazenar informações sobre eventos, usuários e atividades.
- *Armazenamento de Imagens*: As imagens associadas aos eventos são armazenadas localmente no servidor.
- *Servidor*: O aplicativo é implantado em um servidor web para acesso público.
- *Autenticação*: Implementa autenticação com token para garantir a segurança das APIs.

## Aplicativos e seus principais modelos/serializadores/viewsets

### user_data

#### Modelos

- *CustomUser*: Modelo personalizado que representa um usuário, incluindo campos como nome, email, cidade, e informações adicionais do perfil.

- *History*: Registra o histórico de ações dos usuários, incluindo detalhes como data, pontos ganhos e descrição da ação.

#### Serializadores

- *CustomUserSerializer*: Serializa o modelo `CustomUser`, retornando informações do perfil do usuário.

- *HistorySerializer*: Serializa o modelo `History`, permitindo a visualização do histórico de ações dos usuários.

#### ViewSets

- *CustomUserViewSet*: Manipula informações de usuários, permitindo o registro, atualização e autenticação.

- *HistoryViewSet*: Lista o histórico de ações de um usuário específico.

### eventos

#### Modelos

- *Evento*: Representa um evento esportivo, incluindo detalhes como título, esporte, data, local e informações dos organizadores.

- *Participante*: Registra a participação dos usuários em eventos, incluindo detalhes como data de inscrição e status de pagamento.

#### Serializadores

- *EventoSerializer*: Serializa o modelo `Evento`, fornecendo informações detalhadas sobre eventos esportivos.

- *ParticipanteSerializer*: Serializa o modelo `Participante`, permitindo o registro e listagem de participantes em eventos.

#### ViewSets

- *EventoViewSet*: Manipula informações sobre eventos esportivos, permitindo a criação, atualização e listagem de eventos.

- *ParticipanteViewSet*: Lista os participantes inscritos em um evento específico.

### atividades

#### Modelos

- *Atividade*: Registra ações dos usuários relacionadas a eventos, incluindo detalhes como tipo de ação, data e evento associado.

#### Serializadores

- *AtividadeSerializer*: Serializa o modelo `Atividade`, permitindo o registro de ações dos usuários.

#### ViewSets

- *AtividadeViewSet*: Permite o registro de atividades dos usuários relacionadas a eventos.

O aplicativo *DesporPato* oferece um conjunto completo de funcionalidades para gerenciamento de eventos esportivos, participação de usuários e controle de participantes. A documentação técnica acima fornece uma visão geral das principais partes do sistema e como elas estão organizadas.
"