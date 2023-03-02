**Example 1: 查询账号是否存在**



Input: 

```
tccli account CheckAccountExists --cli-unfold-argument  \
    --Account test@qq.com \
    --Type mail \
    --Platform qcloud
```

Output: 
```
{
    "Response": {
        "Exist": false,
        "RequestId": "abf35200-2bf4-4d27-ad1e-1e8e865af9bf"
    }
}
```

