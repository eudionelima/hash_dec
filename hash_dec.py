
---

## 3. hash_dec.py

```python
#!/usr/bin/env python3
# Desenvolvido por: Dione Lima
# GitHub: github.com/eudionelima

import hashlib
import base64
import argparse
import sys

def decodificar(hash_alvo, wordlist):
    """Decodifica hash composto (MD5->B64->SHA1)."""
    
    tentativas = 0
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as lista:
            for palavra in lista:
                tentativas += 1
                palavra = palavra.strip()
                
                # Pipeline
                md5_hash = hashlib.md5(palavra.encode()).hexdigest()
                b64_hash = base64.b64encode(md5_hash.encode()).decode()
                final_hash = hashlib.sha1(b64_hash.encode()).hexdigest()
                
                if final_hash == hash_alvo:
                    return {
                        'ok': True,
                        'palavra': palavra,
                        'md5': md5_hash,
                        'b64': b64_hash,
                        'sha1': final_hash,
                        'tentativas': tentativas
                    }
    except FileNotFoundError:
        print(f"[ERRO] Wordlist não encontrada: {wordlist}")
        sys.exit(1)
    
    return {'ok': False, 'tentativas': tentativas}

def formatar(dados, hash_alvo):
    """Formata resultado."""
    if not dados['ok']:
        return f"\n[-] Hash não decodificado após {dados['tentativas']} tentativas\n"
    
    return f"""
[+] HASH DECODIFICADO!

    Hash: {hash_alvo}
    Palavra: {dados['palavra']}
    
    Processo:
    [1] MD5("{dados['palavra']}") = {dados['md5']}
    [2] Base64("{dados['md5']}") = {dados['b64']}
    [3] SHA1("{dados['b64']}") = {dados['sha1']}
    
    Tentativas: {dados['tentativas']}
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decodificador de hash')
    parser.add_argument('-s', '--hash', required=True, help='Hash para decodificar')
    parser.add_argument('-w', '--wordlist', default='/usr/share/john/password.lst',
                       help='Arquivo de wordlist')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print(f"  HASH: {args.hash}")
    print(f"  WORDLIST: {args.wordlist}")
    print("=" * 60)
    
    resultado = decodificar(args.hash, args.wordlist)
    print(formatar(resultado, args.hash))
    print("=" * 60)
