**Example 1: 创建投递SCF任务-成功**



Input: 

```
tccli cls CreateDeliverCloudFunction --cli-unfold-argument  \
    --TopicId 7953cd3d-993f-4813-822d-1dc65f5ba111 \
    --FunctionName test-client-log-handler \
    --Namespace default \
    --Timeout 60 \
    --Qualifier $LATEST
```

Output: 
```
{
    "Response": {
        "RequestId": "01fd5bcc-d7d4-4edb-9ff5-7ecfc305b831"
    }
}
```

**Example 2: 创建投递SCF任务-失败**



Input: 

```
tccli cls CreateDeliverCloudFunction --cli-unfold-argument  \
    --TopicId 923527bf-0728-4114-88a8-5898c0f527ac \
    --FunctionName functionName1 \
    --Namespace ns1 \
    --Qualifier $LATEST \
    --Timeout 60 \
    --MaxMsgNum 100
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.TopicNotExist",
            "Message": "topic not exist RequestId:[341023a0-26d7-4ce6-8f8f-72fc34661335]"
        },
        "RequestId": "341023a0-26d7-4ce6-8f8f-72fc34661335"
    }
}
```

