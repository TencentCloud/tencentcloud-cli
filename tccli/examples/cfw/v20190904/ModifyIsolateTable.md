**Example 1: 编辑隔离有效期**

使用 DescribeCfwRules（RuleType=intrusion_prevention、ListType=isolate、InstanceId）返回的 rules[].instance_id 编辑隔离有效期。

Input: 

```
tccli cfw ModifyIsolateTable --cli-unfold-argument  \
    --InstanceID ins-doc-isolate-001 \
    --ButtonAction edit \
    --StartTime 2025-01-01 00:00:00 \
    --EndTime 3000-01-01 00:00:00
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

**Example 2: 解除隔离**

使用 DescribeCfwRules（RuleType=intrusion_prevention、ListType=isolate、InstanceId）返回的 rules[].instance_id 解除隔离；delete 不传时间参数。

Input: 

```
tccli cfw ModifyIsolateTable --cli-unfold-argument  \
    --InstanceID ins-doc-isolate-002 \
    --ButtonAction delete
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "00000000-0000-4000-8000-000000000002"
    }
}
```

