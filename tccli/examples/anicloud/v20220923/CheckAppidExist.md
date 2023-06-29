**Example 1: 查询appid是否存在**



Input: 

```
tccli anicloud CheckAppidExist --cli-unfold-argument  \
    --Type xx \
    --SDKAppid xx
```

Output: 
```
{
    "Response": {
        "Msg": "xx",
        "HasError": true,
        "Exist": true,
        "RequestId": "xx"
    }
}
```

