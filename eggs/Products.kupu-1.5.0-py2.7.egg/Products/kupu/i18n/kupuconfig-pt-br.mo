��    q      �      ,      ,     -     @     W     _     t  
   �     �     �     �     �  
   �     �     �               (     ;     J     ]     m     �     �     �     �     �     �     	     	     *	     =	  
   N	     Y	     p	     �	     �	     �	     �	     �	     �	     �	     
     *
     ?
     U
     h
     
     �
     �
     �
     �
     �
     �
          !     4     N     l     y     �     �     �     �     �     �               -     >     T  
   a     l     �     �     �     �     �     �               &     5     G     Z     l     y     �     �     �     �     �     �     �               $  
   0     ;     M  	   [     e     w     �     �     �     �     �     �     �               "     9  �  K          .     M     Z  B   m  	   �     �     �     �     �     �  ?   �  3   1  A   e     �     �  5   �  <   �     <  !   W  s   y     �     �                     @     W  
   _     j     x     �     �     �     �  .   �     �     �  2     l   8  �  �  G   y  �   �  �   h  E  7  6   }  O   �  �     �   �  y   �  �   G  |   �  B   v   [   �   e   !  y   {!     �!  %   �!  	   ""     ,"  /   D"     t"  I   �"     �"     �"  *   �"     #     ##     6#     >#     C#     ^#  
   v#     �#     �#     �#     �#     �#     �#  #   �#  ,   "$     O$     o$     {$  "   �$     �$  *   �$     �$     %     %  }  &%     �'     �'     �'     �'     �'     �'     �'  
   	(     (     &(  )  ;(  r  e)  �   �*  �  �+  \  ,-  3  �.     �/     �/     �/  [   �/     '0   action_url_heading allow_captioned_images any_tag authenticated_member available_tales button_add button_delete button_move_down button_move_up button_save button_set caption_is_supported caption_maybe_supported caption_not_supported check_select_all classes_subheading context_folder context_folder_uri current_context current_context_url default_reference_resource default_resource_heading defscale_subheading fieldname_subheading flash_option global_button_visibility heading_configuration heading_default heading_expression heading_icon_uri heading_id heading_kupu_libraries heading_kupu_resource_types heading_source_uri heading_title heading_toolbar_configuration heading_uri heading_visible help_add_resource help_allow_original_image help_button_visibility help_class_blacklist help_enable_transform help_filter_source help_global_visibility help_image_captioning_url help_image_uid_caption help_link_uid help_navigate_away help_paragraph_styles help_refbrowser help_remove_entities help_style_whitelist help_table_classes help_transform_is_enabled help_update_portal_transforms image_option label_allowOriginalImageSize label_attributes label_class_blacklist label_filtersourceedit label_icon_uri label_install_kupu label_link_uid label_paragraph_styles label_refbrowser label_source_uri label_style_whitelist label_tables label_tags legend_alloworiginalsize legend_button_visibility legend_caption legend_filtersourceedit legend_html_filter legend_link_options legend_map_resource_types legend_refbrowser legend_styles legend_warning loading_links_tab map_resource_types new_types_heading normal_image opt_exclusive opt_inclusive plone_filter_controlpanel portal_object portal_object_url portal_types_heading preview_action_help preview_subheading request resource_heading select_type tab_config tab_documentation tab_libraries tab_links tab_resourcetypes tab_toolbar text_kupu_drawers text_kupu_drawers2 text_kupu_drawers3 text_resource_types text_resource_types2 text_resource_types3 type_heading type_subheading url_heading use_plone_controlpanel whole_tag_removed Project-Id-Version: Kupu
POT-Creation-Date: 2009-07-08 09:15+0000
PO-Revision-Date: 2009-07-09 01:30-0300
Last-Translator: Erico Andrei <erico@simplesconsultoria.com.br>
Language-Team: Português <plone-i18n@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=1; plural=0
Language-Code: pt-br
Language-Name: Português do Brasil
Preferred-Encodings: utf-8 latin1
Domain: kupuconfig
 URLs de ações Permitir legendagem de imagens Qualquer tag Membro autenticado As seguintes variáveis estão disponíveis nas expressões TALES: Adicionar Apagar Mover para baixo Mover para cima Salvar Definir Campos que atualmente aparentam suportar legendagem de imagens: Campos que poderiam suportar legendagem de imagens: Campos que utilizam kupu mas não suportam legendagem de imagens: Selecionar todos os itens classes A pasta na qual o objeto de contexto está localizado A URL da pasta na qual o objeto de contexto está localizado O objeto de contexto atual A URL to objeto de contexto atual especificar um tipo de recurso para ser utilizado por campos de referência com uma lista vazia de tipos permitidos Recurso padrão Escala padrão nome do campo Flash Visibilidade global dos botões Configuração do Kupu Padrão Expressão URI do ícone Identificador Bibliotecas do Kupu Tipos de Recursos do Kupu URI da fonte Título Configuração da barra de ferramentas do Kupu URI Visível utilize esta entrada para adicionar novos recursos Quando selecionado, o manipulador de imagens irá incluir o tamanho original entre os tamanhos disponíveis. Você pode informar uma expressão para controlar a visibilidade de todos os botões simultaneamente. A expressão deverá devolver uma lista de identificadores de botões visíveis, ou <code>None</code> para manter todos os botões visíveis. As regras de visibilidade abaixo são depois aplicadas para uma filtragem adicional de botões individuais. Você pode utilizar isto para restringir uma classe particular de usuários a um subconjunto das funções do kupu. Insira uma lista de nomes de classes a serem excluídas (uma por linha) Caso você habilite este opção, uma transformação que ocultará os UIDs e permitirá o uso de legenda em imagens a partir dos navegadores também será habilitada Quando ativado, a visualização de HTML do Kupu irá mostrar a versão filtrada do HTML, que será enviada ao servidor. Desative esta opção para visualizar o código HTML original, gerado pelo navegador. Controla a visibilidade global dos botões da barra de ferramentas através desta tela. Se não for inserida nenhuma expressão, apenas os botões selecionados são visíveis. Insira uma expressão para um controle mais refinado da visibilidade. Campos individuais podem também desativar ou ativar botões: veja o esquema do campo. <div>Os valores disponíveis nas expressões incluem <code>field</code>, além dos nomes habituais</div> <!-- object_url folder_url portal_url object folder portal nothing request modules member --> Por exemplo, para restringir os botões dos manipuladores para usuários com as permissões apropriadas insira nos botões <code>imagelibdrawer-button</code> e <code>linklibdrawer-button</code> a expressão: <div> <code>python:member and member.has_permission('Kupu: Query libraries',portal)</code> </div> veja a documentação relativa às legendas de imagens Imagens cujos links forem baseados em UID podem ser automaticamente legendadas. Os links criadas pelo Kupu para objetos neste site podem utilizar identificadores únicos de objetos de forma a permanecerem válidas mesmo quando o objeto de destino é renomeado ou movido para outro local no site. O Kupu pode instalar uma opção que avisa o usuário antes de sair de uma página onde tenha iniciado o preenchimento de um formulário (mesmo para campos que não utilizem Kupu). Desative isto para impedir o Kupu de carregar esta opção. Insira uma lista de estilos a incluir no menu de seleção. O formato é título|tag ou título|tag|classe, um por linha. Substituir a <em>widget</em> de seleção de referências do ATReferenceBrowser por uma <em>widget</em> que utiliza os manipuladores do Kupu em vez de uma janela <em>popup</em>. Indique as tags HTML e atributos que devam ser removidos ao salvar os documentos. (Desmarque para remover entradas da lista) Insira uma lista de elementos de estilo permitidos (um por linha). Insira uma lista de nomes de classes para serem disponibilizados no manipulador de tabelas. Uma transformação para ocultar os UIDs dos navegadores de clientes está habilitada para os campos: Caso a transformação não seja habilitada automaticamente, talvez seja necessário atualizar o produto PortalTransforms Imagem Permitir tamanho original das imagens Atributos Classes não permitidas Filtrar HTML na visualização de código fonte URI do ícone Instalar código do Kupu para detecção de alterações nos formulários Criar link usando UIDs Estilos Utilizar navegador de referências do Kupu URI da fonte Estilos permitidos Tabelas Tags Tamanho Original da Imagem Visibilidade de botões Legendagem Visualização de HTML Filtragem de HTML Opções de links Mapeamento de tipos de recursos Navegador de Referências Estilos Avisar antes de perder alterações Caregando a manutenção de links do Kupu... Mapeamento de tipos de recursos Novos tipos Imagem normal não são adicionados à seleção são adicionados à seleção Painel de controle do filtro HTML do Plone O objeto portal URL do portal Tipos de Conteúdo <code>Pré-visualização</code> é uma expressão para utilizar a pré-visualizacão de imagem nos manipuladores [por padrão, está opção está desativada]. <code>Imagem normal</code> é uma expressão para utilizar para a visualização normal de um objeto mídia [string:$object_url]. <code>Nome do campo</code> é o nome do campo para utilizar para variantes escaladas do objeto mídia [image]. <code>Classes</code> é uma lista de nomes de classes que podem ser selecionadas ao inserir o objeto como mídia. <code>Tipo</code> controla se o Kupu insere uma tag <code>img</code> ou <code>object</code> para incluir conteúdo Flash. pré-visualização Requisição Recurso (selecionar tipo) Configuração Documentação Bibliotecas Ligações Tipos de Recursos Barra de ferramentas No formulário abaixo você pode gerenciar a lista de bibliotecas do editor Kupu. Cada propriedade de uma biblioteca é calculada dinamicamente em tempo de execução usando expressões TALES. Desta forma é possível suportar opções como <em>Pasta atual</em> ou <em>Minha pasta</em> facilmente. Bibliotecas com identificadores que comecem com um <em>undescore</em> não serão mostradas na lista inicial. <em>_search</em> será utilizada para definir o ícone e título dos resultados de pesquisa. O primeiro caracter $ no título será substituído pelo termo de pesquisa. <em>_selection</em> será utilizada para definir o ícone e título para a seleção atual. O título pode conter tags HTML &lt;br&gt; para colocar uma quebra de linha no título (não a marca XHTML na forma &lt;br/&gt;), mas outras marcas não são interpretadas. Enquanto as bibliotecas forneçam localizações abstratas para objetos de qualquer tipo, o Kupu distingue os objetos pelo tipo de recurso. Por exemplo, um usuário pode solicitar uma biblioteca que mostre objetos para criar links ou uma biblioteca que mostre objetos para serem inseridos no documento. A localização abstrata (biblioteca) pode ser a mesma, mas a primeira biblioteca teria documentos e a segunda imagens. Esta tela de gerenciamento permite a definição de tipos de recursos utilizando uma lista de tipos de conteúdo. Um tipo de recurso especial, <code>collection</code>, identifica tipos de conteúdo que podem ser vistos como coleções. O tipo de recurso <code>containsanchors</code> é utilizado para listar os tipos que podem conter âncoras HTML. Também nesta tela existem URLs para cada tipo que pode ser previsto como imagens. A expressão pode incluir <code>object_url</code> e <code>portal_type</code>, mas não deve tentar acessar o objeto diretamente. A URL resultante deve idealmente devolver uma imagem que não seja maior do que 128x128 pixels. Tipo tipo URL Por favor, utilize o ${plone_filter_controlpanel} para configurar as opções de filtragem. A tag inteira é removida 