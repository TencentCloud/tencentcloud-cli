**Example 1: 获取证书详情**



Input: 

```
tccli ssl DescribeCertificateDetail --cli-unfold-argument  \
    --CertificateId QL*****M
```

Output: 
```
{
    "Response": {
        "OwnerUin": "1000****920",
        "ProjectId": "0",
        "From": "trustasia",
        "OrderId": "xQOzHUgs_Cwm2Vhn0",
        "CertificateType": "SVR",
        "PackageType": "83",
        "ProductZhName": "TrustAsia C1 DV Free",
        "Domain": "lukesky.online",
        "Alias": "",
        "Status": 1,
        "StatusMsg": null,
        "VulnerabilityStatus": "INACTIVE",
        "RootCert": {
            "Sign": null,
            "Encrypt": null,
            "Standard": "-----BEGIN CERTIFICATE-----***********-----END CERTIFICATE-----\n"
        },
        "EncryptCert": null,
        "EncryptPrivateKey": null,
        "CertificatePrivateKey": "-----BEGIN RSA PRIVATE KEY-----******-----END RSA PRIVATE KEY-----\r\n",
        "CertificatePublicKey": "-----BEGIN CERTIFICATE----*******\n-----END CERTIFICATE-----\n",
        "CertBeginTime": "2026-02-28 08:00:00",
        "CertEndTime": "2026-05-29 07:59:59",
        "ValidityPeriod": "3",
        "InsertTime": "2026-02-28 11:23:09",
        "VulnerabilityReport": null,
        "CertificateId": "QL*****M",
        "TypeName": "TrustAsia C1 DV Free",
        "StatusName": "已颁发",
        "CertificateExtra": {
            "SMCert": 0,
            "ReplacedBy": null,
            "OriginCertificateId": null,
            "ReplacedFor": null,
            "RenewOrder": null,
            "DomainNumber": "1",
            "CompanyType": 1
        },
        "DvAuthDetail": {
            "DvAuths": null,
            "DvAuthKey": null,
            "DvAuthValue": null,
            "DvAuthDomain": null,
            "DvAuthPath": null,
            "DvAuthKeySubDomain": ""
        },
        "VerifyType": "DNS_AUTO",
        "DvRevokeAuthDetail": [],
        "SubjectAltName": [
            "www.lukesky.online"
        ],
        "IsVip": false,
        "IsWildcard": false,
        "IsDv": true,
        "IsVulnerability": false,
        "SubmittedData": null,
        "RenewAble": true,
        "Deployable": true,
        "Tags": [],
        "CertFingerprint": "97E056C1BBDDC*******9CCCE112DF8",
        "EncryptCertFingerprint": null,
        "EncryptAlgorithm": "RSA 2048",
        "CertChainInfo": [
            {
                "Issuer": "TrustAsia DV TLS RSA CA 2025",
                "Subject": "lukesky.online",
                "Fingerprint": "97e05*************3a89ccce112df8",
                "ValidFrom": "2026-02-28 08:00:00",
                "ValidTo": "2026-05-29 07:59:59"
            },
            {
                "Issuer": "DigiCert Global Root G2",
                "Subject": "TrustAsia DV TLS RSA CA 2025",
                "Fingerprint": "7b8a18d***********7c0c634c24994",
                "ValidFrom": "2025-01-08 08:00:00",
                "ValidTo": "2035-01-08 07:59:59"
            }
        ],
        "UseCrossSignRoot": false,
        "DomainType": 1,
        "CertType": "DV",
        "RequestId": "858497b3-d960-4628-9b7c-bbcf96d294e6"
    }
}
```

