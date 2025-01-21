**Example 1: 实例一**



Input: 

```
tccli dlc DescribeLakeFsTaskResult --cli-unfold-argument  \
    --FsPath lakefs://*@dlc7e43-*-*-*-*/*/.system/result/20250109/*
```

Output: 
```
{
    "Response": {
        "AccessToken": {
            "SecretId": "AKI***",
            "SecretKey": "D7****y",
            "Token": "lod",
            "ExpiredTime": 1736421897,
            "IssueTime": 1736420097
        },
        "RequestId": "09d82a50-abc7-419a-a719-1062713d459c"
    }
}
```

