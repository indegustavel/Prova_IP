# PROVA – Introdução à Programação (BIA)
# Nome completo: Gustavo Henrique Barros da Silva
# Matrícula: 202505701
# E-mail institucional: henriquegustavo@discnte.ufg.br

import tkinter as tk #para criar a interface gráfica
from tkinter import ttk, messagebox
import requests #para fazer as chamadas à API
import threading #para não travar a interface durante as requisições
import time
from datetime import datetime #para registrar o momento das atualizações
import json #para manipular o cache de dados
import os


class CryptoApp:
    def __init__(self, root):
        # configura a janela
        self.root = root
        self.root.title("Monitor de Cripto  - By Gustavo H.B. da Silva")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # variaveis p guardar os valores
        self.crypto_var = tk.StringVar()
        self.price_var = tk.StringVar(value="Preço: --")
        self.change_var = tk.StringVar(value="Variação 24h: --")
        self.last_update_var = tk.StringVar(value="Última atualização: --")

        # Controle de requisição
        self.last_req_time = 0

        # Lista de cripto moedas inicial (apenas bitcoin até carregar mais)
        self.crypto_list = [("Bitcoin (BTC)", "bitcoin")]

        # Monta a tela
        self.create_widgets()

        # Carrega a lista de moedas numa thread separada para não travar
        threading.Thread(target=self.load_crypto_list).start()

        # Atualiza os dados da criptomoeda
        self.update_data()

    def load_crypto_list(self):

        # Carrega a lista de criptomoedas disponíveis

        try:
            # Mostra q esta carregando
            self.root.after(0, lambda: self.crypto_dropdown.configure(state="disabled"))

            # Faz a requisição a API das Criptomoedas (CoinGecko)
            response = requests.get(
                "https://api.coingecko.com/api/v3/coins/markets",
                params={
                    "vs_currency": "usd",
                    "order": "market_cap_desc",
                    "per_page": 20,
                    "page": 1,
                }
            )

            if response.status_code == 200:
                data = response.json()
                # Formata os nomes e IDs
                self.crypto_list = [(f"{coin['name']} ({coin['symbol'].upper()})", coin['id']) for coin in data]

                # Atualiza o dropdown)
                self.root.after(0, lambda: self.update_dropdown())
            else:
                print(f"Erro ao carregar lista: {response.status_code}")
        except Exception as e:
            print(f"Falha ao carregar lista: {e}")
        finally:
            # Habilita o dropdown de novo
            self.root.after(0, lambda: self.crypto_dropdown.configure(state="readonly"))

    def update_dropdown(self):
        #Atualiza a lista do dropdown com as moedas carregadas
        self.crypto_dropdown['values'] = [name for name, _ in self.crypto_list]

    def create_widgets(self):

        #Cria os elementos da interface

        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Título
        title_label = tk.Label(
            main_frame,
            text="Monitoramento de Cripto Moedas - By Gustavo H. B. da Silva",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        title_label.pack(pady=(0, 20))

        # Frame para seleção
        select_frame = tk.Frame(main_frame, bg="#f0f0f0")
        select_frame.pack(fill="x", pady=10)

        # Label para dropdown
        select_label = tk.Label(
            select_frame,
            text="Escolha uma moeda:",
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        select_label.pack(side="left", padx=(0, 10))

        # Dropdown de moedas
        self.crypto_dropdown = ttk.Combobox(
            select_frame,
            textvariable=self.crypto_var,
            values=[name for name, _ in self.crypto_list],
            width=25,
            state="readonly"
        )
        self.crypto_dropdown.pack(side="left")
        self.crypto_dropdown.current(0)

        # df para dados
        data_frame = tk.Frame(main_frame, bg="white", bd=1, relief="solid")
        data_frame.pack(fill="both", expand=True, pady=15)

        # Informações de preço
        price_label = tk.Label(
            data_frame,
            textvariable=self.price_var,
            font=("Arial", 20, "bold"),
            bg="white"
        )
        price_label.pack(pady=(20, 5))

        # Informações de variação
        self.change_label = tk.Label(
            data_frame,
            textvariable=self.change_var,
            font=("Arial", 14),
            bg="white"
        )
        self.change_label.pack(pady=5)

        # Informações de atualização
        update_button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        update_button_frame.pack(fill="x", pady=10)

        self.update_button = tk.Button(
            update_button_frame,
            text="ATUALIZAR DADOS",
            command=self.update_data,
            bg="#A9A9A9",  # laranja mais chamativo
            fg="black",
            font=("Arial", 12, "bold"),
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"  # muda o cursor quando passa por cima
        )
        self.update_button.pack(expand=True)

        # Atualiza quando seleciona
        self.crypto_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_data())

    def get_coin_id(self):
        #Pega o ID da moeda selecionada
        selected_name = self.crypto_var.get()
        for name, id in self.crypto_list:
            if name == selected_name:
                return id
        return "bitcoin"  # fallback

    def update_data(self):
        #Atualiza os dados numa thread separada
        threading.Thread(target=self._fetch_data).start()

    def _fetch_data(self):
        #Busca os dados da API
        try:
            # Mostra indicador de carregamento
            self.root.after(0, lambda: self.price_var.set("Carregando..."))
            self.root.after(0, lambda: self.change_var.set(""))

            # Pega o ID da moeda selecionada
            coin_id = self.get_coin_id()

            # Verifica se precisa esperar
            current_time = time.time()
            if current_time - self.last_req_time < 5:  # 5 segundos entre requisições
                # Espera na thread secundária (não trava a interface)
                self.root.after(0, lambda: self.price_var.set("Aguardando API..."))
                time.sleep(5)

            self.last_req_time = time.time()

            # Busca dados
            response = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{coin_id}"
            )

            if response.status_code == 200:
                data = response.json()

                # Extrai os dados
                price = data['market_data']['current_price']['usd']
                change_24h = data['market_data']['price_change_percentage_24h']

                # Atualiza na thread principal
                self.root.after(0, lambda: self.update_ui(price, change_24h))

            elif response.status_code == 429:
                # Erro de muitas requisições
                self.root.after(0, lambda: messagebox.showinfo("Limite",
                                                               "API bloqueou por muitas consultas. Espere um pouco."))
                self.root.after(0, lambda: self.price_var.set("API limitou acesso"))
            else:
                # Outros erros
                self.root.after(0, lambda: self.price_var.set(f"Erro {response.status_code}"))

        except Exception as e:
            print(f"Erro: {e}")
            self.root.after(0, lambda: self.price_var.set("Erro na conexão"))

    def update_ui(self, price, change_24h):
        #Atualiza a interface com os dados recebidos
        # Atualiza preço e variação
        self.price_var.set(f"Preço: ${price:,.2f}")
        self.change_var.set(f"Variação 24h: {change_24h:.2f}%")

        # Cor verde se positivo, vermelho se negativo
        if change_24h >= 0:
            self.change_label.config(fg="green")
        else:
            self.change_label.config(fg="red")

        # Atualiza horário
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.last_update_var.set(f"Última atualização: {current_time}")


# Inicia o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()