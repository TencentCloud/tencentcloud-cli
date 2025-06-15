**Example 1: 示例**

示例

Input: 

```
tccli gs DeleteAndroidInstanceBackupFiles --cli-unfold-argument  \
    --AndroidInstanceZone ap-hangzhou-ec-1 \
    --ObjectKeys 1234/test1.bak 1234/test2.bak \
    --StorageType S3 \
    --S3Options.EndPoint http://192.168.1.10:9910 \
    --S3Options.Bucket testbucket \
    --S3Options.AccessKeyId admin \
    --S3Options.SecretAccessKey DFxjDF
```

Output: 
```
{
    "Response": {
        "RequestId": "92f73a08-f7a7-4092-b690-627878ab2e5b"
    }
}
```

