**Example 1: 查询模型监控指标数据**

查询模型监控指标数据

Input: 

```
tccli wedata GetModelMetric --cli-unfold-argument  \
    --RunIds 1aef2bdca57e418ead19ba960f39647d \
    --MetricName n_features \
    --WorkspaceId 10086
```

Output: 
```
{
    "Response": {
        "Data": {
            "MetricDataList": [
                {
                    "MetricName": "n_features",
                    "RunId": "1aef2bdca57e418ead19ba960f39647d",
                    "RunMetrics": []
                }
            ]
        },
        "RequestId": "47f747fb-8674-495e-9ddd-1692f348aafb"
    }
}
```

