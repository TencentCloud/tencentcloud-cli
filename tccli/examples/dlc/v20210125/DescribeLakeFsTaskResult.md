**Example 1: 实例一**



Input: 

```
tccli dlc DescribeLakeFsTaskResult --cli-unfold-argument  \
    --FsPath abc
```

Output: 
```
{
    "Response": {
        "AccessToken": {
            "SecretId": "abc",
            "SecretKey": "abc",
            "Token": "abc",
            "ExpiredTime": 0,
            "IssueTime": 0
        },
        "RequestId": "abc"
    }
}
```

