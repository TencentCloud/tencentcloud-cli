**Example 1: 修改固件升级任务状态为取消状态**

当固件任务在升级过程需要取消时可使用。或修改为其它允许的状态

Input: 

```
tccli iotcloud UpdateOtaTaskStatus --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --TaskId 10000 \
    --Status 6
```

Output: 
```
{
    "Response": {
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbc"
    }
}
```

