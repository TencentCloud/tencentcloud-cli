**Example 1: 事件查询**

事件查询

Input: 

```
tccli eb SearchLog --cli-unfold-argument  \
    --StartTime 1673233483024 \
    --EndTime 1673838283024 \
    --EventBusId eb-xxxxx \
    --Page 1 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "Results": [
            {
                "Timestamp": "xxx",
                "Message": "xxx-1",
                "Source": "xxx",
                "Type": "xzz",
                "RuleIds": "xxx",
                "Subject": "xxx",
                "Region": "xxx",
                "Status": "xxx"
            }
        ],
        "Total": 1000,
        "Limit": 500,
        "Page": 1
    }
}
```

