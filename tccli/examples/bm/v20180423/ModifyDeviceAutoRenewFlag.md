**Example 1: 修改物理机服务器自动续费标志**



Input: 

```
tccli bm ModifyDeviceAutoRenewFlag --cli-unfold-argument  \
    --InstanceIds cpm-xxx0 cpm-xxx1 \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "40628e2b-13c2-4456-8c81-8f3e017b5562"
    }
}
```

