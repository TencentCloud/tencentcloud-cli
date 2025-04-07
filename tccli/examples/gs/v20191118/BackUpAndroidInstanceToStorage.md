**Example 1: 示例**

示例

Input: 

```
tccli gs BackUpAndroidInstanceToStorage --cli-unfold-argument  \
    --AndroidInstanceId cai-251006279-ea99K3EZgPo \
    --StorageType S3 \
    --ObjectKey testkey \
    --S3Options.EndPoint test-end-point \
    --S3Options.Bucket test-bucket \
    --S3Options.AccessKeyId test-key-id \
    --S3Options.SecretAccessKey test-key
```

Output: 
```
{
    "Response": {
        "RequestId": "e900f8c4-f1c5-455f-aeb2-a9b052fd8b73",
        "TaskId": "ddca8e2f-3b03-4c08-8f42-6e3533f09e7e"
    }
}
```

