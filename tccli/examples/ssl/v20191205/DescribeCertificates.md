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
        "TotalCount": 1,
        "Certificates": [
            {
                "OwnerUin": "123123",
                "ProjectId": "0",
                "From": "trustasia",
                "PackageType": "2",
                "CertificateType": "SVR",
                "ProductZhName": "TrustAsia TLS RSA CA",
                "Domain": "a.qq.com",
                "Alias": "qq",
                "Status": 3,
                "CertificateExtra": {
                    "SMCert": 0,
                    "DomainNumber": "1",
                    "ReplacedBy": null,
                    "OriginCertificateId": null,
                    "ReplacedFor": null,
                    "RenewOrder": null
                },
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": null,
                "VerifyType": "FILE",
                "CertBeginTime": "2021-06-16 08:00:00",
                "CertEndTime": "2022-06-16 07:59:59",
                "ValidityPeriod": "12",
                "InsertTime": "2021-06-16 16:38:41",
                "AutoRenewFlag": 0,
                "PreAuditInfo": {
                    "TotalPeriod": 1,
                    "NowPeriod": 1,
                    "ManagerId": ""
                },
                "EncryptAlgorithm": "RSA 2048",
                "IsSM": false,
                "PackageTypeName": "TrustAsia TLS RSA CA",
                "CertificateId": "nVCOdbjM",
                "SubjectAltName": [
                    "a.qq.com"
                ],
                "StatusName": "已过期",
                "IsVip": false,
                "IsDv": true,
                "IsWildcard": false,
                "IsVulnerability": false,
                "RenewAble": false,
                "CAEncryptAlgorithms": [],
                "CAEndTimes": [],
                "CACommonNames": [],
                "Deployable": true,
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目"
                },
                "IsIgnore": false,
                "BoundResource": null,
                "Tags": []
            }
        ],
        "RequestId": "2846dbc6-edc0-4d29-820e-16bb8b8f4421"
    }
}
```

