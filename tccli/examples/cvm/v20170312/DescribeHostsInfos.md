**Example 1: DescribeHostsInfos**

本接口 (DescribeHostsInfos) 用于查询母机信息。
查询并返回超卖售卖池母机信息
只允许eks调用，会对UIN进行白名单校验。

Input: 

```
tccli cvm DescribeHostsInfos --cli-unfold-argument  \
    --Filters.0.Name pool \
    --Filters.0.Values qcloud \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "HostInfoSet": [
            {
                "Placement": {
                    "Pool": "qcloud",
                    "Zone": "ap-guangzhou-2"
                },
                "HostType": "M1",
                "HostResource": {
                    "CpuTotal": 2400,
                    "CpuAvailable": 2400,
                    "MemTotal": 122880,
                    "MemAvailable": 122880,
                    "DiskTotal": 1200,
                    "DiskAvailable": 1200,
                    "NodeQuotaTotal": "[1200, 1200]",
                    "NodeQuota": "[1200, 1200]"
                }
            }
        ],
        "RequestId": "92c9b8e4-bc5e-40fe-ae29-cace062a0d4b"
    }
}
```

