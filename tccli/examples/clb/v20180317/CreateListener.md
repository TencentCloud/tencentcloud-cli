**Example 1: 创建两个TCP监听器，分别监听7569和7570端口，并分别命名为lis0和lis1**

创建两个TCP监听器，分别监听7569和7570端口，并分别命名为lis0和lis1。

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --ListenerNames lis1 lis0 \
    --Protocol TCP \
    --Ports 7570 7569 \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-d1ubsydq",
            "lbl-4udz130k"
        ],
        "RequestId": "8f272cef-14ff-458c-b67e-1bd21bd2942b"
    }
}
```

**Example 2: 创建TCP监听器的同时设置健康检查信息**

创建TCP监听器的同时设置健康检查信息

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --HealthCheck.UnHealthNum 4 \
    --HealthCheck.HealthNum 4 \
    --HealthCheck.IntervalTime 7 \
    --HealthCheck.TimeOut 5 \
    --HealthCheck.HealthSwitch 1 \
    --Protocol TCP \
    --Ports 7571 \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-lbbxvq26"
        ],
        "RequestId": "fff13c83-dcb5-481a-ba7c-30e92c276c19"
    }
}
```

**Example 3: 创建HTTPS监听器，并绑定已有证书**

创建HTTPS监听器，并绑定已有证书

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --Protocol HTTPS \
    --Ports 7572 \
    --Certificate.SSLMode UNIDIRECTIONAL \
    --Certificate.CertId MsJyaXVm \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-4fbxq45k"
        ],
        "RequestId": "db8ae69f-ebda-402b-8d02-ead459aa6ff9"
    }
}
```

**Example 4: 创建HTTPS监听器，并同时绑定新建的证书**

创建HTTPS监听器，并同时绑定新建的证书

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --Protocol HTTPS \
    --Ports 7573 \
    --Certificate.SSLMode UNIDIRECTIONAL \
    --Certificate.CertContent -----BEGINCERTIFICATE-----\nMIIEjTCCA3WgAwIBAgIQA4ZHUAVOv4yrszl3lLfo3TANBgkqhkiG9w0BAQsFADBy\nMQswCQYDVQQGEwJDTjElMCMGA1UEChMcVHJ1c3RBc2lhIFRlY2hub2xvZ2llcywg\nSW5jLjEdMBsGA1UECxMURG9tYWluIFZhbGlkYXRlZCBTU0wxHTAbBgNVBAMTFFRy\ndXN0QXNpYSBUTFMgUlNBIENBMB4XDTE4MDEwOTAwMDAwMFoXDTE5MDEwOTEyMDAw\nMFowFjEUMBIGA1UEAxMLZmx5Zmx5Lm5hbWUwggEiMA0GCSqGSIb3DQEBAQUAA4IB\nDwAwggEKAoIBAQClpnigB7r3ahv7BMuQw9KzB9Yfq3p+cRUbX9EMRyri2GrJbmrP\npESP8XQuIn4MZESvePR0r4gGHAHVri8nXzyQw6/m77BT/fIf4cQtEyz61gopDlYq\nbLTAKVfGFhGVikvQPoItOYbA9/l2YwtDENl8wBhcFrghWTRifnFSC0bNPj1ot5eu\nL8x5UOZLSa9kaQCm2/RQUBii5w3YBh+HmJgb7HPs8OoHKVScBo6eAyOcr+HNrA8W\nKsM6r4LpS+Rpfng7+fAKGE+vFsssXfRMBTo0TPp+h8ohuM8xqujbK+T7LMEXNWN9\n3FGYuuH+qmPvx/gAXFjLARKVyf0IsNnu6TLLAgMBAAGjggF5MIIBdTAfBgNVHSME\nGDAWgBR/05nzoEcOMQBWViKOt8ye3coBijAdBgNVHQ4EFgQUUCq9/Hmfgli5URvx\nAbSDNsDCCqcwJwYDVR0RBCAwHoILZmx5Zmx5Lm5hbWWCD3d3dy5mbHlmbHkubmFt\nZTAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMC\nMEwGA1UdIARFMEMwNwYJYIZIAYb9bAECMCowKAYIKwYBBQUHAgEWHGh0dHBzOi8v\nd3d3LmRpZ2ljZXJ0LmNvbS9DUFMwCAYGZ4EMAQIBMIGBBggrBgEFBQcBAQR1MHMw\nJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwMi5kaWdpY2VydC5jb20wSgYIKwYBBQUH\nMAKGPmh0dHA6Ly9jYWNlcnRzLmRpZ2l0YWxjZXJ0dmFsaWRhdGlvbi5jb20vVHJ1\nc3RBc2lhVExTUlNBQ0EuY3J0MAkGA1UdEwQCMAAwDQYJKoZIhvcNAQELBQADggEB\nADstNGgqYXG6eBDcBGVZk6DnJdS4GYdSzFZgCwt298cPMmZj107VM0QsB5K8V5Zd\nzJl5c7o4tEXiGP+lk0TVqgP/CkcMXcpxeKB94ldyX9ILii/L4hI9j7hVrLVM1eAn\nfS66Yg65xIYU8PdFtP3uhI9WdhE3nYRngyoHAAMjIvu0bqGPYbqpnHYp8fmjyetF\nC9CZcjkqHmwTSpjXuFjbDLx/BXd1Q81TNXwv8alkuXKfIJ5tW2lH372GmQb8I3oI\nPREP38tlBbmfEu4p7+UzwwuQuD8cEUVuG/x7cUN2uAGiZGoohydrORWm8kqdNY9c\nYOuRvokzVT4lsaln5LKkKxw=\n-----ENDCERTIFICATE----- \
    --Certificate.CertName my-cert \
    --Certificate.CertKey -----BEGINRSAPRIVATEKEY-----\nMIIEoAIBAAKCAQEApaZ4oAe692ob+wTLkMPSswfWH6t6fnEVG1/RDEcq4thqyW5q\nz6REj/F0LiJ+DGREr3j0dK+IBhwB1a4vJ188kMOv5u+wU/3yH+HELRMs+tYKKQ5W\nKmy0wClXxhYRlYpL0D6CLTmGwPf5dmMLQxDZfMAYXBa4IVk0Yn5xUgtGzT49aLeX\nri/MeVDmS0mvZGkAptv0UFAYoucN2AYfh5iYG+xz7PDqBylUnAaOngMjnK/hzawP\nFirDOq+C6UvkaX54O/nwChhPrxbLLF30TAU6NEz6fofKIbjPMaro2yvk+yzBFzVj\nfdxRmLrh/qpj78f4AFxYywESlcn9CLDZ7ukyywIDAQABAoH/KoiULD7g9kAEZrQp\n1SQusYVRl+E8xeVUdQhHcfCyAUkIAEpZzV2TtLd+DFqKrbTvITBT+vd9sYtdU6K7\nZ8cMcMoSpNMq+/+wK/b/m4I/6EqEt8HDb0NpSBBEeWUxQM4fumnsFBcXtew6iCtu\n2vzN7G2IwqUSxI5nbY2SektZ4q5ZRvwEND6gE51uqcqo4i6hA/TYsJLZ63L+Ux0A\nnm0AsmtMct+DT13NAlpyi6feDQCr1cxcSpqfhfgkWpawJVSxtxKvIn044iRBXb7Y\nRcW/8YYU1PrTIhhE9AnES7g8mnAgBHRryxuUotXkk7VotTHDbTO0q5KvO2bZ2T6z\nvQ4BAoGBANqoZE/wAB41wbJ7KwyblxyegI3Y9XYtkPLZlLK+GbCaC9UHNhPqSdaH\nWPoc3rtm8tOFQc7QMTFtxTLwQ3wEeSO4BFckVHgywuJoGRw1ZYxN8vAzHF1Gc/J1\nYcX0CDBuKgc0CxlhM7tDAzOgcfJR0EFRVhvLcUAA9hUoeN3EetSBAoGBAMHwnjWc\n+Y/vBW5yCefQciqppaylwB89H6kds+p0fDlVZQ080VB3b61t6VXOoYAzY4abOjxK\nAfNyVQcOEuO3gtZp3THK3fkV6bKaNHG41Ang32VW3XGb+MeEkJZwJk4JFbLrz8ln\nte4M9PjVpYuEQCJZvUjrhd+LJRubTTUXIHFLAoGAU0KJp/KwaNB5aDgERXG9kbU9\nKEYz+YMSTZbSS1mduKR/2uc7DUxKP3kcRWjW2y8xSZ/VViXqhXLSAzp/x+qAIjzA\n0lnQHFDf6oxO+3HNsCZCWnpr04yvO+S8jT8GG0LnmASWMVzU8Ppsbq0qlmXW0fhh\nvIW0IvX6vkXB+FgHmYECgYBrsJe5P4QYV2oVrP8xGL78T51uY89tyTwWZSbtTmdY\nUsG8+wNjgh6iF8EUY5usG1ztdq58ob+5lcf/FeKJTfI56yjnKDXfxToycYwjhbVA\nEv0ZQYXPOwOGjmbXEklC1aqV4nlL5enQ2KMCtWeqM/KE4H3JyvZYbeRaEv9pNoFO\nRwKBgBs+g0d81ufZSuTBlxfivDwrNV6LNzrgnwsTn+H/T7MfyoIEkT3nSGjanQHF\nwzPYyUpQx5OzNZp1ZEzKeW3GXVWjK+bfKlA7fmrZwDa8/JR6kTfCmc3WRrrQ92yq\nlFRW1kinLCP5y56SJEBz+DRSYV7ql9wOHyaM23sHkbCF0HAa\n-----ENDRSAPRIVATEKEY----- \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-bzfmg9m6"
        ],
        "RequestId": "6082314c-030c-429d-9eae-2dc6b159b5b9"
    }
}
```

**Example 5: 创建UDP监听器，健康检查方式使用Ping（默认方式）**

创建UDP监听器，健康检查方式使用Ping（默认方式）

Input: 

```
tccli clb CreateListener --cli-unfold-argument  \
    --HealthCheck.HealthSwitch 1 \
    --Protocol UDP \
    --ListenerNames lis_test \
    --Ports 432 \
    --LoadBalancerId lb-6wlxe9rj
```

Output: 
```
{
    "Response": {
        "ListenerIds": [
            "lbl-aev333n1"
        ],
        "RequestId": "3b81f03e-6088-448d-abaf-8a487d4f985a"
    }
}
```

