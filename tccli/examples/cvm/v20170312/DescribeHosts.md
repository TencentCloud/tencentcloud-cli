**Example 1: 查询CDH实例列表**

查询一个或多个CDH实例的详细信息

Input: 

```
tccli cvm DescribeHosts --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-2 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HostSet": [
            {
                "Placement": {
                    "Zone": "ap-guangzhou-2",
                    "ProjectId": 0
                },
                "HostId": "host-ey16rkyg",
                "HostType": "HS1",
                "HostName": "bibibibib-111",
                "CageId": "",
                "HostChargeType": "PREPAID",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "CreatedTime": "2018-01-04T09:45:39Z",
                "ExpiredTime": "2025-05-04T09:45:42Z",
                "InstanceIds": [],
                "HostState": "RUNNING",
                "HostResource": {
                    "CpuTotal": 24,
                    "CpuAvailable": 24,
                    "MemTotal": 56.0,
                    "MemAvailable": 56.0,
                    "DiskTotal": 1200,
                    "DiskAvailable": 1200,
                    "DiskType": "LOCAL_BASIC"
                }
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

