**Example 1: ListUpstreamOpsTasks**



Input: 

```
tccli wedata ListUpstreamOpsTasks --cli-unfold-argument  \
    --TaskId 20250725174033396 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "WeData通用内部异常:资源未找到"
        },
        "RequestId": "07faa9b8-f855-48bd-903b-88f35e180f22"
    }
}
```

