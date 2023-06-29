**Example 1: 申请Token延期接口实例**



Input: 

```
tccli bi ApplyEmbedInterval --cli-unfold-argument  \
    --Scope page \
    --BIToken 246cbf0d-aa6c-445d-895d-b368f59159e8 \
    --ExtraParam  \
    --PageId 1 \
    --ProjectId 2
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

