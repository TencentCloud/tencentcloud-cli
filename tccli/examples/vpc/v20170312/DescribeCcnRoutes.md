**Example 1: 查询云联网路由列表**



Input: 

```
tccli vpc DescribeCcnRoutes --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --Filters.0.Name route-id \
    --Filters.0.Values ccnr-bvipc87w ccnr-oc61so0o \
    --Filters.1.Name instance-type \
    --Filters.1.Values VPC DIRECTCONNECT \
    --Filters.2.Name instance-region \
    --Filters.2.Values ap-guangzhou ap-beijing ap-shanghai eu-frankfurt \
    --Filters.3.Name instance-id \
    --Filters.3.Values vpc-r1ckkpid dcg-98qosdc3 \
    --Filters.4.Name cidr-block \
    --Filters.4.Values 10.33.0.0/16 192.168.0.0/24
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "RouteSet": [
            {
                "DestinationCidrBlock": "10.0.0.1/16",
                "UpdateTime": "2020-09-22 00:00:00",
                "RoutePriority": 1,
                "InstanceId": "xx",
                "InstanceUin": "xx",
                "Enabled": true,
                "InstanceExtraName": "xx",
                "IsBgp": true,
                "InstanceRegion": "xx",
                "ExtraState": "xx",
                "RouteId": "xx",
                "InstanceName": "xx",
                "InstanceType": "xx"
            },
            {
                "DestinationCidrBlock": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "RoutePriority": 1,
                "InstanceId": "xx",
                "InstanceName": "xx",
                "Enabled": true,
                "InstanceExtraName": "xx",
                "IsBgp": true,
                "InstanceRegion": "xx",
                "ExtraState": "xx",
                "RouteId": "xx",
                "InstanceUin": "xx",
                "InstanceType": "xx"
            }
        ]
    }
}
```

