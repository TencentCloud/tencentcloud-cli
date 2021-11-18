**Example 1: 查询License文件列表**



Input: 

```
tccli bsca DescribeLicenseFileList --cli-unfold-argument  \
    --AnalysisId f4461442-be34-4c60-ab21-55860baa9940 \
    --ComponentName sugar-datastore
```

Output: 
```
{
    "Response": {
        "FileSet": [
            "/path/libfstools.so"
        ],
        "RequestId": "0d4d25cf-e582-4c16-ab9f-4c5bc6177fa5"
    }
}
```

