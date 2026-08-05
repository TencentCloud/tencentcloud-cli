**Example 1: 查询监控概览数据（瞬时值）**



Input: 

```
tccli dlc QueryMonitorOverview --cli-unfold-argument  \
    --ChartTypes HTTP_QPS \
    --ServiceId svc-migrated-00000022
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ChartType": "HTTP_QPS",
                "Value": 0
            }
        ],
        "RequestId": "cd73c95f-468c-4a70-a5fc-2f43a1caa7a7"
    }
}
```

