**Example 1: 查询集群巡检报告概览**

ClusterIds为空，默认查询所有集群

Input: 

```
tccli tke DescribeClusterInspectionResultsOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "kubejarvis-test-case1",
        "Diagnostics": [
            {
                "Catalogues": [
                    {},
                    {}
                ],
                "Statistics": [
                    {},
                    {},
                    {},
                    {}
                ]
            },
            {
                "Catalogues": [
                    {},
                    {}
                ],
                "Statistics": []
            }
        ],
        "Statistics": [
            {},
            {},
            {},
            {}
        ],
        "InspectionOverview": [
            {
                "ClusterId": "cls-dsafas",
                "Statistics": [
                    {}
                ],
                "Diagnostics": [
                    {
                        "Catalogues": [
                            {},
                            {}
                        ]
                    }
                ]
            }
        ]
    }
}
```

