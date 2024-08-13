**Example 1:  修改CAM用户同步**

 修改CAM用户同步

Input: 

```
tccli organization UpdateUserSyncProvisioning --cli-unfold-argument  \
    --ZoneId z-susn8xnsis \
    --UserProvisioningId up-xusjdjsss \
    --NewDescription this is cam user sync \
    --NewDuplicationStateful KeepBoth \
    --NewDeletionStrategy Delete
```

Output: 
```
{
    "Response": {
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

