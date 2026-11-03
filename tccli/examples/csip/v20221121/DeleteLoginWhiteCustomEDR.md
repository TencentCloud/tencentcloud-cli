**Example 1: DeleteLoginWhiteCustomEDR**

批量删除异常登录自定义白名单

Input: 

```
tccli csip DeleteLoginWhiteCustomEDR --cli-unfold-argument  \
    --Ids 101 102 \
    --SelectAll False
```

Output: 
```
{
    "Response": {
        "DeletedCount": 2,
        "FailedAppIds": [],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

