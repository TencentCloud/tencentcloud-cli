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
                "Name": "test",
                "Statistics": [
                    {},
                    {},
                    {},
                    {}
                ]
            },
            {
                "Name": "test2",
                "Statistics": [
                    {},
                    {},
                    {},
                    {}
                ]
            }
        ],
        "RequestId": "kubejarvis-test-case1"
    }
}
```

