import streamlit as st
import json
import os

ARQUIVO_PRODUTOS = 'produtos.json'

def carregar_produtos():
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []
    with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

st.title("🍽️ Gastro Bar Soberano Paladar")
st.subheader("Registro de Pedidos")

produtos = carregar_produtos()

if not produtos:
    st.warning("⚠️ Nenhum produto cadastrado.")
else:
    produto_nomes = [p['nome'] for p in produtos]
    selecionado = st.selectbox("Escolha um produto:", produto_nomes)
    quantidade = st.number_input("Quantidade", min_value=1, value=1)

    if st.button("Registrar Pedido"):
        idx = produto_nomes.index(selecionado)
        produto = produtos[idx]

        if produto['estoque'] >= quantidade:
            subtotal = produto['preco'] * quantidade
            produto['estoque'] -= quantidade
            salvar_produtos(produtos)
            st.success(f"✅ Pedido registrado:\n\n{quantidade}x {selecionado}\n\n💰 Total: R$ {subtotal:.2f}")
        else:
            st.error("⚠️ Estoque insuficiente!")

st.markdown("---")
st.subheader("📦 Estoque Atualizado")
for p in produtos:
    st.write(f"{p['nome']} - Estoque: {p['estoque']} unidades")