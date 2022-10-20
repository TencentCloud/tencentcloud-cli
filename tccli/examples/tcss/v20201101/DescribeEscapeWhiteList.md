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
        "TotalCount": 1,
        "List": [
            {
                "UpdateTime": "xx",
                "ImageSize": 0,
                "EventType": [
                    "xx"
                ],
                "HostCount": 0,
                "ImageID": "xx",
                "ImageName": "xx",
                "ContainerCount": 0,
                "InsertTime": "xx",
                "ID": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

