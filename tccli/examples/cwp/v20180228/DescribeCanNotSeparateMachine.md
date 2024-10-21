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
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "PrivateIp": "xx.xx.xx.xx",
                "PublicIp": "xx.xx.xx.xx",
                "Alias": "a",
                "Reason": 1,
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e"
            }
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

