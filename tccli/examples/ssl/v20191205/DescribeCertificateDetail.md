**Example 1: 获取证书详情**

获取审核中的证书详情

Input: 

```
tccli ssl DescribeCertificateDetail --cli-unfold-argument  \
    --CertificateId aClRkC90
```

Output: 
```
{
    "Response": {
        "From": "trustasia",
        "SubjectAltName": [],
        "VulnerabilityReport": null,
        "CertificatePrivateKey": "-----BEGIN RSA PRIVATE KEY-----......-----END RSA PRIVATE KEY-----",
        "CertificatePublicKey": null,
        "CertificateExtra": {
            "OriginCertificateId": null,
            "ReplacedBy": null,
            "ReplacedFor": null,
            "DomainNumber": "3",
            "RenewOrder": null
        },
        "RenewAble": false,
        "Status": 5,
        "IsDv": false,
        "IsVulnerability": false,
        "CertBeginTime": null,
        "TypeName": "SecureSite 企业型(OV)",
        "DvAuthDetail": null,
        "VerifyType": null,
        "StatusMsg": null,
        "StatusName": "企业证书，待提交",
        "ProjectId": "0",
        "OwnerUin": "779000108",
        "ProductZhName": "SecureSite 企业型(OV)",
        "CertEndTime": null,
        "PackageType": "6",
        "RequestId": "330979e0-fd50-4b33-86b0-c2e264d8ff52",
        "InsertTime": "2020-01-16 19:26:20",
        "CertificateType": "SVR",
        "IsVip": true,
        "ValidityPeriod": "12",
        "OrderId": null,
        "Domain": "",
        "CertificateId": "aClRkC90",
        "Alias": "",
        "SubmittedData": {
            "OrganizationCity": "深圳市",
            "CsrContent": "",
            "OrganizationName": "Tencent",
            "CertificateDomain": "test-dawd2143e21.com",
            "AdminPhoneNum": "12345678901",
            "AdminPosition": "developer",
            "OrganizationDivision": "Qcloud",
            "DomainList": [
                "test-11111111111111.com",
                "test-222222222222.com"
            ],
            "AdminFirstName": "test",
            "ContactLastName": "test",
            "ContactEmail": "test@tencent.com",
            "ContactNumber": "12345678901",
            "CsrType": "online",
            "PhoneAreaCode": "0755",
            "VerifyType": "",
            "AdminLastName": "test",
            "ContactFirstName": "test",
            "OrganizationCountry": "CN",
            "ContactPosition": "developer",
            "OrganizationRegion": "广东省",
            "PhoneNumber": "86013388",
            "PostalCode": "",
            "AdminEmail": "test@tencent.com",
            "KeyPassword": "",
            "OrganizationAddress": "南山区腾讯大厦1000号"
        },
        "IsWildcard": false,
        "Deployable": false,
        "VulnerabilityStatus": "INACTIVE"
    }
}
```

**Example 2: 获取证书详情-2**

获取已经审核通过的证书详情

Input: 

```
tccli ssl DescribeCertificateDetail --cli-unfold-argument  \
    --CertificateId aCMEQWHt
```

Output: 
```
{
    "Response": {
        "From": "trustasia",
        "SubjectAltName": [
            "test-ev-dawe23r243qfa.com"
        ],
        "VulnerabilityReport": null,
        "CertificatePrivateKey": "-----BEGIN RSA PRIVATE KEY-----......-----END RSA PRIVATE KEY-----",
        "CertificateExtra": {
            "OriginCertificateId": null,
            "ReplacedBy": null,
            "ReplacedFor": null,
            "DomainNumber": "2",
            "RenewOrder": null
        },
        "RenewAble": true,
        "Status": 1,
        "IsDv": false,
        "IsVulnerability": true,
        "CertBeginTime": "2020-01-16 16:00:00",
        "TypeName": "SecureSite 增强型(EV)",
        "DvAuthDetail": null,
        "VerifyType": null,
        "StatusMsg": null,
        "StatusName": "已通过",
        "ProjectId": "0",
        "OwnerUin": "779000108",
        "ProductZhName": "SecureSite 增强型(EV)",
        "CertEndTime": "2020-02-14 16:00:00",
        "PackageType": "4",
        "RequestId": "658b9da1-b5e6-46b3-803c-d59a2cb60277",
        "InsertTime": "2020-01-16 13:19:10",
        "CertificateType": "SVR",
        "IsVip": true,
        "ValidityPeriod": "12",
        "OrderId": "SE8PUhGU",
        "Domain": "test-ev-dae23r32fd.com",
        "CertificateId": "aCMEQWHt",
        "Alias": "",
        "SubmittedData": null,
        "IsWildcard": false,
        "Deployable": true,
        "VulnerabilityStatus": "INACTIVE"
    }
}
```

