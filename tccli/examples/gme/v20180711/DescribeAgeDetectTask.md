**Example 1: 查询年龄语音识别任务结果**



Input: 

```
tccli gme DescribeAgeDetectTask --cli-unfold-argument  \
    --BizId 123456 \
    --TaskId xxx-yyy-zzz
```

Output: 
```
{
    "Response": {
        "TaskId": "xxxxxxxx",
        "Results": [
            {
                "DataId": "xxxx",
                "Url": "https://yy.com",
                "Status": 2,
                "Age": 1
            }
        ],
        "RequestId": "ecefce57a9ae2087d0cbf7fcc0e27bac"
    }
}
```

