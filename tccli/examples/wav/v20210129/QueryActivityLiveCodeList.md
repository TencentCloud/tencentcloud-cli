**Example 1: 查询活码列表**



Input: 

```
tccli wav QueryActivityLiveCodeList --cli-unfold-argument  \
    --Cursor xxxx \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PageData": [
            {
                "ActivityName": "xx",
                "LiveCodeName": "xx",
                "LiveCodeId": 0,
                "LiveCodeState": 0,
                "LiveCodeData": "xx",
                "ActivityId": 0,
                "LiveCodePreview": "xx",
                "ShortChainAddress": "xx",
                "CreateTime": 0,
                "UpdateTime": 0
            }
        ],
        "NextCursor": "xx",
        "RequestId": "xx"
    }
}
```

