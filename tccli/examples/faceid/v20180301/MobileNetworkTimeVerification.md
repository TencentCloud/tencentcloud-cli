**Example 1: 核验失败**



Input: 

```
tccli faceid MobileNetworkTimeVerification --cli-unfold-argument  \
    --Mobile 11111111111
```

Output: 
```
{
    "Response": {
        "Result": "-2",
        "Description": "手机号不存在",
        "Range": "",
        "RequestId": "3151331a-277e-4317-891d-0ef4e0afdd3e"
    }
}
```

**Example 2: 核验成功**



Input: 

```
tccli faceid MobileNetworkTimeVerification --cli-unfold-argument  \
    --Mobile 13800138000
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "成功",
        "Range": "(24,+]",
        "RequestId": "f893bfcf-167d-45df-99aa-60a23fe5809d"
    }
}
```

