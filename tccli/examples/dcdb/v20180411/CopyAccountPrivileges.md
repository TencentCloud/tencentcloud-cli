**Example 1: Copying the permissions of a TencentDB account**



Input: 

```
tccli dcdb CopyAccountPrivileges --cli-unfold-argument  \
    --InstanceId dcdbt-fdpjf5zh\
    --DstUserName testuser2\
    --DstHost %\
    --SrcUserName testuser1\
    --SrcHost 172.17.%
```

Output: 
```
{
    "Response": {
        "RequestId": "95208d7c-66dc-446c-bc03-856738604611"
    }
}
```

