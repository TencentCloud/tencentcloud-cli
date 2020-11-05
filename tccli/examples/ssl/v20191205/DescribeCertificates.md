**Example 1: Obtaining certificate list**

This example shows you how to obtain the certificate list.

Input: 

```
tccli ssl DescribeCertificates --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Certificates": [
            {
                "From": "trustasia",
                "SubjectAltName": null,
                "BoundResource": [],
                "CertificateExtra": {
                    "OriginCertificateId": null,
                    "ReplacedBy": null,
                    "ReplacedFor": "a8xHcaIs",
                    "DomainNumber": null,
                    "RenewOrder": null
                },
                "StatusName": "approved",
                "RenewAble": false,
                "Status": 1,
                "IsDv": true,
                "CertBeginTime": "2020-01-14 16:00:00",
                "IsVulnerability": false,
                "VerifyType": "DNS",
                "StatusMsg": null,
                "ProjectId": "0",
                "OwnerUin": "20548499",
                "ProjectInfo": {
                    "ProjectCreatorUin": 0,
                    "ProjectCreateTime": "0000-00-00 00:00:00",
                    "ProjectId": "0",
                    "OwnerUin": 0,
                    "ProjectResume": "Default project",
                    "ProjectName": "Default project"
                },
                "ProductZhName": "TrustAsia TLS RSA CA",
                "CertEndTime": "2020-02-12 16:00:00",
                "PackageType": "2",
                "InsertTime": "2020-01-14 10:54:47",
                "CertificateType": "SVR",
                "IsVip": false,
                "ValidityPeriod": "0",
                "Domain": "wgc.red",
                "CertificateId": "a90XEOtj",
                "Alias": "New order for a8xHcaIs",
                "IsWildcard": false,
                "PackageTypeName": "TrustAsia TLS RSA CA",
                "VulnerabilityStatus": "INACTIVE",
                "Deployable": true
            }
        ],
        "TotalCount": 12,
        "RequestId": "43b82119-c648-4230-8d38-5be63f039549"
    }
}
```

