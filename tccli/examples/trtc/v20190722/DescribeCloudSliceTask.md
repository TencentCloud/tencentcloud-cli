**Example 1: 查询切片任务信息**



Input: 

```
tccli trtc DescribeCloudSliceTask --cli-unfold-argument  \
    --SdkAppId 20010806 \
    --TaskId -nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ..
```

Output: 
```
{
    "Response": {
        "RequestId": "dc45d9cd-f615-43a5-943e-89f559cb3f7b",
        "Status": "InProgress",
        "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
    }
}
```

