**Example 1: 申请上传单个文件临时凭证**

申请上传单个文件临时凭证

Input: 

```
tccli vod CreateStorageCredentials --cli-unfold-argument  \
    --SubAppId 220209 \
    --DurationSeconds 7200 \
    --Policy %7B%22statement%22%3A%5B%7B%22action%22%3A%5B%22name%2Fvod%3AInitiateMultipartUpload%22%2C%22name%2Fvod%3AListMultipartUploads%22%2C%22name%2Fvod%3AListParts%22%2C%22name%2Fvod%3AUploadPart%22%2C%22name%2Fvod%3ACompleteMultipartUpload%22%5D%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%5B%22qcs%3A%3Avod%3Aap-beijing%3Auid%2F251197738%3Aprefix%2F%2F220209%2Fa%2F001.png%22%5D%7D%5D%2C%22version%22%3A%222.0%22%7D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "SessionToken": "***********************************",
            "AccessKeyId": "***********************************",
            "SecretAccessKey": "***********************************",
            "Expiration": "2024-08-20T13:55:53Z"
        },
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

**Example 2: 申请上传多个文件临时凭证**

申请上传多个文件临时凭证

Input: 

```
tccli vod CreateStorageCredentials --cli-unfold-argument  \
    --SubAppId 220209 \
    --DurationSeconds 7200 \
    --Policy %7B%22statement%22%3A%5B%7B%22action%22%3A%5B%22name%2Fvod%3AInitiateMultipartUpload%22%2C%22name%2Fvod%3AListMultipartUploads%22%2C%22name%2Fvod%3AListParts%22%2C%22name%2Fvod%3AUploadPart%22%2C%22name%2Fvod%3ACompleteMultipartUpload%22%5D%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%5B%22qcs%3A%3Avod%3Aap-beijing%3Auid%2F251197738%3Aprefix%2F%2F220209%2Fa%2F1024x1024.png%22%2C%22qcs%3A%3Avod%3Aap-beijing%3Auid%2F251197738%3Aprefix%2F%2F220209%2Fa%2Fb%2Fc%2F1042x1042.png%22%2C%22qcs%3A%3Avod%3Aap-beijing%3Auid%2F251197738%3Aprefix%2F%2F220209%2Fpath%2F2060.gif_wh300.gif%22%5D%7D%5D%2C%22version%22%3A%222.0%22%7D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "SessionToken": "***********************************",
            "AccessKeyId": "***********************************",
            "SecretAccessKey": "***********************************",
            "Expiration": "2024-08-20T13:55:53Z"
        },
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

**Example 3: 申请列出桶内指定对象键前缀所有对象的临时凭证**

申请列出桶内指定对象键前缀所有对象的临时凭证

Input: 

```
tccli vod CreateStorageCredentials --cli-unfold-argument  \
    --SubAppId 220209 \
    --DurationSeconds 7200 \
    --Policy %7B%22statement%22%3A%5B%7B%22action%22%3A%5B%22name%2Fvod%3AGetBucket%22%5D%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%5B%22qcs%3A%3Avod%3Aap-beijing%3Auid%2F251197738%3Aprefix%2F%2F220209%2F98gw6e1b4hds0zh%2F%22%5D%7D%5D%2C%22version%22%3A%222.0%22%7D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "SessionToken": "***********************************",
            "AccessKeyId": "***********************************",
            "SecretAccessKey": "***********************************",
            "Expiration": "2024-08-20T13:55:53Z"
        },
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

**Example 4: 申请自动就近上传文件的临时凭证**

申请自动就近上传文件的临时凭证

Input: 

```
tccli vod CreateStorageCredentials --cli-unfold-argument  \
    --SubAppId 220209 \
    --DurationSeconds 7200 \
    --Policy %7B%22statement%22%3A%5B%7B%22action%22%3A%5B%22name%2Fvod%3AInitiateMultipartUpload%22%2C%22name%2Fvod%3AListMultipartUploads%22%2C%22name%2Fvod%3AListParts%22%2C%22name%2Fvod%3AUploadPart%22%2C%22name%2Fvod%3ACompleteMultipartUpload%22%5D%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%5B%22qcs%3A%3Avod%3Aauto%3Auid%2F251197738%3Aprefix%2F%2F220209%2Fauto%2F001.png%22%5D%7D%5D%2C%22version%22%3A%222.0%22%7D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "SessionToken": "***********************************",
            "AccessKeyId": "***********************************",
            "SecretAccessKey": "***********************************",
            "Expiration": "2024-08-20T13:55:53Z"
        },
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

