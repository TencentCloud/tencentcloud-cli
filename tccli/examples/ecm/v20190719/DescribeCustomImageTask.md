**Example 1: 查询导入镜像任务**



Input: 

```
tccli ecm DescribeCustomImageTask --cli-unfold-argument  \
    --Filters.0.Name task-id \
    --Filters.0.Values 21
```

Output: 
```
{
    "Response": {
        "ImageTaskSet": [
            {
                "Message": "success",
                "State": "SUCCESS",
                "ImageName": "ecmtest",
                "CreateTime": "2020-06-16 15:43:30"
            }
        ],
        "TotalCount": 1,
        "RequestId": "854aeb35-e3e0-451d-87ad-b0894b99cea4"
    }
}
```

