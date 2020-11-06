**Example 1: 查询镜像仓库信息**

查询指定实例内全部镜像仓库

Input: 

```
tccli tcr DescribeRepositories --cli-unfold-argument  \
    --RegistryId tcr-f7g1ir99 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "772e3357-0b31-4b79-8afb-5b9835a3ada9",
        "RepositoryList": [
            {
                "Name": "mytest/tianzichen",
                "Namespace": "mytest",
                "CreationTime": "2020-02-27 01:07:14.503709 +0800 CST",
                "UpdateTime": "2020-02-27 01:07:14.503709 +0800 CST",
                "Public": false,
                "Description": "mytest",
                "BriefDescription": "test"
            }
        ],
        "TotalCount": 1
    }
}
```

