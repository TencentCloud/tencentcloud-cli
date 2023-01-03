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
                "WanAddress": "xx",
                "RedisShardSize": 1024,
                "RedisShardNum": 3,
                "MonitorVersion": "xx",
                "UpgradeProxyVersion": "5.6.0",
                "InstanceTitle": "xx",
                "ProductType": "xx",
                "UpgradeRedisVersion": "6.2.5",
                "NoAuth": true,
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
                "AutoRenewFlag": 0,
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
                "DiskSize": 0,
                "Engine": "xx",
                "SizeUsed": 0.0,
                "InstanceTags": [
                    {
                        "TagKey": "tke-clusterId",
                        "TagValue": "cls-0kl4et00"
                    }
                ],
                "ProjectId": 0,
                "Region": "xx",
                "DeadlineTime": "2022-11-02 15:04:05",
                "CloseTime": "2022-11-10 15:04:06",
                "ZoneId": 100002,
                "PasswordFree": 0,
                "Appid": 1251006373,
                "WanIp": "xx",
                "NetLimit": 480,
                "InstanceName": "crs-test",
                "Createtime": "2022-08-02 16:27:17",
                "ClientLimit": 10000,
                "PolarisServer": "xx",
                "CurrentRedisVersion": "5.2.0",
                "CurrentProxyVersion": "5.6.0",
                "UniqVpcId": "vpc-fk33jsf4****",
                "DtsStatus": 0,
                "ProjectName": "xx",
                "BillingMode": 1,
                "RemainBandwidthDuration": "xx",
                "ReadOnly": 0,
                "UniqSubnetId": "subnet-6qotc71w",
                "ClientLimitMin": 0,
                "RedisReplicasNum": 1,
                "Port": 6379,
                "Size": 0.0
            }
        ],
        "TotalCount": 1,
        "RequestId": "65e950b9-78e8-49b1-9200-0e62a1925559"
    }
}
```

