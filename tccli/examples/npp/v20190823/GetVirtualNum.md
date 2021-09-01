**Example 1: axb绑定**



Input: 

```
tccli npp GetVirtualNum --cli-unfold-argument  \
    --BizAppId 65535 \
    --Src 008615602455708 \
    --Dst 008613927437352
```

Output: 
```
{
    "Response": {
        "BindId": "14b3eb00-f75a-4181-8138-1d453cca995a",
        "RefNum": "1",
        "ErrorCode": "0",
        "Msg": "",
        "RequestId": "2004112214134693726",
        "VirtualNum": "17130896805"
    }
}
```

