**Example 1: DescribeFiles**



Input: 

```
tccli pts DescribeFiles --cli-unfold-argument  \
    --ProjectIds project-xx \
    --Offset 0 \
    --FileIds file-xx \
    --Limit 0 \
    --FileName file name \
    --Kind 1
```

Output: 
```
{
    "Response": {
        "FileSet": [
            {
                "AppId": 1258344690,
                "Uin": "438167612",
                "SubAccountUin": "100019497941",
                "CreatedAt": "2023-04-11T15:20:18+08:00",
                "UpdatedAt": "2023-04-11T15:20:18+08:00",
                "FileId": "file-218d0901",
                "ProjectId": "project-r92xzqe3",
                "Kind": 1,
                "Name": "demo.csv",
                "Size": 18,
                "Type": "CSV",
                "Status": 2,
                "LineCount": 3,
                "HeadLines": [
                    "msg\r",
                    "world\r",
                    "pts"
                ],
                "TailLines": [],
                "HeaderInFile": true,
                "HeaderColumns": [
                    "msg"
                ],
                "FileInfos": null,
                "ScenarioSet": null,
                "AppID": 0
            }
        ],
        "RequestId": "7baba29e-5545-44e8-b39e-9be261d6369a",
        "Total": 36
    }
}
```

