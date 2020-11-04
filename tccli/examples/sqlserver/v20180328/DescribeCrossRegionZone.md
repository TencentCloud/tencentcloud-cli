**Example 1: 查询备机的容灾地域和可用区**



Input: 

```
tccli sqlserver DescribeCrossRegionZone --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5
```

Output: 
```
{
    "Response": {
        "Region": "ap-guangzhou",
        "RequestId": "6579b707-5393-4579-ad10-349ea17b81e5",
        "Zone": "ap-guangzhou-2"
    }
}
```

