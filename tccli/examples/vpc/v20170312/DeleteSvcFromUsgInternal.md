**Example 1: SVC删除规则**



Input: 

```
tccli vpc DeleteSvcFromUsgInternal --cli-unfold-argument  \
    --DelSvcFromUsgRequest.0.SvcId 123123
```

Output: 
```
{
    "Response": {
        "DelSvcFromUsgResult": [
            {
                "SvcId": "vpce-kifyia9o",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

