**Example 1: 查询刷新用量配额**



Input: 

```
tccli cdn DescribePurgeQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "aee6dbe4-f790-417e-8801-5a1894e8fdba",
        "UrlPurge": [
            {
                "Area": "mainland",
                "Batch": 1000,
                "Total": 10000,
                "Available": 10000
            },
            {
                "Area": "overseas",
                "Batch": 1000,
                "Total": 10000,
                "Available": 10000
            }
        ],
        "PathPurge": [
            {
                "Area": "mainland",
                "Batch": 39,
                "Total": 100,
                "Available": 100
            },
            {
                "Area": "overseas",
                "Batch": 20,
                "Total": 100,
                "Available": 100
            }
        ]
    }
}
```

