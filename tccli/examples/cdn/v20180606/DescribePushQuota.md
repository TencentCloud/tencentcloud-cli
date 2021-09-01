**Example 1: 查询预热用量配额**



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

