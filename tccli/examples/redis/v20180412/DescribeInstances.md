**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstances --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RedisShardSize": 1024,
                "RedisShardNum": 3,
                "MonitorVersion": "xx",
                "AutoRenewFlag": 0,
                "InstanceTitle": "xx",
                "ProductType": "xx",
                "PriceId": 13380,
                "Type": 7,
                "Status": 2,
                "Vip6": "xx",
                "VpcId": 0,
                "InstanceNode": [
                    {
                        "InstanceClusterNode": [
                            {
                                "Status": 0,
                                "Name": "xx",
                                "Keys": 0,
                                "Storage": 0,
                                "StorageSlope": 0.0,
                                "QpsSlope": 0.0,
                                "Connected": 0,
                                "RunId": "xx",
                                "DownTime": "xx",
                                "Qps": 0,
                                "Slots": "xx",
                                "CreateTime": "xx",
                                "Role": 0
                            }
                        ],
                        "Id": 0
                    }
                ],
                "Tags": [
                    "xx"
                ],
                "InstanceId": "xx",
                "ClientLimitMax": 0,
                "RegionId": 1,
                "SubStatus": 19,
                "SlaveReadWeight": 0,
                "OfflineTime": "xx",
                "SubnetId": 0,
                "NodeSet": [
                    {
                        "ZoneName": "xx",
                        "NodeType": 0,
                        "NodeId": 0,
                        "ZoneId": 1
                    }
                ],
                "Engine": "xx",
                "SizeUsed": 0.0,
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
                "DiskSize": 0,
                "NoAuth": true,
                "Appid": 1251006373,
                "WanIp": "xx",
                "NetLimit": 0,
                "InstanceName": "xx",
                "Createtime": "xx",
                "ClientLimit": 0,
                "UniqVpcId": "xx",
                "DtsStatus": 0,
                "ProjectName": "xx",
                "BillingMode": 0,
                "RemainBandwidthDuration": "xx",
                "ReadOnly": 0,
                "UniqSubnetId": "xx",
                "ClientLimitMin": 0,
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

