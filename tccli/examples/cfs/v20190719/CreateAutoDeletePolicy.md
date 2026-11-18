**Example 1: 为指定 CFS 文件系统创建数据自动删除策略**



Input: 

```
tccli cfs CreateAutoDeletePolicy --cli-unfold-argument  \
    --FileSystemId cfs-85nd**** \
    --PolicyName te*** \
    --Paths /cfs/*
```

Output: 
```
{
    "Response": {
        "PolicyId": "adp-c0d0****",
        "RequestId": "277995e0-88d9-4c48-bcf9-d3df31ad3ffa"
    }
}
```

