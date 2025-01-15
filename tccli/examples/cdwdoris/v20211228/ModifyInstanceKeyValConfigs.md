**Example 1: 示例**



Input: 

```
tccli cdwdoris ModifyInstanceKeyValConfigs --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --FileName fe.conf \
    --UpdateItems.0.ConfKey balance_slot_num_per_path \
    --UpdateItems.0.ConfValue 13 \
    --Message add config
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "117ad1ab-8571-4085-8356-382b6a5f07f6",
        "FlowId": 8271
    }
}
```

