**Example 1: 创建项目**

创建项目

Input: 

```
tccli bi CreateProject --cli-unfold-argument  \
    --Name abc \
    --Logo abc \
    --ColorCode abc \
    --Mark abc \
    --IsApply True \
    --DefaultPanelType 0
```

Output: 
```
{
    "Response": {
        "Extra": "abc",
        "Data": {
            "Id": 0
        },
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

