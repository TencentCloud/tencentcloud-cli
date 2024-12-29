**Example 1: 创建证书**



Input: 

```
tccli gaap CreateCertificate --cli-unfold-argument  \
    --CertificateType 2 \
    --CertificateAlias cert-alias \
    --CertificateKey %0A-----BEGIN%20RSA%20PRIVATE%20KEY-----%0Axxxxxxxxxxx%0A-----END%20RSA%20PRIVATE%20KEY-----%0A \
    --CertificateContent %0A-----BEGIN%20CERTIFICATE-----%0AMIIFmDIUJIJL.......C%0A-----END%20CERTIFICATE-----%0A
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8",
        "CertificateId": "cert-jlwr6865"
    }
}
```

**Example 2: 添加服务器ssl证书**



Input: 

```
tccli gaap CreateCertificate --cli-unfold-argument  \
    --CertificateType 2 \
    --CertificateAlias cert-alias \
    --CertificateKey -----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAn7CUY5bRNtt/YVT9BBDtfyqmF09KXzI+BCrIvrGDrjxRdIsT
Hs0xZL5EbZXt7uc5leXJ47RnVAQtNMCOuqeYtFWNMzGydVchMkImBHEsATE+ukqs
7qUSmbg/BjlOD4hmPNmNz6eljrwMXxNxP0D0BdDMuy+JPLxDp/Hp/Sr3rngL6cbu
AvfhnN/l+HvII79KC9D6w8uIyRoAqybaLrP9P+6yXaBFKzdc7o/LanHEAUaxY/Pb
dP+3HFGNu5DiUHopFHzjl5Kr2GCWDL9N5VMI36H4UF40wvrjna1BWc8em5zVzais
Lbj5pZMRTX2KpMfdDluiT/hzPHs1Ex4h0HGUQwIDAQABAoIBAF7K3BsN8N1GiKPH
ZnYecky1jWhy2ewOj/+7QfTovQkVpyiuUchL99EcnNQMVvQk7+sKP8DaWyflXsxc
rZ0hVaVez3WfP5cmBH+oApdKctu2Vs0Q/Pygopz7YPYZ2DuiNUZTwjmNA9rpx9I8
YVIyBWjaXF2VRzr1apfsI4D0G5jFm/ugJqeflnJmyV/ZNix1uJvelN2LvxeH/PN5
k6IZ14IoKe7PdwlUjy306rwWnej89ofbXmVkzNB87C1Z0rHE4UWaOUu2q5B8Rn8j
h+2I8dXwQSXPdbxv6RWFfdcyBci0Y9N7ucmS3zWI+ymQn0sR11Nhv0fOomymUO2+
Na02DbkCgYEAzoPxzdaXgda1bMIQrg+M4hZrUeQiy9FA4hJyNqwZsiO3YLA9fZrQ
w7ITNCcl5vEEsADz3WqWtx2ZdsFQkvv3z4DNbfeLb6NHHNcnNi4WgdxA1MG8726T
TazZHSxY4cZfLdzXU5/Y5AAfhCcBNpU/pGLYPpkhQOB2k3NH7C4jJX0CgYEAxfRC
Ys1VSRq8j7auV0k3aCOSLaPv9gF+m8sg1zVdV1Emy36/WRetmuXSPonS0Nie7MBl
sRwmWgOQZgiTryNKQfnlhMlz2b/ZiaoU1pGVdcKN/aWKBma/KWf9mIx1WyGZdpaH
s7zgEqSWjF0ZMB0UljW6m8NUtghjfClO9VcNzL8CgYBRq8CvBNS6Fm19a2opTCEN
MIyUwEI6lLCyN1VP5dPrrVBSPqCy0c0J95y8nVbR9DNEX7wRrpuYI26TlnQFDPy9
5VRYzvMn3Uy8TSJGvQdNqAtDmLLdhb9fkqHydZ1Y/JibjKDjg23FDX9pRfum2HNo
0WZvqyOJgruiKI8jCkQACQKBgDGeHwG67BSt4fO3240/aebte5d7Dwu/pieQy8OF
ucbILYw2UeoX+EjqMD/CthfpJDS9qP+yyZ4oZIpevf3ZP6S36aLWB/bdkr5h5mU+
CpOA16xrUOR33pSXX0ZcdpIIIvpJkuwnfJbPsHiwYT7hGybngsXGOTaDdcRKamMu
lePrAoGBAJVaQpEyDwgppuAcv9KTUtiIOLRke/pd0WO20wTkZqMiIfiKjDpASq5c
rEzq0M6qYpnmj87wwFpZLLJvMUa9w5KjUpJ+hqBNYywe5/d6laaISFdtYfjoNuLw
4BZI/XcA3ZiqzpPqYWBODrEcnCRZKH4C71c7yyATwQL2iWRHoJkY
-----END RSA PRIVATE KEY----- \
    --CertificateContent -----BEGIN CERTIFICATE-----
MIIDkTCCAnkCCQDOEdu7vXp33jANBgkqhkiG9w0BAQUFADCBhjELMAkGA1UEBhMC
Q04xEjAQBgNVBAgMCUd1YW5nRG9uZzELMAkGA1UEBwwCU1oxEDAOBgNVBAoMB3Rl
bmNlbnQxDTALBgNVBAsMBGNzaWcxFjAUBgNVBAMMDWNhLmNtMTAwMS5jb20xHTAb
BgkqhkiG9w0BCQEWDmNhQHRlbmNlbnQuY29tMB4XDTE5MDcyOTEyMjI1MFoXDTI5
MDcyNjEyMjI1MFowgY0xCzAJBgNVBAYTAkNOMRIwEAYDVQQIDAlHdWFuZ0Rvbmcx
CzAJBgNVBAcMAlNaMRAwDgYDVQQKDAd0ZW5jZW50MQ0wCwYDVQQLDARjc2lnMRow
GAYDVQQDDBF3d3cuY2hyaXN0ZXN0LmNvbTEgMB4GCSqGSIb3DQEJARYRY2hyaXNA
dGVuY2VudC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCfsJRj
ltE2239hVP0EEO1/KqYXT0pfMj4EKsi+sYOuPFF0ixMezTFkvkRtle3u5zmV5cnj
tGdUBC00wI66p5i0VY0zMbJ1VyEyQiYEcSwBMT66SqzupRKZuD8GOU4PiGY82Y3P
p6WOvAxfE3E/QPQF0My7L4k8vEOn8en9KveueAvpxu4C9+Gc3+X4e8gjv0oL0PrD
y4jJGgCrJtous/0/7rJdoEUrN1zuj8tqccQBRrFj89t0/7ccUY27kOJQeikUfOOX
kqvYYJYMv03lUwjfofhQXjTC+uOdrUFZzx6bnNXNqKwtuPmlkxFNfYqkx90OW6JP
+HM8ezUTHiHQcZRDAgMBAAEwDQYJKoZIhvcNAQEFBQADggEBAGKJdazyji4aSAAk
dcH9/he1RhfkdkBinNQspYWrl7n3+YfX2aCBwkHDTnUUA+HIpUtaWekRqRGHXaKg
MjSKOHW715VVR3CMekIRkhQkBMmicaC2YRTpJNOOkehAqeszytDXoICgDc34zkmy
VBPRYckYnXE8gwmew1Ogg8PxeC2WgNAQtm/GXmdfe8Wtoy88Ugz8NSV//lIkQJkM
zc7+GvWbIsfP7i7Cz8pIMNuJsfrVerbDpbpSSXr6lvTfeCbh9Sq43jpJTbhg2BoU
SpnKCvccuOEJnGOwb9WyZ/vrO2JG2RUdglpKh6l5c4+33yOgPqEcGnqMqsDDjAct
GjxzvQ4
```

Output: 
```
{
    "Response": {
        "RequestId": "bdef4308-69b2-4941-aeeb-9612f2c0cb2a",
        "CertificateId": "cert-li3tu2id"
    }
}
```

