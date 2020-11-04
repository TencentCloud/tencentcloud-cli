**Example 1: 查询文件信誉度**

根据文件MD5查询相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

Input: 

```
tccli tics DescribeFileInfo --cli-unfold-argument  \
    --Key 011d6ce51b7806dca26c300e8d26f9bb
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "Result": "black",
        "Confidence": 90,
        "FileInfo": {},
        "Tags": [],
        "Intelligences": [],
        "Context": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

