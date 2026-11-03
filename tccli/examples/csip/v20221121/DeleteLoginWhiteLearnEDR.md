**Example 1: DeleteLoginWhiteLearnEDR**

删除异常登录自学习白名单规则组

Input: 

```
tccli csip DeleteLoginWhiteLearnEDR --cli-unfold-argument  \
    --Ids 42383278
```

Output: 
```
{
    "Response": {
        "DeletedCount": 3,
        "FailedAppIds": [],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

