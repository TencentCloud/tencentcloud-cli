**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstances --cli-unfold-argument  \
    --Status 0 1 2 \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RedisShardSize": 16384,
                "RedisShardNum": 1,
                "MonitorVersion": "xx",
                "AutoRenewFlag": 0,
                "InstanceTitle": "xx",
                "ProductType": "xx",
                "PriceId": 1006984,
                "Type": 13,
                "Status": 2,
                "Vip6": "xx",
                "VpcId": 16770892,
                "ClientLimit": 0,
                "Tags": [
                    "xx"
                ],
                "InstanceId": "xx",
                "ClientLimitMax": 40000,
                "RegionId": 1,
                "SubStatus": 19,
                "SlaveReadWeight": 0,
                "OfflineTime": "xx",
                "SubnetId": 2061142,
                "NodeSet": [
                    {
                        "ZoneName": "xx",
                        "NodeType": 0,
                        "NodeId": 0,
                        "ZoneId": 1
                    }
                ],
                "Engine": "xx",
                "InstanceTags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ProjectId": 0,
                "Region": "xx",
                "DeadlineTime": "xx",
                "CloseTime": "xx",
                "ZoneId": 100002,
                "PasswordFree": 0,
                "DiskSize": 50000,
                "NoAuth": false,
                "Appid": 251200002,
                "WanIp": "xx",
                "NetLimit": 0,
                "InstanceName": "xx",
                "Createtime": "xx",
                "UniqVpcId": "xx",
                "DtsStatus": 0,
                "ProjectName": "xx",
                "BillingMode": 1,
                "RemainBandwidthDuration": "xx",
                "ReadOnly": 0,
                "UniqSubnetId": "xx",
                "ClientLimitMin": 10000,
                "RedisReplicasNum": 1,
                "Port": 6379,
                "Size": 0.0
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

