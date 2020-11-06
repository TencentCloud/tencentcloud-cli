**Example 1: Customer A initiates a custom video processing**



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

