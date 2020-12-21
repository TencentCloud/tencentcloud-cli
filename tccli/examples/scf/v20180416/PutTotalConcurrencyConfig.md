**Example 1: 设置用户并发内存配额**



Input: 

```
tccli scf PutTotalConcurrencyConfig --cli-unfold-argument  \
    --TotalConcurrencyMem 128000
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

