**Example 1: 查询预热用量配额**

用于查询预热配额和每日可用量。

Input: 

```
tccli cdn DescribePushQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6f5a231e-f629-42fa-a9f0-5a9ebc127c04",
        "UrlPush": [
            {
                "Batch": 1000,
                "Total": 10000,
                "Available": 10000,
                "Area": "mainland"
            }
        ]
    }
}
```

