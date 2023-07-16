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
        "OwnerUin": "abc",
        "ProjectId": "abc",
        "From": "abc",
        "CertificateType": "abc",
        "PackageType": "abc",
        "ProductZhName": "abc",
        "Domain": "abc",
        "Alias": "abc",
        "Status": 1,
        "StatusMsg": "abc",
        "VerifyType": "abc",
        "VulnerabilityStatus": "abc",
        "CertBeginTime": "2020-09-22 00:00:00",
        "CertEndTime": "2020-09-22 00:00:00",
        "ValidityPeriod": "abc",
        "InsertTime": "2020-09-22 00:00:00",
        "OrderId": "abc",
        "CertificateExtra": {
            "DomainNumber": "abc",
            "OriginCertificateId": "abc",
            "ReplacedBy": "abc",
            "ReplacedFor": "abc",
            "RenewOrder": "abc",
            "SMCert": 0
        },
        "CertificatePrivateKey": "abc",
        "CertificatePublicKey": "abc",
        "DvAuthDetail": {
            "DvAuthKey": "abc",
            "DvAuthValue": "abc",
            "DvAuthDomain": "abc",
            "DvAuthPath": "abc",
            "DvAuthKeySubDomain": "abc",
            "DvAuths": [
                {
                    "DvAuthKey": "abc",
                    "DvAuthValue": "abc",
                    "DvAuthDomain": "abc",
                    "DvAuthPath": "abc",
                    "DvAuthSubDomain": "abc",
                    "DvAuthVerifyType": "abc"
                }
            ]
        },
        "VulnerabilityReport": "abc",
        "CertificateId": "abc",
        "TypeName": "abc",
        "StatusName": "abc",
        "SubjectAltName": [
            "abc"
        ],
        "IsVip": true,
        "IsWildcard": true,
        "IsDv": true,
        "IsVulnerability": true,
        "SubmittedData": {
            "CsrType": "abc",
            "CsrContent": "abc",
            "CertificateDomain": "abc",
            "DomainList": [
                "abc"
            ],
            "KeyPassword": "abc",
            "OrganizationName": "abc",
            "OrganizationDivision": "abc",
            "OrganizationAddress": "abc",
            "OrganizationCountry": "abc",
            "OrganizationCity": "abc",
            "OrganizationRegion": "abc",
            "PostalCode": "abc",
            "PhoneAreaCode": "abc",
            "PhoneNumber": "abc",
            "AdminFirstName": "abc",
            "AdminLastName": "abc",
            "AdminPhoneNum": "abc",
            "AdminEmail": "abc",
            "AdminPosition": "abc",
            "ContactFirstName": "abc",
            "ContactLastName": "abc",
            "ContactNumber": "abc",
            "ContactEmail": "abc",
            "ContactPosition": "abc",
            "VerifyType": "abc"
        },
        "RenewAble": true,
        "Deployable": true,
        "Tags": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "RootCert": {
            "Sign": "abc",
            "Encrypt": "abc",
            "Standard": "abc"
        },
        "EncryptCert": "abc",
        "EncryptPrivateKey": "abc",
        "CertFingerprint": "abc",
        "EncryptCertFingerprint": "abc",
        "EncryptAlgorithm": "abc",
        "DvRevokeAuthDetail": [
            {
                "DvAuthKey": "abc",
                "DvAuthValue": "abc",
                "DvAuthDomain": "abc",
                "DvAuthPath": "abc",
                "DvAuthSubDomain": "abc",
                "DvAuthVerifyType": "abc"
            }
        ],
        "RequestId": "abc"
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
        "OwnerUin": "abc",
        "ProjectId": "abc",
        "From": "abc",
        "CertificateType": "abc",
        "PackageType": "abc",
        "ProductZhName": "abc",
        "Domain": "abc",
        "Alias": "abc",
        "Status": 1,
        "StatusMsg": "abc",
        "VerifyType": "abc",
        "VulnerabilityStatus": "abc",
        "CertBeginTime": "2020-09-22 00:00:00",
        "CertEndTime": "2020-09-22 00:00:00",
        "ValidityPeriod": "abc",
        "InsertTime": "2020-09-22 00:00:00",
        "OrderId": "abc",
        "CertificateExtra": {
            "DomainNumber": "abc",
            "OriginCertificateId": "abc",
            "ReplacedBy": "abc",
            "ReplacedFor": "abc",
            "RenewOrder": "abc",
            "SMCert": 0
        },
        "CertificatePrivateKey": "abc",
        "CertificatePublicKey": "abc",
        "DvAuthDetail": {
            "DvAuthKey": "abc",
            "DvAuthValue": "abc",
            "DvAuthDomain": "abc",
            "DvAuthPath": "abc",
            "DvAuthKeySubDomain": "abc",
            "DvAuths": [
                {
                    "DvAuthKey": "abc",
                    "DvAuthValue": "abc",
                    "DvAuthDomain": "abc",
                    "DvAuthPath": "abc",
                    "DvAuthSubDomain": "abc",
                    "DvAuthVerifyType": "abc"
                }
            ]
        },
        "VulnerabilityReport": "abc",
        "CertificateId": "abc",
        "TypeName": "abc",
        "StatusName": "abc",
        "SubjectAltName": [
            "abc"
        ],
        "IsVip": true,
        "IsWildcard": true,
        "IsDv": true,
        "IsVulnerability": true,
        "SubmittedData": {
            "CsrType": "abc",
            "CsrContent": "abc",
            "CertificateDomain": "abc",
            "DomainList": [
                "abc"
            ],
            "KeyPassword": "abc",
            "OrganizationName": "abc",
            "OrganizationDivision": "abc",
            "OrganizationAddress": "abc",
            "OrganizationCountry": "abc",
            "OrganizationCity": "abc",
            "OrganizationRegion": "abc",
            "PostalCode": "abc",
            "PhoneAreaCode": "abc",
            "PhoneNumber": "abc",
            "AdminFirstName": "abc",
            "AdminLastName": "abc",
            "AdminPhoneNum": "abc",
            "AdminEmail": "abc",
            "AdminPosition": "abc",
            "ContactFirstName": "abc",
            "ContactLastName": "abc",
            "ContactNumber": "abc",
            "ContactEmail": "abc",
            "ContactPosition": "abc",
            "VerifyType": "abc"
        },
        "RenewAble": true,
        "Deployable": true,
        "Tags": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "RootCert": {
            "Sign": "abc",
            "Encrypt": "abc",
            "Standard": "abc"
        },
        "EncryptCert": "abc",
        "EncryptPrivateKey": "abc",
        "CertFingerprint": "abc",
        "EncryptCertFingerprint": "abc",
        "EncryptAlgorithm": "abc",
        "DvRevokeAuthDetail": [
            {
                "DvAuthKey": "abc",
                "DvAuthValue": "abc",
                "DvAuthDomain": "abc",
                "DvAuthPath": "abc",
                "DvAuthSubDomain": "abc",
                "DvAuthVerifyType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

