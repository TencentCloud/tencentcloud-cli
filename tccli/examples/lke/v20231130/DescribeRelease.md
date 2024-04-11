**Example 1: 查询发布详情**

查询最近一次发布详情

Input: 

```
tccli lke DescribeRelease --cli-unfold-argument  \
    --BotBizId 1727231073371148288 \
    --ReleaseBizId 0
```

Output: 
```
{
    "Response": {
        "CreateTime": "1700650168",
        "Description": "",
        "RequestId": "bba35062-8508-4cb5-b5c7-526370171ab0",
        "Status": 3,
        "StatusDesc": "发布成功"
    }
}
```

