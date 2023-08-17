**Example 1: 查询j集群CHDFS权限组**

查询j集群CHDFS权限组



Input: 

```
tccli oceanus DescribeCHDFSAccessGroups --cli-unfold-argument  \
    --ClusterId cluster-abc \
    --WorkSpaceId space-abc
```

Output: 
```
{
    "Response": {
        "CHDFSAccessGroups": [
            {
                "AccessGroupId": "ag-abc",
                "AccessGroupName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

