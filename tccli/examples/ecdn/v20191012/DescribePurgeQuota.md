**Example 1: DescribePurgeQuota**



Input: 

```
tccli ecdn DescribePurgeQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6f5a231e-f629-42fa-a9f0-5a9ebc127c04",
        "UrlPurge": {
            "Batch": 1000,
            "Total": 10000,
            "Available": 10000
        },
        "PathPurge": {
            "Batch": 20,
            "Total": 100,
            "Available": 100
        }
    }
}
```

