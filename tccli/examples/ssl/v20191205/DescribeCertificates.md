**Example 1: 获取证书列表**

获取证书列表

Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Certificates": [
            {
                "OwnerUin": "10*******",
                "ProjectId": "zr*****",
                "From": "upload",
                "PackageType": "company",
                "CertificateType": "svr",
                "ProductZhName": "DigiCert Secure Site CN CA G3",
                "Domain": "www.zrh.com",
                "Alias": "upload cert",
                "Status": 1,
                "CertificateExtra": {
                    "DomainNumber": "10983",
                    "OriginCertificateId": "hj****",
                    "ReplacedBy": "hkk****",
                    "ReplacedFor": "ete****",
                    "RenewOrder": "feg****",
                    "SMCert": 0,
                    "CompanyType": 0
                },
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": "PRE-REVIEWING",
                "VerifyType": "DNS",
                "CertBeginTime": "2024-11-06 08:00:0",
                "CertEndTime": "2025-12-02 07:59:59",
                "ValidityPeriod": "13",
                "InsertTime": "2024-11-11 11:53:07",
                "CertificateId": "hdhd**",
                "SubjectAltName": [
                    "zrh"
                ],
                "PackageTypeName": "company",
                "StatusName": "证书已颁发",
                "IsVip": true,
                "IsDv": true,
                "IsWildcard": true,
                "IsVulnerability": true,
                "RenewAble": true,
                "ProjectInfo": {
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 1,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目",
                    "OwnerUin": 1,
                    "ProjectId": "0"
                },
                "BoundResource": [
                    ""
                ],
                "Deployable": true,
                "Tags": [
                    {
                        "TagKey": "zrh",
                        "TagValue": "ok"
                    }
                ],
                "IsIgnore": true,
                "IsSM": true,
                "EncryptAlgorithm": "svr",
                "CAEncryptAlgorithms": [
                    "svr"
                ],
                "CAEndTimes": [],
                "CACommonNames": [],
                "PreAuditInfo": {
                    "TotalPeriod": 0,
                    "NowPeriod": 0,
                    "ManagerId": "84994"
                },
                "AutoRenewFlag": 0,
                "HostingStatus": 0,
                "HostingCompleteTime": "2024-11-06 08:00:00",
                "HostingRenewCertId": "2024-11-06 08:00:00",
                "HasRenewOrder": "yes",
                "ReplaceOriCertIsDelete": true,
                "IsExpiring": true,
                "DVAuthDeadline": "2024-11-06 08:00:00",
                "ValidationPassedTime": "2024-11-06 08:00:00",
                "CertSANs": [
                    "normal"
                ],
                "AwaitingValidationMsg": "wait",
                "AllowDownload": true,
                "IsDNSPODResolve": true,
                "IsPackage": true,
                "KeyPasswordCustomFlag": true,
                "SupportDownloadType": {
                    "NGINX": true,
                    "APACHE": true,
                    "TOMCAT": true,
                    "IIS": true,
                    "JKS": true,
                    "OTHER": true,
                    "ROOT": true
                },
                "IsHostingUploadRenewCert": false
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 2: 获取证书列表 - SearchKey查询域名**



Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --SearchKey ninghhuang
```

Output: 
```
{
    "Response": {
        "TotalCount": 54,
        "Certificates": [
            {
                "OwnerUin": "815836472",
                "ProjectId": "0",
                "From": "trustasia",
                "ProductZhName": "TrustAsia C1 DV Free",
                "Domain": "ninghhuang.online",
                "Alias": "",
                "Status": 1,
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": "ca-reviewing",
                "VerifyType": "DNS_AUTO",
                "CertBeginTime": "2025-02-12 08:00:00",
                "CertEndTime": "2025-05-14 07:59:59",
                "ValidityPeriod": "3",
                "InsertTime": "2025-02-12 10:11:21",
                "AutoRenewFlag": 1,
                "EncryptAlgorithm": "RSA 2048",
                "IsIgnore": false,
                "PreAuditInfo": {
                    "TotalPeriod": 1,
                    "NowPeriod": 1,
                    "ManagerId": ""
                },
                "IsSM": false,
                "SubjectAltName": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "StatusName": "证书已颁发",
                "IsVip": false,
                "IsDv": true,
                "IsWildcard": false,
                "IsVulnerability": false,
                "HasRenewOrder": "",
                "ReplaceOriCertIsDelete": false,
                "RenewAble": false,
                "IsExpiring": false,
                "DVAuthDeadline": "2025-02-19 10:11:21",
                "ValidationPassedTime": "--",
                "CertSANs": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "CertRevokedTime": "",
                "CAEncryptAlgorithms": [],
                "CAEndTimes": [],
                "CACommonNames": [],
                "Deployable": true,
                "AwaitingValidationMsg": "",
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目"
                },
                "Tags": [],
                "CertificateId": "LtIaSxlb",
                "CertificateType": "SVR",
                "PackageType": "83",
                "PackageTypeName": "TrustAsia C1 DV Free",
                "KeyPasswordCustomFlag": false,
                "SupportDownloadType": {
                    "NGINX": true,
                    "APACHE": true,
                    "TOMCAT": true,
                    "IIS": true,
                    "JKS": true,
                    "OTHER": true,
                    "ROOT": true
                },
                "CertificateExtra": {
                    "DomainNumber": "1",
                    "OriginCertificateId": null,
                    "ReplacedBy": null,
                    "ReplacedFor": null,
                    "RenewOrder": null,
                    "SMCert": 0,
                    "CompanyType": 1
                },
                "AllowDownload": false,
                "IsPackage": false,
                "HostingStatus": -1,
                "HostingCompleteTime": "",
                "HostingRenewCertId": "",
                "HostingResourceTypes": [],
                "IsDNSPODResolve": false,
                "IsHostingUploadRenewCert": false,
                "BoundResource": []
            }
        ],
        "RequestId": "e7f6021f-47bb-476b-a424-6a0cde19a1eb"
    }
}
```

**Example 3: 获取证书列表 - SearchKey查询证书ID**



Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --SearchKey LtIaS
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Certificates": [
            {
                "OwnerUin": "815836472",
                "ProjectId": "0",
                "From": "trustasia",
                "ProductZhName": "TrustAsia C1 DV Free",
                "Domain": "ninghhuang.online",
                "Alias": "",
                "Status": 1,
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": "",
                "VerifyType": "DNS_AUTO",
                "CertBeginTime": "2025-02-12 08:00:00",
                "CertEndTime": "2025-05-14 07:59:59",
                "ValidityPeriod": "3",
                "InsertTime": "2025-02-12 10:11:21",
                "AutoRenewFlag": 1,
                "EncryptAlgorithm": "RSA 2048",
                "IsIgnore": false,
                "PreAuditInfo": {
                    "TotalPeriod": 1,
                    "NowPeriod": 1,
                    "ManagerId": ""
                },
                "IsSM": false,
                "SubjectAltName": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "StatusName": "证书已颁发",
                "IsVip": false,
                "IsDv": true,
                "IsWildcard": false,
                "IsVulnerability": false,
                "HasRenewOrder": "",
                "ReplaceOriCertIsDelete": false,
                "RenewAble": false,
                "IsExpiring": false,
                "DVAuthDeadline": "2025-02-19 10:11:21",
                "ValidationPassedTime": "--",
                "CertSANs": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "CertRevokedTime": "",
                "CAEncryptAlgorithms": [],
                "CAEndTimes": [],
                "CACommonNames": [],
                "Deployable": true,
                "AwaitingValidationMsg": "",
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目"
                },
                "Tags": [],
                "CertificateId": "LtIaSxlb",
                "CertificateType": "SVR",
                "PackageType": "83",
                "PackageTypeName": "TrustAsia C1 DV Free",
                "KeyPasswordCustomFlag": false,
                "SupportDownloadType": {
                    "NGINX": true,
                    "APACHE": true,
                    "TOMCAT": true,
                    "IIS": true,
                    "JKS": true,
                    "OTHER": true,
                    "ROOT": true
                },
                "CertificateExtra": {
                    "DomainNumber": "1",
                    "OriginCertificateId": null,
                    "ReplacedBy": null,
                    "ReplacedFor": null,
                    "RenewOrder": null,
                    "SMCert": 0,
                    "CompanyType": 1
                },
                "AllowDownload": false,
                "IsPackage": false,
                "HostingStatus": -1,
                "HostingCompleteTime": "",
                "HostingRenewCertId": "",
                "HostingResourceTypes": [],
                "IsDNSPODResolve": false,
                "IsHostingUploadRenewCert": false,
                "BoundResource": []
            }
        ],
        "RequestId": "e7f6021f-47bb-476b-a424-6a0cde19a1eb"
    }
}
```

