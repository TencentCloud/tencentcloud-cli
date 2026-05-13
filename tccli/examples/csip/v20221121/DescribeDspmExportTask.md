**Example 1: 查询导出任务**



Input: 

```
tccli csip DescribeDspmExportTask --cli-unfold-argument  \
    --TaskStatus 0 \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 0,
                "AppId": 0,
                "Percentage": 0,
                "TaskStatus": 0,
                "CreateTime": 0,
                "ModifyTime": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "1230-222k-xx"
    }
}
```

