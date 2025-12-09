**Example 1: 获取 WS Token**

获取 WS Token

Input: 

```
tccli lke GetWsToken --cli-unfold-argument  \
    --LoginUin 6000005624511 \
    --LoginSubAccountUin 6000005624511 \
    --Type 5 \
    --BotAppKey abcdefg
```

Output: 
```
{
    "Response": {
        "RequestId": "3fa293a5-****-****-8c0b-95252cfef12f",
        "Token": "0457ad8d-****-****-9f2f-81863f4b0182"
    }
}
```

