**Example 1: 查询轻量级实例列表**



Input: 

```
tccli cynosdb DescribeLightInstances --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --OrderBy abc \
    --OrderByType abc \
    --Filters.0.Names abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Filters.0.Name abc \
    --Filters.0.Operator abc \
    --DbType abc \
    --Status abc \
    --InstanceIds abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceSet": [
            {
                "AppId": 0,
                "Zone": "abc",
                "ProjectId": 0,
                "InstanceId": "abc",
                "InstanceName": "abc",
                "Status": "abc",
                "ClusterId": "abc",
                "ClusterName": "abc",
                "StatusDesc": "abc",
                "Vip": "abc",
                "Vport": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

