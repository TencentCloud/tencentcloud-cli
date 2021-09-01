**Example 1: 固件版本测试发布**



Input: 

```
tccli iotvideo RunTestOtaVersion --cli-unfold-argument  \
    --ProductId 12345678910 \
    --OtaVersion 1.1.1 \
    --Tids xxx0 xxx1 \
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

