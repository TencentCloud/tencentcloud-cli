**Example 1: 获取NFS扫描全局配置**

获取NFS扫描全局配置

Input: 

```
tccli csip DescribeNFSScanConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Enable": 1,
        "ExcludeQuuid": [
            "3913529d-2d2c-485a-b07b-384f28781452"
        ],
        "IncludeQuuid": [
            "3913529d-2d2c-485a-b07b-384f28781452"
        ],
        "Scope": 1,
        "RequestId": "0cafa484-a508-42b8-908a-3c647cef761e"
    }
}
```

