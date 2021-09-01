**Example 1: 获取targets列表**



Input: 

```
tccli tke DescribePrometheusTargets --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "Targets": [
                    {
                        "LastScrape": "xx",
                        "ScrapeDuration": 0.0,
                        "Url": "xx",
                        "Labels": [
                            {
                                "Name": "xx",
                                "Value": "xx"
                            }
                        ],
                        "State": "xx",
                        "Error": "xx"
                    }
                ],
                "Total": 1,
                "Up": 1,
                "JobName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

