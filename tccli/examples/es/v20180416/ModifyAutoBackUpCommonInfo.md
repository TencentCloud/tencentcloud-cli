**Example 1: demo**



Input: 

```
tccli es ModifyAutoBackUpCommonInfo --cli-unfold-argument  \
    --InstanceId es-m6d4maox \
    --CosBackupCommonInfo.CosEncryption 1 \
    --CosBackupCommonInfo.KmsKey 7d7ab665-c03a-11f0-9d19-6a80edb7c8d5
```

Output: 
```
{
    "Response": {
        "Status": true,
        "RequestId": "602b7b48-25ac-465c-a0bf-b6a7196ca869"
    }
}
```

