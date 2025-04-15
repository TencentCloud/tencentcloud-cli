**Example 1: 查询任务消耗明细**

查询任务消耗明细

Input: 

```
tccli dlc QueryTaskCostDetail --cli-unfold-argument  \
    --Filters.0.Name task-state \
    --Filters.0.Values 2 \
    --Filters.1.Name task-id \
    --Filters.1.Values d98f6a98ed0211ef9d775254007bf0be \
    --StartTime 2025-02-17 00:00:00 \
    --EndTime 2025-02-18 00:00:00 \
    --DataEngineName dlc_spark \
    --SearchAfter 1735716131761 \
    --PageSize 10000
```

Output: 
```
{
    "Response": {
        "Data": "[[\"任务ID\",\"引擎具体类别\",\"任务提交时间\",\"引擎耗时(ms)\",\"引擎名称\",\"使用人\",\"资源总使用情况(cu*ms)\",\"资源拆分情况\"],[\"d98f6a98ed0211ef9d775254007bf0be\",\"SparkSQLTask\",\"1739778196761\",\"28113\",\"dlc_spark\",\"100****995\",\"171825\",\"\"]]",
        "RequestId": "c7c21737-eb92-4489-ad3d-1ccfa3ac9083",
        "SearchAfter": "[1739778196761]"
    }
}
```

