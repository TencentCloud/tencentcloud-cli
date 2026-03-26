**Example 1: ListFunction**



Input: 

```
tccli tcb ListFunctions --cli-unfold-argument  \
    --EnvId lowcode-5gtny6fc61de9566 \
    --Order DESC \
    --Orderby ModTime
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "AddTime": "2025-04-22 20:49:17",
                "AsyncRunEnable": "FALSE",
                "Description": "低码数据源函数，自动生成，请勿删除",
                "FunctionId": "lam-5s91bx6p",
                "FunctionName": "lowcode-datasource-preview",
                "ModTime": "2025-12-24 15:04:36",
                "Namespace": "lowcode-5gtny6fc61de9566",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs12.16",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "Event"
            }
        ],
        "TotalCount": 5,
        "RequestId": "819b5c9d-43e0-4704-b4de-d9368e500c76"
    }
}
```

