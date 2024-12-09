**Example 1: 查询证书ApiGateway云资源部署实例列表**

查询证书ApiGateway云资源部署实例列表

Input: 

```
tccli ssl DescribeHostApiGatewayInstanceList --cli-unfold-argument  \
    --CertificateId sg****j \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --ResourceType apigateway \
    --OldCertificateId sh**jj
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "ServiceId": "svc-******",
                "ServiceName": "zrh",
                "Domain": "www.zrh.com",
                "CertId": "hd***kl",
                "Protocol": "https"
            }
        ],
        "TotalCount": 1,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

