**Example 1: 查询高优路由表**

查询高优路由表

Input: 

```
tccli vpc DescribeHighPriorityRouteTables --cli-unfold-argument  \
    --HighPriorityRouteTableIds hprtb-hd4tl8cg \
    --NeedRouterInfo True
```

Output: 
```
{
    "Response": {
        "HighPriorityRouteTableSet": [
            {
                "CreatedTime": "2024-07-10 21:16:50",
                "HighPriorityRouteSet": [
                    {
                        "CdcId": "",
                        "CreatedTime": "2024-07-11 17:07:03",
                        "Description": "demo",
                        "DestinationCidrBlock": "172.20.0.0/18",
                        "GatewayId": "172.16.0.11",
                        "GatewayType": "NORMAL_CVM",
                        "HighPriorityRouteId": "hprti-hd4tl8cr",
                        "IsCdc": false,
                        "SubnetRouteAlgorithm": "ECMP_QUINTUPLE_HASH"
                    },
                    {
                        "CdcId": "",
                        "CreatedTime": "2024-07-11 17:14:14",
                        "Description": "demo",
                        "DestinationCidrBlock": "192.168.0.0/20",
                        "GatewayId": "172.16.0.11",
                        "GatewayType": "NORMAL_CVM",
                        "HighPriorityRouteId": "hprti-f9qln349",
                        "IsCdc": false,
                        "SubnetRouteAlgorithm": "ECMP_QUINTUPLE_HASH"
                    }
                ],
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg",
                "Name": "demo",
                "SubnetSet": [
                    "subnet-a9pjzfq0"
                ],
                "VpcId": "vpc-mcqaoy0f"
            }
        ],
        "RequestId": "98c77fa8-578c-4190-a613-43a4cd4ea7a0",
        "TotalCount": 1
    }
}
```

