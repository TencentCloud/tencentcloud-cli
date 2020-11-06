**Example 1: 创建分类**



Input: 

```
tccli cme CreateClass --cli-unfold-argument  \
    --Platform test \
    --Owner.Id 1111 \
    --Owner.Type PERSON \
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

