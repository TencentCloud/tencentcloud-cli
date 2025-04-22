**Example 1: 查询Ipv4全局路由**

查询Ipv4全局路由

Input: 

```
tccli vpc DescribeGlobalRoutes --cli-unfold-argument  \
    --GlobalRouteIds gr-remsfl8e
```

Output: 
```
{
    "Response": {
        "GlobalRouteSet": [
            {
                "CreatedTime": "2025-02-21 16:32:36",
                "Description": "ivan_gr",
                "DestinationCidrBlock": "192.168.0.0/16",
                "GatewayId": "10.0.16.4",
                "GatewayType": "NORMAL_CVM",
                "GlobalRouteId": "gr-remsfl8e",
                "SubnetRouteAlgorithm": "ECMP_QUINTUPLE_HASH",
                "VpcId": "vpc-mcqaoy0f"
            }
        ],
        "RequestId": "1c76c527-aa4e-45cc-9b0b-25dbe81072e4",
        "TotalCount": 1
    }
}
```

