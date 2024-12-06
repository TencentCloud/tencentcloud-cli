**Example 1: 查询证书ddos云资源部署实例列表**

查询证书ddos云资源部署实例列表

Input: 

```
tccli ssl DescribeHostDdosInstanceList --cli-unfold-argument  \
    --ResourceType ddos \
    --IsCache 1 \
    --CertificateId jk****j \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "www.zrh.com",
                "InstanceId": "ins-*******",
                "Protocol": "https",
                "CertId": "h****KL",
                "VirtualPort": "80"
            }
        ],
        "TotalCount": 1,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

