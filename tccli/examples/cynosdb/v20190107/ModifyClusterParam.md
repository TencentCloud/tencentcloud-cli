**Example 1: 修改集群参数**



Input: 

```
tccli cynosdb ModifyClusterParam --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ins-jhi2gdi0 \
    --ParamList.0.CurrentValue 59 \
    --ParamList.0.OldValue 60 \
    --ParamList.0.ParamName authentication_timeout
```

Output: 
```
{
    "Response": {
        "RequestId": "164063",
        "AsyncRequestId": "56317d06-8078-4e5c-b675-9e048995c820"
    }
}
```

