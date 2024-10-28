# Criptografia: Conceitos, Métodos e Aplicações Práticas

A criptografia é o conjunto de técnicas e práticas para proteger informações por meio de codificação, transformando dados em um formato ilegível para terceiros. Ao longo dos anos, a criptografia evoluiu significativamente, desde a icônica máquina Enigma, usada na Segunda Guerra Mundial para proteger comunicações militares, até algoritmos avançados empregados para proteger dados em serviços digitais modernos.

## Conceitos Básicos

Criptografar dados significa aplicar métodos que dificultem ou impeçam o acesso direto às informações sem as devidas chaves de decodificação. A criptografia é essencial para manter a segurança de dados em transações financeiras, comunicações online e armazenamento de informações pessoais.

### Tipos de Criptografia

#### 1. Criptografia Simétrica
Na criptografia simétrica, uma única chave é usada tanto para criptografar quanto para descriptografar os dados. A segurança depende da confidencialidade da chave: se for comprometida, qualquer pessoa com acesso pode decifrar a informação.

#### 2. Criptografia Assimétrica
Diferente da criptografia simétrica, a criptografia assimétrica usa duas chaves distintas: uma chave pública e uma chave privada. A chave pública pode ser compartilhada livremente e é usada para criptografar dados, enquanto a chave privada, que deve ser mantida em sigilo, é usada para descriptografar esses dados. Esse tipo de criptografia é amplamente utilizado na comunicação segura de dados pela internet, como em servidores web para processos de login e transferências seguras.

### Cifra de Substituição

A cifra de substituição substitui caracteres específicos para codificar uma mensagem. O Base64, por exemplo, é um método comum de codificação, que representa dados binários em caracteres ASCII. Ele é amplamente usado para transferir dados textuais, como ao codificar credenciais em cabeçalhos de autenticação básica.

### Hash e Salt

O hash é uma função que transforma dados em uma sequência fixa de caracteres (chamada “hash”), geralmente irreversível, usada para verificar a integridade de arquivos e senhas. Algoritmos como SHA-512 são muito mais seguros que o MD5, já que possuem menos vulnerabilidades.

Para aumentar a segurança, o “salt” é frequentemente adicionado ao hash. Trata-se de um valor aleatório incluído antes da operação de hash, tornando mais difícil para atacantes decifrar a senha. No entanto, mesmo com o salt, técnicas de força bruta (bruteforcing) ainda podem, em alguns casos, conseguir decifrar os dados.

#### Websites e Ferramentas de Consulta de Hashes

Sites como [hashes.com](http://hashes.com) e [hashkiller.co.uk](http://hashkiller.co.uk) permitem a consulta de hashes conhecidos, facilitando a descoberta de senhas. Essas plataformas podem ser úteis em auditorias de segurança para checar a robustez das senhas.

## Técnicas e Ferramentas de Bruteforcing

Bruteforcing é um método que utiliza tentativa e erro para descobrir senhas ou chaves criptográficas. Este método automatiza tentativas com diversas combinações para obter acesso a um sistema protegido.

### John the Ripper

John the Ripper é uma ferramenta popular para quebrar hashes de senhas. Ele permite o uso de wordlists personalizadas, facilitando o processo:

```bash
john senha.txt # Execução básica
john senha.txt --format=raw-md5 # Definindo o tipo de hash
john senha.txt --format=raw-md5 --show # Exibindo senhas quebradas
