**Example 1: 创建链接**



Input: 

```
tccli cme CreateLink --cli-unfold-argument  \
    --Platform test\
    --Type MATERIAL\
    --Name link\
    --ClassPath /a/b\
    --Owner.Id 1111\
    --Owner.Type PERSON\
    --DestinationId 123456789\
    --DestinationOwner.Id 1234\
    --DestinationOwner.Type PERSON
```

Output: 
```
{
    "Response": {
        "MaterialId": "234567890",
        "RequestId": "requestId"
    }
}
```

