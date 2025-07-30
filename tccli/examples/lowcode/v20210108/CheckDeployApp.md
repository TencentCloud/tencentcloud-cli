**Example 1: 检查应用发布状态**



Input: 

```
tccli lowcode CheckDeployApp --cli-unfold-argument  \
    --EnvId lowcode-5gzbnlvd9 \
    --Id app-k82WCPM \
    --BuildId b62b-c1c6f403d6e1
```

Output: 
```
{
    "Response": {
        "RequestId": "b722653b-c49a-46bd-8ff0-6d8ba61a37d1",
        "Status": "building"
    }
}
```

