**Example 1: 获取资源套餐和增值包摘要信息**



Input: 

```
tccli adp DescribeResourceSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AddOnPackage": {
            "AddOnTotal": 0,
            "AddOnUsage": 0,
            "ConcurrencyStatus": 1,
            "ExclusiveComputeUnit": 0,
            "ExclusiveComputeUnitStatus": 1,
            "ExclusiveConcurrency": 0,
            "ExclusiveTpm": 0,
            "ExclusiveTpmStatus": 1,
            "ResourceStatus": 1
        },
        "ResourcePackage": {
            "KnowledgeCapacity": 0,
            "KnowledgeUsage": 0,
            "PackageType": 2,
            "ResourceStatus": 3,
            "ResourceTotal": 150000,
            "ResourceUsage": 150000
        },
        "RequestId": "556a8474-d04f-4d1d-a660-982d99a8f05c"
    }
}
```

