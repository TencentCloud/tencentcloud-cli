**Example 1: 查看实例列表**



Input: 

```
tccli tcr DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Registries": [
            {
                "RegistryId": "cls-xxxxxxx",
                "RegistryName": "aaa",
                "Status": "Running",
                "RegistryType": "standard",
                "PublicDomain": "mytest.tencentcloudcr.com",
                "InternalEndpoint": "8.9.10.9",
                "ExpiredAt": "2020-09-10",
                "PayMod": 1,
                "RenewFlag": 1
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

