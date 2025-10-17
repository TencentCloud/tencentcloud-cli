**Example 1: 获取入站终端节点**



Input: 

```
tccli privatedns DescribeInboundEndpointList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name EndPointId \
    --Filters.0.Values inbound-6842b66693 \
    --Filters.1.Name EndPointVip \
    --Filters.1.Values 172.16.0.6 \
    --Filters.2.Name EndPointName \
    --Filters.2.Values test-inbound
```

Output: 
```
{
    "Response": {
        "InboundEndpointSet": [
            {
                "CreatedAt": "2025-06-06 17:35:34",
                "EndPointId": "inbound-6842b66693",
                "EndPointName": "test-inbound",
                "EndPointService": [
                    {
                        "EndPointIsolateFlag": 0,
                        "EndPointRemark": "",
                        "EndPointState": 0,
                        "EndPointStatus": 1,
                        "EndPointVip": "172.16.0.6"
                    }
                ],
                "UniqVpcId": "vpc-ptyhb4st",
                "UpdatedAt": "2025-06-06 17:35:34"
            }
        ],
        "RequestId": "07402391-c687-48b0-8bb0-2004b75a184b",
        "TotalCount": 1
    }
}
```

