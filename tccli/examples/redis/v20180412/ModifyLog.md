**Example 1: 请求示例**



Input: 

```
tccli redis ModifyLog --cli-unfold-argument  \
    --InstanceId crs-kqqge823 \
    --LogType auditLog \
    --LogSubType write \
    --LogExpireDay 7 \
    --HighLogExpireDay 7 \
    --DegradeStrategy 600
```

Output: 
```
{
    "Response": {
        "RequestId": "2feabd25-287c-4530-9612-173246e3ac50"
    }
}
```

