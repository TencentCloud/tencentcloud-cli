**Example 1: 提交自定义函数**



Input: 

```
tccli wedata SubmitCustomFunction --cli-unfold-argument  \
    --Comment test \
    --ClusterIdentifier emr-terse \
    --FunctionId d65df5af-28b4-4171-9a24-ce96fc4e83fa \
    --ProjectId 153160354643453465952
```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "FunctionId": "d65df5af-28b4-4171-9a24-ce96fc4e83fa",
        "RequestId": "ef431542-96ae-467c-b821-f594df8ac83c"
    }
}
```

