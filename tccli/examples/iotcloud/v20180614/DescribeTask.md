**Example 1: 获取任务详情**



Input: 

```
tccli iotcloud DescribeTask --cli-unfold-argument  \
    --Id 5ad5aa513332ea4cb86e9ad5
```

Output: 
```
{
    "Response": {
        "Type": "PublishMessage",
        "Id": "5ad5b9a53332ea3de678ea52",
        "ProductId": "ABCDE12345",
        "Status": 3,
        "CreateTime": 1523956133,
        "UpdateTime": 1523958284,
        "DoneTime": 1523956134,
        "ScheduleTime": 1523956133,
        "RetCode": 0,
        "ErrMsg": "",
        "Percent": 0,
        "AllDeviceCnt": 2,
        "DoneDeviceCnt": 2,
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

