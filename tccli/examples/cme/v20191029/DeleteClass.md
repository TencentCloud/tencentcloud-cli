**Example 1: 删除分类**



Input: 

```
tccli cme DeleteClass --cli-unfold-argument  \
    --Platform test\
    --Owner.Id 1111\
    --Owner.Type PERSON\
    --ClassPath /a/b
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

