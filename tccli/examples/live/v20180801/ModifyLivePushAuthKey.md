**Example 1: Sample request**



Input: 

```
tccli live ModifyLivePushAuthKey --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com\
    --Enable 0\
    --MasterAuthKey xxxx\
    --BackupAuthKey xxx\
    --AuthDelta 300
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

