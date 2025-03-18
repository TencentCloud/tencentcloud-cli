**Example 1: 获取主机安全服务列表**

获取主机安全服务列表

Input: 

```
tccli ssl DescribeHostWafInstanceList --cli-unfold-argument  \
    --CertificateId T****j \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --OldCertificateId Yj****k
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "hh**.com",
                "CertId": "K***hh",
                "Keepalive": 1
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

