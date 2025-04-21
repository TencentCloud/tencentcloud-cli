**Example 1: 获取sso证书**

根据证书类型获取对应的证书

Input: 

```
tccli ioa DescribeCertManageStatus --cli-unfold-argument  \
    --CertTypes abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "SSOCerts": [
                {
                    "Id": 0,
                    "CertName": "abc",
                    "ServiceSn": "abc",
                    "ServiceEndTime": "abc",
                    "ClientSn": "abc",
                    "ClientEndTime": "abc",
                    "RootSn": "abc",
                    "RootEndTime": "abc",
                    "CertType": "abc",
                    "Status": 0,
                    "CreateTime": "abc"
                }
            ],
            "HTTPSCerts": [
                {
                    "Id": 0,
                    "CertName": "abc",
                    "ServiceSn": "abc",
                    "ServiceEndTime": "abc",
                    "ClientSn": "abc",
                    "ClientEndTime": "abc",
                    "RootSn": "abc",
                    "RootEndTime": "abc",
                    "CertType": "abc",
                    "Status": 0,
                    "CreateTime": "abc"
                }
            ],
            "MDMCerts": [
                {
                    "Id": 0,
                    "CertName": "abc",
                    "ServiceSn": "abc",
                    "ServiceEndTime": "abc",
                    "ClientSn": "abc",
                    "ClientEndTime": "abc",
                    "RootSn": "abc",
                    "RootEndTime": "abc",
                    "CertType": "abc",
                    "Status": 0,
                    "CreateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

