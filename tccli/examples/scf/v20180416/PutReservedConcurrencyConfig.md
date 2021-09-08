**Example 1: 设置最大独占配额**



Input: 

```
tccli scf PutReservedConcurrencyConfig --cli-unfold-argument  \
    --FunctionName test \
    --ReservedConcurrencyMem 12800
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

