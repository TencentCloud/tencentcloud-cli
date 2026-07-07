**Example 1: 查询异步任务信息**



Input: 

```
tccli alb DescribeAsyncJobs --cli-unfold-argument  \
    --RequestIds c318a537-9bfa-40c2-b6d5-e6f872ad4b1f
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "ApiName": "DisassociateBandwidthPackageFromLoadBalancer",
                "RequestId": "c318a537-9bfa-40c2-b6d5-e6f872ad4b1f",
                "ResourceIds": [
                    "alb-f8q2xk9m"
                ],
                "Status": "Succeeded"
            }
        ],
        "MaxResults": 20,
        "NextToken": "",
        "TotalCount": 1,
        "RequestId": "e4bf85e4-739f-4a3e-9ce1-d98d1fa2a876"
    }
}
```

