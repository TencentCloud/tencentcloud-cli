**Example 1: 获取结构化结果接口示例**



Input: 

```
tccli cii DescribeStructureTaskResult --cli-unfold-argument  \
    --MainTaskId 37835597617481728
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "Status": "0",
        "Results": [
            {
                "Quality": 0.72,
                "StructureResult": "xxxxxx"
            }
        ]
    }
}
```

