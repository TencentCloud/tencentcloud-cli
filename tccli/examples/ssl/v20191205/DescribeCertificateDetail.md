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
        "From": "xx",
        "SubjectAltName": [
            "xx"
        ],
        "VulnerabilityReport": "xx",
        "EncryptCertFingerprint": "xx",
        "EncryptPrivateKey": "xx",
        "CertificatePrivateKey": "xx",
        "CertificatePublicKey": "xx",
        "StatusName": "xx",
        "RenewAble": false,
        "Status": 1,
        "IsDv": false,
        "IsVulnerability": false,
        "CertBeginTime": "2020-09-22 00:00:00",
        "TypeName": "xx",
        "CertificateExtra": {
            "ReplacedBy": "xx",
            "ReplacedFor": "xx",
            "OriginCertificateId": "xx",
            "DomainNumber": "xx",
            "RenewOrder": "xx"
        },
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
        "RootCert": {
            "Standard": "xx",
            "Encrypt": "xx",
            "Sign": "xx"
        },
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
        "CertFingerprint": "xx",
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
                "test-11111111111111.com",
                "test-222222222222.com"
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
        "Deployable": false,
        "EncryptCert": "xx",
        "EncryptAlgorithm": "RSA 2048",
        "VulnerabilityStatus": "xx"
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
            "xx"
        ],
        "VulnerabilityReport": "xx",
        "EncryptCertFingerprint": "xx",
        "EncryptPrivateKey": "xx",
        "CertificatePrivateKey": "xx",
        "CertificatePublicKey": "xx",
        "StatusName": "xx",
        "RenewAble": false,
        "Status": 1,
        "IsDv": false,
        "IsVulnerability": false,
        "CertBeginTime": "2020-09-22 00:00:00",
        "TypeName": "xx",
        "CertificateExtra": {
            "ReplacedBy": "xx",
            "ReplacedFor": "xx",
            "OriginCertificateId": "xx",
            "DomainNumber": "xx",
            "RenewOrder": "xx"
        },
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
        "RootCert": {
            "Standard": "xx",
            "Encrypt": "xx",
            "Sign": "xx"
        },
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
        "CertFingerprint": "xx",
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
                "test-11111111111111.com",
                "test-222222222222.com"
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
        "Deployable": false,
        "EncryptCert": "xx",
        "EncryptAlgorithm": "RSA 2048",
        "VulnerabilityStatus": "xx"
    }
}
```

