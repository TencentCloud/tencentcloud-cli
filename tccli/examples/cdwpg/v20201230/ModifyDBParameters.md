**Example 1: 修改集群配置**

修改集群配置

Input: 

```
tccli cdwpg ModifyDBParameters --cli-unfold-argument  \
    --InstanceId cdwpg-rzshdeh1 \
    --NodeConfigParams.0.NodeType cn \
    --NodeConfigParams.0.ConfigParams.0.ParameterName max_connections \
    --NodeConfigParams.0.ConfigParams.0.ParameterValue 630 \
    --NodeConfigParams.0.ConfigParams.0.ParameterOldValue 625
```

Output: 
```
{
    "Response": {
        "RequestId": "d455ac94-9ab9-4794-95af-41ee85a71f5a",
        "TaskId": 9897
    }
}
```

