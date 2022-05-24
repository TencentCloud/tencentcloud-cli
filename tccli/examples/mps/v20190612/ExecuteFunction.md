**Example 1: A 客户发起定制的媒体处理**



Input: 

```
tccli mps ExecuteFunction --cli-unfold-argument  \
    --FunctionName ExampleFunc \
    --FunctionArg XXX
```

Output: 
```
{
    "Response": {
        "RequestId": "8ad61e3a-6b8e-4b4e-9256-fdc701190064ef0",
        "Result": "XXX"
    }
}
```

