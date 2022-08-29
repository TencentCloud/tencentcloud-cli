**Example 1: 查询USG属性**



Input: 

```
tccli vpc DescribeUSGInternal --cli-unfold-argument  \
    --GetUSGRequest.0.Id sg-aassaa
```

Output: 
```
{
    "Response": {
        "USGSet": [
            {
                "Sys": 0,
                "ProjectId": "0",
                "SgName": "test_all",
                "ErrorCode": 0,
                "AppId": "251197522",
                "SafeGroupId": "sg-5q4brrmt",
                "Os": 0,
                "CreateTime": "2021-12-08 21:00:33",
                "SgRemark": "自定义"
            },
            {
                "Sys": 0,
                "ProjectId": "0",
                "SgName": "test_pro",
                "ErrorCode": 0,
                "AppId": "251197522",
                "SafeGroupId": "sg-h4q2qsjv",
                "Os": 0,
                "CreateTime": "2021-12-02 11:03:42",
                "SgRemark": "自定义"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: demo**



Input: 

```
tccli vpc DescribeUSGInternal --cli-unfold-argument  \
    --GetUSGRequest.0.Id sg-5q4brrmt
```

Output: 
```
{
    "Response": {
        "USGSet": [
            {
                "Sys": 0,
                "ProjectId": "0",
                "SgName": "test_all",
                "ErrorCode": 0,
                "AppId": "251197522",
                "SafeGroupId": "sg-5q4brrmt",
                "Os": 0,
                "CreateTime": "2021-12-08 21:00:33",
                "SgRemark": "自定义"
            }
        ],
        "RequestId": "21d73a37-a0a8-4801-b9f2-df428c26d9e8"
    }
}
```

