**Example 1: Updating the Function Code**



Input: 

```
tccli scf UpdateFunctionCode --cli-unfold-argument  \
    --FunctionName test \
    --Handler index.main \
    --CosBucketName <CosBucketName> \
    --CosObjectName <CosObjectName>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

