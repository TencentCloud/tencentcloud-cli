**Example 1: 查询任务状态**

查询任务状态

Input: 

```
tccli wedata QueryJobStatus --cli-unfold-argument  \
    --JobId 6820260206163217095 \
    --WorkspaceId 17678671667189298
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1770366737",
            "EndTime": "0",
            "JobErrCode": 1134102,
            "JobErrMsg": "type:business, code:1133104, msg:[TencentCloudSDKError] Code=InvalidParameter, Message=InvalidParameter\n{\"errStr\":\"InvalidParameter\",\"errDesc\":\"InvalidParameter\",\"errCode\":\"13000\",\"errMsg\":\"ResourceGroupName  not exist\"}, RequestId=4af46fc1-6f86-494f-abdc-f2cb171295d1",
            "JobId": "6820260206163217095",
            "JobStatus": "LAUNCHED",
            "Progress": 0,
            "StartTime": "0",
            "SubJobs": []
        },
        "RequestId": "0ff85de7-8215-488a-8390-fe28ea309e5f"
    }
}
```

