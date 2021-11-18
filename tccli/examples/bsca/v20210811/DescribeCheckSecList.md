**Example 1: 查询CheckSec列表**



Input: 

```
tccli bsca DescribeCheckSecList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "CheckSecSet": [
            {
                "FileName": "/path/demo_file1",
                "Canary": false,
                "NonExecutable": true,
                "PositionIndependentExecutable": false,
                "RelReadOnly": false,
                "RuntimeSearchPath": false,
                "RunPath": false,
                "Symbols": false
            },
            {
                "FileName": "/path/demo_file2",
                "Canary": false,
                "NonExecutable": true,
                "PositionIndependentExecutable": false,
                "RelReadOnly": false,
                "RuntimeSearchPath": false,
                "RunPath": false,
                "Symbols": false
            }
        ],
        "FieldValuesSet": [
            {
                "Field": "Relro",
                "Values": [
                    "false"
                ]
            },
            {
                "Field": "Rpath",
                "Values": [
                    "false"
                ]
            },
            {
                "Field": "Runpath",
                "Values": [
                    "false"
                ]
            },
            {
                "Field": "Symbols",
                "Values": [
                    "false",
                    "true"
                ]
            },
            {
                "Field": "Canary",
                "Values": [
                    "false",
                    "true"
                ]
            },
            {
                "Field": "Nx",
                "Values": [
                    "true"
                ]
            },
            {
                "Field": "Pie",
                "Values": [
                    "false",
                    "true"
                ]
            }
        ],
        "TotalCount": 145,
        "RequestId": "5b02f4d7-ea1d-4ee0-8380-25687e653da6"
    }
}
```

