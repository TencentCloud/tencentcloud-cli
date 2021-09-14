**Example 1: 获取函数最大独占配额详情**



Input: 

```
tccli scf GetReservedConcurrencyConfig --cli-unfold-argument  \
    --FunctionName test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ReservedMem": 128
    }
}
```

