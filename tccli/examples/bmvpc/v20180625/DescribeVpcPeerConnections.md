**Example 1: 查询对等连接列表**



Input: 

```
tccli bmvpc DescribeVpcPeerConnections --cli-unfold-argument  \
    --Version 2018-06-25
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
        "TotalCount": 1,
        "VpcPeerConnectionSet": [
            {
                "VpcId": "vpc-3l4sx5zj",
                "PeerVpcId": "vpc-i4pt50rc",
                "AppId": "251001815",
                "PeerAppId": "251000873",
                "VpcPeerConnectionId": "pcx-l9nnly7y",
                "VpcPeerConnectionName": "ericxing-NotDelete-peer",
                "State": "available",
                "VpcZone": null,
                "PeerVpcZone": "1000100002",
                "DeleteFlag": 1,
                "CreateTime": "2018-04-23 11:02:54",
                "Uin": 100000005204,
                "PeerUin": 1307774067,
                "PeerType": 1,
                "Bandwidth": 10000,
                "PeerRegion": "sh_bm",
                "Region": "gz"
            }
        ]
    }
}
```

