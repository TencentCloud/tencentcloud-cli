**Example 1: Modifying the password of a TencentDB instance account**



Input: 

```
tccli cdb ModifyAccountPassword --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --Accounts.0.user ajnnw \
    --NewPassword Gx18ux23F^X \
    --Accounts.0.host 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

