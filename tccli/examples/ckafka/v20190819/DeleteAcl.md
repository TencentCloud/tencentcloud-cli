**Example 1: 删除ACL**



Input: 

```
tccli ckafka DeleteAcl --cli-unfold-argument  \
    --InstanceId xxx \
    --ResourceType 2 \
    --ResourceName 1 \
    --Operation 2 \
    --PermissionType 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnMessage": "ok[apply ok]",
            "ReturnCode": "0",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "2140f435-b350-4429-a105-9b83efe104b0"
    }
}
```

