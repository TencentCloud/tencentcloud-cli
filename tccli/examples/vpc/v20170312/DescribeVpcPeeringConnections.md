**Example 1: 根据资源ID查询实例信息**

根据资源ID查询实例信息

Input: 

```
tccli vpc DescribeVpcPeeringConnections --cli-unfold-argument  \
    --PeeringConnectionIds pcx-test1234
```

Output: 
```
{
    "Response": {
        "PeerConnectionSet": [
            {
                "AppId": 1000001,
                "SourceUin": 1000001234,
                "SourceRegion": "gz",
                "SourceVpcId": "vpc-test1234",
                "PeerAppId": 1000001,
                "DestinationUin": 1000001234,
                "DestinationRegion": "gz",
                "PeerVpcId": "vpc-test4567",
                "DestinationVpcId": "vpc-test4567",
                "PeeringConnectionId": "pcx-test6789",
                "PeeringConnectionName": "测试用",
                "IsNgw": false,
                "CreateTime": "2024-11-14 11:58:54",
                "Bandwidth": 0,
                "Type": "VPC0",
                "State": "ACTIVE",
                "TagSet": [],
                "ChargeType": "POSTPAID_BY_DAY_MAX",
                "QosLevel": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "65def86e-3408-4bce-b520-37c12559b082"
    }
}
```

