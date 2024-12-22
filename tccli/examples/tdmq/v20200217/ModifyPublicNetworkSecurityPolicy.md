**Example 1: 示例**



Input: 

```
tccli tdmq ModifyPublicNetworkSecurityPolicy --cli-unfold-argument  \
    --InstanceId pulsar-47emajuiaoam \
    --PolicyList.0.Route 1.1.1.1/24 \
    --PolicyList.0.Policy True \
    --PolicyList.0.Remark allow
```

Output: 
```
{
    "Response": {
        "ModifyResult": "SUCCESS",
        "InstanceId": "pulsar-47emajuiaoam",
        "RequestId": "5d6c7091-e82c-4a9c-a18f-34d5fc46006e"
    }
}
```

