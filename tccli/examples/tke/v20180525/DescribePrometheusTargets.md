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
                        "Url": "abc",
                        "State": "abc",
                        "Labels": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "LastScrape": "abc",
                        "ScrapeDuration": 0,
                        "Error": "abc"
                    }
                ],
                "JobName": "abc",
                "Total": 1,
                "Up": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

