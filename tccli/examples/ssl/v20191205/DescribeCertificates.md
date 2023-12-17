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
                "OwnerUin": "abc",
                "ProjectId": "abc",
                "From": "abc",
                "PackageType": "abc",
                "CertificateType": "abc",
                "ProductZhName": "abc",
                "Domain": "abc",
                "Alias": "abc",
                "Status": 1,
                "CertificateExtra": {
                    "DomainNumber": "abc",
                    "OriginCertificateId": "abc",
                    "ReplacedBy": "abc",
                    "ReplacedFor": "abc",
                    "RenewOrder": "abc",
                    "SMCert": 0,
                    "CompanyType": 0
                },
                "VulnerabilityStatus": "abc",
                "StatusMsg": "abc",
                "VerifyType": "abc",
                "CertBeginTime": "abc",
                "CertEndTime": "abc",
                "ValidityPeriod": "abc",
                "InsertTime": "abc",
                "CertificateId": "abc",
                "SubjectAltName": [
                    "abc"
                ],
                "PackageTypeName": "abc",
                "StatusName": "abc",
                "IsVip": true,
                "IsDv": true,
                "IsWildcard": true,
                "IsVulnerability": true,
                "RenewAble": true,
                "ProjectInfo": {
                    "ProjectName": "abc",
                    "ProjectCreatorUin": 1,
                    "ProjectCreateTime": "abc",
                    "ProjectResume": "abc",
                    "OwnerUin": 1,
                    "ProjectId": "abc"
                },
                "BoundResource": [
                    "abc"
                ],
                "Deployable": true,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "IsIgnore": true,
                "IsSM": true,
                "EncryptAlgorithm": "abc",
                "CAEncryptAlgorithms": [
                    "abc"
                ],
                "CAEndTimes": [
                    "abc"
                ],
                "CACommonNames": [
                    "abc"
                ],
                "PreAuditInfo": {
                    "TotalPeriod": 0,
                    "NowPeriod": 0,
                    "ManagerId": "abc"
                },
                "AutoRenewFlag": 0,
                "HostingStatus": 0,
                "HostingCompleteTime": "abc",
                "HostingRenewCertId": "abc",
                "HasRenewOrder": "abc",
                "ReplaceOriCertIsDelete": true,
                "IsExpiring": true,
                "DVAuthDeadline": "abc",
                "ValidationPassedTime": "abc",
                "CertSANs": [
                    "abc"
                ],
                "AwaitingValidationMsg": "abc",
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
        "RequestId": "abc"
    }
}
```

