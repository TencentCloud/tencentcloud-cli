**Example 1: 查询私有CA证书列表**



Input: 

```
tccli iotcloud DescribePrivateCAs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CAs": [
            {
                "EffectiveTime": 1622448592,
                "ExpireTime": 1653984592,
                "CertText": "-----BEGIN CERTIFICATE-----\nXyf+Eg==\n-----END CERTIFICATE-----",
                "CertName": "certname",
                "CertSN": "5ff69e4c8afce5d6de8d395b34672944f5b4765a",
                "IssuerName": "CN=AAA,O=AAA,L=shenzhen,ST=guangdong,C=CN",
                "Subject": "CN=AAA,O=AAA,L=shenzhen,ST=guangdong,C=CN",
                "CreateTime": 1623070089
            }
        ],
        "RequestId": "xxxxxx"
    }
}
```

