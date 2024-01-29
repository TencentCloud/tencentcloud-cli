**Example 1: 请求demo**



Input: 

```
tccli wedata DownloadNewSqlResult --cli-unfold-argument  \
    --DetailId 123 \
    --FileName default \
    --ProjectId 1111 \
    --SeparatorChar /
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "CosPath": "111",
        "CosBucketName": "default"
    }
}
```

