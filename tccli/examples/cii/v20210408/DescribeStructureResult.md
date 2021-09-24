**Example 1: 查询结构化结果接口示例**



Input: 

```
tccli cii DescribeStructureResult --cli-unfold-argument  \
    --MainTaskId 37835597617481728
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "Status": 0,
        "MainTaskId": "xx",
        "Results": [
            {
                "Code": 1,
                "SubTaskId": "xx",
                "StructureResult": "xx",
                "TaskType": "HealthReport"
            }
        ]
    }
}
```

