**Example 1: 开启restful api**

制定clusterid，开启restful api

Input: 

```
tccli tcaplusdb EnableRestProxy --cli-unfold-argument  \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "RestProxyStatus": 1,
        "RequestId": "request-xxx123",
        "TaskId": "838418134-44"
    }
}
```

