**Example 1: 查询交互式 session列表**

查询交互式 session列表

Input: 

```
tccli dlc DescribeNotebookSessions --cli-unfold-argument  \
    --DataEngineName abc \
    --State abc \
    --SortFields abc \
    --Asc True \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Sessions": [
            {
                "Kind": "spark",
                "Name": "session1",
                "ProxyUser": "root",
                "State": "not_started",
                "SessionId": "d3018ad4-9a7e-4f64-a3f4-f38507c69742",
                "SparkAppId": "spark-4ke6a46618d24e9c7yh2b62f0ddebdks",
                "CreateTime": "2006-01-02 15:04:05",
                "DataEngineName": "data_engin_1",
                "LastRunningTime": "2006-01-02 15:04:05",
                "SparkUiUrl": "http://xx",
                "Creator": "232132443"
            }
        ],
        "TotalPages": 2,
        "TotalElements": 20,
        "Page": 1,
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Size": 10
    }
}
```

