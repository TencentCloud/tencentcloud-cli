**Example 1: 分页获取任务补录计划实例**

运维中心-数据补录

Input: 

```
tccli wedata ListDataBackfillInstances --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --DataBackfillPlanId a4bd6263-5bb2-4a88-ae00-5fc6ed9c8af4 \
    --TaskId 20230515143235 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "TotalPageNumber": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "TaskName": "iceberg_emr-20vq9aml_ICEBERG_collect_job",
                    "TaskId": "20250820214547578",
                    "CurRunDate": "2025-08-20 00:00:00",
                    "State": "EXPIRED",
                    "StartTime": "2025-08-20 23:45:14",
                    "EndTime": "2025-08-20 23:45:14",
                    "CostTime": "00:00:00.000"
                }
            ]
        },
        "RequestId": "85482e0d-fcb5-4fc6-9a9a-15ea7ef6b2f2"
    }
}
```

