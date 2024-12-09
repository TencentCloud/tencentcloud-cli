**Example 1: 获取证书信息**

获取证书信息

Input: 

```
tccli ssl DescribeCertificate --cli-unfold-argument  \
    --CertificateId CertificateId
```

Output: 
```
{
    "Response": {
        "OwnerUin": "100017***920",
        "ProjectId": "0",
        "From": "trustasia",
        "CertificateType": "SVR",
        "PackageType": "83",
        "ProductZhName": "TrustAsia C1 DV Free",
        "Domain": "zrhh.online",
        "Alias": "",
        "Status": 1,
        "StatusMsg": "CA-REVIEWING",
        "VerifyType": "DNS_AUTO",
        "VulnerabilityStatus": "INACTIVE",
        "CertBeginTime": "2024-11-27 08:00:00",
        "CertEndTime": "2025-02-26 07:59:59",
        "ValidityPeriod": "3",
        "InsertTime": "2024-11-27 17:44:36",
        "OrderId": "Hy***85G_mZOLxSuw",
        "DvAuthDetail": {
            "DvAuths": null,
            "DvAuthKey": null,
            "DvAuthValue": null,
            "DvAuthDomain": null,
            "DvAuthPath": null,
            "DvAuthKeySubDomain": ""
        },
        "VulnerabilityReport": null,
        "CertificateId": "Juz8JAxn",
        "StatusName": "已颁发",
        "SubjectAltName": [
            "www.zrhh.online"
        ],
        "IsVip": false,
        "IsWildcard": false,
        "IsDv": true,
        "IsVulnerability": false,
        "RenewAble": false,
        "SubmittedData": null,
        "Deployable": true,
        "Tags": [],
        "CAEncryptAlgorithms": [],
        "CACommonNames": [],
        "CAEndTimes": [],
        "DvRevokeAuthDetail": [],
        "CertificateExtra": {
            "SMCert": 0,
            "ReplacedBy": null,
            "OriginCertificateId": null,
            "ReplacedFor": null,
            "RenewOrder": null,
            "DomainNumber": "1",
            "CompanyType": 1
        },
        "PackageTypeName": "TrustAsia C1 DV Free",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

