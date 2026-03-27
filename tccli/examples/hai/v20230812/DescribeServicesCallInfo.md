**Example 1: DescribeServicesCallInfo**



Input: 

```
tccli hai DescribeServicesCallInfo --cli-unfold-argument  \
    --ServiceIds svc-fnay2k0u \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "CallInfoSet": [
            {
                "ApiKey": "55*f0c9f*77*1a0589a*0019960*59*7*3*4*c2*56*f*ec*d2f9*8475d83*dbc",
                "PublicEndpoint": "http://lb-*p**ypc*-4*xo*d*yk7ra1vsm.clb.bj-tencentclb.net",
                "ServiceId": "svc-fnay2k0u",
                "VpcEndpoint": "http://127.0.0.1"
            }
        ],
        "RequestId": "353df959-b901-47be-9da6-8c94f67cd061"
    }
}
```

