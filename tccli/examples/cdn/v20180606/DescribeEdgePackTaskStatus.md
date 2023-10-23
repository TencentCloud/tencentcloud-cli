**Example 1: 查询动态打包任务状态列**



Input: 

```
tccli cdn DescribeEdgePackTaskStatus --cli-unfold-argument  \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EdgePackTaskStatusSet": [
            {
                "Apk": "test.apk",
                "UploadTime": "2020-09-22T00:00:00+00:00",
                "SrcDir": [
                    "/src/"
                ],
                "DstDir": "/ext/",
                "StatusDesc": "",
                "Status": "done"
            }
        ],
        "RequestId": "9b231c10-72a3-4a92-8498-ffxxxxxxx"
    }
}
```

