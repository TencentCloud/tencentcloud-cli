**Example 1: 获取物模型历史版本列表**



Input: 

```
tccli iotvideo DescribeIotModels --cli-unfold-argument  \
    --ProductId 12345678910
```

Output: 
```
{
    "Response": {
        "RequestId": "fdc630bb-80f4-4e11-863e-138e9a90a0c6",
        "Data": [
            {
                "Revision": 1,
                "ReleaseTime": 1578363614
            }
        ]
    }
}
```

