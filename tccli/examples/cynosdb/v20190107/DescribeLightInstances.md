**Example 1: 查询轻量级实例列表**



Input: 

```
tccli cynosdb DescribeLightInstances --cli-unfold-argument  \
    --OrderBy xx \
    --Status xx \
    --DbType xx \
    --OrderByType xx \
    --Filters.0.Values cynosdbmysql-ins-bzkxxrmt \
    --Filters.0.Names xx \
    --Filters.0.ExactMatch True \
    --Filters.0.Name xx \
    --Offset 0 \
    --Limit 0 \
    --InstanceIds xx
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "Status": "xx",
                "Zone": "xx",
                "InstanceId": "xx",
                "ProjectId": 0,
                "ClusterId": "xx",
                "ClusterName": "xx",
                "AppId": 251007582,
                "StatusDesc": "xx",
                "InstanceName": "xx"
            },
            {
                "Status": "xx",
                "Zone": "xx",
                "InstanceId": "xx",
                "ProjectId": 0,
                "ClusterId": "xx",
                "ClusterName": "xx",
                "AppId": 251007582,
                "StatusDesc": "xx",
                "InstanceName": "xx"
            }
        ],
        "TotalCount": 26,
        "RequestId": "xx"
    }
}
```

