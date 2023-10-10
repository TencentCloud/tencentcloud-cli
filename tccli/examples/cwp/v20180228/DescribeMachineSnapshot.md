**Example 1: 漏洞修护-查询主机创建的快照**



Input: 

```
tccli cwp DescribeMachineSnapshot --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Quuids djskldjksld \
    --Type 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreateTime": "2021-04-06 17:25:57",
                "DiskId": "disk-fc19gd5w",
                "HostIp": "10.104.9.143",
                "HostName": "win_poc测试(129.204.117.208)",
                "InstanceId": "ins-lamp8810",
                "Quuid": "b9b4f569-22fc-4a90-8d7f-c9e45349cd5b",
                "RegionId": 1,
                "SnapshotId": "snap-fav9fuhd",
                "SnapshotName": "漏洞修复_openssl拒绝服务漏洞"
            }
        ],
        "RequestId": "67060fe1-d34e-468f-8f22-d00105304496",
        "TotalCount": 1,
        "SnapshotCheck": true
    }
}
```

