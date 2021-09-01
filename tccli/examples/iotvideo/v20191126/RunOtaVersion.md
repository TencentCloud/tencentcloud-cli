**Example 1: 固件版本正式发布**



Input: 

```
tccli iotvideo RunOtaVersion --cli-unfold-argument  \
    --ProductId 12345678910 \
    --OtaVersion 1.1.1 \
    --OldVersions 0.9.0 0.9.1 \
    --GrayValue 60 \
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

