**Example 1: 删除关键词接口示例**

删除词库关键词

Input: 

```
tccli cms DeleteLibSamples --cli-unfold-argument  \
    --LibID abc \
    --SampleIDs abc \
    --SampleContents 违规
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Details": [
            {
                "SampleID": "1",
                "Content": "",
                "Deleted": false,
                "ErrorInfo": "NotFound"
            },
            {
                "SampleID": "2",
                "Content": "xixi",
                "Deleted": true,
                "ErrorInfo": ""
            }
        ],
        "RequestId": "xxx"
    }
}
```

