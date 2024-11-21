**Example 1: 查询网页防篡改防护目录列表**



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
        "TotalCount": 1,
        "List": [
            {
                "DirName": "sdfdsf",
                "DirPath": "/home/te****",
                "RelatedServerNum": 1,
                "ProtectServerNum": 1,
                "NoProtectServerNum": 1,
                "Id": "/home/te****",
                "ProtectStatus": 1,
                "ProtectException": 1,
                "AutoRestoreSwitchStatus": 1,
                "FirstProtectTime": "2020-11-21 15:16:00",
                "LatestProtectTime": "2020-11-21 15:16:00",
                "ProtectFileType": ".php;.js",
                "ProtectFilesCount": 0
            }
        ],
        "RequestId": "2eedad67-5a4c-4746-82d2-52a8e5d91c6a"
    }
}
```

