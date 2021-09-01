**Example 1: 调用失败示例**



Input: 

```
tccli bda ModifyPersonInfo --cli-unfold-argument  \
    --PersonId 12313123 \
    --PersonName testG10P1M1
```

Output: 
```
{
    "Response": {
        "RequestId": "5844914d-b2e1-4afc-9970-8d1cdd6a7138"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda ModifyPersonInfo --cli-unfold-argument  \
    --PersonId testG10P1 \
    --PersonName testG10P1M1
```

Output: 
```
{
    "Response": {
        "RequestId": "327920d1-f111-463d-b9d3-3eaa0a473508"
    }
}
```

