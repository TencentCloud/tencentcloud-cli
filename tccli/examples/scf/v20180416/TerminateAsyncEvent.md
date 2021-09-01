**Example 1: 终止异步事件**



Input: 

```
tccli scf TerminateAsyncEvent --cli-unfold-argument  \
    --Namespace default \
    --FunctionName helloworld \
    --InvokeRequestId b379787f-8487-4bac-bd8c-17a20a9ce40e
```

Output: 
```
{
    "Response": {
        "RequestId": "ee33a89b-3825-4d2f-bd88-35a8fa27aae1"
    }
}
```

