**Example 1: 修改素材信息**



Input: 

```
tccli cme ModifyMaterial --cli-unfold-argument  \
    --Platform test\
    --MaterialId 123245678\
    --Owner.Id 1111\
    --Owner.Type PERSON\
    --Name name_modify
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

