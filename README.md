# hash_dec.py

Ferramenta de quebra de hash composto via ataque de dicionário, aplicando um pipeline de transformação MD5 → Base64 → SHA1.

## Sobre

O `hash_dec.py` testa palavras de uma wordlist contra um hash alvo, aplicando uma cadeia de transformações (MD5, depois Base64, depois SHA1) sobre cada candidato até encontrar uma correspondência. Útil para identificar a palavra original quando se sabe (ou suspeita) que o hash foi gerado por esse pipeline específico.

## Uso

```bash
python3 hash_dec.py -s <hash> -w <wordlist>
```

**Exemplo:**

```bash
python3 hash_dec.py -s 5f4dcc3b5aa765d61d8327deb882cf99 -w rockyou.txt
```

## Parâmetros

| Parâmetro | Descrição |
|-----------|-----------|
| `-s`      | Hash alvo a ser quebrado |
| `-w`      | Caminho para o arquivo de wordlist |

## Pipeline de Transformação

Para cada palavra candidata da wordlist, é aplicada a seguinte sequência:

```
palavra → MD5 → Base64 → SHA1 → compara com o hash alvo
```

1. **MD5** da palavra candidata
2. **Base64** do hash MD5 resultante
3. **SHA1** do resultado em Base64

Se o SHA1 final coincidir com o hash informado, a palavra é considerada encontrada.

## Requisitos

- Python 3.x
- Nenhuma dependência externa (usa apenas bibliotecas padrão: `hashlib`, `base64`)

## Aviso

Esta ferramenta deve ser utilizada **apenas em contextos autorizados**, como auditorias de segurança em sistemas próprios ou com permissão explícita. A quebra de hashes de terceiros sem autorização pode violar leis locais e internacionais.

## 📄 Licença

MIT
