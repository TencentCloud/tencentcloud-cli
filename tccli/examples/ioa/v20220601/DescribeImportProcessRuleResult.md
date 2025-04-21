**Example 1: 查询进程结果**

查询进程结果

Input: 

```
tccli ioa DescribeImportProcessRuleResult --cli-unfold-argument  \
    --FileName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorSegmentCount": 0,
            "Items": [
                {
                    "Name": "abc",
                    "Rules": [
                        {
                            "Desc": "abc",
                            "Name": "abc",
                            "Op": "abc"
                        }
                    ],
                    "ErrorSegment": [
                        "abc"
                    ],
                    "Row": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

