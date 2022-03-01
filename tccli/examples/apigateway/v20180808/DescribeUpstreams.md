**Example 1: 查询vpc**



Input: 

```
tccli apigateway DescribeUpstreams --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "UpstreamSet": [
                {
                    "Retries": 1,
                    "Algorithm": "xx",
                    "UniqVpcId": "xx",
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "UpstreamId": "xx",
                    "UpstreamName": "xx",
                    "UpstreamDescription": "xx",
                    "Nodes": [
                        {
                            "VmInstanceId": "xx",
                            "Host": "xx",
                            "Port": 1,
                            "Weight": 1,
                            "Tags": [
                                "xx"
                            ]
                        }
                    ],
                    "Scheme": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

