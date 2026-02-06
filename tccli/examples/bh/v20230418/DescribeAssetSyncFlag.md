**Example 1: 查询是否开启资产自动同步**

查询是否开启资产自动同步

Input: 

```
tccli bh DescribeAssetSyncFlag --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "AssetSyncFlags": {
            "RoleGranted": true,
            "AutoSync": true
        }
    }
}
```

