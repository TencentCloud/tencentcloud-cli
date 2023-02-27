**Example 1: 删除分类**



Input: 

```
tccli cme DeleteClass --cli-unfold-argument  \
    --Owner.Type PERSON \
    --Owner.Id 1111 \
    --Platform test \
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

