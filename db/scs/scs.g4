grammar scs;

/* Parser rules */
syntax
    : (sentence ';;')* EOF
    ;
       
sentence
    // level 1
    : sentence_lvl1
    | sentence_lvl_common
    ;
    
idtf_lvl1_preffix returns [std::string text]
    : 'sc_node'
    | 'sc_link'
    | 'sc_arc_common'
    | 'sc_edge'
    | 'sc_arc_main'
    | 'sc_arc_access'
    ;
       
idtf_lvl1
    : (idtf_lvl1_preffix '#')? ID_SYSTEM
    ;

idtf_system
    : ID_SYSTEM
    ;

idtf_edge
    : '(' idtf_system
          connector attr_list?
          idtf_system
      ')'
    ;
    
idtf_set
    : '{'
         attr_list? idtf_common
         (';'
          attr_list? idtf_common
         )*
       '}'
    ;

idtf_common
    : idtf_system
    | idtf_edge
    | idtf_set
    | content
    | link
    ;

idtf_list
    : idtf_common
      internal_sentence_list?
      (';'
       idtf_common
       internal_sentence_list?
      )*
    ;
    
internal_sentence
    : connector attr_list? idtf_list
    ;
    
internal_sentence_list
    : '(*' (internal_sentence ';;')+ '*)'
    ;

sentence_lvl1
    : idtf_lvl1 '|' idtf_lvl1  '|' idtf_lvl1
    ;

sentence_lvl_4_list
    : ( connector attr_list? idtf_list)
    ;

sentence_lvl_common
    : idtf_common 
      sentence_lvl_4_list (';' sentence_lvl_4_list)*
    ;

attr_list
    : (
        ID_SYSTEM
        EDGE_ATTR
      )+
    ;


connector
     :  ( 
         '<>'  | '>'   | '<'   |
         '..>' | '<..' | '->'  |
         '<-'  | '<=>' | '=>'  | '<=' |
         '-|>' | '<|-' | '-/>' | '</-' |
         '~>'  | '<~'  | '~|>' | '<|~' |
         '~/>' | '</~' | '_<>' | '_>'  |
         '_<'  | '_..>'| '_<..'| '_->' |
         '_<-' | '_<=>'| '_=>' | '_<=' |
         '_-|>'| '_<|-'| '_-/>'| '_</-'|
         '_~>' | '_<~' | '_~|>'| '_<|~'|
         '_~/>'| '_</~'
         )
      ;

content
    @init {
        count = 1
    }
    : ('_')? '['
      (
         { count > 0 }?
         (
           ~ ('[' | ']')
           | '[' { count += 1 } 
           | ']' { count -= 1 }
         )
      )*
    ;

  link
     :  '"' (   ~('"')  | '\\"'  )* '"'
     ;



// --------------- separators -----------------

ID_SYSTEM
    :   ('a'..'z'|'A'..'Z'|'_'|'.'|'0'..'9')+
    ;
   
EDGE_ATTR
    :   (':'|'::')
    ;

COMMENT
    :   
    ( '//' ~('\n'|'\r')* '\r'? '\n'
    | ('/*' | '/!*') (.)*? '*/'
    ) -> channel(HIDDEN)
    ;
     
fragment
HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> channel(HIDDEN)
    ;

fragment
OCTAL_ESC
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;

fragment
UNICODE_ESC
    :   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
    ;
