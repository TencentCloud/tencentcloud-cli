**Example 1: 测试**

测试

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
            "Id": "0c2dd8d6-ab68-48cc-8264-85b70ff4b291"
        },
        "RequestId": "261c5c56-2891-49f4-a725-edd755065485"
    }
}
```

