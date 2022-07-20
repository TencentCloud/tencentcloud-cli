**Example 1: 创建搜索下载攻击日志任务**



Input: 

```
tccli waf PostAttackDownloadTask --cli-unfold-argument  \
    --StartTime 2020-08-2800:00:00 \
    --EndTime 2020-08-2814:12:36 \
    --Domain all \
    --QueryString method:GET \
    --Sort desc
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

