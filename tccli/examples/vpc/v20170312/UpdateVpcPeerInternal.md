**Example 1: 更新vpc peer**



Input: 

```
tccli vpc UpdateVpcPeerInternal --cli-unfold-argument  \
    --VpcPeerRequestSet.0.VpcPeerId 2 \
    --VpcPeerRequestSet.0.Owner 251198225 \
    --VpcPeerRequestSet.0.State 0 \
    --VpcPeerRequestSet.0.Name 11 \
    --VpcPeerRequestSet.0.Bandwidth 0 \
    --VpcPeerRequestSet.0.OwedFlag 0 \
    --VpcPeerRequestSet.0.VirtualSafeGroupIp 1.2.3.5 \
    --VpcPeerRequestSet.0.NewAfcFlag 1
```

Output: 
```
{
    "Response": {
        "UpdatePeerSet": [
            {
                "SrcVpcSubnet": "172.16.0.0",
                "DestVpcId": 76644,
                "PublishDockerCidrFlag": 0,
                "OldDestVpcSubnet": "10.0.0.0",
                "OldNewAfcFlag": 0,
                "OldVirtualSafeGroupIp": "0.0.0.0",
                "UniqueDestVpcId": "vpc-n05ss3vl",
                "OldLocalBandwidth": 0,
                "OldName": "DDDD",
                "SrcOwner": "251198225",
                "Owner": "251198225",
                "OldZoneVpcPeerFlag": 0,
                "OldOwedFlag": 0,
                "OldLastState": 0,
                "SrcVpcId": 78257,
                "State": 1,
                "OldSrcVpcIntMask": 16,
                "LocalBandwidth": 0,
                "DestVpcIntMask": 16,
                "DestOwner": "251198225",
                "Type": 0,
                "LastState": 0,
                "OldDestExpireTime": "2021-12-31 19:41:49",
                "OldDestVpcIntMask": 16,
                "OldSrcVpcSubnet": "172.16.0.0",
                "DestRegion": 0,
                "OldState": 1,
                "OldSrcExpireTime": "2021-12-31 19:41:49",
                "WanOutLimit": 0,
                "SrcViewFlag": 1,
                "OldDestViewFlag": 1,
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
                "Bandwidth": 0,
                "UniqueVpcPeerId": "pcx-fh7xs34s",
                "OldPublishDockerCidrFlag": 0,
                "AfcVpcPeerGlobalId": 0,
                "SrcVpcIntMask": 16,
                "DestViewFlag": 1,
                "OldBandwidth": 0,
                "OldSrcViewFlag": 1,
                "OldWanOutLimit": 0,
                "DestExpireTime": "2021-12-31 19:41:49"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

