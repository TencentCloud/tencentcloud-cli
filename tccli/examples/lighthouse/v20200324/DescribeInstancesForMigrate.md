**Example 1: 指定在线临时实例ID查询**



Input: 

```
tccli lighthouse DescribeInstancesForMigrate --cli-unfold-argument  \
    --InstanceIds lhmins-4r4pvtbg \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceSet": [
            {
                "InstanceId": "lhmins-4r4pvtbg",
                "OriginInstanceId": "ins-mt5cxaxs",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-issyxx1m"
                },
                "CPU": 2,
                "Memory": 8,
                "Uuid": "dab281fb-dd6c-4b3f-ae30-36da354ac20e",
                "OsType": "WINDOWS",
                "InstanceType": "S2.MEDIUM8",
                "PublicIpAddresses": [
                    "10.1.128.14"
                ],
                "InstanceState": "RUNNING",
                "LatestOperation": "CreateBlueprintForMigrate",
                "LatestOperationState": "SUCCESS",
                "LatestOperationRequestId": "e4907750-3aa0-488d-a146-aeab66513441"
            }
        ],
        "RequestId": "242ff914-0de6-4462-b5fc-6e4c88aa4b07"
    }
}
```

