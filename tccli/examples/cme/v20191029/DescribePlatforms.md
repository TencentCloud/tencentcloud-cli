**Example 1: 获取所有创建的平台列表**



Input: 

```
tccli cme DescribePlatforms --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PlatformInfoSet": [
            {
                "Platform": "1112",
                "Status": "Valid",
                "Description": "test",
                "VodSubAppId": 140000303,
                "LicenseId": "cmelid_8621ba0483c211ea90dc6c92bf621f6e",
                "CreateTime": "2018-12-01T13:00:00Z",
                "UpdateTime": "2018-12-01T13:00:00Z"
            }
        ],
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

**Example 2: 指定绑定的 License Id 获取平台列表**



Input: 

```
tccli cme DescribePlatforms --cli-unfold-argument  \
    --LicenseIds cmelid_8621ba0483c211ea90dc6c92bf621f6e
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PlatformInfoSet": [
            {
                "Platform": "1112",
                "Status": "Valid",
                "Description": "test",
                "VodSubAppId": 140000303,
                "LicenseId": "cmelid_8621ba0483c211ea90dc6c92bf621f6e",
                "CreateTime": "2018-12-01T13:00:00Z",
                "UpdateTime": "2018-12-01T13:00:00Z"
            }
        ],
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

