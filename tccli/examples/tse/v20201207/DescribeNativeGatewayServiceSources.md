**Example 1: 查询网关服务来源实例列表**



Input: 

```
tccli tse DescribeNativeGatewayServiceSources --cli-unfold-argument  \
    --SourceID ins-5ef8277d \
    --SourceName nacos-learn-prod \
    --OrderType AES \
    --Limit 1 \
    --SourceTypes TSE-Nacos \
    --OrderField SourceName \
    --Offset 1 \
    --GatewayID gateway-dde03567
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "GatewayID": "gateway-dde03567",
                "SourceID": "ins-5ef8277d",
                "SourceName": "nacos-learn-prod",
                "SourceType": "TSE-Nacos",
                "SourceInfo": {
                    "VpcInfo": {
                        "VpcID": "vpc-83p03121",
                        "SubnetID": "subnet-83p03121"
                    },
                    "Addresses": [
                        "10.0.0.1:8848"
                    ],
                    "Auth": {
                        "Username": "tse@tencentUser",
                        "Password": "tse@tencentPwd",
                        "AccessToken": ""
                    }
                },
                "CreateTime": "2024-12-09 18:11:19",
                "ModifyTime": "2024-12-09 18:11:19"
            }
        ],
        "RequestId": "0bcf3f70-550e-439d-81ee-7ebe260c2f06",
        "Total": 3
    }
}
```

