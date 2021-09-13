**Example 1: 获取爆破阻断模式**



Input: 

```
tccli cwp DescribeBanMode --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Mode": "STANDARD_MODE",
        "StandardModeConfig": {
            "Ttl": 1
        },
        "RequestId": "132456798"
    }
}
```

