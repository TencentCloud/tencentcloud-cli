**Example 1: 添加仿冒链接（举报）**



Input: 

```
tccli bma CreateBPFakeURL --cli-unfold-argument  \
    --ProtectURLId 123 \
    --FakeURL xxx \
    --SnapshotNames xxx yyy \
    --Note xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

