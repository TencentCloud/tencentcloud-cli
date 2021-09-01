**Example 1: 批量创建子网**



Input: 

```
tccli vpc CreateSubnets --cli-unfold-argument  \
    --VpcId vpc-6v2ht8q5 \
    --Subnets.0.CidrBlock 10.4.14.0/24 \
    --Subnets.0.SubnetName t1 \
    --Subnets.0.Zone ap-guangzhou-2 \
    --Subnets.1.CidrBlock 10.4.15.0/24 \
    --Subnets.1.SubnetName t2 \
    --Subnets.1.Zone ap-guangzhou-3 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "NetworkAclId": "xx",
                "RouteTableId": "xx",
                "VpcId": "xx",
                "EnableBroadcast": false,
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
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "CreatedTime": "xx",
                "SubnetId": "xx",
                "CidrBlock": "xx",
                "IsDefault": false
            },
            {
                "NetworkAclId": "xx",
                "IsRemoteVpcSnat": true,
                "TotalIpAddressCount": 253,
                "VpcId": "vpc-6v2ht8q5",
                "SubnetId": "subnet-f84xsjpa",
                "SubnetName": "t2",
                "CidrBlock": "10.4.15.0/24",
                "Ipv6CidrBlock": "xx",
                "IsDefault": false,
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou-3",
                "RouteTableId": "rtb-3ryrwzuu",
                "CreatedTime": "2018-11-29 19:16:45",
                "AvailableIpAddressCount": 253,
                "CdcId": "cluster-1234rdet",
                "IsCdcSubnet": 0,
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ]
            }
        ],
        "RequestId": "158ac65e-d504-42f6-baac-b716f5855254"
    }
}
```

