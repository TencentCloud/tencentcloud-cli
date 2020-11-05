**Example 1: Obtaining certificate information**



Input: 

```
tccli ssl DescribeCertificate --cli-unfold-argument  \
    --CertificateId CertificateId
```

Output: 
```
{
    "Response": {
        "From": "trustasia",
        "SubjectAltName": null,
        "VulnerabilityReport": null,
        "StatusName": "approved",
        "CertificateExtra": {
            "OriginCertificateId": null,
            "ReplacedBy": null,
            "ReplacedFor": "a8xHcaIs",
            "DomainNumber": null
        },
        "RenewAble": false,
        "Status": 1,
        "IsDv": true,
        "CertBeginTime": "2020-01-14 16:00:00",
        "IsVulnerability": false,
        "DvAuthDetail": null,
        "VerifyType": "DNS",
        "StatusMsg": null,
        "ProjectId": "0",
        "OwnerUin": "20548499",
        "ProductZhName": "TrustAsia TLS RSA CA",
        "CertEndTime": "2020-02-12 16:00:00",
        "PackageType": "2",
        "RequestId": "6209102a-0f05-411d-a05c-c841431cb636",
        "InsertTime": "2020-01-14 10:54:47",
        "CertificateType": "SVR",
        "IsVip": false,
        "ValidityPeriod": "0",
        "OrderId": "TBD8NHC9J_01",
        "Domain": "wgc.red",
        "CertificateId": "a90XEOtj",
        "Alias": "New order for a8xHcaIs",
        "SubmittedData": null,
        "IsWildcard": false,
        "PackageTypeName": "TrustAsia TLS RSA CA",
        "VulnerabilityStatus": "INACTIVE"
    }
}
```

