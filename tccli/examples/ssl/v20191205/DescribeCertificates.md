**Example 1: 获取证书列表**

获取证书列表

Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Certificates": [
            {
                "From": "trustasia",
                "SubjectAltName": null,
                "BoundResource": [],
                "CertificateExtra": {
                    "OriginCertificateId": null,
                    "ReplacedBy": null,
                    "ReplacedFor": "a8xHcaIs",
                    "DomainNumber": null,
                    "RenewOrder": null
                },
                "StatusName": "已通过",
                "RenewAble": false,
                "Status": 1,
                "IsDv": true,
                "CertBeginTime": "2020-01-14 16:00:00",
                "IsVulnerability": false,
                "VerifyType": "DNS",
                "StatusMsg": null,
                "ProjectId": "0",
                "OwnerUin": "20548499",
                "ProjectInfo": {
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectResume": "默认项目",
                    "ProjectName": "默认项目"
                },
                "ProductZhName": "TrustAsia TLS RSA CA",
                "CertEndTime": "2020-02-12 16:00:00",
                "PackageType": "2",
                "InsertTime": "2020-01-14 10:54:47",
                "CertificateType": "SVR",
                "IsVip": false,
                "ValidityPeriod": "0",
                "Domain": "wgc.red",
                "CertificateId": "a90XEOtj",
                "Alias": "a8xHcaIs的重颁发订单",
                "IsWildcard": false,
                "PackageTypeName": "TrustAsia TLS RSA CA",
                "VulnerabilityStatus": "INACTIVE",
                "Deployable": true,
                "IsIgnore": true,
                "IsSM": true,
                "Tags": [
                    {
                        "TagKey": "testtag",
                        "TagValue": "testtag"
                    },
                    {
                        "TagKey": "x",
                        "TagValue": "testtag"
                    }
                ]
            }
        ],
        "TotalCount": 12,
        "RequestId": "43b82119-c648-4230-8d38-5be63f039549"
    }
}
```

**Example 2: 证书列表**



Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --FilterSource buy \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 86,
        "Certificates": [
            {
                "OwnerUin": "700000141969",
                "ProjectId": "0",
                "From": "trustasia",
                "PackageType": "12",
                "CertificateType": "SVR",
                "ProductZhName": "TrustAsia 域名型(DV)通配符",
                "Domain": "*.ninghhuang.top",
                "Alias": "",
                "Status": 1,
                "CertificateExtra": null,
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": "",
                "VerifyType": "DNS",
                "CertBeginTime": "2022-01-12 16:00:00",
                "CertEndTime": "2022-05-12 16:00:00",
                "ValidityPeriod": "12",
                "InsertTime": "2022-01-12 15:39:35",
                "PackageTypeName": "TrustAsia 域名型(DV)通配符",
                "CertificateId": "su5NDtqX",
                "SubjectAltName": null,
                "StatusName": "已通过",
                "IsVip": true,
                "IsDv": true,
                "IsWildcard": true,
                "IsVulnerability": false,
                "RenewAble": false,
                "Deployable": true,
                "IsIgnore": false,
                "IsSM": true,
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目"
                },
                "BoundResource": null,
                "Tags": []
            }
        ],
        "RequestId": "e398dd3e-68c3-4a7e-be51-bc3db5631a5d"
    }
}
```

