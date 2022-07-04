**Example 1: 查询全局路由**



Input: 

```
tccli vpc DescribeGlobalRouteInternal --cli-unfold-argument  \
    --VpcId 1 \
    --Remote 172.16.0.2 \
    --UniqueVpcId vpc-jmaywf6r
```

Output: 
```
{
    "Response": {
        "GlobalRouteSet": [
            {
                "VpcId": 22,
                "Subnet": "100.64.0.0",
                "IntMask": 24,
                "Remote": "172.16.0.2",
                "Master": "16.5.3.6"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

