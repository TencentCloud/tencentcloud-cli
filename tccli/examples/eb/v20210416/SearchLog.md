**Example 1: 日志检索**

日志检索

Input: 

```
tccli eb SearchLog --cli-unfold-argument ```

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

