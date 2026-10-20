**Example 1: 获取事件**

获取任务相关的事件(k8s事件)信息

Input: 

```
tccli tione DescribeEvents --cli-unfold-argument  \
    --Service NOTEBOOK \
    --Limit 10 \
    --Offset 0 \
    --ServiceId nb-1694306254472012288-cw0bo5hocmps
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "Id": "44b40fe5-9546-42fd-b75d-557802e0029d",
                "Message": "Created container sidecar-nginx",
                "FirstTimestamp": "2022-01-10T19:22:04+08:00",
                "LastTimestamp": "2022-01-10T19:22:04+08:00",
                "Count": 1,
                "Type": "Normal",
                "ResourceKind": "Pod",
                "ResourceName": "nb-1694306254472012288-cw0bo5hocmps"
            }
        ],
        "TotalCount": 1,
        "RequestId": "090e057a-0d4e-488a-978b-83b1636fee99"
    }
}
```

