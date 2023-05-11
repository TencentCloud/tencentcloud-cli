**Example 1: 批量创建子网**

批量创建子网

Input: 

```
tccli vpc CreateSubnets --cli-unfold-argument  \
    --VpcId vpc-6v2ht8q5 \
    --Subnets.0.CidrBlock 10.4.14.0/24 \
    --Subnets.0.SubnetName t1 \
    --Subnets.0.Zone ap-guangzhou-2 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "NetworkAclId": "acl-6v2ht8q5",
                "RouteTableId": "rtb-pwtiswpd",
                "VpcId": "vpc-6v2ht8q5",
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou-2",
                "IsCdcSubnet": 0,
                "Ipv6CidrBlock": "",
                "CdcId": "",
                "AvailableIpAddressCount": 1,
                "IsRemoteVpcSnat": true,
                "SubnetName": "t1",
                "TotalIpAddressCount": 1,
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "CreatedTime": "2023-03-29 14:32:17",
                "SubnetId": "subnet-5v5nrzz9",
                "CidrBlock": "10.4.14.0/24",
                "IsDefault": false
            }
        ],
        "RequestId": "158ac65e-d504-42f6-baac-b716f5855254"
    }
}
```

