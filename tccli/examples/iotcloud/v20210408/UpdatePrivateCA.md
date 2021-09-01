**Example 1: 更新私有CA证书**



Input: 

```
tccli iotcloud UpdatePrivateCA --cli-unfold-argument  \
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

