**Example 1: 批量销毁实例（部分成功）**

批量销毁两个实例，其中一个因状态不允许而失败。

Input: 

```
tccli edgezone TerminateInstances --cli-unfold-argument  \
    --InstanceIds epm-mnop3456 epm-abcd1234
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "bms-mnop3456"
        ],
        "FailedInstanceSet": [
            {
                "InstanceId": "bms-abcd1234",
                "ErrorCode": "UnsupportedOperation.InvalidInstanceState",
                "ErrorMessage": "Instance bms-abcd1234 is in allocating status, cannot terminate"
            }
        ],
        "RequestId": "f2a3b456-7c8d-9e0f-1a2b-3c4d5e6f7a8b"
    }
}
```

**Example 2: 销毁单个实例**

销毁指定实例，成功后实例状态变更为 terminating。

Input: 

```
tccli edgezone TerminateInstances --cli-unfold-argument  \
    --InstanceIds epm-mnop3456
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "bms-mnop3456"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

