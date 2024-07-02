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
        "OwnerUin": "a1b2c3",
        "ProjectId": "a1b2c3",
        "From": "a1b2c3",
        "CertificateType": "a1b2c3",
        "PackageType": "a1b2c3",
        "ProductZhName": "a1b2c3",
        "Domain": "a1b2c3",
        "Alias": "a1b2c3",
        "Status": 1,
        "StatusMsg": "a1b2c3",
        "VerifyType": "a1b2c3",
        "VulnerabilityStatus": "a1b2c3",
        "CertBeginTime": "2020-09-22 00:00:00",
        "CertEndTime": "2020-09-22 00:00:00",
        "ValidityPeriod": "a1b2c3",
        "InsertTime": "2020-09-22 00:00:00",
        "OrderId": "a1b2c3",
        "CertificateExtra": {
            "DomainNumber": "a1b2c3",
            "OriginCertificateId": "a1b2c3",
            "ReplacedBy": "a1b2c3",
            "ReplacedFor": "a1b2c3",
            "RenewOrder": "a1b2c3",
            "SMCert": 0,
            "CompanyType": 2
        },
        "CertificatePrivateKey": "a1b2c3",
        "CertificatePublicKey": "a1b2c3",
        "DvAuthDetail": {
            "DvAuthKey": "a1b2c3",
            "DvAuthValue": "a1b2c3",
            "DvAuthDomain": "a1b2c3",
            "DvAuthPath": "a1b2c3",
            "DvAuthKeySubDomain": "a1b2c3",
            "DvAuths": [
                {
                    "DvAuthKey": "a1b2c3",
                    "DvAuthValue": "a1b2c3",
                    "DvAuthDomain": "a1b2c3",
                    "DvAuthPath": "a1b2c3",
                    "DvAuthSubDomain": "a1b2c3",
                    "DvAuthVerifyType": "a1b2c3"
                }
            ]
        },
        "VulnerabilityReport": "a1b2c3",
        "CertificateId": "a1b2c3",
        "TypeName": "a1b2c3",
        "StatusName": "a1b2c3",
        "SubjectAltName": [
            "a1b2c3"
        ],
        "IsVip": true,
        "IsWildcard": true,
        "IsDv": true,
        "IsVulnerability": true,
        "SubmittedData": {
            "CsrType": "a1b2c3",
            "CsrContent": "a1b2c3",
            "CertificateDomain": "a1b2c3",
            "DomainList": [
                "a1b2c3"
            ],
            "KeyPassword": "a1b2c3",
            "OrganizationName": "a1b2c3",
            "OrganizationDivision": "a1b2c3",
            "OrganizationAddress": "a1b2c3",
            "OrganizationCountry": "a1b2c3",
            "OrganizationCity": "a1b2c3",
            "OrganizationRegion": "a1b2c3",
            "PostalCode": "a1b2c3",
            "PhoneAreaCode": "a1b2c3",
            "PhoneNumber": "a1b2c3",
            "AdminFirstName": "a1b2c3",
            "AdminLastName": "a1b2c3",
            "AdminPhoneNum": "a1b2c3",
            "AdminEmail": "a1b2c3",
            "AdminPosition": "a1b2c3",
            "ContactFirstName": "a1b2c3",
            "ContactLastName": "a1b2c3",
            "ContactNumber": "a1b2c3",
            "ContactEmail": "a1b2c3",
            "ContactPosition": "a1b2c3",
            "VerifyType": "a1b2c3"
        },
        "RenewAble": true,
        "Deployable": true,
        "Tags": [
            {
                "TagKey": "a1b2c3",
                "TagValue": "a1b2c3"
            }
        ],
        "RootCert": {
            "Sign": "a1b2c3",
            "Encrypt": "a1b2c3",
            "Standard": "a1b2c3"
        },
        "EncryptCert": "a1b2c3",
        "EncryptPrivateKey": "a1b2c3",
        "CertFingerprint": "a1b2c3",
        "EncryptCertFingerprint": "a1b2c3",
        "EncryptAlgorithm": "a1b2c3",
        "DvRevokeAuthDetail": [
            {
                "DvAuthKey": "a1b2c3",
                "DvAuthValue": "a1b2c3",
                "DvAuthDomain": "a1b2c3",
                "DvAuthPath": "a1b2c3",
                "DvAuthSubDomain": "a1b2c3",
                "DvAuthVerifyType": "a1b2c3"
            }
        ],
        "RequestId": "a1b2c3"
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
        "OwnerUin": "a1b2c3",
        "ProjectId": "a1b2c3",
        "From": "a1b2c3",
        "CertificateType": "a1b2c3",
        "PackageType": "a1b2c3",
        "ProductZhName": "a1b2c3",
        "Domain": "a1b2c3",
        "Alias": "a1b2c3",
        "Status": 1,
        "StatusMsg": "a1b2c3",
        "VerifyType": "a1b2c3",
        "VulnerabilityStatus": "a1b2c3",
        "CertBeginTime": "2020-09-22 00:00:00",
        "CertEndTime": "2020-09-22 00:00:00",
        "ValidityPeriod": "a1b2c3",
        "InsertTime": "2020-09-22 00:00:00",
        "OrderId": "a1b2c3",
        "CertificateExtra": {
            "DomainNumber": "a1b2c3",
            "OriginCertificateId": "a1b2c3",
            "ReplacedBy": "a1b2c3",
            "ReplacedFor": "a1b2c3",
            "RenewOrder": "a1b2c3",
            "SMCert": 0,
            "CompanyType": 2
        },
        "CertificatePrivateKey": "a1b2c3",
        "CertificatePublicKey": "a1b2c3",
        "DvAuthDetail": {
            "DvAuthKey": "a1b2c3",
            "DvAuthValue": "a1b2c3",
            "DvAuthDomain": "a1b2c3",
            "DvAuthPath": "a1b2c3",
            "DvAuthKeySubDomain": "a1b2c3",
            "DvAuths": [
                {
                    "DvAuthKey": "a1b2c3",
                    "DvAuthValue": "a1b2c3",
                    "DvAuthDomain": "a1b2c3",
                    "DvAuthPath": "a1b2c3",
                    "DvAuthSubDomain": "a1b2c3",
                    "DvAuthVerifyType": "a1b2c3"
                }
            ]
        },
        "VulnerabilityReport": "a1b2c3",
        "CertificateId": "a1b2c3",
        "TypeName": "a1b2c3",
        "StatusName": "a1b2c3",
        "SubjectAltName": [
            "a1b2c3"
        ],
        "IsVip": true,
        "IsWildcard": true,
        "IsDv": true,
        "IsVulnerability": true,
        "SubmittedData": {
            "CsrType": "a1b2c3",
            "CsrContent": "a1b2c3",
            "CertificateDomain": "a1b2c3",
            "DomainList": [
                "a1b2c3"
            ],
            "KeyPassword": "a1b2c3",
            "OrganizationName": "a1b2c3",
            "OrganizationDivision": "a1b2c3",
            "OrganizationAddress": "a1b2c3",
            "OrganizationCountry": "a1b2c3",
            "OrganizationCity": "a1b2c3",
            "OrganizationRegion": "a1b2c3",
            "PostalCode": "a1b2c3",
            "PhoneAreaCode": "a1b2c3",
            "PhoneNumber": "a1b2c3",
            "AdminFirstName": "a1b2c3",
            "AdminLastName": "a1b2c3",
            "AdminPhoneNum": "a1b2c3",
            "AdminEmail": "a1b2c3",
            "AdminPosition": "a1b2c3",
            "ContactFirstName": "a1b2c3",
            "ContactLastName": "a1b2c3",
            "ContactNumber": "a1b2c3",
            "ContactEmail": "a1b2c3",
            "ContactPosition": "a1b2c3",
            "VerifyType": "a1b2c3"
        },
        "RenewAble": true,
        "Deployable": true,
        "Tags": [
            {
                "TagKey": "a1b2c3",
                "TagValue": "a1b2c3"
            }
        ],
        "RootCert": {
            "Sign": "a1b2c3",
            "Encrypt": "a1b2c3",
            "Standard": "a1b2c3"
        },
        "EncryptCert": "a1b2c3",
        "EncryptPrivateKey": "a1b2c3",
        "CertFingerprint": "a1b2c3",
        "EncryptCertFingerprint": "a1b2c3",
        "EncryptAlgorithm": "a1b2c3",
        "DvRevokeAuthDetail": [
            {
                "DvAuthKey": "a1b2c3",
                "DvAuthValue": "a1b2c3",
                "DvAuthDomain": "a1b2c3",
                "DvAuthPath": "a1b2c3",
                "DvAuthSubDomain": "a1b2c3",
                "DvAuthVerifyType": "a1b2c3"
            }
        ],
        "RequestId": "a1b2c3"
    }
}
```

