**Example 1: 关闭restful api**

制定clusterid，关闭restful api

Input: 

```
tccli tcaplusdb DisableRestProxy --cli-unfold-argument  \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "RestProxyStatus": 3,
        "RequestId": "request-xxx123",
        "TaskId": "838418134-44"
    }
}
```

