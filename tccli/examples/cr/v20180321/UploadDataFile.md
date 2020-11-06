**Example 1: 上传到期/逾期提醒文件**



Input: 

```
tccli cr UploadDataFile --cli-unfold-argument  \
    --Module Data \
    --Operation Upload \
    --FileName data_1542284923873.xlsx
%FileUrl
```

Output: 
```
{
    "Response": {
        "DataResId": "tad-iccc970kgp",
        "RequestId": "13cb0b60-6e0d-43e2-9123-b9361bf0f93e"
    }
}
```

**Example 2: 上传还款文件**



Input: 

```
tccli cr UploadDataFile --cli-unfold-argument  \
    --Module Data \
    --Operation Upload \
    --UploadModel repay \
    --FileName data_1542284924562.xlsx
%FileUrl
```

Output: 
```
{
    "Response": {
        "DataResId": "tad-qccc310kgp",
        "RequestId": "13cb0b60-1e0d-43e2-9123-b3361bf0f93e"
    }
}
```

