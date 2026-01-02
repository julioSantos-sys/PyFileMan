# Nome do programa
PROGRAM_NAME = pyfman

# Diretório de instalação dos arquivos
INSTALL_DIR ?= /usr/local/lib/$(PROGRAM_NAME)

# Diretório do wrapper executável
BIN_DIR ?= /usr/local/bin

# Python usado para rodar o script
PYTHON = python3

# Target default
all: install

# Instala o programa
install:
	@echo "Criando diretório de instalação..."
	@sudo mkdir -p $(INSTALL_DIR)
	@echo "Copiando arquivos para $(INSTALL_DIR)..."
	@sudo cp -r app.py core interface $(INSTALL_DIR)/
	@echo "Criando wrapper executável em $(BIN_DIR)/$(PROGRAM_NAME)..."
	@echo "#!/bin/sh" | sudo tee $(BIN_DIR)/$(PROGRAM_NAME) > /dev/null
	@echo "$(PYTHON) $(INSTALL_DIR)/app.py" | sudo tee -a $(BIN_DIR)/$(PROGRAM_NAME) > /dev/null
	@sudo chmod +x $(BIN_DIR)/$(PROGRAM_NAME)
	@echo "Instalação concluída! Rode '$(PROGRAM_NAME)' para iniciar."

# Remove a instalação
uninstall:
	@echo "Removendo wrapper..."
	@sudo rm -f $(BIN_DIR)/$(PROGRAM_NAME)
	@echo "Removendo arquivos do programa..."
	@sudo rm -rf $(INSTALL_DIR)
	@echo "Programa removido!"

# Limpeza de arquivos temporários (opcional)
clean:
	find . -name "*.pyc" -delete
	@echo "Arquivos temporários removidos."

# Rodar o programa sem instalar
run:
	$(PYTHON) app.py
