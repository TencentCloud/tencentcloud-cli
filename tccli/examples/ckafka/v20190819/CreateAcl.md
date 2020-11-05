**Example 1: Adding ACL policy**



Input: 

```
tccli ckafka CreateAcl --cli-unfold-argument  \
    --InstanceId xxx\
    --ResourceType xxx\
    --ResourceName 1\
    --Operation 2\
    --PermissionType 2\
    --Host 2\
    --Principal 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]"
        },
        "RequestId": "b1ce770b-3623-47d3-b31b-538f8941142d"
    }
}
```

