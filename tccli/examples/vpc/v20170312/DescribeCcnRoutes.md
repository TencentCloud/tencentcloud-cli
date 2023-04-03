**Example 1: 查询云联网路由列表**

查询云联网路由列表

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
        "RequestId": "3e866888-83ea-4716-b99b-21592cba6548",
        "RouteSet": [
            {
                "DestinationCidrBlock": "10.33.0.0/16",
                "UpdateTime": "2020-09-22 00:00:00",
                "RoutePriority": 1,
                "InstanceId": "vpc-r1ckkpid",
                "InstanceUin": "234532345",
                "Enabled": true,
                "InstanceExtraName": "test",
                "IsBgp": true,
                "InstanceRegion": "ap-guangzhou",
                "ExtraState": "Running",
                "RouteId": "ccnr-bvipc87w",
                "InstanceName": "test",
                "InstanceType": "VPC"
            },
            {
                "DestinationCidrBlock": "192.168.0.0/24",
                "UpdateTime": "2020-09-22 00:00:00",
                "RoutePriority": 1,
                "InstanceId": "vpc-r1ckkpid",
                "InstanceName": "test",
                "Enabled": true,
                "InstanceExtraName": "test",
                "IsBgp": true,
                "InstanceRegion": "ap-guangzhou",
                "ExtraState": "Running",
                "RouteId": "ccnr-oc61so0o",
                "InstanceUin": "234532345",
                "InstanceType": "VPC"
            }
        ]
    }
}
```

