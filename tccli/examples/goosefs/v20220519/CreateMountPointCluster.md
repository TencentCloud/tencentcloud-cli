**Example 1: 创建GooseFS MountPoint集群**



Input: 

```
tccli goosefs CreateMountPointCluster --cli-unfold-argument  \
    --Name hello goosefs mount point \
    --Description hello goosefs mount point \
    --NodeIds ins-0vtvh***
```

Output: 
```
{
    "Response": {
        "ClusterId": "clst-Icq926tk",
        "RequestId": "a0ae68c6-45e4-4bc8-8b5a-4672763b3af4"
    }
}
```

