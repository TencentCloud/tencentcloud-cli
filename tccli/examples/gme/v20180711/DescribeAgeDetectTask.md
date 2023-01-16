**Example 1: 查询年龄语音识别任务结果**

查询年龄语音识别任务结果

Input: 

```
tccli gme DescribeAgeDetectTask --cli-unfold-argument  \
    --BizId 1400000000 \
    --TaskId 6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b
```

Output: 
```
{
    "Response": {
        "TaskId": "6330xxxx-9xx7-11ed-98e3-52xxxxe4ac3b",
        "Results": [
            {
                "DataId": "1400000000_test_data_id",
                "Url": "https://yy.com",
                "Status": 2,
                "Age": 1
            }
        ],
        "RequestId": "c72659a3-841d-4e42-b5ea-040f4577cc67"
    }
}
```

