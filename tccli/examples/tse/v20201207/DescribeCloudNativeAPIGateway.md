**Example 1: 测试获取云原生API网关基础信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGateway --cli-unfold-argument  \
    --GatewayId <GatewayId>
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": "Creating",
            "EnableCls": true,
            "TradeType": 0,
            "Name": "test",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "FeatureVersion": "xx",
            "VpcConfig": {
                "SubnetId": "xx",
                "VpcId": "xx"
            },
            "IsolateTime": "xx",
            "CurDeadline": "xx",
            "EnableInternet": true,
            "GatewayVersion": "2.4.1",
            "AutoRenewFlag": 0,
            "NodeConfig": {
                "Specification": "1c2g",
                "Number": 2
            },
            "EngineRegion": "xx",
            "GatewayId": "gateway-7bb4fcb0",
            "Type": "Kong",
            "CreateTime": "2021-09-09 11:52:30",
            "InternetMaxBandwidthOut": 1,
            "Description": "测试"
        },
        "RequestId": "0f2cc04f-0e03-4e70-8df8-c57288b04373"
    }
}
```

