**Example 1: 修改ES集群实例名称**

用以修改指定ES集群实例的名称

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxx\
    --InstanceName newName
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

**Example 2: ES集群节点规格变更**

用以对指定ES集群实例进行横向扩缩容，纵向扩缩容，增加专用主节点，专用主节点横向扩缩容，纵向扩缩容等操作，NodeInfoList要传递目标的全量节点信息

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxx\
    --NodeInfoList.0.Type hotData\
    --NodeInfoList.0.NodeNum 2\
    --NodeInfoList.0.NodeType ES.S1.SMALL2\
    --NodeInfoList.0.DiskType CLOUD_SSD\
    --NodeInfoList.0.DiskSize 100\
    --NodeInfoList.1.Type dedicatedMaster\
    --NodeInfoList.1.NodeNum 3\
    --NodeInfoList.1.NodeType ES.S1.SMALL2
```

Output: 
```
{
    "Response": {
        "RequestId": "6001962a-17c5-4604-a0af-0d4719xxxxxx"
    }
}
```

**Example 3: 修改ES集群实例配置**

用以对指定的ES集群实例的配置进行修改操作

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx\
    --EsConfig {"action.destructive_requires_name":"true"}
```

Output: 
```
{
    "Response": {
        "RequestId": "e7c1bb22-e5f2-42f1-8a12-a97a6dxxxxxx"
    }
}
```

**Example 4: 重置Kibana密码**

重置指定ES集群实例Kibana密码

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx\
    --Password newPwd_123
```

Output: 
```
{
    "Response": {
        "RequestId": "1b72089e-720f-4f95-a4ae-4da461xxxxxx"
    }
}
```

**Example 5: ES集群纵向扩缩容**

用以对集群的节点规格（核数、内存大小）和磁盘大小进行扩缩容操作（当前仅支持纵向扩容）

Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx\
    --NodeType ES.S1.MEDIUM4\
    --DiskSize 150
```

Output: 
```
{
    "Response": {
        "RequestId": "dd3f624d-9a72-4057-85cb-f5d32exxxxxx"
    }
}
```

**Example 6: ES设置COS自动备份**



Input: 

```
tccli es UpdateInstance --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx\
    --CosBackup.IsAutoBackup true\
    --CosBackup.BackupTime 23:00
```

Output: 
```
{
    "Response": {
        "RequestId": "dd3f624d-9a72-4057-85cb-f5d32exxxxxx"
    }
}
```

