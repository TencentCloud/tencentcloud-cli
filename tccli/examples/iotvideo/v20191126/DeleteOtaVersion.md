**Example 1: 删除固件版本信息**



Input: 

```
tccli iotvideo DeleteOtaVersion --cli-unfold-argument  \
    --ProductId 12345678910 \
    --OtaVersion 1.1.1 \
    --Operator zhangsan
```

Output: 
```
{
    "Response": {
        "RequestId": "9396ceb0-4abd-4b8a-b991-abff1131c334"
    }
}
```

