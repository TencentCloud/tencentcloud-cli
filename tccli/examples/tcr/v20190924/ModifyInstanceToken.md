**Example 1: 更新描述**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --TokenId 2ab3af0d-893d-423f-91b1-27713566f95f \
    --Desc aaa \
    --ModifyFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6cd302c6-c4c9-425a-8d07-8c59b7f4cf3f"
    }
}
```

**Example 2: 启用实例长期访问凭证**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --TokenId 2ab3af0d-893d-423f-91b1-27713566f95f \
    --Enable true
```

Output: 
```
{
    "Response": {
        "RequestId": "6cd302c6-c4c9-425a-8d07-8c59b7f4cf3f"
    }
}
```

**Example 3: 禁用实例长期访问凭证**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --TokenId 2ab3af0d-893d-423f-91b1-27713566f95f \
    --Enable false
```

Output: 
```
{
    "Response": {
        "RequestId": "6cd302c6-c4c9-425a-8d07-8c59b7f4cf3f"
    }
}
```

