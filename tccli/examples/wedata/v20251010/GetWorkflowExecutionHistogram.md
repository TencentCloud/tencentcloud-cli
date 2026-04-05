**Example 1: 查询运行数量变化趋势图信息**



Input: 

```
tccli wedata GetWorkflowExecutionHistogram --cli-unfold-argument  \
    --WorkspaceId 1 \
    --Filters.0.Name StartTime \
    --Filters.0.Values 1761290500000 \
    --Filters.1.Name EndTime \
    --Filters.1.Values 1761304900000
```

Output: 
```
{
    "Response": {
        "Data": {
            "EndTime": "1761304900",
            "Histogram": {
                "CodeLabels": [
                    "NotFound"
                ],
                "Histograms": [
                    {
                        "CodeCounts": [
                            0
                        ],
                        "EndTime": "1761294100",
                        "StartTime": "1761290500",
                        "TotalCount": "0"
                    },
                    {
                        "CodeCounts": [
                            0
                        ],
                        "EndTime": "1761297700",
                        "StartTime": "1761294100",
                        "TotalCount": "0"
                    },
                    {
                        "CodeCounts": [
                            1
                        ],
                        "EndTime": "1761301300",
                        "StartTime": "1761297700",
                        "TotalCount": "1"
                    },
                    {
                        "CodeCounts": [
                            0
                        ],
                        "EndTime": "1761304900",
                        "StartTime": "1761301300",
                        "TotalCount": "0"
                    },
                    {
                        "CodeCounts": [
                            0
                        ],
                        "EndTime": "1761308500",
                        "StartTime": "1761304900",
                        "TotalCount": "0"
                    }
                ]
            },
            "StartTime": "1761290500"
        },
        "RequestId": "2a1583af-55d0-4481-a5c2-7390b5f53a51"
    }
}
```

