# Generated by Django 4.2.11 on 2024-06-03 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('data', models.DateField(db_comment='Data da aula')),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('V', 'Vespertino'), ('N', 'Noite'), ('I', 'Integral')], db_comment='Turno da aula', max_length=1)),
                ('qtd_aluno', models.IntegerField(db_comment='Número de alunos previsto')),
                ('confirmada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'db_table': 'aula',
                'ordering': ['data', 'turno', 'disciplina'],
            },
        ),
        migrations.CreateModel(
            name='AulaReceita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('qtd_receita', models.IntegerField(db_comment='Quantidade de receitas previstas para a aula')),
            ],
            options={
                'verbose_name': 'Receita da Aula',
                'verbose_name_plural': 'Receitas das Aulas',
                'db_table': 'aulareceita',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome da disciplina', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'db_table': 'disciplina',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do fornecedor', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'db_table': 'fornecedor',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do produto', max_length=100, unique=True)),
                ('quantidade', models.DecimalField(db_comment='Quantidade disponível', decimal_places=5, default=0, max_digits=11)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'produto',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do tipo de receita', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
                'db_table': 'receita',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('sigla', models.CharField(db_comment='Sigla da unidade de medida', max_length=5, unique=True)),
                ('descricao', models.CharField(db_comment='Descrição da unidade de medida', max_length=100)),
            ],
            options={
                'verbose_name': 'Unidade de Medida',
                'verbose_name_plural': 'Unidades de Medida',
                'db_table': 'unidademedida',
                'ordering': ['sigla'],
                'indexes': [models.Index(fields=['sigla'], name='unidademedi_sigla_65c422_idx')],
            },
        ),
        migrations.CreateModel(
            name='TipoCulinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do tipo de culinária', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Culinária',
                'verbose_name_plural': 'Tipos de Culinária',
                'db_table': 'tipoculinaria',
                'ordering': ['nome'],
                'indexes': [models.Index(fields=['nome'], name='tipoculinar_nome_c8e1f6_idx')],
            },
        ),
        migrations.CreateModel(
            name='ReceitaIngrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('quantidade', models.DecimalField(db_comment='quantidade usada na receita por unidade de medida', decimal_places=5, max_digits=11)),
                ('produto', models.ForeignKey(db_comment='ligação com a tabela de produto', on_delete=django.db.models.deletion.RESTRICT, to='apis.produto')),
                ('receita', models.ForeignKey(db_comment='ligação com a tabela de receita', on_delete=django.db.models.deletion.RESTRICT, to='apis.receita')),
            ],
            options={
                'verbose_name': 'Ingrediente da Receita',
                'verbose_name_plural': 'Ingredientes da Receita',
                'db_table': 'receitaingrediente',
            },
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.ManyToManyField(through='apis.ReceitaIngrediente', to='apis.produto'),
        ),
        migrations.AddField(
            model_name='receita',
            name='tipo',
            field=models.ForeignKey(db_comment='ligacao com a tabela de tipo de culinaria', on_delete=django.db.models.deletion.RESTRICT, related_name='tipoculinara', to='apis.tipoculinaria'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do professor', max_length=100)),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'db_table': 'professor',
                'ordering': ['nome'],
                'indexes': [models.Index(fields=['nome'], name='professor_nome_e930d3_idx')],
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='receitas',
            field=models.ManyToManyField(through='apis.ReceitaIngrediente', to='apis.receita'),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.ForeignKey(db_comment='ligação com tabela de unidade de medida', on_delete=django.db.models.deletion.RESTRICT, to='apis.unidademedida'),
        ),
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('data_cotacao', models.DateField(db_comment='Data Cotação')),
                ('valor', models.DecimalField(db_comment='Valor cotado por unidade de medida', decimal_places=2, default=0, max_digits=9)),
                ('produto', models.ForeignKey(db_comment='ligação com tabela de produto', on_delete=django.db.models.deletion.RESTRICT, to='apis.produto')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
                'db_table': 'preco',
                'ordering': ['produto'],
            },
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('data_emissao', models.DateField(db_comment='Data de emissão da nota fiscal')),
                ('valor', models.DecimalField(db_comment='Valor total da nota fiscal', decimal_places=2, max_digits=9)),
                ('fornecedor', models.ForeignKey(db_comment='ligacao com a tabela de fornecedor', on_delete=django.db.models.deletion.RESTRICT, to='apis.fornecedor')),
            ],
            options={
                'verbose_name': 'Nota Fiscal',
                'verbose_name_plural': 'Notas Fiscais',
                'db_table': 'notafiscal',
                'ordering': ['data_emissao'],
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída'), ('A', 'Ajuste de auditoria')], db_comment='Tipo do movimento', max_length=1)),
                ('quantidade', models.DecimalField(db_comment='Quantidade movimentada', decimal_places=2, max_digits=9)),
                ('produto', models.ForeignKey(db_comment='Ligação com a tabela de produto', on_delete=django.db.models.deletion.RESTRICT, to='apis.produto')),
            ],
            options={
                'verbose_name': 'Movimento',
                'verbose_name_plural': 'Movimentos',
                'db_table': 'movimento',
                'ordering': ['produto', 'tipo'],
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('nome', models.CharField(db_comment='Nome do laboratório', max_length=100, unique=True)),
                ('localizacao', models.CharField(db_comment='Localização do laboratório', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Laboratório',
                'verbose_name_plural': 'Laboratórios',
                'db_table': 'laboratorio',
                'ordering': ['nome'],
                'indexes': [models.Index(fields=['nome'], name='laboratorio_nome_89a47b_idx')],
            },
        ),
        migrations.CreateModel(
            name='ItemNotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_comment='Momento da criação do dado')),
                ('data_ateracao', models.DateTimeField(auto_now=True, db_comment='momento da atualização do dado')),
                ('ativo', models.BooleanField(db_comment='Indicador se o dado ainda está ativo', default=True)),
                ('usuario', models.CharField(editable=False, max_length=50)),
                ('preco_unitario', models.DecimalField(db_comment='preço unitário do produto', decimal_places=2, max_digits=9)),
                ('quantidade', models.DecimalField(db_comment='Quantidade comprada', decimal_places=5, max_digits=11)),
                ('notafiscal', models.ForeignKey(db_comment='ligacao com a tabela de nota fiscal', on_delete=django.db.models.deletion.RESTRICT, to='apis.notafiscal')),
                ('produto', models.ForeignKey(db_comment='ligacao com a tabela de produtos', on_delete=django.db.models.deletion.RESTRICT, to='apis.produto')),
            ],
            options={
                'verbose_name': 'Item da Nota Fiscal',
                'verbose_name_plural': 'Itens da Notas Fiscais',
                'db_table': 'itemnotafiscal',
                'ordering': ['notafiscal', 'produto'],
            },
        ),
        migrations.AddIndex(
            model_name='fornecedor',
            index=models.Index(fields=['nome'], name='fornecedor_nome_aaa24a_idx'),
        ),
        migrations.AddIndex(
            model_name='disciplina',
            index=models.Index(fields=['nome'], name='disciplina_nome_0178e1_idx'),
        ),
        migrations.AddField(
            model_name='aulareceita',
            name='aula',
            field=models.ForeignKey(db_comment='Ligação com a tabela de aula', on_delete=django.db.models.deletion.RESTRICT, to='apis.aula'),
        ),
        migrations.AddField(
            model_name='aulareceita',
            name='receita',
            field=models.ForeignKey(db_comment='Ligação com a tabela de receita', on_delete=django.db.models.deletion.RESTRICT, to='apis.receita'),
        ),
        migrations.AddField(
            model_name='aula',
            name='disciplina',
            field=models.ForeignKey(db_comment='Ligação com a tabela de disciplina', on_delete=django.db.models.deletion.RESTRICT, to='apis.disciplina'),
        ),
        migrations.AddField(
            model_name='aula',
            name='laboratorio',
            field=models.ForeignKey(db_comment='Ligação com a tabela de laboratorio', on_delete=django.db.models.deletion.RESTRICT, to='apis.laboratorio'),
        ),
        migrations.AddField(
            model_name='aula',
            name='professor',
            field=models.ForeignKey(db_comment='Ligação com a tabela de professor', on_delete=django.db.models.deletion.RESTRICT, to='apis.professor'),
        ),
        migrations.AddField(
            model_name='aula',
            name='receitas',
            field=models.ManyToManyField(through='apis.AulaReceita', to='apis.receita'),
        ),
        migrations.AddIndex(
            model_name='receitaingrediente',
            index=models.Index(fields=['receita'], name='receitaingr_receita_c2b5a4_idx'),
        ),
        migrations.AddIndex(
            model_name='receitaingrediente',
            index=models.Index(fields=['produto'], name='receitaingr_produto_9431fe_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='receitaingrediente',
            unique_together={('receita', 'produto')},
        ),
        migrations.AddIndex(
            model_name='receita',
            index=models.Index(fields=['nome'], name='receita_nome_49d64e_idx'),
        ),
        migrations.AddIndex(
            model_name='receita',
            index=models.Index(fields=['tipo'], name='receita_tipo_id_988a27_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='receita',
            unique_together={('nome', 'tipo')},
        ),
        migrations.AddIndex(
            model_name='produto',
            index=models.Index(fields=['nome'], name='produto_nome_6bd8e8_idx'),
        ),
        migrations.AddIndex(
            model_name='produto',
            index=models.Index(fields=['unidade'], name='produto_unidade_a1063a_idx'),
        ),
        migrations.AddIndex(
            model_name='preco',
            index=models.Index(fields=['produto'], name='preco_produto_ed67ff_idx'),
        ),
        migrations.AddIndex(
            model_name='notafiscal',
            index=models.Index(fields=['fornecedor'], name='notafiscal_fornece_1a9f9b_idx'),
        ),
        migrations.AddIndex(
            model_name='movimento',
            index=models.Index(fields=['produto'], name='movimento_produto_f6dddc_idx'),
        ),
        migrations.AddIndex(
            model_name='itemnotafiscal',
            index=models.Index(fields=['notafiscal'], name='itemnotafis_notafis_70ed22_idx'),
        ),
        migrations.AddIndex(
            model_name='itemnotafiscal',
            index=models.Index(fields=['produto'], name='itemnotafis_produto_6d925d_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='itemnotafiscal',
            unique_together={('notafiscal', 'produto')},
        ),
        migrations.AddIndex(
            model_name='aulareceita',
            index=models.Index(fields=['aula'], name='aulareceita_aula_id_e1f870_idx'),
        ),
        migrations.AddIndex(
            model_name='aulareceita',
            index=models.Index(fields=['receita'], name='aulareceita_receita_a88ed8_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='aulareceita',
            unique_together={('aula', 'receita')},
        ),
        migrations.AddIndex(
            model_name='aula',
            index=models.Index(fields=['disciplina'], name='aula_discipl_020b79_idx'),
        ),
        migrations.AddIndex(
            model_name='aula',
            index=models.Index(fields=['professor'], name='aula_profess_7c9d49_idx'),
        ),
        migrations.AddIndex(
            model_name='aula',
            index=models.Index(fields=['laboratorio'], name='aula_laborat_6c5f90_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='aula',
            unique_together={('data', 'turno', 'professor')},
        ),
    ]
