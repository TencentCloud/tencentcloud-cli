**Example 1: 用户证书下载**



Input: 

```
tccli tbaas DownloadUserCert --cli-unfold-argument  \
    --Module cert_mng \
    --Operation cert_download_for_user \
    --CertId 171781 \
    --CertDn C \
    --ClusterId 251005746bckuobc41mpu \
    --GroupName youtuOrg
```

Output: 
```
{
    "Response": {
        "CertCtx": "-----BEGIN CERTIFICATE-----\nMIIC4DCCAoagAwIBAgIBBzAKBggqhkjOPQQDAjBpMQswCQYDVQQGEwJDTjERMA8G\nA1UECAwIU2hlblpoZW4xETAPBgNVBAcMCFNoZW5aaGVuMREwDwYDVQQKDAh5b3V0\ndU9yZzEhMB8GA1UEAwwYY2EueW91dHVvcmcuYmNrdW9iYzQxbXB1MB4XDTE5MTAx\nNjA2NDY0NVoXDTIyMDkzMDA2NDY0NVowgYUxCzAJBgNVBAYTAkNOMREwDwYDVQQI\nEwhTaGVuWmhlbjESMBAGA1UEBxMJNFNoZW5aaGVuMREwDwYDVQQKEwh5b3V0dU9y\nZzEPMA0GA1UECxMGY2xpZW50MSswKQYDVQQDFCJreWxvekB5b3V0dW9yZy5iY2t1\nb2JjNDFtcHVAY2xpZW50MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEwitZ4tmO\nK9tMvDLP4kx+ZmM8QnzHgfxr8KeoEjBwJomODlwyo6L5XIUeQIz1K/gwU6o8Arus\nTrab1cWzgHyF8qOCAQAwgf0wCQYDVR0TBAIwADARBglghkgBhvhCAQEEBAMCBkAw\nHQYDVR0OBBYEFNeW9zH7j/rxDklNBz4OB5aWVY66MIGbBgNVHSMEgZMwgZCAFDdP\n92WahmfoPabh45gYaozILIVooW2kazBpMQswCQYDVQQGEwJDTjERMA8GA1UECAwI\nU2hlblpoZW4xETAPBgNVBAcMCFNoZW5aaGVuMREwDwYDVQQKDAh5b3V0dU9yZzEh\nMB8GA1UEAwwYY2EueW91dHVvcmcuYmNrdW9iYzQxbXB1ggkA+Nat6MctlAowCwYD\nVR0PBAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAoGCCqGSM49BAMCA0gAMEUC\nIQDquRCXMx6T1QUi9YviE6cpGfQyIQIJ+SAp/6u5EhgzjgIgaf9eX823ZRWLG+S7\nCdWSk/oVVeSoelyUDYqTvYYqXtI=\n-----END CERTIFICATE-----\n",
        "CertName": "kyloz@youtuorg.bckuobc41mpu@client.pem",
        "RequestId": "5f6192d9-fbcd-4d1d-9b52-61006f33543b"
    }
}
```

