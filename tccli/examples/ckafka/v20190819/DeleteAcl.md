**Example 1: Deleting ACL**



Input: 

```
tccli ckafka DeleteAcl --cli-unfold-argument  \
    --InstanceId xxx\
    --ResourceType xxx\
    --ResourceName 1\
    --Operation 2\
    --PermissionType 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]"
        },
        "RequestId": "2140f435-b350-4429-a105-9b83efe104b0"
    }
}
```

