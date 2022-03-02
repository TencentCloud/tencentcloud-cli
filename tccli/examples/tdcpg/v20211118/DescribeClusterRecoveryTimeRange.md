**Example 1: 查询集群可回档时间范围**



Input: 

```
tccli tdcpg DescribeClusterRecoveryTimeRange --cli-unfold-argument  \
    --ClusterId tdcpg-xxx \
    --DataPoint 2022-01-08T19:50:54+08:00
```

Output: 
```
{
    "Response": {
        "AvailableRecoveryTimeRangeSet": [
            {
                "AvailableBeginTime": "2022-01-08T19:50:54+08:00",
                "AvailableEndTime": "2022-01-08T19:50:54+08:00"
            }
        ],
        "RequestId": "e0ef1b06-405f-48cc-863f-185dbb6eb037"
    }
}
```

