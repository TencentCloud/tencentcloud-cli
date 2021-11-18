**Example 1: 查询含有CVE的组件列表**



Input: 

```
tccli bsca DescribeCVEComponentList --cli-unfold-argument  \
    --AnalysisId 34b0e422-c7be-404a-8861-a543af8393c8 \
    --IsLinuxKernel False \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ComponentSet": [
            {
                "Name": "busybox",
                "Version": "1.29.3",
                "Description": "Busybox is a single binary which includes versions of a large number\nof system commands, including a shell.  The version contained in this\npackage is a minimal configuration intended for use with the Petitboot\nbootloader used on PlayStation 3. The busybox package provides a binary\nbetter suited to normal use.",
                "FileCount": 3,
                "FilePath": "/path/demo_file1",
                "CVECount": {
                    "CriticalCount": 0,
                    "HighCount": 9,
                    "MediumCount": 0,
                    "LowCount": 0
                }
            },
            {
                "Name": "bzip2",
                "Version": "1.0.6",
                "Description": "\nLibraries for applications using the bzip2 compression format.",
                "FileCount": 3,
                "FilePath": "/path/demo_file2",
                "CVECount": {
                    "CriticalCount": 3,
                    "HighCount": 0,
                    "MediumCount": 3,
                    "LowCount": 0
                }
            }
        ],
        "TotalCount": 6,
        "FieldValuesSet": [
            {
                "Field": "ComponentName",
                "Values": [
                    "busybox",
                    "bzip2",
                    "ncurses",
                    "openssl",
                    "pip (python-pkg)"
                ]
            },
            {
                "Field": "CVSSRank",
                "Values": [
                    "MEDIUM",
                    "LOW",
                    "HIGH"
                ]
            },
            {
                "Field": "Category",
                "Values": [
                    "web应用漏洞"
                ]
            }
        ],
        "RequestId": "910ca0d3-6cf0-4602-a9fb-23d78f1d7013"
    }
}
```

