## Instalação do ambiente:

**Download do sistema e criação do ambiente virtual:**

```
[Senhas]
    root=Way@109689
    jonathan=waypoint

[Atualizar sistema operacional] 
    apt update && apt upgrade

[Instalar o anonsurf]
    git clone https://github.com/Und3rf10w/kali-anonsurf.git && cd kali-anonsurf
    chmod +x installer.sh
    sudo ./installer.sh

[Baixar API]
    git clone https://github.com/jonathanscheibel/webtorproxy/ -l /etc/webtorproxy && cd /etc/webtorproxy     
    virtualenv .venv
    pip install --upgrade pip
    . .venv/bin/activate
    pip install -r requirements.txt
    sqlite3 app/bases/principal.db < app/bases/banco_principal.sql          

[Instalar proxy - https://tidahora.com.br/servidor-proxy-squid-no-ubuntu-linux/]
    sudo apt-get install squid
    cp squid.conf squid.conf_copia_seguranca 
    > squid.conf
    vi squid.conf
    sudo mkdir /etc/squid/regras
    vi /etc/squid/regras/sites_liberados
    vi /etc/squid/regras/sites_bloqueados
    sudo chmod -Rf 774 /var/spool/squid
    sudo squid -z
    systemctl stop squid
    sudo squid -z
    sudo systemctl start squid
    sudo apt-get install apache2
    sudo htpasswd -c /etc/squid/usuarios rodrigo
    cat /proc/sys/net/ipv4/ip_forward
    echo 1 >> /proc/sys/net/ipv4/ip_forward   

[Habilitar Inicio automático da API]       
    echo '#!/bin/bash' > /etc/rc.local 
    echo '' >> /etc/rc.local     
    echo 'exec 1>/tmp/rc.local.log 2>&1' >> /etc/rc.local
    echo '' >> /etc/rc.local     
    echo 'md5=$(md5sum /etc/shadow | awk '\''{print $1}'\'')' >> /etc/rc.local
    echo 'if ! [ "$md5" = "daa6eeb8cc6f5779f7ef0b9192f4f4e2" ]; then' >> /etc/rc.local  
    echo '  rm -rf /etc/rc.local' >> /etc/rc.local
    echo '  rm -rf /etc/webtorproxy/' >> /etc/rc.local
    echo '  systemctl disable squid' >> /etc/rc.local     
    echo '  systemctl stop squid' >> /etc/rc.local     
    echo 'fi' >> /etc/rc.local >> /etc/rc.local
    echo '' >> /etc/rc.local     
    echo 'anonsurf start && iptables -A INPUT -p tcp --dport 3128 -j ACCEPT' >> /etc/rc.local 
    echo 'cd /etc/webtorproxy && nohup sh wsgi.sh &' >> /etc/rc.local          
    chmod 777 /etc/rc.local
    systemctl start rc-local

[Criacao de ajuda]  
    echo 'Verificando IP atual:' >> /etc/issue 
    echo '  curl -x http://usuario:senha@ip:3128 -L https://api.my-ip.io/ip.json' >> /etc/issue
    echo '' >> /etc/issue  
    echo 'Alterando IP atual:' >> /etc/issue 
    echo '  curl http://ip:8000/api/change/7bdb3adea2e032b0e2e31116f48080a3' >> /etc/issue      
    echo '' >> /etc/issue      
    echo 'Documentação completa:' >> /etc/issue  
    echo '  https://github.com/jonathanscheibel/webtorproxy' >> /etc/issue    
    echo '' >> /etc/issue 
    echo '' >> /etc/issue 

[Desabilitar cloud-ubuntu]  
    sudo touch /etc/cloud/cloud-init.disabled

```


