**Example 1: 创建IPv4全局路由**

创建IPv4全局路由

Input: 

```
tccli vpc CreateGlobalRoutes --cli-unfold-argument  \
    --VpcId vpc-mcqaoy0f \
    --GlobalRoutes.0.DestinationCidrBlock 192.168.0.0/16 \
    --GlobalRoutes.0.GatewayType NORMAL_CVM \
    --GlobalRoutes.0.GatewayId 10.0.16.4 \
    --GlobalRoutes.0.Description ivan_gr
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
        "RequestId": "cabe9ed4-554f-4b3a-8611-fe5c4e63ccc1"
    }
}
```

