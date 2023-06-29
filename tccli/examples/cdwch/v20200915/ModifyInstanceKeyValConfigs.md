**Example 1: 示例**



Input: 

```
tccli cdwch ModifyInstanceKeyValConfigs --cli-unfold-argument  \
    --InstanceId xx \
    --UpdateItems.0.ConfKey xx \
    --UpdateItems.0.ConfValue xx \
    --DeleteItems.ConfKey xx \
    --DeleteItems.ConfValue xx \
    --AddItems.0.ConfKey xx \
    --AddItems.0.ConfValue xx
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "xx",
        "RequestId": "xx",
        "FlowId": 0
    }
}
```

