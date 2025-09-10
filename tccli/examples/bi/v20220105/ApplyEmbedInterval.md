**Example 1: 申请Token延期接口实例**



Input: 

```
tccli bi ApplyEmbedInterval --cli-unfold-argument  \
    --ProjectId 1982493789748932 \
    --PageId 1982493789748932 \
    --BIToken BIToken \
    --ExtraParam ExtraParam \
    --Intention Intention \
    --Scope Scope
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "e60a2172-715b-4305-beb2-40792ae53856",
        "Extra": "",
        "Data": {
            "Result": true
        }
    }
}
```

