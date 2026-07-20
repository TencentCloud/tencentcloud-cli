**Example 1: ModifyIsolateTable 隔离列表操作**



Input: 

```
tccli cfw ModifyIsolateTable --cli-unfold-argument  \
    --InstanceID ins-8888 \
    --ButtonAction edit \
    --StartTime 2022-03-08 09:12:47 \
    --EndTime 2022-03-15 09:12:48
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "450a0c76-8911-41d3-ab54-27b83357e4a2"
    }
}
```

