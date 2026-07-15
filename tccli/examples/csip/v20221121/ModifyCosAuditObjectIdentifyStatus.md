**Example 1: 修改对象存储识别开关状态**



Input: 

```
tccli csip ModifyCosAuditObjectIdentifyStatus --cli-unfold-argument  \
    --ResourceId cos-audit-757d9973 \
    --TextIdentifyStatus 1 \
    --ImageIdentifyStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "dfa48ae2-857d-460f-b194-ad4f267f6050"
    }
}
```

