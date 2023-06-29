**Example 1: 查询敏感私钥文件列表**



Input: 

```
tccli bsca DescribeSensitivePrivateKeyList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SensitiveFileSet": [
            {
                "File": {
                    "Name": "/path/demo_text",
                    "Type": "TEXT"
                },
                "SubClass": "Private Key",
                "ContentList": [
                    "-----BEGIN EC PRIVATE KEY-----DEMOAgEBBEGO2n7NN363qSCvJVdlQtCvudtaW4o0fEufXRjE1AsCrle+VXX0Zh0wY1slSeDHMndpakoiF+XkQ+bhcB867UV6aKAHBgUrgQQAI6GBiQOBhgAEAQb6jDpobyy1tF8Zucg0TMGUzIN2DK+RZJ3QQRdWdirO25OIC3FoFi1Yird6rpoB6HlNyJ7R0bNG9Uv34bSHMn8yAFoiqxUCdJZQbEenMoZsi6COaePe3e0QqvDMr0hEWT23Sr3tLpEV7eZGFfFIJw5wSUp2KOcs+O9WjmoukTWtDEMO-----END EC PRIVATE KEY-----"
                ]
            },
            {
                "File": {
                    "Name": "/path/demo_binary",
                    "Type": "BINARY"
                },
                "SubClass": "Private Key",
                "ContentList": [
                    "-----BEGIN EC PRIVATE KEY-----DEMOAQEEGLjezFcbgDMeApVrdtZHvu/k1a8/tVZ41KAKBggqhkjOPQMBAaE0AzIABO1lciKdgxeRH8k64vxcaV1OYIK9akVrW02Dw21MXhRLP0l0wzCw6LGSr5rS6ADEMO==-----END EC PRIVATE KEY-----"
                ]
            }
        ],
        "FieldValuesSet": [],
        "TotalCount": 20,
        "RequestId": "34b0e422-c7be-404a-8861-a543af8393c8"
    }
}
```

