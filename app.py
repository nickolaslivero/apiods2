import streamlit as st
from vaccineBlockchain import VaccineBlockchain
from vaccineRecord import VaccineRecord

# Inicializando a blockchain com dificuldade 4
blockchain = VaccineBlockchain(4)

# Função para adicionar um novo registro de vacina
def add_vaccine_record():
    global blockchain
    st.title("Sistema de Registro de Vacinas com Blockchain")

    patient_name = st.text_input("Nome do Paciente")
    vaccine_type = st.text_input("Tipo de Vacina")
    vaccination_date = st.date_input("Data da Vacinação")
    unique_id = st.text_input("ID Único")

    if st.button("Adicionar Registro de Vacina"):
        if patient_name and vaccine_type and vaccination_date and unique_id:
            blockchain.create_vaccine_record(
                patient_name,
                vaccine_type,
                vaccination_date.strftime("%Y-%m-%d"),
                unique_id,
            )
            st.success("Registro de vacina adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")


# Função para visualizar a blockchain
def view_blockchain():
    global blockchain
    st.title("Visualizar Blockchain de Vacinas")
    for block in blockchain.blocks:
        st.write(block)

# Menu de navegação
st.sidebar.title("Navegação")
option = st.sidebar.selectbox("Escolha uma opção", ["Adicionar Registro de Vacina", "Visualizar Blockchain"])

if option == "Adicionar Registro de Vacina":
    add_vaccine_record()
elif option == "Visualizar Blockchain":
    view_blockchain()
