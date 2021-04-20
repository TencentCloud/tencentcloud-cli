**Example 1: 手动执行版本保留**



Input: 

```
tccli tcr CreateTagRetentionExecution --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --RetentionId 1 \
    --DryRun false
```

Output: 
```
{
    "Response": {
        "RequestId": "c8bf292d-38c7-49d9-8da3-737d08160cfc"
    }
}
```

