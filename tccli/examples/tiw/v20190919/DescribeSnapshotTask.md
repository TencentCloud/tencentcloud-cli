**Example 1: 获取任务信息**



Input: 

```
tccli tiw DescribeSnapshotTask --cli-unfold-argument  \
    --SdkAppId 1400127230 \
    --TaskID f2e1728c-6e87-4481-abe1-cde8542a5a10
```

Output: 
```
{
    "Response": {
        "CreateTime": 1626249427,
        "FinishTime": 1626250455,
        "RequestId": "38d75752-85e0-4931-9837-d41be5409a0a",
        "Result": {
            "ErrorCode": "OK",
            "ErrorMessage": "",
            "Snapshots": [
                "http://tiw-snapshot-1259648581.cos.ap-guangzhou.myqcloud.com/880520/f2e1728c-6e87-4481-abe1-cde8542a5a10/53255368873480.png",
                "http://tiw-snapshot-1259648581.cos.ap-guangzhou.myqcloud.com/880520/f2e1728c-6e87-4481-abe1-cde8542a5a10/53255373174978.png",
                "http://tiw-snapshot-1259648581.cos.ap-guangzhou.myqcloud.com/880520/f2e1728c-6e87-4481-abe1-cde8542a5a10/53255375472670.png"
            ],
            "Total": 3
        },
        "Status": "Finished",
        "TaskID": "f2e1728c-6e87-4481-abe1-cde8542a5a10"
    }
}
```

