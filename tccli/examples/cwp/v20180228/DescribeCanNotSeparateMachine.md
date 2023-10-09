**Example 1: 示例**

获取木马不可隔离的主机

Input: 

```
tccli cwp DescribeCanNotSeparateMachine --cli-unfold-argument  \
    --UpdateAll True \
    --Ids 1 \
    --ExcludeId 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Uuid": "xx",
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "Alias": "xx",
                "Reason": 1,
                "Quuid": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

