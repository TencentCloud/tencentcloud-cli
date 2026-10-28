**Example 1: 示例**



Input: 

```
tccli databuddy RemoveWorkspaceUsers --cli-unfold-argument  \
    --UserUins 700003439148 \
    --WorkspaceId 17700183032157854
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailItems": [
                {
                    "FailReason": "uin 700003439148 cannot be removed",
                    "Item": "700003439148"
                }
            ],
            "Status": true,
            "SuccessUins": [
                "700002562959"
            ]
        },
        "RequestId": "9d1644ec-d6a7-470d-9cd9-5d9ade676b8e"
    }
}
```

