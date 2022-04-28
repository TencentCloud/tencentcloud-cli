**Example 1: 查看订阅配置详情**



Input: 

```
tccli dts DescribeSubscribeConf --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e
```

Output: 
```
{
    "Response": {
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
        "RequestId": "e580eac0-26c7-11ea-8e66-910ac0afe95e",
        "SdkConsumedTime": "0000-00-00 00:00:00",
        "SdkHost": "",
        "Status": "normal",
        "SubsStatus": "configured",
        "SubscribeId": "subs-58zcu8bax0",
        "SubscribeName": "测试实例",
        "SubscribeObjectType": 3,
        "SubscribeObjects": [
            {
                "DatabaseName": "dts",
                "ObjectsType": 0,
                "TableNames": null
            }
        ],
        "UniqSubnetId": "subnet-4p1hpsj8",
        "SubscribeVersion": "kafka",
        "UniqVpcId": "vpc-fbg8gh1j",
        "Vip": "192.168.1.143",
        "Vport": 7507,
        "AutoRenewFlag": 0,
        "Errors": [
            {
                "Message": ""
            }
        ],
        "Tags": [
            {
                "TagKey": "userDefineKey",
                "TagValue": "userDefineValue"
            }
        ]
    }
}
```

