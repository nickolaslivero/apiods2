from vaccineBlockchain import VaccineBlockchain

def main():
    blockchain = VaccineBlockchain(4)
    
    # Criar registros de vacina
    blockchain.create_vaccine_record("John Doe", "Pfizer", "2024-05-01", "ID12345")
    blockchain.create_vaccine_record("Jane Smith", "Moderna", "2024-05-02", "ID12346")
    blockchain.create_vaccine_record("Alice Johnson", "AstraZeneca", "2024-05-03", "ID12347")
    blockchain.create_vaccine_record("Bob Brown", "Pfizer", "2024-05-04", "ID12348")

    print(blockchain)

    # Ler registro de vacina
    record = blockchain.read_vaccine_record("ID12345")
    print("Ler registro:", record)

    print("Blockchain é válido?")    
    if not blockchain.is_blockchain_valid():
        print("Não é Válido!!!")
    else:
        print("Sim é Válido!!!")

if __name__ == "__main__":
    main()
