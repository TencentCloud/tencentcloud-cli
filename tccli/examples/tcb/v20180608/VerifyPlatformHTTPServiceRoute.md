**Example 1: 校验域名**



Input: 

```
tccli tcb VerifyPlatformHTTPServiceRoute --cli-unfold-argument  \
    --PlatformId pf-t960szfwv1cs \
    --Domain.Domain *.rgw.***************.cn
```

Output: 
```
{
    "Response": {
        "Blacklist": {
            "Message": "not in blacklist",
            "Status": "PASS"
        },
        "CDNResource": {
            "Message": "access type is not CDN, cdn resource check skipped",
            "Status": "SKIPPED"
        },
        "Cert": {
            "Message": "CertId is empty, cert verify skipped",
            "Status": "SKIPPED"
        },
        "DomainConflict": {
            "Message": "no domain conflict",
            "Status": "PASS"
        },
        "EO": {
            "Message": "access type is not EO, EO check skipped",
            "Status": "SKIPPED"
        },
        "InternalAccount": {
            "Message": "not an internal domain, skipped",
            "Status": "SKIPPED"
        },
        "Ownership": {
            "Message": "domain ownership verified",
            "Status": "PASS"
        },
        "Passed": true,
        "Quota": {
            "Message": "quota check passed",
            "Status": "PASS"
        },
        "RouteConflict": {
            "Message": "no routes provided, route conflict check skipped",
            "Status": "SKIPPED"
        },
        "RequestId": "0de3dab3-6917-4a6b-a243-432aa4cd8ed3"
    }
}
```

