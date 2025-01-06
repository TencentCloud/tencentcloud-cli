**Example 1: 更新描述**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --TokenId ct3ucep1qcle9n4kmv00 \
    --Enable False \
    --RegistryId tcr-dg284imq \
    --Desc update desc \
    --ModifyFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cff207ed-446a-4e62-8098-12b0c91a929b"
    }
}
```

**Example 2: 启用实例长期访问凭证**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --TokenId ct3ucep1qcle9n4kmv00 \
    --Enable True \
    --RegistryId tcr-dg284imq \
    --ModifyFlag 2
```

Output: 
```
{
    "Response": {
        "RequestId": "b6e898ab-b817-43c6-9a51-31d3baaa2f68"
    }
}
```

**Example 3: 禁用实例长期访问凭证**



Input: 

```
tccli tcr ModifyInstanceToken --cli-unfold-argument  \
    --TokenId ct3ucep1qcle9n4kmv00 \
    --Enable False \
    --RegistryId tcr-dg284imq \
    --ModifyFlag 2
```

Output: 
```
{
    "Response": {
        "RequestId": "14d569e1-e3cf-4399-a096-b6bd7b373240"
    }
}
```

