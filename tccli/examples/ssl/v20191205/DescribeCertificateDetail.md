**Example 1: Obtaining certificate details**

This example shows you how to obtain the details of a certificate which is being reviewed.

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
        "SubjectAltName": null,
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
        "TypeName": "Secure Site OV",
        "DvAuthDetail": null,
        "VerifyType": null,
        "StatusMsg": null,
        "StatusName": "OV certificate, to be submitted",
        "ProjectId": "0",
        "OwnerUin": "779000108",
        "ProductZhName": "Secure Site OV",
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
            "OrganizationCity": "Shenzhen",
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
            "OrganizationRegion": "Guangdong",
            "PhoneNumber": "86013388",
            "PostalCode": "",
            "AdminEmail": "test@tencent.com",
            "KeyPassword": "",
            "OrganizationAddress": "Tencent Building, No. 10000 Shennan Road, Nanshan District"
        },
        "IsWildcard": false,
        "Deployable": false,
        "VulnerabilityStatus": "INACTIVE"
    }
}
```

**Example 2: Obtaining certificate details-2**

This example shows you how to obtain the details of a certificate which has been approved.

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
        "TypeName": "Secure Site EV",
        "DvAuthDetail": null,
        "VerifyType": null,
        "StatusMsg": null,
        "StatusName": "approved",
        "ProjectId": "0",
        "OwnerUin": "779000108",
        "ProductZhName": "Secure Site EV",
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

