**Example 1: 获取主密钥列表详情**



Input: 

```
tccli kms ListKeyDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Role 0 \
    --OrderType 0 \
    --KeyState 0 \
    --SearchKeyAlias Weijiali \
    --Origin TENCENT_KMS \
    --KeyUsage ALL \
    --TagFilters.0.TagKey env \
    --TagFilters.0.TagValue dev \
    --HsmClusterId cls-hsm-3dflmo9g
```

Output: 
```
{
    "Response": {
        "KeyMetadatas": [
            {
                "Alias": "Weijiali_test_000000005",
                "CreateTime": 1725354067,
                "CreatorUin": 700001028674,
                "DeletionDate": 0,
                "Description": "weijiali_test_00000000000005",
                "HsmClusterId": "cls-hsm-3dflmo9g",
                "KeyId": "0ed49d3e-69d3-11ef-9841-52540089bc41",
                "KeyRotationEnabled": false,
                "KeyState": "Enabled",
                "KeyUsage": "ASYMMETRIC_SIGN_VERIFY_SM2",
                "NextRotateTime": 1756890067,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/700001028674/0ed49d3e-69d3-11ef-9841-52540089bc41",
                "Type": 4,
                "ValidTo": 0
            },
            {
                "Alias": "Weijiali_test_00000000000004",
                "CreateTime": 1725354055,
                "CreatorUin": 700001028674,
                "DeletionDate": 0,
                "Description": "Weijiali_test_00000000000004",
                "HsmClusterId": "cls-hsm-3dflmo9g",
                "KeyId": "07ad2031-69d3-11ef-9841-52540089bc41",
                "KeyRotationEnabled": false,
                "KeyState": "Enabled",
                "KeyUsage": "ASYMMETRIC_DECRYPT_SM2",
                "NextRotateTime": 1756890055,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/700001028674/07ad2031-69d3-11ef-9841-52540089bc41",
                "Type": 4,
                "ValidTo": 0
            },
            {
                "Alias": "weijiali_test_00000000000003",
                "CreateTime": 1725354040,
                "CreatorUin": 700001028674,
                "DeletionDate": 0,
                "Description": "weijiali_test_00000000000003",
                "HsmClusterId": "cls-hsm-3dflmo9g",
                "KeyId": "fea98175-69d2-11ef-910d-525400d834e5",
                "KeyRotationEnabled": false,
                "KeyState": "Enabled",
                "KeyUsage": "ENCRYPT_DECRYPT",
                "NextRotateTime": 1756890040,
                "Origin": "TENCENT_KMS",
                "Owner": "user",
                "ResourceId": "creatorUin/700001028674/fea98175-69d2-11ef-910d-525400d834e5",
                "Type": 4,
                "ValidTo": 0
            }
        ],
        "RequestId": "57c12411-dd1a-4f3c-aaff-aec49a442b6c",
        "TotalCount": 3
    }
}
```

