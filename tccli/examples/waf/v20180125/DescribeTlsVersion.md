**Example 1: TLS版本**



Input: 

```
tccli waf DescribeTlsVersion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d05712e6-2229-4c15-a56d-86480e5c62b3",
        "TLS": [
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
            },
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
            }
        ]
    }
}
```

**Example 2: 查询用户TLS版本**



Input: 

```
tccli waf DescribeTlsVersion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "TLS": [
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
            },
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
            }
        ]
    }
}
```

