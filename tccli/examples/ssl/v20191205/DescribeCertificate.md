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
        "CertBeginTime": "abc",
        "CertEndTime": "abc",
        "ValidityPeriod": "abc",
        "InsertTime": "abc",
        "OrderId": "abc",
        "CertificateExtra": {
            "DomainNumber": "abc",
            "OriginCertificateId": "abc",
            "ReplacedBy": "abc",
            "ReplacedFor": "abc",
            "RenewOrder": "abc",
            "SMCert": 0
        },
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
        "PackageTypeName": "abc",
        "StatusName": "abc",
        "SubjectAltName": [
            "abc"
        ],
        "IsVip": true,
        "IsWildcard": true,
        "IsDv": true,
        "IsVulnerability": true,
        "RenewAble": true,
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
        "Deployable": true,
        "Tags": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "CAEncryptAlgorithms": [
            "abc"
        ],
        "CACommonNames": [
            "abc"
        ],
        "CAEndTimes": [
            "abc"
        ],
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

