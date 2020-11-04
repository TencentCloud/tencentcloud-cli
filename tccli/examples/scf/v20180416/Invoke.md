**Example 1: 运行函数**



Input: 

```
tccli scf Invoke --cli-unfold-argument  \
    --FunctionName xxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "MemUsage": 3207168,
            "Log": "",
            "RetMsg": "hello from scf",
            "BillDuration": 100,
            "FunctionRequestId": "6add56fa-58f1-11e8-89a9-5254005d5fdb",
            "Duration": 0.826,
            "ErrMsg": "",
            "InvokeResult": 0
        },
        "RequestId": "c2af8a64-c922-4d55-aee0-bd86a5c2cd12"
    }
}
```

