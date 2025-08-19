**Example 1: 账号可清理列表**

检测大账号下是否存在资源

Input: 

```
tccli lighthousedb CheckCleanableUserAppIds --cli-unfold-argument  \
    --UserAppIds 623134343
```

Output: 
```
{
    "Response": {
        "CleanableUserAppIdSet": [
            12345,
            12345
        ],
        "RequestId": "f040a2e4-803e-438f-8afb-8877028be0f5",
        "TotalCount": 2
    }
}
```

