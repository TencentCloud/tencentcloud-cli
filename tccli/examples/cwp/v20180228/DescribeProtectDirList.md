**Example 1: 示例**

示例

Input: 

```
tccli cwp DescribeProtectDirList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": "/root",
                "DirName": "网站名称1",
                "DirPath": "网站防护目录地址1",
                "NoProtectServerNum": 0,
                "ProtectServerNum": 0,
                "RelatedServerNum": 0,
                "ProtectException": 0,
                "ProtectStatus": 2,
                "AutoRestoreSwitchStatus": 1
            }
        ],
        "RequestId": "",
        "TotalCount": 1
    }
}
```

