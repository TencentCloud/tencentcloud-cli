**Example 1: 上传数据**



Input: 

```
tccli cr UploadDataJson --cli-unfold-argument  \
    --Module Data \
    --Operation UploadJson \
    --UploadModel repay \
    --Data {\"work_data\":\"o\"}
```

Output: 
```
{
    "Response": {
        "Data": "ok",
        "RequestId": "13ca0b60-ff5g-43e2-9123-b9361bf0f93e"
    }
}
```

