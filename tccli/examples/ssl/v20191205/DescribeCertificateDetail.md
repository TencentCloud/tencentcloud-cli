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
        "EncryptCert": "",
        "EncryptPrivateKey": "",
        "CertificateExtra": {
            "OriginCertificateId": null,
            "ReplacedBy": null,
            "ReplacedFor": null,
            "DomainNumber": "3",
            "RenewOrder": null
        },
        "RootCert": {},
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
        "VulnerabilityStatus": "INACTIVE",
        "Tags": [
            {
                "TagKey": "责任人",
                "TagValue": "yaxinliu"
            },
            {
                "TagKey": "部门",
                "TagValue": "IT部"
            }
        ]
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
        "From": "xx",
        "SubjectAltName": [
            "test-ev-dawe23r243qfa.com"
        ],
        "EncryptCert": "",
        "EncryptPrivateKey": "",
        "VulnerabilityReport": "xx",
        "CertificatePrivateKey": "xx",
        "CertificatePublicKey": "xx",
        "CertificateExtra": {
            "ReplacedBy": "xx",
            "ReplacedFor": "xx",
            "OriginCertificateId": "xx",
            "DomainNumber": "xx",
            "RenewOrder": "xx"
        },
        "RenewAble": true,
        "Status": 1,
        "RootCert": {},
        "IsDv": false,
        "IsVulnerability": true,
        "CertBeginTime": "2020-09-22 00:00:00",
        "TypeName": "xx",
        "VulnerabilityStatus": "xx",
        "DvAuthDetail": {
            "DvAuths": [
                {
                    "DvAuthSubDomain": "xx",
                    "DvAuthVerifyType": "xx",
                    "DvAuthDomain": "xx",
                    "DvAuthValue": "xx",
                    "DvAuthKey": "xx",
                    "DvAuthPath": "xx"
                }
            ],
            "DvAuthKeySubDomain": "xx",
            "DvAuthDomain": "xx",
            "DvAuthValue": "xx",
            "DvAuthKey": "xx",
            "DvAuthPath": "xx"
        },
        "VerifyType": "xx",
        "StatusMsg": "xx",
        "ProjectId": "xx",
        "OwnerUin": "xx",
        "ProductZhName": "xx",
        "CertEndTime": "2020-09-22 00:00:00",
        "PackageType": "xx",
        "RequestId": "xx",
        "InsertTime": "2020-09-22 00:00:00",
        "CertificateType": "xx",
        "IsVip": true,
        "ValidityPeriod": "xx",
        "OrderId": "xx",
        "Domain": "xx",
        "CertificateId": "xx",
        "Alias": "xx",
        "SubmittedData": {
            "OrganizationCity": "xx",
            "CsrContent": "xx",
            "OrganizationName": "xx",
            "CertificateDomain": "xx",
            "AdminPhoneNum": "xx",
            "AdminPosition": "xx",
            "OrganizationDivision": "xx",
            "DomainList": [
                "xx"
            ],
            "AdminFirstName": "xx",
            "ContactLastName": "xx",
            "ContactEmail": "xx",
            "ContactNumber": "xx",
            "CsrType": "xx",
            "PhoneAreaCode": "xx",
            "VerifyType": "xx",
            "AdminLastName": "xx",
            "ContactFirstName": "xx",
            "OrganizationCountry": "xx",
            "ContactPosition": "xx",
            "OrganizationRegion": "xx",
            "PhoneNumber": "xx",
            "PostalCode": "xx",
            "AdminEmail": "xx",
            "KeyPassword": "xx",
            "OrganizationAddress": "xx"
        },
        "Tags": [
            {
                "TagKey": "xx",
                "TagValue": "xx"
            },
            {
                "TagKey": "xx",
                "TagValue": "xx"
            }
        ],
        "IsWildcard": false,
        "Deployable": true,
        "StatusName": "xx"
    }
}
```

