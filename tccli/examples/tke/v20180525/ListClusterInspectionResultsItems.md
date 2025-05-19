**Example 1: 获取巡检结果历史**

获取巡检结果历史

Input: 

```
tccli tke ListClusterInspectionResultsItems --cli-unfold-argument  \
    --ClusterId cls-54n6gepo
```

Output: 
```
{
    "Response": {
        "InspectionResultsItems": [
            {
                "Name": "ClusterSecurity",
                "Statistics": [
                    {
                        "HealthyLevel": "risk",
                        "Count": 2
                    },
                    {
                        "HealthyLevel": "serious",
                        "Count": 1
                    },
                    {
                        "HealthyLevel": "failed",
                        "Count": 0
                    },
                    {
                        "HealthyLevel": "good",
                        "Count": 10
                    }
                ]
            },
            {
                "Name": "NodeHealth",
                "Statistics": [
                    {
                        "HealthyLevel": "serious",
                        "Count": 1
                    },
                    {
                        "HealthyLevel": "failed",
                        "Count": 0
                    },
                    {
                        "HealthyLevel": "good",
                        "Count": 10
                    },
                    {
                        "HealthyLevel": "risk",
                        "Count": 2
                    }
                ]
            }
        ],
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

