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
                "PrivateIp": "1.1.1.1",
                "PublicIp": "1.1.1.1",
                "Alias": "dsger***",
                "Reason": 1,
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e"
            }
        ],
        "RequestId": "1ce68339-8828-457f-b358-d5b1b34e4fe9"
    }
}
```

