**Example 1: Querying the CCN route list**



Input: 

```
tccli vpc DescribeCcnRoutes --cli-unfold-argument  \
    --CcnId ccn-gree226l\
    --Filters.0.Name route-id\
    --Filters.0.Values ccnr-bvipc87w ccnr-oc61so0o\
    --Filters.1.Name instance-type\
    --Filters.1.Values VPC DIRECTCONNECT\
    --Filters.2.Name instance-region\
    --Filters.2.Values ap-guangzhou ap-beijing ap-shanghai eu-frankfurt\
    --Filters.3.Name instance-id\
    --Filters.3.Values vpc-r1ckkpid dcg-98qosdc3\
    --Filters.4.Name cidr-block\
    --Filters.4.Values 10.33.0.0/16 192.168.0.0/24
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": "ccnr-bvipc87w",
                "DestinationCidrBlock": "10.33.0.0/24",
                "InstanceType": "VPC",
                "InstanceId": "vpc-r1ckkpid",
                "InstanceName": "vpc0420",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "979137",
                "UpdateTime": "2018-06-21 11:32:29"
            },
            {
                "RouteId": "ccnr-oc61so0o",
                "DestinationCidrBlock": "192.168.0.0/24",
                "InstanceType": "DIRECTCONNECT",
                "InstanceId": "dcg-98qosdc3",
                "InstanceName": "test",
                "InstanceRegion": "ap-guangzhou",
                "InstanceUin": "979137",
                "UpdateTime": "2018-06-21 11:32:29"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

