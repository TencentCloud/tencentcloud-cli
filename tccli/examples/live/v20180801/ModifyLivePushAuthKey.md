**Example 1: 请求示例**

请求示例。

Input: 

```
tccli live ModifyLivePushAuthKey --cli-unfold-argument  \
    --DomainName abc.com \
    --Enable 0 \
    --MasterAuthKey abc*&^ \
    --BackupAuthKey  \
    --AuthDelta 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e48b9f8d-d9d1-4de4-a732-5ab8a333c0d8"
    }
}
```

