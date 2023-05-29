**Example 1: 创建搜索下载攻击日志任务**

创建搜索下载攻击日志任务

Input: 

```
tccli waf PostAttackDownloadTask --cli-unfold-argument  \
    --Domain abc \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --QueryString abc \
    --TaskName abc \
    --Sort abc \
    --Count 0
```

Output: 
```
{
    "Response": {
        "Flow": "ead32d5d-a9ac-496f-b8e3-d3a92f1fb1ce",
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

