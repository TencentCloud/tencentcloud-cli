**Example 1: 获取函数保留并发详情**



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

