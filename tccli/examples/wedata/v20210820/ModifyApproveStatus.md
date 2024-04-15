**Example 1: 成功示例**



Input: 

```
tccli wedata ModifyApproveStatus --cli-unfold-argument  \
    --Status pass \
    --Remark 通过了 \
    --ApproveIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5a175a45-226d-4f0b-9b96-d01e264e443f",
        "Data": [
            {
                "ApproveId": "1",
                "Success": true
            }
        ]
    }
}
```

