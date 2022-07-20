**Example 1: 创建子网**



Input: 

```
tccli vpc CreateSubnet --cli-unfold-argument  \
    --SubnetName TestSubnet \
    --VpcId vpc-m3ul053f \
    --CidrBlock 10.8.0.0/16 \
    --Zone ap-guangzhou-1 \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "Subnet": {
            "NetworkAclId": "xx",
            "RouteTableId": "xx",
            "VpcId": "xx",
            "EnableBroadcast": true,
            "Zone": "xx",
            "IsCdcSubnet": 0,
            "Ipv6CidrBlock": "xx",
            "CdcId": "xx",
            "AvailableIpAddressCount": 1,
            "IsRemoteVpcSnat": true,
            "SubnetName": "xx",
            "TotalIpAddressCount": 1,
            "TagSet": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "CreatedTime": "xx",
            "SubnetId": "xx",
            "CidrBlock": "xx",
            "IsDefault": false
        },
        "RequestId": "xx"
    }
}
```

