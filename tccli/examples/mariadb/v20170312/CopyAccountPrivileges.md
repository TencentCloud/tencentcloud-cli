**Example 1: Copying TencentDB account permissions**



Input: 

```
tccli mariadb CopyAccountPrivileges --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh \
    --DstUserName testuser2 \
    --DstHost % \
    --SrcUserName testuser1 \
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

