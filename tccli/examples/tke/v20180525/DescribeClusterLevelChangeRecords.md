**Example 1: 查询集群变配记录**



Input: 

```
tccli tke DescribeClusterLevelChangeRecords --cli-unfold-argument  \
    --Limit 1 \
    --ClusterID xx \
    --EndAt xx \
    --StartAt xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Items": [
            {
                "Status": "xx",
                "EndedAt": "xx",
                "ClusterID": "xx",
                "TriggerType": "xx",
                "NewLevel": "xx",
                "OldLevel": "xx",
                "StartedAt": "xx",
                "Message": "xx",
                "ID": "xx"
            }
        ]
    }
}
```

