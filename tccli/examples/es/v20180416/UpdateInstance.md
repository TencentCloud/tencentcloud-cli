**Example 1: 修改ES集群实例名称**

用以修改指定ES集群实例的名称

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxx \
    --InstanceName newName
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

**Example 2: ES集群节点规格变更**

用以对指定ES集群实例进行横向扩缩容，纵向扩缩容，增加专用主节点，专用主节点横向扩缩容，纵向扩缩容等操作，NodeInfoList要传递目标的全量节点信息

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxx \
    --NodeInfoList.0.NodeType ES.S1.SMALL2 \
    --NodeInfoList.0.NodeNum 3 \
    --NodeInfoList.0.Type dedicatedMaster \
    --NodeInfoList.1.DiskSize 100 \
    --NodeInfoList.1.NodeType ES.S1.SMALL2 \
    --NodeInfoList.1.NodeNum 2 \
    --NodeInfoList.1.Type hotData \
    --NodeInfoList.1.DiskType CLOUD_SSD
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

**Example 3: 修改ES集群实例配置**

用以对指定的ES集群实例的配置进行修改操作

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --EsConfig {"action.destructive_requires_name":"true"}
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

**Example 4: 重置Kibana密码**

重置指定ES集群实例Kibana密码

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --Password newPwd_123
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

**Example 5: ES集群纵向扩缩容**

用以对集群的节点规格（核数、内存大小）和磁盘大小进行扩缩容操作（当前仅支持纵向扩容）

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --DiskSize 150 \
    --NodeType ES.S1.MEDIUM4
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DealName": "xx"
    }
}
```

