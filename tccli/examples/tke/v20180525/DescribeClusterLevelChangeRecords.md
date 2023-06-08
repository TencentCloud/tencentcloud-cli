**Example 1: 查询集群变配记录**

查询集群变配记录

Input: 

```
tccli tke DescribeClusterLevelChangeRecords --cli-unfold-argument  \
    --Limit 1 \
    --ClusterID cls-7t1eo183 \
    --EndAt 2022-07-11 17:45:02 \
    --StartAt 2022-07-11 16:45:02 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ID": "548",
                "ClusterID": "cls-7t1eo183",
                "Status": "success",
                "Message": "",
                "OldLevel": "L5",
                "NewLevel": "L20",
                "TriggerType": "manual",
                "CreatedAt": "2022-07-11 17:40:22",
                "StartedAt": "2022-07-11 17:40:22",
                "EndedAt": "2022-07-11 17:45:02"
            }
        ],
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886",
        "TotalCount": 1
    }
}
```

