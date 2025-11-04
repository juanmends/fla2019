import pandas as pd

#ID FLAMENGO = 614
ANO = 2019
MINIMO = 2014
TIME = 614
TIME_STRING = "Flamengo"

transferencias = "TransferenciasFutebol/transfers.csv"
jogadores = "TransferenciasFutebol/players.csv"
clubes = "TransferenciasFutebol/clubs.csv"
brasileiro = "CampeonatoBrasileiro/campeonato-brasileiro-full.csv"
gols_brasileiro = "CampeonatoBrasileiro/campeonato-brasileiro-gols.csv"

df_jogos_brasileiro = pd.read_csv(brasileiro)

df_jogadores = pd.read_csv(jogadores)

df_gols = pd.read_csv(gols_brasileiro)

df_transferencias_geral = pd.read_csv(transferencias) #IMPORTA CSV
df_transferencias_entrada = df_transferencias_geral[df_transferencias_geral["joined_club_id"] == TIME] #JOGADORES QUE FORAM TRANSFERIDOS PARA O FLAMENGO
df_transferencias_entrada = df_transferencias_entrada[df_transferencias_entrada["year"] <= ANO] #JOGADORES QUE FORAM TRANSFERIDOS ANTES OU DURANTE 2019
df_transferencias_entrada = df_transferencias_entrada[df_transferencias_entrada["year"] > MINIMO]
df_transferencias_saida = df_transferencias_geral[df_transferencias_geral["left_club_id"] == TIME]
df_transferencias_saida = df_transferencias_saida[df_transferencias_saida["year"] < ANO]

ids_entrada = set(df_transferencias_entrada["player_id"])
ids_saida = set(df_transferencias_saida["player_id"])

ids_jogadores = ids_entrada - ids_saida

df_transferencias_entrada = df_transferencias_entrada.loc[df_transferencias_entrada["player_id"].isin(ids_jogadores)]

df_elenco = df_jogadores.loc[df_jogadores["id"].isin(ids_jogadores)].copy()

#JOGADORES SEM TAXA!
transfer_jogadores_sem_taxa = df_transferencias_entrada[df_transferencias_entrada["transfer_fee"] == 0]
jogadores_sem_taxa =  df_elenco[df_elenco["id"].isin(transfer_jogadores_sem_taxa["player_id"])]

#JOGADORES COM TAXA!
transfer_jogadores_com_taxa = df_transferencias_entrada[df_transferencias_entrada["transfer_fee"] > 0]
jogadores_com_taxa = df_elenco[df_elenco["id"].isin(transfer_jogadores_com_taxa["player_id"])]

#JOGOS NO BRASILEIRO
df_jogos_brasileiro["ano"] = pd.to_datetime(df_jogos_brasileiro["data"], format="%d/%m/%Y").dt.year
df_jogos_brasileiro = df_jogos_brasileiro[df_jogos_brasileiro["ano"] == ANO]

jogos_mandante = df_jogos_brasileiro[df_jogos_brasileiro["mandante"] == TIME_STRING]
jogos_visitante = df_jogos_brasileiro[df_jogos_brasileiro["visitante"] == TIME_STRING]

jogos_mandante_vencidos = jogos_mandante[jogos_mandante["vencedor"] == TIME_STRING]
jogos_visitante_vencidos = jogos_visitante[jogos_visitante["vencedor"] == TIME_STRING]

#GOLS NO BRASILEIRO
df_gols = df_gols[df_gols["partida_id"] >= 6506]
df_gols = df_gols[df_gols["partida_id"] < 6886]
df_gols = df_gols[df_gols["clube"] == TIME_STRING]

#GOLS JOGADORES COM TAXA


print(df_gols)

# print(jogos_mandante_vencidos)
# print("\n")
# print(jogos_visitante_vencidos)

# print(df_transferencias_entrada)
# print(jogadores_com_taxa[["name","id"]])
# print(jogadores_sem_taxa[["name","id"]])