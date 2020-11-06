**Example 1: 创建子网**



Input: 

```
tccli ecm CreateSubnet --cli-unfold-argument  \
    --VpcId vpc-ila64qtl \
    --SubnetName subnet_test \
    --CidrBlock 10.0.1.0/24 \
    --Zone ap-hangzhou-ecm-1 \
    --Tags.0.Key city \
    --Tags.0.Value hangzhou \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "Subnet": {
            "NetworkAclId": "",
            "RouteTableId": "",
            "VpcId": "vpc-ila64qtl",
            "EnableBroadcast": false,
            "Zone": "ap-hangzhou-ecm-1",
            "Ipv6CidrBlock": "",
            "Region": "ap-hangzhou-ecm",
            "SubnetName": "subnet_test",
            "AvailableIpAddressCount": 253,
            "IsRemoteVpcSnat": false,
            "SubnetId": "subnet-heaa1hzo",
            "InstanceCount": 0,
            "VpcCidrBlock": "10.0.0.0/16",
            "TagSet": [
                {
                    "Value": "hangzhou",
                    "Key": "city"
                }
            ],
            "CreatedTime": "2020-08-14 10:38:40",
            "ZoneName": "杭州一区",
            "CidrBlock": "10.0.1.0/24",
            "IsDefault": false,
            "VpcIpv6CidrBlock": ""
        },
        "RequestId": "d0c21b3b-4c46-4ac3-a6ad-576303682731"
    }
}
```

