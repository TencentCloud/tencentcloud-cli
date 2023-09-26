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
        "TotalCount": 0,
        "PeerConnectionSet": [
            {
                "SourceVpcId": "abc",
                "PeerVpcId": "abc",
                "PeeringConnectionId": "abc",
                "PeeringConnectionName": "abc",
                "State": "abc",
                "IsNgw": true,
                "Bandwidth": 0,
                "SourceRegion": "abc",
                "DestinationRegion": "abc",
                "CreateTime": "abc",
                "AppId": 0,
                "PeerAppId": 0,
                "ChargeType": "abc",
                "SourceUin": 0,
                "DestinationUin": 0,
                "TagSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "QosLevel": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

