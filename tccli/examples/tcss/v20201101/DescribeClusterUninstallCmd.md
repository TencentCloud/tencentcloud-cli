**Example 1: 查询集群卸载命令**



Input: 

```
tccli tcss DescribeClusterUninstallCmd --cli-unfold-argument  \
    --ClusterName abc
```

Output: 
```
{
    "Response": {
        "Command": "abc",
        "URL": "abc",
        "FileContent": "abc",
        "RequestId": "abc"
    }
}
```

