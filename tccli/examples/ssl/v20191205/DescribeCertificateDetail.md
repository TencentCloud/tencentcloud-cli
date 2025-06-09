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
        "OwnerUin": "815836472",
        "ProjectId": "0",
        "From": "trustasia",
        "OrderId": "u1hD8*****mXue",
        "CertificateType": "SVR",
        "PackageType": "48",
        "ProductZhName": "DNSPod-域名型(DV)SSL证书",
        "Domain": "ninghhuang.online",
        "Alias": "",
        "Status": 4,
        "StatusMsg": "CA-REVIEWING",
        "VulnerabilityStatus": "INACTIVE",
        "RootCert": {
            "Sign": null,
            "Encrypt": null,
            "Standard": null
        },
        "EncryptCert": null,
        "EncryptPrivateKey": null,
        "CertificatePrivateKey": "*******",
        "CertificatePublicKey": null,
        "CertBeginTime": null,
        "CertEndTime": null,
        "ValidityPeriod": "12",
        "InsertTime": "2024-12-02 19:12:46",
        "VulnerabilityReport": null,
        "CertificateId": "K33dxkOk",
        "TypeName": "DNSPod-域名型(DV)SSL证书",
        "StatusName": "待验证",
        "CertificateExtra": {
            "SMCert": 0,
            "ReplacedBy": null,
            "OriginCertificateId": null,
            "ReplacedFor": null,
            "RenewOrder": null,
            "DomainNumber": "1",
            "CompanyType": 2
        },
        "DvAuthDetail": {
            "DvAuths": [
                {
                    "DvAuthKey": "_875bed25cf9e03596931d91cb0a52bd9.ninghhuang.online",
                    "DvAuthValue": "a3108492878a2d989949fa50522dd2b0.cc7346307ff022fcfa68e025f6dbf6ad.cmcdpcwca5iljv.trust-provider.com",
                    "DvAuthDomain": "ninghhuang.online",
                    "DvAuthPath": "",
                    "DvAuthSubDomain": "_875bed25cf9e03596931d91cb0a52bd9",
                    "DvAuthVerifyType": "CNAME"
                }
            ],
            "DvAuthKey": "_875bed25cf9e03596931d91cb0a52bd9.ninghhuang.online",
            "DvAuthValue": "a3108492878a2d989949fa50522dd2b0.cc7346307ff022fcfa68e025f6dbf6ad.cmcdpcwca5iljv.trust-provider.com",
            "DvAuthDomain": "ni****ang.online",
            "DvAuthPath": "",
            "DvAuthKeySubDomain": "_875bed25cf9e03596931d91cb0a52bd9"
        },
        "VerifyType": "DNS_AUTO",
        "DvRevokeAuthDetail": [],
        "SubjectAltName": [],
        "IsVip": true,
        "IsWildcard": false,
        "IsDv": true,
        "IsVulnerability": false,
        "SubmittedData": null,
        "RenewAble": false,
        "Deployable": true,
        "Tags": [],
        "CertFingerprint": null,
        "EncryptCertFingerprint": null,
        "EncryptAlgorithm": "RSA 2048",
        "CertChainInfo": null,
        "DomainType": 1,
        "CertType": "OV",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
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
        "OwnerUin": "815836472",
        "ProjectId": "0",
        "From": "trustasia",
        "OrderId": "PVpvxIN2_E*****pvjw",
        "CertificateType": "SVR",
        "PackageType": "43",
        "ProductZhName": "DNSPod-企业型(OV)SSL证书",
        "Domain": "ninghhuang.online",
        "Alias": "",
        "Status": 4,
        "StatusMsg": "PRE-REVIEWING",
        "VulnerabilityStatus": "INACTIVE",
        "RootCert": {
            "Sign": null,
            "Encrypt": null,
            "Standard": null
        },
        "EncryptCert": null,
        "EncryptPrivateKey": null,
        "CertificatePrivateKey": "*****",
        "CertificatePublicKey": null,
        "CertBeginTime": null,
        "CertEndTime": null,
        "ValidityPeriod": "12",
        "InsertTime": "2024-11-27 20:06:51",
        "VulnerabilityReport": null,
        "CertificateId": "Jv8u7beI",
        "TypeName": "DNSPod-企业型(OV)SSL证书",
        "StatusName": "待验证",
        "CertificateExtra": {
            "SMCert": 0,
            "ReplacedBy": null,
            "OriginCertificateId": null,
            "ReplacedFor": null,
            "RenewOrder": null,
            "DomainNumber": "1",
            "CompanyType": 2
        },
        "DvAuthDetail": {
            "DvAuths": [
                {
                    "DvAuthKey": "_882a77cde28ffe49e5764ab3afb75849.ninghhuang.online",
                    "DvAuthValue": "97f80ec4c7947178cec6b5a093ed34b0.a5cd7986aaaffdfd37437c9c6de1dd30.cmcopc2ncmbffy.trust-provider.com",
                    "DvAuthDomain": "ninghhuang.online",
                    "DvAuthPath": "",
                    "DvAuthSubDomain": "_882a77cde28ffe49e5764ab3afb75849",
                    "DvAuthVerifyType": "CNAME"
                }
            ],
            "DvAuthKey": "_882a77cde28ffe49e5764ab3afb75849.ninghhuang.online",
            "DvAuthValue": "97f80ec4c7947178cec6b5a093ed34b0.a5cd7986aaaffdfd37437c9c6de1dd30.cmcopc2ncmbffy.trust-provider.com",
            "DvAuthDomain": "ninghhuang.online",
            "DvAuthPath": "",
            "DvAuthKeySubDomain": "_882a77cde28ffe49e5764ab3afb75849"
        },
        "VerifyType": "DNS_AUTO",
        "DvRevokeAuthDetail": [],
        "SubjectAltName": [],
        "IsVip": true,
        "IsWildcard": false,
        "IsDv": false,
        "IsVulnerability": false,
        "SubmittedData": null,
        "RenewAble": false,
        "Deployable": true,
        "Tags": [],
        "CertFingerprint": null,
        "EncryptCertFingerprint": null,
        "EncryptAlgorithm": "RSA 2048",
        "CertChainInfo": null,
        "DomainType": 1,
        "CertType": "OV",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

