**Example 1: 请求示例**

查询单个复制组信息

Input: 

```
tccli redis DescribeReplicationGroup --cli-unfold-argument  \
    --Limit 20 \
    --GroupId crs-rpl-lkgv**** \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "65e950b9-78e8-49b1-9200-0e62a1925557",
        "Groups": [
            {
                "Status": 37,
                "Remark": "测试复制组",
                "InstanceCount": 1,
                "Instances": [
                    {
                        "Engine": "社区版Redis",
                        "Vip6": "",
                        "UpdateTime": "2022-11-02 15:04:05",
                        "VpcID": 16770550,
                        "InstanceId": "crs-9c36****",
                        "RedisShardSize": 1024,
                        "RegionId": 1,
                        "RedisShardNum": 1,
                        "Status": 1,
                        "Vip": "10.0.4.42",
                        "DiskSize": 0,
                        "CreateTime": "2022-11-02 15:04:05",
                        "ProductType": 9,
                        "AppId": 0,
                        "Role": "rw",
                        "VPort": 6379,
                        "ZoneId": 1,
                        "InstanceName": "crs-test",
                        "RedisReplicasNum": 1,
                        "GrocerySysId": 1000259
                    }
                ],
                "RegionId": 1,
                "GroupName": "crs-ben-test",
                "AppId": 0,
                "GroupId": "crs-rpl-lkgv****"
            }
        ]
    }
}
```

