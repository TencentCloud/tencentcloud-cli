**Example 1: 设备控制**

成功响应

Input: 

```
tccli weilingwith ControlDevice --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --WIDSet 70e673c7-11b8-4ca0-b11c-dfa360a44638 \
    --ControlData left \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "21909094-b304-4942-af6a-eb781ddd0a2a",
        "Result": {
            "Set": [
                {
                    "Code": 0,
                    "Result": "success",
                    "Seq": "21909094-b304-4942-af6a-eb781ddd0a2a",
                    "WID": "70e673c7-11b8-4ca0-b11c-dfa360a44638"
                }
            ]
        }
    }
}
```

