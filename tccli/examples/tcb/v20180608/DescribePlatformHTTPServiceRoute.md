**Example 1: 平台下域名路由信息**



Input: 

```
tccli tcb DescribePlatformHTTPServiceRoute --cli-unfold-argument  \
    --PlatformId pf-************ \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "AccessType": "EO",
                "CertId": "afCtB6as",
                "Cname": "3usgm1731e24.****************hou.cn.eo.dnse5.com",
                "CreateTime": "2026-09-09T16:07:24+08:00",
                "DNSStatus": "INVALID",
                "Domain": "*.rgw.***************.cn",
                "DomainType": "HTTPSERVICE",
                "Enable": true,
                "IsDefault": false,
                "PlatformCnameDNSStatus": "INVALID",
                "Protocol": "HTTP_AND_HTTPS",
                "Status": "SUCCESS",
                "UpdateTime": "2026-09-09T16:15:59+08:00"
            }
        ],
        "OriginDomain": "***************.*********-expr.tencentcloudbase.com",
        "TotalCount": 1,
        "RequestId": "c989cae9-a075-4deb-8f99-af7189b9c5e0"
    }
}
```

