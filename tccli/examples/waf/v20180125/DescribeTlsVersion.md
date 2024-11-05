**Example 1: 查询支持的TLS版本**



Input: 

```
tccli waf DescribeTlsVersion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4740ae4a-ea83-4f22-bb51-465c1623eaa1",
        "TLS": [
            {
                "VersionId": 3,
                "VersionName": "TLSv1.0;TLSv1.1;TLSv1.2"
            },
            {
                "VersionId": 4,
                "VersionName": "TLSv1.1;TLSv1.2"
            },
            {
                "VersionId": 5,
                "VersionName": "TLSv1.2"
            },
            {
                "VersionId": 0,
                "VersionName": "TLSv1.0;TLSv1.1;TLSv1.2;TLSv1.3"
            },
            {
                "VersionId": 1,
                "VersionName": "TLSv1.1;TLSv1.2;TLSv1.3"
            },
            {
                "VersionId": 2,
                "VersionName": "TLSv1.2;TLSv1.3"
            }
        ]
    }
}
```

