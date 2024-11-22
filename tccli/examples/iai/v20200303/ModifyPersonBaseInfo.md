**Example 1: 修改人员基础信息成功示例**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 2001 \
    --PersonName JunlyWang \
    --Gender 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2a0fb7-7c9e-45c7-abf1-338457d1def7"
    }
}
```

**Example 2: 修改人员基础信息失败示例**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 9001 \
    --PersonName EvanLiao \
    --Gender 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.GroupPersonMapExist",
            "Message": "组中已包含对应的人员Id。"
        },
        "RequestId": "f944657d-6260-4a2e-a4d8-9c1845f39e56"
    }
}
```

