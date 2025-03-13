**Example 1: 获取spark 作业任务日志详情**



Input: 

```
tccli dlc DescribeTaskLog --cli-unfold-argument  \
    --TaskId 84f55bb7-4f9c-4995-90c5-a40fdff9bc62 \
    --StartTime 1736931692631 \
    --EndTime 1737104492631 \
    --Limit 10 \
    --Context 
```

Output: 
```
{
    "Response": {
        "Context": "",
        "ListOver": true,
        "LogUrl": "",
        "RequestId": "********-****-****-****-303d24983adb",
        "Results": []
    }
}
```

