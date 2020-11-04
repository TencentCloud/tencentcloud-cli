**Example 1: 获取NAT网关列表**



Input: 

```
tccli bmvpc DescribeNatGateways --cli-unfold-argument  \
    --VpcId vpc-mi51u7gs
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "NatGatewayInfoSet": [
            {
                "NatId": "nat-2duawe5v",
                "NatName": "测试",
                "VpcId": "vpc-mi51u7gs",
                "VpcName": "test网络",
                "ProductionStatus": 1,
                "Eips": [
                    "139.199.40.18",
                    "139.199.40.53"
                ],
                "Zone": "ap-guangzhou-blsh3-1",
                "MaxConcurrent": 1000000,
                "Type": "small",
                "Exclusive": 0,
                "ForwardMode": 0,
                "VpcCidrBlock": "192.168.0.0/16",
                "CreateTime": "2018-10-18 11:04:12"
            },
            {
                "NatId": "nat-1tw1oc0t",
                "NatName": "test",
                "VpcId": "vpc-mi51u7gs",
                "VpcName": "test网络",
                "ProductionStatus": 1,
                "Eips": [
                    "139.199.40.17"
                ],
                "Zone": "ap-guangzhou-blsh3-1",
                "MaxConcurrent": 3000000,
                "Type": "middle",
                "Exclusive": 0,
                "ForwardMode": 0,
                "VpcCidrBlock": "192.168.0.0/16",
                "CreateTime": "2018-10-19 17:17:26"
            }
        ],
        "RequestId": "182fc08f-016a-4a03-b4a7-d92d88fb81ab"
    }
}
```

