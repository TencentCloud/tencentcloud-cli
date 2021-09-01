**Example 1: 查询数据订阅实例列表**



Input: 

```
tccli dts DescribeSubscribes --cli-unfold-argument  \
    --Status isolate \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Items": [
            {
                "ChannelId": "dts-channel-C9rS58f2rFx11ZEZ",
                "ConsumeStartTime": "2019-12-19 16:23:45",
                "CreateTime": "2019-12-20 14:59:07",
                "ExpireTime": "0000-00-00 00:00:00",
                "InstanceId": "cdb-forsubsc",
                "InstanceStatus": "running",
                "IsolateTime": "0000-00-00 00:00:00",
                "ModifyTime": "2019-12-20 18:06:26",
                "OfflineTime": "0000-00-00 00:00:00",
                "PayType": 1,
                "Product": "mysql",
                "Region": "ap-guangzhou",
                "SdkConsumedTime": "0000-00-00 00:00:00",
                "Status": "normal",
                "SubsStatus": "configured",
                "SubscribeId": "subs-58zcu8bax0",
                "SubscribeName": "测试实例",
                "UniqSubnetId": "subnet-4p1hpsj8",
                "UniqVpcId": "vpc-fbg8gh1j",
                "Vip": "192.168.1.143",
                "Vport": 7507
            }
        ],
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

