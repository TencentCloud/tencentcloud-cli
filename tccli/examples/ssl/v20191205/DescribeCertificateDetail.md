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
        "From": "xx123",
        "SubjectAltName": [
            "xx123"
        ],
        "VulnerabilityReport": "xx123",
        "EncryptCertFingerprint": "xx123",
        "EncryptPrivateKey": "xx123",
        "CertificatePrivateKey": "xx123",
        "CertificatePublicKey": "xx123",
        "StatusName": "xx123",
        "RenewAble": false,
        "Status": 1,
        "IsDv": false,
        "IsVulnerability": false,
        "CertBeginTime": "2020-09-22 00:00:00",
        "TypeName": "xx123",
        "CertificateExtra": {
            "ReplacedBy": "xx123",
            "ReplacedFor": "xx123",
            "OriginCertificateId": "xx123",
            "DomainNumber": "xx123",
            "RenewOrder": "xx123"
        },
        "DvAuthDetail": {
            "DvAuths": [
                {
                    "DvAuthSubDomain": "xx123",
                    "DvAuthVerifyType": "xx123",
                    "DvAuthDomain": "xx123",
                    "DvAuthValue": "xx123",
                    "DvAuthKey": "xx123",
                    "DvAuthPath": "xx123"
                }
            ],
            "DvAuthKeySubDomain": "xx123",
            "DvAuthDomain": "xx123",
            "DvAuthValue": "xx123",
            "DvAuthKey": "xx123",
            "DvAuthPath": "xx123"
        },
        "VerifyType": "xx123",
        "StatusMsg": "xx123",
        "RootCert": {
            "Standard": "xx123",
            "Encrypt": "xx123",
            "Sign": "xx123"
        },
        "ProjectId": "xx123",
        "OwnerUin": "xx123",
        "ProductZhName": "xx123",
        "CertEndTime": "2020-09-22 00:00:00",
        "PackageType": "xx123",
        "RequestId": "xx123",
        "InsertTime": "2020-09-22 00:00:00",
        "CertificateType": "xx123",
        "IsVip": true,
        "ValidityPeriod": "xx123",
        "OrderId": "xx123",
        "CertFingerprint": "xx123",
        "Domain": "xx123",
        "CertificateId": "xx123",
        "Alias": "xx123",
        "SubmittedData": {
            "OrganizationCity": "xx123",
            "CsrContent": "xx123",
            "OrganizationName": "xx123",
            "CertificateDomain": "xx123",
            "AdminPhoneNum": "xx123",
            "AdminPosition": "xx123",
            "OrganizationDivision": "xx123",
            "DomainList": [
                "test-11111111111111.com",
                "test-222222222222.com"
            ],
            "AdminFirstName": "xx123",
            "ContactLastName": "xx123",
            "ContactEmail": "xx123",
            "ContactNumber": "xx123",
            "CsrType": "xx123",
            "PhoneAreaCode": "xx123",
            "VerifyType": "xx123",
            "AdminLastName": "xx123",
            "ContactFirstName": "xx123",
            "OrganizationCountry": "xx123",
            "ContactPosition": "xx123",
            "OrganizationRegion": "xx123",
            "PhoneNumber": "xx123",
            "PostalCode": "xx123",
            "AdminEmail": "xx123",
            "KeyPassword": "xx123",
            "OrganizationAddress": "xx123"
        },
        "Tags": [
            {
                "TagKey": "xx123",
                "TagValue": "xx123"
            },
            {
                "TagKey": "xx123",
                "TagValue": "xx123"
            }
        ],
        "IsWildcard": false,
        "Deployable": false,
        "EncryptCert": "xx123",
        "EncryptAlgorithm": "RSA 2048",
        "VulnerabilityStatus": "xx123"
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
        "From": "xx123",
        "SubjectAltName": [
            "xx123"
        ],
        "VulnerabilityReport": "xx123",
        "EncryptCertFingerprint": "xx123",
        "EncryptPrivateKey": "xx123",
        "CertificatePrivateKey": "xx123",
        "CertificatePublicKey": "xx123",
        "StatusName": "xx123",
        "RenewAble": false,
        "Status": 1,
        "IsDv": false,
        "IsVulnerability": false,
        "CertBeginTime": "2020-09-22 00:00:00",
        "TypeName": "xx123",
        "CertificateExtra": {
            "ReplacedBy": "xx123",
            "ReplacedFor": "xx123",
            "OriginCertificateId": "xx123",
            "DomainNumber": "xx123",
            "RenewOrder": "xx123"
        },
        "DvAuthDetail": {
            "DvAuths": [
                {
                    "DvAuthSubDomain": "xx123",
                    "DvAuthVerifyType": "xx123",
                    "DvAuthDomain": "xx123",
                    "DvAuthValue": "xx123",
                    "DvAuthKey": "xx123",
                    "DvAuthPath": "xx123"
                }
            ],
            "DvAuthKeySubDomain": "xx123",
            "DvAuthDomain": "xx123",
            "DvAuthValue": "xx123",
            "DvAuthKey": "xx123",
            "DvAuthPath": "xx123"
        },
        "VerifyType": "xx123",
        "StatusMsg": "xx123",
        "RootCert": {
            "Standard": "xx123",
            "Encrypt": "xx123",
            "Sign": "xx123"
        },
        "ProjectId": "xx123",
        "OwnerUin": "xx123",
        "ProductZhName": "xx123",
        "CertEndTime": "2020-09-22 00:00:00",
        "PackageType": "xx123",
        "RequestId": "xx123",
        "InsertTime": "2020-09-22 00:00:00",
        "CertificateType": "xx123",
        "IsVip": true,
        "ValidityPeriod": "xx123",
        "OrderId": "xx123",
        "CertFingerprint": "xx123",
        "Domain": "xx123",
        "CertificateId": "xx123",
        "Alias": "xx123",
        "SubmittedData": {
            "OrganizationCity": "xx123",
            "CsrContent": "xx123",
            "OrganizationName": "xx123",
            "CertificateDomain": "xx123",
            "AdminPhoneNum": "xx123",
            "AdminPosition": "xx123",
            "OrganizationDivision": "xx123",
            "DomainList": [
                "test-11111111111111.com",
                "test-222222222222.com"
            ],
            "AdminFirstName": "xx123",
            "ContactLastName": "xx123",
            "ContactEmail": "xx123",
            "ContactNumber": "xx123",
            "CsrType": "xx123",
            "PhoneAreaCode": "xx123",
            "VerifyType": "xx123",
            "AdminLastName": "xx123",
            "ContactFirstName": "xx123",
            "OrganizationCountry": "xx123",
            "ContactPosition": "xx123",
            "OrganizationRegion": "xx123",
            "PhoneNumber": "xx123",
            "PostalCode": "xx123",
            "AdminEmail": "xx123",
            "KeyPassword": "xx123",
            "OrganizationAddress": "xx123"
        },
        "Tags": [
            {
                "TagKey": "xx123",
                "TagValue": "xx123"
            },
            {
                "TagKey": "xx123",
                "TagValue": "xx123"
            }
        ],
        "IsWildcard": false,
        "Deployable": false,
        "EncryptCert": "xx123",
        "EncryptAlgorithm": "RSA 2048",
        "VulnerabilityStatus": "xx123"
    }
}
```

