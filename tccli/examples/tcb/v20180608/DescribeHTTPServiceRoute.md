**Example 1: 查询路由信息**

通过域名过滤查询单个域名信息

Input: 

```
tccli tcb DescribeHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Filters.0.Name Domain \
    --Filters.0.Values xxx.***************.cn \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "AccessType": "DIRECT",
                "CertId": "VF******",
                "Cname": "xxx.*********************************.tencentcloudbase.com",
                "CreateTime": "2026-03-13T10:03:25+08:00",
                "DNSStatus": "INVALID",
                "Domain": "xxx.***************.cn",
                "DomainType": "HTTPSERVICE",
                "Enable": true,
                "IsDefault": false,
                "Protocol": "HTTP_AND_HTTPS",
                "Routes": [
                    {
                        "CreateTime": "2026-03-13T10:03:26+08:00",
                        "Enable": true,
                        "EnableAuth": false,
                        "EnablePathTransmission": false,
                        "EnableSafeDomain": false,
                        "Path": "/api/v1",
                        "PathRewrite": {},
                        "QPSPolicy": {
                            "QPSPerClient": {
                                "LimitBy": "ClientIP",
                                "LimitValue": 10
                            },
                            "QPSTotal": 100
                        },
                        "UpdateTime": "2026-03-13T10:03:26+08:00",
                        "UpstreamResourceName": "my-service",
                        "UpstreamResourceType": "CBR"
                    }
                ],
                "Status": "SUCCESS",
                "UpdateTime": "2026-03-13T10:03:25+08:00"
            }
        ],
        "OriginDomain": "***********************************************.tencentcloudbase.com",
        "TotalCount": 1,
        "RequestId": "9d15e1e6-24a7-4de5-9be0-d6470f32120b"
    }
}
```

