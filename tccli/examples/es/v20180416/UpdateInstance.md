**Example 1: Resetting Kibana password**

This example shows you how to reset the Kibana password of a specified ES cluster instance.

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

**Example 2: Modifying the configuration of ES cluster instance**

This example shows you how to modify the configuration of a specified ES cluster instance.

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

**Example 3: Vertically scaling ES cluster**

This example shows you how to vertically scale the node specification (number of cores and memory size) and disk size in a cluster (only vertical scaling is supported currently).

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

**Example 4: Setting auto-backup to COS for ES**

This example shows you how to reset the Kibana password of the specified ES cluster instance.

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

**Example 5: Modifying the node specification of ES cluster**

This example shows you how to perform operations such as horizontally or vertically scaling the specified ES cluster instance or dedicated master node, where `NodeInfoList` contains the information of all target nodes to be passed in.

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

**Example 6: Renaming ES cluster instances**

This example shows you how to rename a specified ES cluster instance.

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

