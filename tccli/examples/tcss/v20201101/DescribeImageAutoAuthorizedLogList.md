**Example 1: 查询镜像自动授权结果列表**



Input: 

```
tccli tcss DescribeImageAutoAuthorizedLogList --cli-unfold-argument  \
    --TaskId 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "List": [
            {
                "Status": "SUCCESS",
                "AuthorizedTime": "xx",
                "ImageName": "xx",
                "IsAuthorized": 1,
                "ImageId": "xx"
            }
        ]
    }
}
```

