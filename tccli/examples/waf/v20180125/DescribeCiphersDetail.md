**Example 1: Saas型WAF接入域名查询加密套件信息**



Input: 

```
tccli waf DescribeCiphersDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "767bb64b-0c26-4797-b77d-3242a63199b9",
        "Ciphers": [
            {
                "VersionId": 0,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            }
        ]
    }
}
```

