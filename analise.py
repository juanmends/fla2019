import pandas as pd

#ID FLAMENGO = 614
ANO = 2019
TIME = 614

transferencias = "TransferenciasFutebol/transfers.csv"
jogadores = "TransferenciasFutebol/players.csv"
clubes = "TransferenciasFutebol/clubs.csv"
brasileiro = "CampeonatoBrasileiro/campeonato-brasileiro-full.csv"

df_jogadores = pd.read_csv(jogadores)
df_transferencias_geral = pd.read_csv(transferencias) #IMPORTA CSV
df_transferencias_entrada = df_transferencias_geral[df_transferencias_geral["joined_club_id"] == TIME] #JOGADORES QUE FORAM TRANSFERIDOS PARA O FLAMENGO
df_transferencias_entrada = df_transferencias_entrada[df_transferencias_entrada["year"] <= ANO] #JOGADORES QUE FORAM TRANSFERIDOS ANTES OU DURANTE 2019
df_transferencias_entrada = df_transferencias_entrada[df_transferencias_entrada["year"] > 2014]
df_transferencias_saida = df_transferencias_geral[df_transferencias_geral["left_club_id"] == TIME]
df_transferencias_saida = df_transferencias_saida[df_transferencias_saida["year"] < ANO]

ids_entrada = set(df_transferencias_entrada["player_id"])
ids_saida = set(df_transferencias_saida["player_id"])

ids_jogadores = ids_entrada - ids_saida

df_transferencias_entrada = df_transferencias_entrada.loc[df_transferencias_entrada["player_id"].isin(ids_jogadores)]

df_elenco = df_jogadores.loc[df_jogadores["id"].isin(ids_jogadores)].copy()

print(df_elenco[["name","id"]])

print(df_transferencias_entrada)


print()