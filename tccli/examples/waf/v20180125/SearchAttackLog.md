**Example 1: 搜索攻击日志详情内容**

搜索攻击日志详情内容

Input: 

```
tccli waf SearchAttackLog --cli-unfold-argument  \
    --Domain all \
    --StartTime 2024-10-28 20:56:07 \
    --EndTime 2024-10-29 20:56:07 \
    --QueryString bot:1 \
    --Context cont \
    --Sort desc \
    --Count 10 \
    --Page 0
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Context": "cont",
        "ListOver": false,
        "SqlFlag": false,
        "Data": [
            {
                "Content": "{\"action\":1,\"args_name\":\"HTTP Header\"}",
                "FileName": "name",
                "Source": "sre",
                "TimeStamp": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "ead32d5d-a9ac-496f-b8e3-d3a92f1fb1ce"
    }
}
```

