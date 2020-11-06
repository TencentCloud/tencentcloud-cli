**Example 1: 获取证书列表**



Input: 

```
tccli wss DescribeCertList --cli-unfold-argument  \
    --Page 1 \
    --Count 1 \
    --SearchKey as \
    --ProjectId 1000 \
    --CertType CA \
    --Id sad \
    --WithCert 1 \
    --AltDomain asd \
    --ModuleType ssl
```

Output: 
```
{
    "Response": {
        "TotalNum": 12,
        "List": [
            {
                "OwnerUin": "664372747",
                "ProjectId": "0",
                "From": "trustasia",
                "Type": "2",
                "CertType": "SVR",
                "ProductZhName": "TrustAsia TLS RSA CA",
                "Domain": "cl.f-xj.cn",
                "Alias": "",
                "Status": 1,
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": null,
                "VerifyType": "DNS_AUTO",
                "CertBeginTime": "2017-12-20 08:00:00",
                "CertEndTime": "2018-12-20 20:00:00",
                "ValidityPeriod": "12",
                "InsertTime": "2017-12-20 21:25:00",
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "name": "默认项目",
                    "CreatorUin": 0,
                    "CreateTime": "0000-00-00 00:00:00",
                    "Info": "默认项目"
                },
                "Id": "GjTNRoK7",
                "SubjectAltName": [
                    "cl.f-xj.cn"
                ],
                "TypeName": "TrustAsia TLS RSA CA",
                "StatusName": "已通过",
                "IsVip": false,
                "IsDv": true,
                "IsWildcard": false,
                "IsVulnerability": false
            }
        ]
    }
}
```

