**Example 1: 查询资源包使用详情**

查询资源包使用详情


Input: 

```
tccli cynosdb DescribeResourcePackageDetail --cli-unfold-argument  \
    --PackageId abc \
    --ClusterIds abc \
    --StartTime abc \
    --EndTime abc \
    --Offset abc \
    --Limit abc
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Detail": [
            {
                "AppId": 0,
                "PackageId": "abc",
                "InstanceId": "abc",
                "SuccessDeductSpec": 0,
                "PackageTotalUsedSpec": 0,
                "StartTime": "abc",
                "EndTime": "abc",
                "ExtendInfo": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

