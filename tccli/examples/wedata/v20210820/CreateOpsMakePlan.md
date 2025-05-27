**Example 1: 批量补数据（创建补录任务）**

任务运维-补数据

Input: 

```
tccli wedata CreateOpsMakePlan --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --ParallelNum 2 \
    --MakeName patch_20230327104543_3122 \
    --TaskIdList 20230313154453331 \
    --MakeDatetimeList.0.StartDate 2023-03-01 \
    --MakeDatetimeList.0.EndDate 2023-03-01 \
    --MakeDatetimeList.0.StartTime 00:00 \
    --MakeDatetimeList.0.EndTime 23:59 \
    --CheckParent True \
    --SameSelfDependType False \
    --SelfDependence parallel \
    --Remark  \
    --SameCycle True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "patch_20250527184634_1417_ok"
        },
        "RequestId": "261c5c56-2891-49f4-a725-edd755065485"
    }
}
```

