**Example 1: 查询逃逸白名单**



Input: 

```
tccli tcss DescribeEscapeWhiteList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ContainerCount": 0,
                "EventType": [
                    "MOUNT_SENSITIVE_PTAH"
                ],
                "HostCount": 4,
                "ID": 7172,
                "ImageID": "sha256:a24bb4013296f61e89ba57005a7b3e52274d8edd3ae2077d04395f806b63d83e",
                "ImageName": "alpine:3.12.0",
                "ImageSize": 10000000,
                "InsertTime": "2024-10-17 22:31:18",
                "UpdateTime": "2024-10-27 08:51:02"
            }
        ],
        "RequestId": "ef5c9885-aaaa-bbbb-cccc-4fccf03883cf",
        "TotalCount": 1
    }
}
```

