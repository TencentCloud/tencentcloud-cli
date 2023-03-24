**Example 1: 移动分类**

移动分类

Input: 

```
tccli cme MoveClass --cli-unfold-argument  \
    --Platform test \
    --Owner.Id 6866c9a7-a2ca-4d6 \
    --Owner.Type PERSON \
    --SourceClassPath /a/b \
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

