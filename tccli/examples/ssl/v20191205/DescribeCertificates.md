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
                }
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

