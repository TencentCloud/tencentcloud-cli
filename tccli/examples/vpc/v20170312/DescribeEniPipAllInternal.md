**Example 1: 用于获取弹性网卡的信息**



Input: 

```
tccli vpc DescribeEniPipAllInternal --cli-unfold-argument  \
    --Limit 100 \
    --UniqueEniId eniid \
    --VpcId 1 \
    --EniId 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "EniPipSet": [
            {
                "VpcId": 81292,
                "EniId": 1869306,
                "Description": "",
                "UniqueVpcId": "vpc-7f2w7dl7",
                "VpcDefaultFlag": 0,
                "VpcSubnet": "10.0.0.0",
                "PrivateIp": "10.0.0.2",
                "HavIpFlag": 0,
                "VpcName": "new_test",
                "Owner": "251197522",
                "CreateTime": "2021-03-31 17:05:58",
                "VpcIntMask": 16,
                "UniqueEniId": "eni-kqnhkoxz",
                "Eni": {
                    "VpcId": 81292,
                    "EniId": 1869306,
                    "UniqueVpcId": "vpc-7f2w7dl7",
                    "TrunkingFlag": 0,
                    "SubnetId": 1991149,
                    "UniqueSubnetId": "subnet-fjfixflc",
                    "Owner": "251197522",
                    "UniqueEniId": "eni-kqnhkoxz",
                    "BFlushSubEniHavip": 0,
                    "State": 1,
                    "BusinessOwner": "",
                    "Type": 0,
                    "Description": "",
                    "Business": "",
                    "Mac": "20:90:6F:45:52:00",
                    "TagProto": "vlan",
                    "CreateTime": "2021-03-31 17:05:58",
                    "Name": "test_eni",
                    "ArpLearningFlag": 1,
                    "ElasticNetworkCardName": "veni_vFspeba8"
                },
                "EniPipId": 40563,
                "Mac": "20:90:6F:45:52:00",
                "VpcMask": "255.255.0.0",
                "DhcpIpFlag": 0,
                "State": 1,
                "WanIp": "0.0.0.0",
                "Type": 1,
                "BlockedFlag": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

