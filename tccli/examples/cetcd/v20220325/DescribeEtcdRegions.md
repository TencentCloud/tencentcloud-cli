**Example 1: 查看etcd支持地域**



Input: 

```
tccli cetcd DescribeEtcdRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Regions": [
            {
                "Alias": "gz",
                "RegionId": 1,
                "RegionName": "ap-guangzhou"
            }
        ],
        "RequestId": "32daac92-b940-4894-b9d8-1d325f1ee9d1"
    }
}
```

