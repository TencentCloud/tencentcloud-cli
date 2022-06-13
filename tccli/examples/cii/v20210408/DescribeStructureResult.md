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
        "Status": 1,
        "MainTaskId": "xx",
        "Results": [
            {
                "TaskFiles": [
                    "xx"
                ],
                "Code": 1,
                "StructureResult": "xx",
                "SubTaskId": "xx",
                "TaskType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

