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
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "List": [
            {
                "Status": "SUCCESS",
                "AuthorizedTime": "2022-01-01 00:00:00",
                "ImageName": "镜像名称",
                "IsAuthorized": 1,
                "ImageId": "镜像id image-id"
            }
        ]
    }
}
```

