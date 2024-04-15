**Example 1: 获取ws token**



Input: 

```
tccli lke GetWsToken --cli-unfold-argument  \
    --Type 1 \
    --BotAppKey c65bf398 \
    --VisitorBizId 
```

Output: 
```
{
    "Response": {
        "Token": "c91a8c01-c543-42e2-ba8a-d119b7cba434",
        "RequestId": "abc"
    }
}
```

**Example 2: 获取 WS Token**

获取 WS Token

Input: 

```
tccli lke GetWsToken --cli-unfold-argument  \
    --Type 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3fa293a5-9d46-4f26-8c0b-95252cfef12f",
        "Token": "0457ad8d-2c64-40d9-9f2f-81863f4b0182"
    }
}
```