**Example 4: 获取证书列表 - SearchKey查询备注名称**



Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --SearchKey K926htp2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Certificates": [
            {
                "OwnerUin": "815836472",
                "ProjectId": "0",
                "From": "trustasia",
                "ProductZhName": "TrustAsia C1 DV Free",
                "Domain": "ninghhuang.online",
                "Alias": "K926htp2的自动续费证书",
                "Status": 1,
                "VulnerabilityStatus": "INACTIVE",
                "StatusMsg": "",
                "VerifyType": "DNS_AUTO",
                "CertBeginTime": "2025-02-05 08:00:00",
                "CertEndTime": "2025-05-07 07:59:59",
                "ValidityPeriod": "3",
                "InsertTime": "2025-02-05 08:26:42",
                "AutoRenewFlag": 1,
                "EncryptAlgorithm": "RSA 2048",
                "IsIgnore": false,
                "PreAuditInfo": {
                    "TotalPeriod": 1,
                    "NowPeriod": 1,
                    "ManagerId": ""
                },
                "IsSM": false,
                "SubjectAltName": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "StatusName": "证书已颁发",
                "IsVip": false,
                "IsDv": true,
                "IsWildcard": false,
                "IsVulnerability": false,
                "HasRenewOrder": "",
                "ReplaceOriCertIsDelete": false,
                "RenewAble": false,
                "IsExpiring": false,
                "DVAuthDeadline": "2025-02-12 08:26:42",
                "ValidationPassedTime": "--",
                "CertSANs": [
                    "ninghhuang.online",
                    "www.ninghhuang.online"
                ],
                "CertRevokedTime": "",
                "CAEncryptAlgorithms": [],
                "CAEndTimes": [],
                "CACommonNames": [],
                "Deployable": true,
                "AwaitingValidationMsg": "",
                "ProjectInfo": {
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectName": "默认项目",
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectResume": "默认项目"
                },
                "Tags": [],
                "CertificateId": "Li1AKHnS",
                "CertificateType": "SVR",
                "PackageType": "83",
                "PackageTypeName": "TrustAsia C1 DV Free",
                "KeyPasswordCustomFlag": false,
                "SupportDownloadType": {
                    "NGINX": true,
                    "APACHE": true,
                    "TOMCAT": true,
                    "IIS": true,
                    "JKS": true,
                    "OTHER": true,
                    "ROOT": true
                },
                "CertificateExtra": {
                    "DomainNumber": "1",
                    "OriginCertificateId": "K926htp2",
                    "ReplacedBy": null,
                    "ReplacedFor": null,
                    "RenewOrder": null,
                    "SMCert": 0,
                    "CompanyType": 1
                },
                "AllowDownload": false,
                "IsPackage": false,
                "HostingStatus": 0,
                "HostingCompleteTime": "2025-02-05 08:39:30",
                "HostingRenewCertId": "",
                "HostingResourceTypes": [
                    "cdn",
                    "clb",
                    "cos"
                ],
                "HostingConfig": {
                    "MessageTypes": [
                        0
                    ],
                    "ReplaceEndTime": "23:59:59",
                    "ReplaceStartTime": "00:00:00",
                    "ReplaceTime": 999
                },
                "IsDNSPODResolve": false,
                "IsHostingUploadRenewCert": false,
                "BoundResource": []
            }
        ],
        "RequestId": "e7f6021f-47bb-476b-a424-6a0cde19a1eb"
    }
}
```

