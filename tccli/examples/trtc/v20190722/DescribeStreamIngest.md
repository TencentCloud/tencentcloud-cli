**Example 1: 查询任务**

查询SdkAppId为1234567890下的TaskId为1234的任务状态

Input: 

```
tccli trtc DescribeStreamIngest --cli-unfold-argument  \
    --SdkAppId 1234567890 \
    --TaskId 1234
```

Output: 
```
{
    "Response": {
        "Status": "InProgress",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

