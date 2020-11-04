**Example 1: 移动分类**



Input: 

```
tccli cme MoveClass --cli-unfold-argument  \
    --Platform test\
    --Owner.Id 1111\
    --Owner.Type PERSON\
    --SourceClassPath /a/b\
    --DestinationClassPath /a/b
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

