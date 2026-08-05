**Example 1: 校验路由**



Input: 

```
tccli tcb VerifyHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Domain.Domain ********************.cn \
    --Domain.AccessType EO \
    --Domain.Protocol HTTP_AND_HTTPS \
    --Domain.Enable True \
    --Domain.Routes.0.Path /autotest/api \
    --Domain.Routes.0.UpstreamResourceType CBR \
    --Domain.Routes.0.UpstreamResourceName autotest-service \
    --Domain.Routes.0.EnableSafeDomain True \
    --Domain.Routes.0.EnableAuth False \
    --Domain.Routes.0.EnablePathTransmission False \
    --Domain.Routes.0.QPSPolicy.QPSTotal 500 \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitBy ClientIP \
    --Domain.Routes.0.QPSPolicy.QPSPerClient.LimitValue 50 \
    --Domain.Routes.0.Enable True \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Key X-Route-Header \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Value route-value \
    --Domain.Routes.0.Extension.HeadersHandler.RequestHeadersToAdd.0.Action OVERWRITE_IF_EXISTS_OR_ADD \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Key X-Route-Response \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Value route-resp-value \
    --Domain.Routes.0.Extension.HeadersHandler.ResponseHeadersToAdd.0.Action OVERWRITE_IF_EXISTS_OR_ADD
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
            "Message": "域名尚未备案",
            "Status": "FAIL"
        },
        "InternalAccount": {
            "Message": "not an internal domain, skipped",
            "Status": "SKIPPED"
        },
        "Ownership": {
            "Message": "domain ownership verification failed for ab7.woyaodaguaishou1.cn",
            "OwnershipVerification": {
                "DnsVerification": [
                    {
                        "RecordType": "TXT",
                        "RecordValue": "*****************-7ezncwdd421446",
                        "Subdomain": "_cloudbase-challenge.********************.cn"
                    }
                ],
                "Domain": "********************.cn"
            },
            "Status": "FAIL"
        },
        "Passed": false,
        "Quota": {
            "Message": "quota check passed",
            "Status": "PASS"
        },
        "RouteConflict": {
            "Message": "no route conflict",
            "Status": "PASS"
        },
        "RequestId": "b4912cfe-d26d-4cc0-bb55-eb47cee7fdcb"
    }
}
```

