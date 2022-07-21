**Example 1: 查询vpc peer**



Input: 

```
tccli vpc DescribeVpcPeerInternal --cli-unfold-argument  \
    --Owner 1231231 \
    --Limit 100 \
    --UniqueVpcPeerId xxx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "VpcPeerSet": [
            {
                "SrcVpcSubnet": "172.16.0.0",
                "DestVpcId": 76644,
                "PublishDockerCidrFlag": 0,
                "UniqueDestVpcId": "vpc-n05ss3vl",
                "Bandwidth": 0,
                "SrcOwner": "251198225",
                "SrcVpcId": 78257,
                "DestExpireTime": "2021-12-31 19:41:49",
                "State": 1,
                "LocalBandwidth": 0,
                "DestVpcIntMask": 16,
                "DestOwner": "251198225",
                "Type": 0,
                "LastState": 0,
                "DestRegion": 0,
                "WanOutLimit": 0,
                "SrcViewFlag": 1,
                "DestViewFlag": 1,
                "ImageId": "",
                "DestVpcSubnet": "10.0.0.0",
                "CreateTime": "2021-12-31 19:41:49",
                "SrcExpireTime": "2021-12-31 19:41:49",
                "VpcPeerId": 26574,
                "ZoneVpcPeerFlag": 0,
                "UniqueSrcVpcId": "vpc-jmaywf6r",
                "OwedFlag": 0,
                "Name": "DDDD",
                "NfvFlag": 0,
                "VirtualSafeGroupIp": "0.0.0.0",
                "NewAfcFlag": 0,
                "SrcRegion": 0,
                "UniqueVpcPeerId": "pcx-fh7xs34s",
                "AfcVpcPeerGlobalId": 0,
                "SrcVpcIntMask": 16
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

