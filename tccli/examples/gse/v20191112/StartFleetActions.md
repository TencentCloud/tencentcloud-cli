**Example 1: 启用服务器舰队自动扩缩容**

启用服务器舰队自动扩缩容

Input: 

```
tccli gse StartFleetActions --cli-unfold-argument  \
    --FleetId fleet-qp3g3fn6-p6l46gnu \
    --Actions AUTO_SCALING
```

Output: 
```
{
    "Response": {
        "FleetId": "fleet-qp3g3fn6-p6l46gnu",
        "RequestId": "e23dc127-80b8-481b-b85d-1d802546c738"
    }
}
```

