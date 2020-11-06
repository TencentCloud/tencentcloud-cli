**Example 1: Querying file details by specifying cluster ID and file ID**

This example shows you how to query file details by specifying the cluster ID and file ID.

Input: 

```
tccli tcaplusdb DescribeIdlFileInfos --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --IdlFileIds 564
```

Output: 
```
{
    "Response": {
        "IdlFileInfos": [
            {
                "FileContent": "syntax%3D%22proto2%22%3Bpackage%20myTcaplusTable%3Bimport%20%22tcaplusservice.optionv1.proto%22%3Bmessage%20tb_example%7Boption%28tcaplusservice.tcaplus_primary_key%29%3D%22uin%2Cname%22%3Brequired%20int64%20uin%20%3D%201%3Brequired%20string%20name%20%3D%202%3Brequired%20int32%20gamesvrid%20%3D%203%3Boptional%20string%20logintime%20%3D%204%3B%7D",
                "FileExtType": "proto",
                "FileId": 564,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            }
        ],
        "RequestId": "5d592aa1-ee73-4b5e-90bf-062efcc05966",
        "TotalCount": 1
    }
}
```

**Example 2: Querying description file details**

This example shows you how to query the description file list by specifying a cluster ID.

Input: 

```
tccli tcaplusdb DescribeIdlFileInfos --cli-unfold-argument  \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "IdlFileInfos": [
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 600,
                "FileName": "tb_example_modify",
                "FileSize": 292,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 548,
                "FileName": "tb_example",
                "FileSize": 298,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 549,
                "FileName": "tb_example",
                "FileSize": 298,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 550,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 551,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 552,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 553,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 559,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 560,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 561,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 562,
                "FileName": "tb_example",
                "FileSize": 267,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 563,
                "FileName": "tb_example",
                "FileSize": 380,
                "FileType": "PROTO"
            },
            {
                "FileContent": null,
                "FileExtType": "proto",
                "FileId": 564,
                "FileName": "tb_example",
                "FileSize": 266,
                "FileType": "PROTO"
            }
        ],
        "RequestId": "1b6a5d3f-beb3-4380-9b6d-3d9f2d83654c",
        "TotalCount": 13
    }
}
```

