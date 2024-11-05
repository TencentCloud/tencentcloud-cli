**Example 1: Saas型WAF接入域名查询加密套件信息**



Input: 

```
tccli waf DescribeCiphersDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9b4a918c-b442-4dfe-a783-9b082f5a70bb",
        "Ciphers": [
            {
                "VersionId": 0,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 0,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 0,
                "CipherId": 20,
                "CipherName": "TLS_AES_256_GCM_SHA384（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 0,
                "CipherId": 21,
                "CipherName": "TLS_CHACHA20_POLY1305_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 0,
                "CipherId": 22,
                "CipherName": "TLS_AES_128_GCM_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 1,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 1,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 1,
                "CipherId": 20,
                "CipherName": "TLS_AES_256_GCM_SHA384（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 1,
                "CipherId": 21,
                "CipherName": "TLS_CHACHA20_POLY1305_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 1,
                "CipherId": 22,
                "CipherName": "TLS_AES_128_GCM_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 2,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 2,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 2,
                "CipherId": 20,
                "CipherName": "TLS_AES_256_GCM_SHA384（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 2,
                "CipherId": 21,
                "CipherName": "TLS_CHACHA20_POLY1305_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 2,
                "CipherId": 22,
                "CipherName": "TLS_AES_128_GCM_SHA256（支持版本：TLS 1.3）"
            },
            {
                "VersionId": 3,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 3,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 3,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 4,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 4,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 0,
                "CipherName": "DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 1,
                "CipherName": "ECDHE-RSA-DES-CBC3-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 2,
                "CipherName": "AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 3,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES256-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 4,
                "CipherName": "AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 5,
                "CipherName": "ECDHE-RSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2），ECDHE-ECDSA-AES128-SHA（支持版本：TLS 1.0,TLS 1.1,TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 6,
                "CipherName": "AES256-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 7,
                "CipherName": "AES256-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 8,
                "CipherName": "AES256-CCM（支持版本：TLS 1.2） "
            },
            {
                "VersionId": 5,
                "CipherId": 9,
                "CipherName": "AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 10,
                "CipherName": "ECDHE-RSA-AES256-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 11,
                "CipherName": "ECDHE-RSA-AES256-SHA（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 12,
                "CipherName": "ECDHE-RSA-AES256-GCM-SHA384（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 13,
                "CipherName": "AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 14,
                "CipherName": "AES128-CCM（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 15,
                "CipherName": "AES128-CCM8（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 16,
                "CipherName": "AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 17,
                "CipherName": "ECDHE-RSA-AES128-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 18,
                "CipherName": "ECDHE-RSA-AES128-GCM-SHA256（支持版本：TLS 1.2）"
            },
            {
                "VersionId": 5,
                "CipherId": 19,
                "CipherName": "ECDHE-RSA-CHACHA20-POLY1305（支持版本：TLS 1.2）"
            }
        ]
    }
}
```

