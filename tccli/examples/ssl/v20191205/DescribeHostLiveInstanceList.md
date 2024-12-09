**Example 1: 查询证书live云资源部署实例列表**

查询证书live云资源部署实例列表

Input: 

```
tccli ssl DescribeHostLiveInstanceList --cli-unfold-argument  \
    --CertificateId yy****k \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --OldCertificateId P****jj
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "Domain": "ww.zrh.com",
                "CertId": "J***KL",
                "Status": 0
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

