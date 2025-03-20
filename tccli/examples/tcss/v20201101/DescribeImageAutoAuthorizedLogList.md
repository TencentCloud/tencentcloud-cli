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
                "ImageName": "imageName-01",
                "IsAuthorized": 1,
                "ImageId": "sha256:707540fd8a54ab3ebc086ecc96d2d6143fd92c1cac4d0b23353e1b7078b5937b"
            }
        ]
    }
}
```

