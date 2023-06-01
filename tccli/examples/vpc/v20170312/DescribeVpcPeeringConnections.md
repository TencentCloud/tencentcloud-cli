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
                "SourceVpcId": "vpc-ebmfbrg7",
                "PeeringConnectionId": "pcx-b050bu7c",
                "PeeringConnectionName": "andytesttong",
                "State": "PENDING",
                "IsNgw": false,
                "Bandwidth": 10,
                "SourceRegion": "ca",
                "DestinationRegion": "gz",
                "CreateTime": "2021-12-08 14:56:35",
                "AppId": 1255486055,
                "PeerAppId": 1254277469,
                "ChargeType": "POSTPAID_BY_DAY_MAX",
                "SourceUin": 100002840660,
                "DestinationUin": 100001332514,
                "QosLevel": "",
                "Type": "VPC_BM_PEER",
                "TagSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "c9f0e94c-3e0c-4d39-8155-fcf5ba13ec96"
    }
}
```

