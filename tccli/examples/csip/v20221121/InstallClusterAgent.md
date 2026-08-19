**Example 1: 安装单个集群容器安全Agent**

传入单个 ClusterCaMD5，为该集群安装容器安全Agent

Input: 

```
tccli csip InstallClusterAgent --cli-unfold-argument  \
    --ClusterCaMD5List e3b0c44298fc1c149afbf4c8996fb924
```

Output: 
```
{
    "Response": {
        "RequestId": "c368eae2-8739-4cc2-b4f8-8f4284a93b41"
    }
}
```

**Example 2: 批量安装多个集群容器安全Agent**

传入多个 ClusterCaMD5，批量安装容器安全Agent

Input: 

```
tccli csip InstallClusterAgent --cli-unfold-argument  \
    --ClusterCaMD5List e3b0c44298fc1c149afbf4c8996fb924 d41d8cd98f00b204e9800998ecf8427e
```

Output: 
```
{
    "Response": {
        "RequestId": "d479fbf3-9840-4dd3-c5f9-9f5395ba4c52"
    }
}
```

