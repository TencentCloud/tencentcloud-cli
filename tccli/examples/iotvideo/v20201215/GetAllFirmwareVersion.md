**Example 1: 获取所有版本列表**



Input: 

```
tccli iotvideo GetAllFirmwareVersion --cli-unfold-argument  \
    --ProductID asdfbasd
```

Output: 
```
{
    "Response": {
        "Version": [
            "1.0.0",
            "1.0.1"
        ],
        "RequestId": "xx"
    }
}
```

