**Example 1: ModifyApp**

修改应用

Input: 

```
tccli adp ModifyApp --cli-unfold-argument  \
    --AppId 2070037792884085504 \
    --AppMode 2 \
    --UpdateMask.Paths AppMode
```

Output: 
```
{
    "Response": {
        "AppId": "2070037792884085504",
        "UpdateTime": "1782819327",
        "RequestId": "f4871251-9d39-4284-ae9a-349307e05913"
    }
}
```

