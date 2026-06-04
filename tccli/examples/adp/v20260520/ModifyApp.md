**Example 1: ModifyApp**



Input: 

```
tccli adp ModifyApp --cli-unfold-argument  \
    --AppId 2060252238143184320 \
    --AppMode 2 \
    --UpdateMask.Paths AppMode
```

Output: 
```
{
    "Response": {
        "AppId": "2060252238143184320",
        "UpdateTime": "1780390885",
        "RequestId": "479bbb70-2ba4-4aee-98da-1628f477a6ea"
    }
}
```

