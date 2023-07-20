**Example 1: 获取数据源类型列表**

任务运维-获取数据源类型列表

Input: 

```
tccli wedata DescribeOperateOpsTaskDatasourceType --cli-unfold-argument  \
    --ProjectId abc \
    --ServiceKind abc \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeId": 0,
                "CandidateTexts": "abc",
                "CandidateValues": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

