**Example 1: 查询子网列表**

查询子网列表

Input: 

```
tccli ecm DescribeSubnets --cli-unfold-argument  \
    --Filters.0.Name subnet-id \
    --Filters.0.Values subnet-ae71tjp6 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "NetworkAclId": "",
                "ISPType": "CMCC",
                "RouteTableId": "rtb-cahjl2qq",
                "VpcId": "vpc-hqhu0suj",
                "EnableBroadcast": false,
                "Zone": "ap-hangzhou-ecm-1",
                "Ipv6CidrBlock": "",
                "Region": "ap-hangzhou-ecm",
                "SubnetName": "subnet_test",
                "AvailableIpAddressCount": 253,
                "IsRemoteVpcSnat": false,
                "SubnetId": "subnet-ae71tjp6",
                "InstanceCount": 0,
                "VpcCidrBlock": "192.168.0.0/18",
                "TagSet": [
                    {
                        "Value": "hangzhou",
                        "Key": "city"
                    }
                ],
                "CreatedTime": "2020-08-14 11:38:33",
                "ZoneName": "杭州一区",
                "CidrBlock": "192.168.1.0/24",
                "IsDefault": false,
                "VpcIpv6CidrBlock": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "6e863039-2a22-4a98-8577-93823b250674"
    }
}
```

