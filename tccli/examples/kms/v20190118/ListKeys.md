**Example 1: 获取主密钥列表示例**

获取主密钥列表

Input: 

```
tccli kms ListKeys --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Role 0 \
    --HsmClusterId cls-hsm-3dflmo9g
```

Output: 
```
{
    "Response": {
        "Keys": [
            {
                "KeyId": "515d337d-70b4-11ef-bc87-02ac442a5a1f"
            },
            {
                "KeyId": "0ed49d3e-69d3-11ef-9841-52540089bc41"
            }
        ],
        "RequestId": "28c0e45c-c034-4d8b-b006-f018aa88597d",
        "TotalCount": 14
    }
}
```

