# DROP TABLES

student_table_drop      = "DROP TABLE IF EXISTS student"
course_table_drop       = "DROP TABLE IF EXISTS course"
tests_table_drop        = "DROP TABLE IF EXISTS tests"
progress_table_drop     = "DROP TABLE IF EXISTS progress"
group_course_table_drop = "DROP TABLE IF EXISTS group_course"
certificate_table_drop  = "DROP TABLE IF EXISTS certificate"
log_table_drop          = "DROP TABLE IF EXISTS log"
groupstudent_table_drop = "DROP TABLE IF EXISTS groupstudent"

# CREATE TABLES

student_table_create = ("""
                                        CREATE TABLE IF NOT EXISTS student (
                                            id BIGSERIAL,
                                            aluno_id int,
                                            nome varchar(255) NULL,
                                            email varchar(255) NULL,
                                            username varchar(255) NULL,
                                            cpf varchar(255) NULL,
                                            nascimento varchar(255) NULL,
                                            ddd varchar(255) NULL,
                                            telefone varchar(255) NULL,
                                            endereco varchar(255) NULL,
                                            numero varchar(255) NULL,
                                            complemento varchar(255) NULL,
                                            bairro varchar(255) NULL,
                                            cep varchar(255) NULL,
                                            cidade varchar(255) NULL,
                                            uf varchar(255) NULL,
                                            profissao varchar(255) NULL,
                                            email_contato varchar(255) NULL,
                                            site varchar(255) NULL,
                                            twitter varchar(255) NULL,
                                            facebook varchar(255) NULL,
                                            google varchar(255) NULL,
                                            linkedin varchar(255) NULL,
                                            curriculum text NULL,
                                            biografia varchar(255) NULL,
                                            tipo varchar(255) NULL,
                                            status varchar(255) NULL,
                                            data_cadastro varchar(255) NULL,
                                            ultimo_acesso varchar(255) NULL,
                                            personalizado varchar(255) NULL,
                                            anotacoes text NULL,
                                            campos_personalizados varchar(255) NULL,
                                            foto varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

course_table_create                = ("""
                                        CREATE TABLE IF NOT EXISTS course (
                                            id BIGSERIAL,
                                            curso_id varchar(255) NULL,
                                            categoria_id varchar(255) NULL,
                                            titulo varchar(255) NULL,
                                            titulo_apresentacao varchar(255) NULL,
                                            titulo_destaque varchar(255) NULL,
                                            chamada text NULL,
                                            data_lancamento varchar(255) NULL,
                                            carga_horaria varchar(255) NULL,
                                            periodo_acesso varchar(255) NULL,
                                            url_curso varchar(255) NULL,
                                            url_index_course varchar(255) NULL,
                                            url_checkout varchar(255) NULL,
                                            suporte varchar(255) NULL,
                                            periodo_suporte varchar(255) NULL,
                                            emitir_certificado varchar(255) NULL,
                                            eduzz_cod varchar(255) NULL,
                                            link_eduzz varchar(255) NULL,
                                            hotmart_cod varchar(255) NULL,
                                            hotlink varchar(255) NULL,
                                            ordem_curso varchar(255) NULL,
                                            nome_professor varchar(255) NULL,
                                            foto_professor varchar(255) NULL,
                                            professor_id varchar(255) NULL,
                                            preco varchar(255) NULL,
                                            preco_sem_desconto varchar(255) NULL,
                                            parcelamento_maximo varchar(255) NULL,
                                            parcelamento_sem_juros varchar(255) NULL,
                                            tipo_boleto_vencimento varchar(255) NULL,
                                            periodo_boleto_venc varchar(255) NULL,
                                            opcao_venda varchar(255) NULL,
                                            data_venc_boleto varchar(255) NULL,
                                            opcao_pagamento varchar(255) NULL,
                                            tipo_checkout varchar(255) NULL,
                                            inicio_vendas varchar(255) NULL,
                                            fim_vendas varchar(255) NULL,
                                            status_lancamento varchar(255) NULL,
                                            status varchar(255) NULL,
                                            foto text NULL,
                                            cover text NULL,
                                            video text NULL,
                                            resumo text NULL,
                                            sobre text NULL,
                                            destina text NULL,
                                            media_emitir varchar(255) NULL,
                                            sobre_certificado text NULL,
                                            certificado_template_id varchar(255) NULL,
                                            vender_certificado varchar(255) NULL,
                                            parcelamento_maximo_certificado varchar(255) NULL,
                                            parcelamento_sem_juros_certificado varchar(255) NULL,
                                            tipo_boleto_vencimento_certificado varchar(255) NULL,
                                            periodo_boleto_venc_certificado varchar(255) NULL,
                                            data_venc_boleto_certificado varchar(255) NULL,
                                            opcao_pagamento_certificado varchar(255) NULL,
                                            tipo_checkout_certificado varchar(255) NULL,
                                            valor_certificado varchar(255) NULL,
                                            vender_prazo varchar(255) NULL,
                                            parcelamento_maximo_periodo varchar(255) NULL,
                                            parcelamento_sem_juros_periodo varchar(255) NULL,
                                            tipo_boleto_vencimento_periodo varchar(255) NULL,
                                            periodo_boleto_venc_periodo varchar(255) NULL,
                                            data_venc_boleto_periodo varchar(255) NULL,
                                            opcao_pagamento_periodo varchar(255) NULL,
                                            tipo_checkout_periodo varchar(255) NULL,
                                            vender_suporte varchar(255) NULL,
                                            parcelamento_maximo_suporte varchar(255) NULL,
                                            parcelamento_sem_juros_suporte varchar(255) NULL,
                                            tipo_boleto_vencimento_suporte varchar(255) NULL,
                                            periodo_boleto_venc_suporte varchar(255) NULL,
                                            data_venc_boleto_suporte varchar(255) NULL,
                                            opcao_pagamento_suporte varchar(255) NULL,
                                            tipo_checkout_suporte varchar(255) NULL,
                                            tipo_pix_vencimento varchar(255) NULL,
                                            periodo_pix_venc varchar(255) NULL,
                                            data_venc_pix varchar(255) NULL,
                                            tipo_pix_vencimento_periodo varchar(255) NULL,
                                            periodo_pix_venc_periodo varchar(255) NULL,
                                            data_venc_pix_periodo varchar(255) NULL,
                                            tipo_pix_vencimento_suporte varchar(255) NULL,
                                            periodo_pix_venc_suporte varchar(255) NULL,
                                            data_venc_pix_suporte varchar(255) NULL,
                                            tipo_pix_vencimento_certificado varchar(255) NULL,
                                            periodo_pix_venc_certificado varchar(255) NULL,
                                            data_venc_pix_certificado varchar(255) NULL,
                                            total_aulas varchar(255) NULL,
                                            total_modulos varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

tests_table_create             = ("""
                                        CREATE TABLE IF NOT EXISTS tests (
                                            id BIGSERIAL,
                                            curso_id varchar(255) NULL,
                                            curso varchar(255) NULL,
                                            aluno_id varchar(255) NULL,
                                            nome_aluno varchar(255) NULL,
                                            prova varchar(255) NULL,
                                            tipo varchar(255) NULL,
                                            modulo varchar(255) NULL,
                                            modulo_id varchar(255) NULL,
                                            aula varchar(255) NULL,
                                            aula_id varchar(255) NULL,
                                            nota_prova varchar(255) NULL,
                                            pontos varchar(255) NULL,
                                            status_prova varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

progress_table_create         = ("""
                                        CREATE TABLE IF NOT EXISTS progress (
                                            id BIGSERIAL, 
                                            curso_id varchar(255) NULL,
                                            curso_tiulo varchar(255) NULL,
                                            aluno_id varchar(255) NULL,
                                            aluno_nome varchar(255) NULL,
                                            total_aula varchar(255) NULL,
                                            aulas_acessadas varchar(255) NULL,
                                            progresso varchar(255) NULL,
                                            visualizacoes varchar(255) NULL,
                                            suporte varchar(255) NULL,
                                            ultimo_acesso varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        ) 
                                    """)

group_course_table_create     = ("""
                                        CREATE TABLE IF NOT EXISTS group_course (
                                            id serial,
                                            grupo_id varchar(255) NULL,
                                            grupo_nome varchar(255) NULL,
                                            status varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

certificate_table_create  = ("""
                                        CREATE TABLE IF NOT EXISTS certificate (
                                            id BIGSERIAL,
                                            certificado_id varchar(255) NULL,
                                            curso_id varchar(255) NULL,
                                            curso_titulo varchar(255) NULL,
                                            aluno_id varchar(255) NULL,
                                            aluno_nome varchar(255) NULL,
                                            media_final varchar(255) NULL,
                                            iniciado varchar(255) NULL,
                                            concluido varchar(255) NULL,
                                            carga_horaria varchar(255) NULL,
                                            certificado_link varchar(255) NULL,
                                            certificado_pdf varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

log_table_create  = ("""
                                        CREATE TABLE IF NOT EXISTS log (
                                            id BIGSERIAL,
                                            log_id varchar(255) NULL,
                                            curso_id varchar(255) NULL,
                                            curso_titulo varchar(255) NULL,
                                            modulo_id varchar(255) NULL,
                                            aula_id varchar(255) NULL,
                                            aula_titulo varchar(255) NULL,
                                            aluno_id varchar(255) NULL,
                                            aluno_nome varchar(255) NULL,
                                            ultima_visualizacao varchar(255) NULL,
                                            tempo_aula varchar(255) NULL,
                                            data_conclusao varchar(255) NULL,
                                            aula_concluido varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)

groupstudent_table_create = ("""
                                        CREATE TABLE IF NOT EXISTS groupstudent (
                                            id BIGSERIAL,
                                            grupo_id varchar(255) NULL,
                                            grupo_nome varchar(255) NULL,
                                            aluno_id varchar(255) NULL,
                                            nome varchar(255) NULL,
                                            email varchar(255) NULL,
                                            PRIMARY KEY(id)
                                        )
                                    """)



# INSERT RECORDS

student_table_insert   = ("""
                                        INSERT INTO student 
                                            (
                                                aluno_id,
                                                nome,
                                                email,
                                                username,
                                                cpf,
                                                nascimento,
                                                ddd,
                                                telefone,
                                                endereco,
                                                numero,
                                                complemento,
                                                bairro,
                                                cep,
                                                cidade,
                                                uf,
                                                profissao,
                                                email_contato,
                                                site,
                                                twitter,
                                                facebook,
                                                google,
                                                linkedin,
                                                curriculum,
                                                biografia,
                                                tipo,
                                                status,
                                                data_cadastro,
                                                ultimo_acesso,
                                                personalizado,
                                                anotacoes,
                                                campos_personalizados,
                                                foto) 
                                        VALUES 
                                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                                    """)

course_table_insert                  = ("""
                                        INSERT INTO course 
                                            (
                                                curso_id,
                                                categoria_id,
                                                titulo,
                                                titulo_apresentacao,
                                                titulo_destaque,
                                                chamada,
                                                data_lancamento,
                                                carga_horaria,
                                                periodo_acesso,
                                                url_curso,
                                                url_index_course,
                                                url_checkout,
                                                suporte,
                                                periodo_suporte,
                                                emitir_certificado,
                                                eduzz_cod,
                                                link_eduzz,
                                                hotmart_cod,
                                                hotlink,
                                                ordem_curso,
                                                nome_professor,
                                                foto_professor,
                                                professor_id,
                                                preco,
                                                preco_sem_desconto,
                                                parcelamento_maximo,
                                                parcelamento_sem_juros,
                                                tipo_boleto_vencimento,
                                                periodo_boleto_venc,
                                                opcao_venda,
                                                data_venc_boleto,
                                                opcao_pagamento,
                                                tipo_checkout,
                                                inicio_vendas,
                                                fim_vendas,
                                                status_lancamento,
                                                status,
                                                foto,
                                                cover,
                                                video,
                                                resumo,
                                                sobre,
                                                destina,
                                                media_emitir,
                                                sobre_certificado,
                                                certificado_template_id,
                                                vender_certificado,
                                                parcelamento_maximo_certificado,
                                                parcelamento_sem_juros_certificado,
                                                tipo_boleto_vencimento_certificado,
                                                periodo_boleto_venc_certificado,
                                                data_venc_boleto_certificado,
                                                opcao_pagamento_certificado,
                                                tipo_checkout_certificado,
                                                valor_certificado,
                                                vender_prazo,
                                                parcelamento_maximo_periodo,
                                                parcelamento_sem_juros_periodo,
                                                tipo_boleto_vencimento_periodo,
                                                periodo_boleto_venc_periodo,
                                                data_venc_boleto_periodo,
                                                opcao_pagamento_periodo,
                                                tipo_checkout_periodo,
                                                vender_suporte,
                                                parcelamento_maximo_suporte,
                                                parcelamento_sem_juros_suporte,
                                                tipo_boleto_vencimento_suporte,
                                                periodo_boleto_venc_suporte,
                                                data_venc_boleto_suporte,
                                                opcao_pagamento_suporte,
                                                tipo_checkout_suporte,
                                                tipo_pix_vencimento,
                                                periodo_pix_venc,
                                                data_venc_pix,
                                                tipo_pix_vencimento_periodo,
                                                periodo_pix_venc_periodo,
                                                data_venc_pix_periodo,
                                                tipo_pix_vencimento_suporte,
                                                periodo_pix_venc_suporte,
                                                data_venc_pix_suporte,
                                                tipo_pix_vencimento_certificado,
                                                periodo_pix_venc_certificado,
                                                data_venc_pix_certificado,
                                                total_aulas,
                                                total_modulos
                                            ) 
                                        VALUES 
                                            (
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                %s,%s,%s,%s,%s
                                            ) 
                                    """)

tests_table_insert               = ("""
                                        INSERT INTO tests 
                                            (
                                                curso_id,
                                                curso,
                                                aluno_id,
                                                nome_aluno,
                                                prova,
                                                tipo,
                                                modulo,
                                                modulo_id,
                                                aula,
                                                aula_id,
                                                nota_prova,
                                                pontos,
                                                status_prova
                                            ) 
                                        VALUES 
                                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                                    """)

progress_table_insert           = ("""
                                        INSERT INTO progress 
                                            ( 
                                                curso_id,
                                                curso_tiulo,
                                                aluno_id,
                                                aluno_nome,
                                                total_aula,
                                                aulas_acessadas,
                                                progresso,
                                                visualizacoes,
                                                suporte,
                                                ultimo_acesso
                                            ) 
                                        VALUES 
                                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                                        """)
group_course_table_insert = ("""
                                        INSERT INTO group_course 
                                            (
                                                grupo_id,
                                                grupo_nome,
                                                status
                                            ) 
                                        VALUES 
                                            (%s, %s, %s) 
                                    """)

certificate_table_insert    = ("""
                                        INSERT INTO certificate
                                            (
                                                certificado_id,
                                                curso_id,
                                                curso_titulo,
                                                aluno_id,
                                                aluno_nome,
                                                media_final,
                                                iniciado,
                                                concluido,
                                                carga_horaria,
                                                certificado_link,
                                                certificado_pdf
                                            ) 
                                        VALUES 
                                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                                    """)

log_table_insert    = ("""
                                        INSERT INTO log
                                            (
                                                log_id,
                                                curso_id,
                                                curso_titulo,
                                                modulo_id,
                                                aula_id,
                                                aula_titulo,
                                                aluno_id,
                                                aluno_nome,
                                                ultima_visualizacao,
                                                tempo_aula,
                                                data_conclusao,
                                                aula_concluido
                                            ) 
                                        VALUES 
                                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
                                    """)

groupstudent_table_insert   = ("""
                                        INSERT INTO groupstudent
                                            (
                                                grupo_id,
                                                grupo_nome,
                                                aluno_id,
                                                nome,
                                                email
                                            ) 
                                        VALUES 
                                            (%s, %s, %s, %s, %s)  
                                    """)

# QUERY LISTS

create_table_queries = ([
                            student_table_create,
                            course_table_create,
                            tests_table_create,
                            progress_table_create,
                            group_course_table_create,
                            certificate_table_create,
                            log_table_create,
                            groupstudent_table_create
                        ])
drop_table_queries   = ([
                            student_table_drop,     
                            course_table_drop,      
                            tests_table_drop,       
                            progress_table_drop,    
                            group_course_table_drop,       
                            certificate_table_drop, 
                            log_table_drop,         
                            groupstudent_table_drop
                       ])
insert_table_queries = ({
                            "student":student_table_insert,
                            "course":course_table_insert,
                            "tests":tests_table_insert,
                            "progress":progress_table_insert,
                            "group_course":group_course_table_insert,
                            "certificate":certificate_table_insert,
                            "log":log_table_insert,
                            "groupstudent":groupstudent_table_insert
                        })