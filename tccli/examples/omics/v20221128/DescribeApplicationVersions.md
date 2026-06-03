**Example 1: 查询指定应用可用版本**



Input: 

```
tccli omics DescribeApplicationVersions --cli-unfold-argument  \
    --ProjectId prj-wide-cerulean-cicadia-967487 \
    --ApplicationId app-articulate-aqua-starfish-027347 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ApplicationVersions": [
            {
                "ApplicationVersionId": "6",
                "CosSource": {
                    "Bucket": "",
                    "Region": "",
                    "Uri": ""
                },
                "CreateTime": "2026-01-20 16:43:18",
                "CreatorId": "d7b36454199f4e56b1cebddf02d19e23",
                "CreatorName": "nekowu",
                "Description": "",
                "Entrypoint": "main.wdl",
                "GitSource": {
                    "Branch": "",
                    "GitHttpPath": "",
                    "GitTokenOrPassword": "",
                    "GitUserName": "",
                    "Tag": ""
                },
                "Name": "",
                "Type": "HISTORY"
            }
        ],
        "TotalCount": 6,
        "RequestId": "1b37a8ea-a91b-4d72-bf4f-9b04909814ac"
    }
}
```

