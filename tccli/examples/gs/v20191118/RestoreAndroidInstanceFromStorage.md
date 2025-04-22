**Example 1: 示例**

示例

Input: 

```
tccli gs RestoreAndroidInstanceFromStorage --cli-unfold-argument  \
    --AndroidInstanceId cai-251006279-ea99K3EZgPo \
    --ObjectKey test-object \
    --StorageType S3 \
    --S3Options.EndPoint test-end-point \
    --S3Options.Bucket test-bucket \
    --S3Options.AccessKeyId test-key-id \
    --S3Options.SecretAccessKey test-key
```

Output: 
```
{
    "Response": {
        "RequestId": "f2ed9fc0-a946-41aa-93be-86afb2cd1375",
        "TaskId": "7a9dfd20-d6f3-4488-97b1-02fa76eec053"
    }
}
```

