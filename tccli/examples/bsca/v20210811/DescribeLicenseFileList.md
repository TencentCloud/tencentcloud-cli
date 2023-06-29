**Example 1: 查询开源风险组件关联的文件信息列表**



Input: 

```
tccli bsca DescribeLicenseFileList --cli-unfold-argument  \
    --AnalysisId f4461442-be34-4c60-ab21-55860baa9940 \
    --ComponentName ncurses 6.1_p20190105-r0
```

Output: 
```
{
    "Response": {
        "FileSet": [
            "/etc/terminfo/a/ansi",
            "/etc/terminfo/d/dumb"
        ],
        "FileInfoSet": [
            {
                "FileName": "/etc/terminfo/a/ansi",
                "Evidence": "Package Manager"
            },
            {
                "FileName": "/etc/terminfo/d/dumb",
                "Evidence": "Package Manager"
            }
        ],
        "TotalCount": 2783,
        "RequestId": "f968723d-3438-431f-93ed-27405990f1c2"
    }
}
```

