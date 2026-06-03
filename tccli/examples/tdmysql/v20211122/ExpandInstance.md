**Example 1: 双副本扩容节点**



Input: 

```
tccli tdmysql ExpandInstance --cli-unfold-argument  \
    --InstanceId tdsql3-ecab00ac \
    --StorageNodeNum 4 \
    --Zones ap-chengdu-1
```

Output: 
```
{
    "Response": {
        "FlowId": 4295036759,
        "RequestId": "5b104d05-7e16-4869-87fe-dbd2e8f30b70"
    }
}
```

