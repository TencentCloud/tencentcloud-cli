**Example 1: 添加仿冒上报链接**



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

