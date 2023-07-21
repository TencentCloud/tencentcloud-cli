**Example 1: 搜索攻击日志详情内容**

搜索攻击日志详情内容

Input: 

```
tccli waf SearchAttackLog --cli-unfold-argument  \
    --StartTime '2020-09-22 00:00:00' \
    --EndTime '2020-09-22 00:00:00' \
    --Domain all \
    --Context  \
    --QueryString method:GET \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Context": "abc",
        "Data": [
            {
                "Content": "abc",
                "FileName": "abc",
                "Source": "abc",
                "TimeStamp": "2020-09-22 00:00:00"
            }
        ],
        "ListOver": true,
        "SqlFlag": true,
        "RequestId": "abc"
    }
}
```

