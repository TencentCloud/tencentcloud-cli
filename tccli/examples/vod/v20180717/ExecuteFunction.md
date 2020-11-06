**Example 1: Initiating custom video processing by customer A**



Input: 

```
tccli vod ExecuteFunction --cli-unfold-argument  \
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

