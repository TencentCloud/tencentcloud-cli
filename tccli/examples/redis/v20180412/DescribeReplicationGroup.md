**Example 1: 请求示例**



Input: 

```
tccli redis DescribeReplicationGroup --cli-unfold-argument  \
    --SearchKey xx \
    --Limit 20 \
    --GroupId xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Groups": [
            {
                "Status": 0,
                "Remark": "xx",
                "InstanceCount": 1,
                "Instances": [
                    {
                        "Engine": "xx",
                        "Vip6": "xx",
                        "UpdateTime": "xx",
                        "VpcID": 16770550,
                        "InstanceId": "xx",
                        "RedisShardSize": 1024,
                        "RegionId": 1,
                        "RedisShardNum": 1,
                        "Status": 1,
                        "Vip": "xx",
                        "DiskSize": 0,
                        "CreateTime": "xx",
                        "ProductType": 9,
                        "AppId": 0,
                        "Role": "xx",
                        "VPort": 6379,
                        "ZoneId": 1,
                        "InstanceName": "xx",
                        "RedisReplicasNum": 1,
                        "GrocerySysId": 1000259
                    }
                ],
                "RegionId": 1,
                "GroupName": "xx",
                "AppId": 0,
                "GroupId": "xx"
            }
        ]
    }
}
```

