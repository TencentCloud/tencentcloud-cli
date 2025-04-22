**Example 1: 查询任务消耗**

查询任务消耗

Input: 

```
tccli dlc DescribeTasksCostInfo --cli-unfold-argument  \
    --Filters.0.Name task-id \
    --Filters.0.Values cbe230ab-c05f-47a2-bcd7-9417babf5826 \
    --StartTime 2025-01-21 00:00:00 \
    --EndTime 2025-02-22 00:00:00 \
    --DataEngineName dlc_spark \
    --SearchAfter 1735716131082 \
    --PageSize 10000
```

Output: 
```
{
    "Response": {
        "Data": "[[\"任务ID\",\"引擎具体类别\",\"任务提交时间\",\"引擎耗时(ms)\",\"引擎名称\",\"使用人\",\"资源总使用情况(cu*ms)\",\"资源拆分情况\"],[\"cbe230ab-*-*-*-*\",\"SparkBatchSQL\",\"1738914913082\",\"117823\",\"dlc_spark\",\"100****217\",\"0\",\"\"]]",
        "RequestId": "835600fe-*-*-*-015a9f638fff",
        "SearchAfter": "[1738914913082]"
    }
}
```

