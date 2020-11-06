**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "Appid": 1251006373,
                "AutoRenewFlag": 0,
                "BillingMode": 0,
                "CloseTime": "0000-00-00 00:00:00",
                "Createtime": "0000-00-00 00:00:00",
                "DeadlineTime": "0000-00-00 00:00:00",
                "Engine": "社区版Redis",
                "InstanceId": "crs-7ponppu3",
                "InstanceName": "crs-7ponppu3",
                "InstanceNode": [],
                "InstanceTags": [
                    {
                        "TagKey": "aaa",
                        "TagValue": "111"
                    }
                ],
                "InstanceTitle": "实例运行中",
                "OfflineTime": "",
                "Port": 6379,
                "PriceId": 13380,
                "ProductType": "Redis4.0集群版",
                "ProjectId": 0,
                "RedisReplicasNum": 1,
                "RedisShardNum": 3,
                "RedisShardSize": 1024,
                "RegionId": 1,
                "Size": 3072,
                "SizeUsed": 0,
                "SlaveReadWeight": 0,
                "Status": 2,
                "SubStatus": 19,
                "SubnetId": 0,
                "Tags": [],
                "Type": 7,
                "UniqSubnetId": "",
                "UniqVpcId": "",
                "VpcId": 0,
                "WanIp": "10.66.153.160",
                "ZoneId": 100002
            }
        ],
        "RequestId": "e3d683fc-f2ff-43c9-980d-fae7a1166abc",
        "TotalCount": 1
    }
}
```

