**Example 1: 创建VPC**

创建VPC

Input: 

```
tccli vpc CreateVpc --cli-unfold-argument  \
    --VpcName TestVPC \
    --CidrBlock 10.8.0.0/16 \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "RequestId": "0a74f7fe-0cfe-4bc7-b1d2-6575168d7a44",
        "Vpc": {
            "VpcId": "vpc-2ln96dly",
            "DomainName": "TEST",
            "Ipv6CidrBlock": "2001::85b:3c51:f5ff:ffdb",
            "EnableDhcp": true,
            "DnsServerSet": [
                "183.60.82.98",
                "183.60.83.1"
            ],
            "EnableMulticast": false,
            "VpcName": "TEST",
            "AssistantCidrSet": [
                {
                    "SubnetSet": [
                        {
                            "NetworkAclId": "acl-n8w3ppae",
                            "RouteTableId": "rtb-57ruphgv",
                            "VpcId": "vpc-lrrlomg7",
                            "EnableBroadcast": true,
                            "Zone": "ap-guangzhou-1",
                            "IsCdcSubnet": 0,
                            "Ipv6CidrBlock": "2001::85b:3c51:f5ff:ffda",
                            "CdcId": "cluster-gbo27yc4",
                            "AvailableIpAddressCount": 1,
                            "IsRemoteVpcSnat": true,
                            "SubnetName": "TEST",
                            "TotalIpAddressCount": 1,
                            "CreatedTime": "2020-09-18 19:46:07",
                            "SubnetId": "subnet-p9oa3yo7",
                            "CidrBlock": "10.0.0.0/16",
                            "TagSet": [
                                {
                                    "Value": "TEST",
                                    "Key": "TEST"
                                }
                            ],
                            "IsDefault": true
                        }
                    ],
                    "VpcId": "vpc-lrrlomg7",
                    "CidrBlock": "10.0.0.0/16",
                    "AssistantType": 0
                }
            ],
            "TagSet": [
                {
                    "Value": "TEST",
                    "Key": "TESt"
                }
            ],
            "DhcpOptionsId": "dopt-058pu85z",
            "CreatedTime": "0000-00-00 00:00:00",
            "CidrBlock": "10.0.0.0/16",
            "IsDefault": false
        }
    }
}
```

