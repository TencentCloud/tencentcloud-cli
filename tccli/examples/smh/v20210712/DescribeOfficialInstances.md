**Example 1: 查询官方实例**



Input: 

```
tccli smh DescribeOfficialInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "InstanceId": "jexrwwoa",
                "Domain": "jexrwwoa.cofile.net",
                "EffectiveTime": "2021-11-17T03:03:45Z",
                "ExpireTime": "2021-12-17T23:59:59Z",
                "UserLimit": 5,
                "StorageLimit": "53687091200",
                "StorageLimitGB": 50,
                "Isolated": false,
                "AutoRenew": 1,
                "SuperAdminAccount": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "27ec9933-ad39-46b0-9ea1-f863a89dd00c"
    }
}
```

