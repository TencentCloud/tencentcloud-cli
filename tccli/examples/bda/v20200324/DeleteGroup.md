**Example 1: 调用失败示例**



Input: 

```
tccli bda DeleteGroup --cli-unfold-argument  \
    --GroupId 1231231
```

Output: 
```
{
    "Response": {
        "RequestId": "cb24cce3-beb9-4f8b-9f61-e79fb075a9a4"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda DeleteGroup --cli-unfold-argument  \
    --GroupId testG10
```

Output: 
```
{
    "Response": {
        "RequestId": "bc9be78c-6d08-430e-9119-959d903769c9"
    }
}
```

