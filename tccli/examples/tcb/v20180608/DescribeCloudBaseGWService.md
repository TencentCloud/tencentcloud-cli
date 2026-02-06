**Example 1: DescribeCloudBaseGWService示例**



Input: 

```
tccli tcb DescribeCloudBaseGWService --cli-unfold-argument  \
    --ServiceId “aa”
```

Output: 
```
{
    "Response": {
        "ServiceSet": [
            {
                "Status": 0,
                "EnableRegion": true,
                "Domain": "www.domain.com",
                "OpenTime": 1,
                "ForceHttps": true,
                "IcpForbidStatus": 0,
                "Cname": "www.cname.com",
                "CertId": "certid",
                "ServiceId": "envid",
                "IsPreempted": true,
                "UnionStatus": 0,
                "CustomRoutingRules": "{route}",
                "CnameStatus": 0
            }
        ],
        "CustomRoutingRules": "{route}",
        "EnableService": true,
        "RequestId": "requestid",
        "EnableUnion": true,
        "EnableCheckAcrossDomain": true,
        "DefaultDomain": "envid-appid.app.tcloudbase.com",
        "OriginDomain": ".app-in.tencentcloudbase.com"
    }
}
```

