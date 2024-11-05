**Example 1: 查询资源包使用详情**

查询资源包使用详情


Input: 

```
tccli cynosdb DescribeResourcePackageDetail --cli-unfold-argument  \
    --PackageId package-twox8tqx \
    --ClusterIds cynosdbmysql-ou5cnw2x \
    --StartTime 2024-09-28 10:11:23 \
    --EndTime 2024-10-28 10:11:23 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Total": 20,
        "Detail": [
            {
                "AppId": 251232125,
                "PackageId": "package-abcr4312",
                "InstanceId": "cynosdbmysql-ins-anji1234",
                "SuccessDeductSpec": 100,
                "PackageTotalUsedSpec": 200,
                "StartTime": "2020-01-01 00:00:01",
                "EndTime": "2020-01-02 00:00:01",
                "ExtendInfo": "{\"ClusterId\":\"cynosdbmysql-i58mvikj\",\"RequestId\":\"1724306460000666497_c7bedc2d-3454-4fe9-9768-335a9901f10f\"}"
            }
        ],
        "RequestId": "3d56fe0b-f839-42c6-b84e-1d5fbc874cba"
    }
}
```

