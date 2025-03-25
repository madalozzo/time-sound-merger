# Time Wave Merger

Transforma 24 arquivos de hora e 60 arquivos de minuto em 1440 arquivos WAV consolidados, cada um representando uma combinação de hora e minuto.
Evita a necessidade de criar manualmente 1440 arquivos WAV.

## Formato dos Arquivos WAV de entrada

- 24 arquivos de hora no formato "Hxx.wav" (exemplo: "H00.wav", "H01.wav", ..., "H23.wav").
- 60 arquivos de minuto no formato "Mxx.wav" (exemplo: "M00.wav", "M01.wav", ..., "M59.wav").

Se for mesclar 4 arquivos WAV, os arquivos de pré e pós devem ser nomeados como "PRE.wav" e "POS.wav".

Todos os arquivos WAV de entrada devem ter o mesmo formato de áudio (sample rate, número de canais etc.).

## Como Funciona

### merge-two.py
O script merge-two.py mescla dois arquivos WAV (hora e minuto) em um único arquivo WAV consolidado na pasta “out”.

### merge-four.py
O script merge-four.py mescla quatro arquivos WAV (pré, hora, minuto e pós) em um único arquivo WAV consolidado na pasta “out”.

## Requisitos

- Python 3.x  
- Biblioteca nativa “wave” (faz parte da biblioteca padrão do Python)

## Como Executar

1. Coloque seus arquivos WAV na pasta in conforme o padrão acima
2. Ajuste os nomes dos arquivos conforme necessário no código.  
3. Execute o script com:  
   ```bash
   python merge-two.py
   ```
   ou 
   ```bash
    python merge-four.py
   ```
4. Os arquivos de saída serão gerados na pasta “out”, nomeados seguindo o formato “HHHMMM.wav”, por exemplo, “00H00M.wav”, “00H01M.wav”, etc.
