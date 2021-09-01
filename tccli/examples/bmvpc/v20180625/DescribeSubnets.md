**Example 1: 查询子网列表**



Input: 

```
tccli bmvpc DescribeSubnets --cli-unfold-argument  \
    --SubnetIds subnet-jzc4ky5d
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "VpcId": "vpc-ajhuxpbc",
                "VpcName": "test_vpc33333333",
                "VpcCidrBlock": "10.27.0.0/16",
                "SubnetId": "subnet-d6tl3i45",
                "SubnetName": "test_sub2",
                "CidrBlock": "10.27.2.0/24",
                "Type": 0,
                "ZoneId": 1000100002,
                "Zone": "ap-guangzhoutest-blshw-1",
                "VpcZoneId": 1000100002,
                "VpcZone": "ap-guangzhoutest-blshw-1",
                "CpmNum": 1,
                "VlanId": 5,
                "DistributedFlag": 1,
                "DhcpEnable": 0,
                "DhcpServerIp": [],
                "IpReserve": 0,
                "AvailableIpNum": 249,
                "TotalIpNum": 253,
                "SubnetCreateTime": "2017-01-12 16:17:07",
                "IsSmartNic": 0,
                "BroadcastFlag": 0
            }
        ],
        "TotalCount": 69,
        "RequestId": "d6f18c72-704e-4205-8bf4-9b7bbc5257bd"
    }
}
```

