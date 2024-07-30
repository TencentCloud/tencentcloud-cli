**Example 1: 缩容API**



Input: 

```
tccli cdwdoris ReduceInstance --cli-unfold-argument  \
    --InstanceId cdwdoris-xqewrqx \
    --Type MASTER \
    --DelHosts 10.0.1.12 \
    --HaType 1
```

Output: 
```
{
    "Response": {
        "FlowId": "1231",
        "InstanceId": "cdwdoris-xqewrqx",
        "ErrorMsg": "",
        "RequestId": "xasdfkqe2-a12q29-axdfas"
    }
}
```

