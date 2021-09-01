**Example 1: 查询杭州一区的默认子网**



Input: 

```
tccli ecm DescribeDefaultSubnet --cli-unfold-argument  \
    --EcmRegion ap-hangzhou-ecm \
    --Zone ap-hangzhou-ecm-1
```

Output: 
```
{
    "Response": {
        "Subnet": {
            "NetworkAclId": "",
            "RouteTableId": "rtb-8dq69epw",
            "VpcId": "vpc-07kqm4uj",
            "EnableBroadcast": false,
            "Zone": "ap-hangzhou-ecm-1",
            "Ipv6CidrBlock": "",
            "Region": "ap-hangzhou-ecm",
            "SubnetName": "Default-Subnet",
            "AvailableIpAddressCount": 4090,
            "IsRemoteVpcSnat": false,
            "SubnetId": "subnet-68hie5i6",
            "InstanceCount": 2,
            "VpcCidrBlock": "172.16.0.0/16",
            "TagSet": null,
            "CreatedTime": "2020-08-12 10:44:56",
            "ZoneName": "杭州一区",
            "CidrBlock": "172.16.0.0/20",
            "IsDefault": true,
            "VpcIpv6CidrBlock": ""
        },
        "RequestId": "7d67dea3-c6ff-45ca-aa5a-477cfae6697f"
    }
}
```

