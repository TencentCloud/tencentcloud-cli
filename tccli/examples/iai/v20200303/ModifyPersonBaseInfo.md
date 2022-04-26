**Example 1: 修改人员基础信息接口**



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

**Example 2: 修改人员基础信息接口-2**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001 \
    --PersonName EvanLiao \
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

