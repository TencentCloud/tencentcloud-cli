**Example 1: 查询镜像仓库命名空间列表**



Input: 

```
tccli csip DescribeImageRegistryNamespaceList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "NamespaceList": [
            {
                "Namespace": "csip"
            }
        ],
        "TotalCount": 5,
        "RequestId": "ee4b9f43-470e-472b-a937-4e1da081fc44"
    }
}
```

