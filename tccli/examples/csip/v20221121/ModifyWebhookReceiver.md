**Example 1: 示例**



Input: 

```
tccli csip ModifyWebhookReceiver --cli-unfold-argument  \
    --Name f2 \
    --Type SCF \
    --SCFRegion ap-guangzhou \
    --Namespace default \
    --FunctionName f2 \
    --FunctionVersion $LATEST \
    --Alias alias2
```

Output: 
```
{
    "Response": {
        "ID": 21,
        "RequestId": "72c22c12-d0e3-4c35-928c-64225477dc46"
    }
}
```

