**Example 1: 获取集群命名空间列表**



Input: 

```
tccli wedata DescribeClusterNamespaceList --cli-unfold-argument  \
    --ClusterId xx \
    --ProjectId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Namespaces": [
            {
                "Status": "xx",
                "Name": "xx",
                "CreatedAt": "xx"
            }
        ]
    }
}
```

