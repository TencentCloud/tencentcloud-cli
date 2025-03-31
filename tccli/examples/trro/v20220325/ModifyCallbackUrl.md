**Example 1: 设置回调URL**



Input: 

```
tccli trro ModifyCallbackUrl --cli-unfold-argument  \
    --ProjectId m82k5408n123phvb \
    --CallbackUrl http://123.45.81.121:9999 \
    --SignKey abcd1234
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Msg": "ok",
        "RequestId": "c1f72a62-e199-4d04-bf2c-ee3e97a3c4af"
    }
}
```

