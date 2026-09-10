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

**Example 2: ListFunction-0819**



Input: 

```
tccli tcb ListFunctions --cli-unfold-argument  \
    --EnvId jackvyli-d1g5v7p5e7191af47
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "AddTime": "2026-08-19 16:37:23",
                "AsyncRunEnable": "FALSE",
                "Description": "Hello World",
                "FunctionId": "lam-hlxwkilh",
                "FunctionName": "jackvylitest6",
                "ModTime": "2026-08-19 16:37:23",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "CreateFailed",
                "StatusDesc": "",
                "StatusReasons": [
                    {
                        "ErrorCode": "ResourceNotFound.BootstrapFile",
                        "ErrorMessage": "BuildCodeViaSCF Failed resp:null: ResourceNotFound.Entryfile Error,Err:&{ResourceNotFound.Entryfile Unzip entryfile Failded,Err:exit status 11 OUT:caution: filename not matched:  scf_bootstrap\n}"
                    }
                ],
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-19 16:32:07",
                "AsyncRunEnable": "FALSE",
                "Description": "Hello World",
                "FunctionId": "lam-oz9u16zl",
                "FunctionName": "scfnodejshelloworldasdf",
                "ModTime": "2026-08-19 16:32:07",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "Event"
            },
            {
                "AddTime": "2026-08-18 15:05:47",
                "AsyncRunEnable": "FALSE",
                "Description": "Nodejs 语言 Websocket 模板",
                "FunctionId": "lam-9t9ss2xx",
                "FunctionName": "jackvylitest5",
                "ModTime": "2026-08-18 15:05:47",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-18 15:05:16",
                "AsyncRunEnable": "FALSE",
                "Description": "Nodejs 语言 Websocket 模板",
                "FunctionId": "lam-1i4pllmx",
                "FunctionName": "jackvylitest4",
                "ModTime": "2026-08-18 15:05:16",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-18 14:56:16",
                "AsyncRunEnable": "FALSE",
                "Description": "Nodejs 语言 Websocket 模板",
                "FunctionId": "lam-6jcmfig1",
                "FunctionName": "jackvylitest3",
                "ModTime": "2026-08-18 14:56:16",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-17 18:03:30",
                "AsyncRunEnable": "FALSE",
                "Description": "Nodejs 语言 Websocket 模板",
                "FunctionId": "lam-oz8ntn37",
                "FunctionName": "jackvylitest",
                "ModTime": "2026-08-17 18:03:30",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-17 17:09:31",
                "AsyncRunEnable": "FALSE",
                "Description": "Nodejs 语言 Websocket 模板",
                "FunctionId": "lam-6mv2t7lt",
                "FunctionName": "httpnodejswebsocket",
                "ModTime": "2026-08-17 17:09:31",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-17 15:59:22",
                "AsyncRunEnable": "FALSE",
                "Description": "基于 Nodejs 语言框架 Express 实现的 HTTP 调用示例",
                "FunctionId": "lam-9enjzkkv",
                "FunctionName": "httpnodejsexpress",
                "ModTime": "2026-08-17 15:59:22",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs20.19",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "HTTP"
            },
            {
                "AddTime": "2026-08-13 14:33:50",
                "AsyncRunEnable": "FALSE",
                "Description": "asd",
                "FunctionId": "lam-0qxuqwmn",
                "FunctionName": "scfnodejshelloworld",
                "ModTime": "2026-08-17 15:47:28",
                "Namespace": "jackvyli-d1g5v7p5e7191af47",
                "ReservedConcurrencyMem": 0,
                "Runtime": "Nodejs18.15",
                "Status": "Active",
                "StatusDesc": "",
                "StatusReasons": null,
                "Tags": null,
                "TotalProvisionedConcurrencyMem": 0,
                "TraceEnable": "FALSE",
                "Type": "Event"
            }
        ],
        "RequestId": "e225e7f0-12a3-42d1-aa96-21a397867a65",
        "TotalCount": 9
    }
}
```

