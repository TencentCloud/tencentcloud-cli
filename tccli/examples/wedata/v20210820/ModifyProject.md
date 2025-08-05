**Example 1: 样例**

modify project

Input: 

```
tccli wedata ModifyProject --cli-unfold-argument  \
    --DisplayName bs_test \
    --Description bs_test \
    --TaskSubmitApproval True \
    --ProjectId 111111111111 \
    --ResourcePoolInfo.ResourcePools 1234455555 \
    --ResourcePoolInfo.StorageSize 0 \
    --ResourcePoolInfo.StorageFileNum 0 \
    --ResourcePoolInfo.ClusterId 123123123123 \
    --ResourcePoolInfo.StorageType 123123123 \
    --ProjectManagers 12312312312 \
    --TaskStrictMode True \
    --ExtraOptions 12312312 \
    --Model 123123123
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: modify project**

modify project

Input: 

```
tccli wedata ModifyProject --cli-unfold-argument  \
    --TaskSubmitApproval true \
    --ProjectId 978203585769070592 \
    --DisplayName bs_test \
    --Description bs_test
```

Output: 
```
{
    "Response": {
        "RequestId": "72fda28b-e1c8-4017-9fd0-a67c79178bde"
    }
}
```

**Example 3: 升级到标准模式**

升级到标准模式

Input: 

```
tccli wedata ModifyProject --cli-unfold-argument  \
    --ProjectId 2082166847290601472 \
    --Model STANDARD
```

Output: 
```
{
    "Response": {
        "RequestId": "059e6ab7-b35c-42be-b1a6-cc0fc1329441"
    }
}
```

**Example 4: modify task script ready only**

modify project

Input: 

```
tccli wedata ModifyProject --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "64f07492-8c96-4928-a06f-f37c61382e06"
    }
}
```

