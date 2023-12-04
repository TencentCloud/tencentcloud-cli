**Example 1: 创建投递SCF任务**



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

