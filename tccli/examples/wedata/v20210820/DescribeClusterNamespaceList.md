**Example 1: 获取集群命名空间列表**



Input: 

```
tccli wedata DescribeClusterNamespaceList --cli-unfold-argument  \
    --ClusterId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Namespaces": [
            {
                "Status": "abc",
                "Name": "abc",
                "CreatedAt": "abc"
            }
        ]
    }
}
```

