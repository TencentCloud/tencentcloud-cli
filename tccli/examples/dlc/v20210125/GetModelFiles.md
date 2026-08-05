**Example 1: 调用 GetModelFiles 示例**



Input: 

```
tccli dlc GetModelFiles --cli-unfold-argument  \
    --ModelUid m-xgboost-aaa-6a301c6f-17e6 \
    --ModelVersion v2
```

Output: 
```
{
    "Response": {
        "Files": [],
        "ModelId": 48,
        "ModelName": "xgboost_aaa",
        "RequestId": "339c269c-222f-49a5-9fb9-53ac5ba79a5f"
    }
}
```

