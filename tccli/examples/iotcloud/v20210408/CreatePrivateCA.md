**Example 1: 创建私有CA证书**



Input: 

```
tccli iotcloud CreatePrivateCA --cli-unfold-argument  \
    --CertName cert_dev \
    --CertText '-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----' \
    --VerifyCertText '-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----'
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

