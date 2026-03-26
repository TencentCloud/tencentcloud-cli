**Example 1: 请求示例**



Input: 

```
tccli redis OpenLog --cli-unfold-argument  \
    --InstanceId crs-k2vhnkix \
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
        "RequestId": "8936d9b0-3819-479d-855e-919422cffdb9"
    }
}
```

