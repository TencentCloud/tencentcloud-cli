**Example 1: 查询高优路由表条目**

查询高优路由表条目

Input: 

```
tccli vpc DescribeHighPriorityRoutes --cli-unfold-argument  \
    --HighPriorityRouteTableId hprtb-hd4tl8cg \
    --Filters.0.Name gateway-id \
    --Filters.0.Values 172.16.0.11
```

Output: 
```
{
    "Response": {
        "HighPriorityRouteSet": [
            {
                "CdcId": "",
                "CreatedTime": "2024-07-11 17:34:48",
                "Description": "ivan_test",
                "DestinationCidrBlock": "192.168.0.0/24",
                "GatewayId": "172.16.0.11",
                "GatewayType": "NORMAL_CVM",
                "HighPriorityRouteId": "hprti-0sb1mbut",
                "HighPriorityRouteTableId": "hprtb-hd4tl8cg",
                "IsCdc": false,
                "SubnetRouteAlgorithm": "ECMP_QUINTUPLE_HASH"
            }
        ],
        "RequestId": "482a9736-73ed-4212-8b08-79403cd34cd3",
        "TotalCount": 1
    }
}
```

