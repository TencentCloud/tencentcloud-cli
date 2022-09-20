**Example 1: 获取默认证书**



Input: 

```
tccli teo DescribeDefaultCertificates --cli-unfold-argument  \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-fafcasdf
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "084d5612-67a7-4aca-aac9-827aa3662b2d",
        "DefaultServerCertInfo": [
            {
                "Status": "deployed",
                "CertId": "teo-285inl1otbtd",
                "SubjectAltName": [
                    "*.test.com",
                    "test.com"
                ],
                "EffectiveTime": "2020-09-22T00:00:00+00:00",
                "CommonName": "test.com",
                "ExpireTime": "2020-09-22T00:00:00+00:00",
                "Alias": "EdgeOne default",
                "Message": "",
                "Type": "default"
            }
        ]
    }
}
```

