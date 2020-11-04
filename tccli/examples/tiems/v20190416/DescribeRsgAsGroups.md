**Example 1: 查询资源组的伸缩组信息**



Input: 

```
tccli tiems DescribeRsgAsGroups --cli-unfold-argument  \
    --Filters.0.Values rsg-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3d96e8c0-97a9-43a2-8268-99ff505fbd84",
        "RsgAsGroupSet": [
            {
                "Id": "asg-xxxxxxxx",
                "Region": "ap-beijing",
                "Zone": "ap-beijing-5",
                "Cluster": "ap-beijing",
                "RsgId": "rsg-xxxxxxxx",
                "Name": "rsg-xxxxxxxx",
                "MaxSize": 3,
                "MinSize": 0,
                "CreateTime": "2019-12-24T17:39:40+08:00",
                "UpdateTime": "2019-12-24T17:39:40+08:00",
                "Status": "Enabled",
                "InstanceType": "sv_tiems_instance_8c32g1t4",
                "InstanceCount": 1
            }
        ],
        "TotalCount": 1
    }
}
```

