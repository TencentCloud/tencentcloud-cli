**Example 1: 仅修改辅助CIDR**

添加辅助CIDR：172.16.1.0/24。

Input: 

```
tccli vpc ModifyAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-nswq8wkq \
    --NewCidrBlocks 172.16.0.0/24
```

Output: 
```
{
    "Response": {
        "AssistantCidrSet": [
            {
                "VpcId": "vpc-nswq8wkq",
                "CidrBlock": "172.16.0.0/24",
                "AssistantType": 0,
                "SubnetSet": [
                    {
                        "VpcId": "vpc-nswq8wkq",
                        "SubnetId": "subnet-12345678",
                        "SubnetName": "demo",
                        "CidrBlock": "10.0.4.0/24",
                        "Ipv6CidrBlock": "",
                        "IsDefault": false,
                        "IsRemoteVpcSnat": false,
                        "EnableBroadcast": false,
                        "Zone": "ap-guangzhou-2",
                        "RouteTableId": "rtb-pnpcflil",
                        "NetworkAclId": "",
                        "TotalIpAddressCount": "253",
                        "AvailableIpAddressCount": "253",
                        "CreatedTime": "2020-06-08 10:00:00",
                        "TagSet": []
                    }
                ]
            }
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

**Example 2: 修改（添加和删除）辅助CIDR**

添加辅助CIDR：172.16.1.0/24，同时删除辅助CIDR：172.16.0.0/24。

Input: 

```
tccli vpc ModifyAssistantCidr --cli-unfold-argument  \
    --VpcId vpc-pnpcflil \
    --OldCidrBlocks 172.16.0.0/24 \
    --NewCidrBlocks 172.16.1.0/24
```

Output: 
```
{
    "Response": {
        "AssistantCidrSet": [
            {
                "VpcId": "vpc-pnpcflil",
                "CidrBlock": "172.16.1.0/24",
                "AssistantType": 0,
                "SubnetSet": [
                    {
                        "VpcId": "vpc-pnpcflil",
                        "SubnetId": "subnet-hj3he929",
                        "SubnetName": "demo",
                        "CidrBlock": "1172.16.1.0/24",
                        "Ipv6CidrBlock": "",
                        "IsDefault": false,
                        "IsRemoteVpcSnat": false,
                        "EnableBroadcast": false,
                        "Zone": "ap-guangzhou-2",
                        "RouteTableId": "rtb-h0fk8lfc",
                        "NetworkAclId": "",
                        "TotalIpAddressCount": "253",
                        "AvailableIpAddressCount": "253",
                        "CreatedTime": "2020-06-08 10:00:00",
                        "TagSet": []
                    }
                ]
            }
        ],
        "RequestId": "6aa316a4-07d2-4355-b87d-40b7f22972b0"
    }
}
```

