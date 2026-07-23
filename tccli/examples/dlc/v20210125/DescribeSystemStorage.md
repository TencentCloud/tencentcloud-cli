**Example 1: 查询指定的托管存储的系统目录**



Input: 

```
tccli dlc DescribeSystemStorage --cli-unfold-argument  \
    --Type 0
```

Output: 
```
{
    "Response": {
        "LakeFileSystem": {
            "Resource": "xx",
            "AccessToken": {
                "SecretKey": "xx",
                "Token": "xx",
                "SecretId": "xx",
                "ExpiredTime": 0,
                "IssueTime": 0
            },
            "Region": "xx",
            "Namespace": "xx",
            "Uri": "xx",
            "Schema": "xx"
        },
        "RequestId": "xx"
    }
}
```

