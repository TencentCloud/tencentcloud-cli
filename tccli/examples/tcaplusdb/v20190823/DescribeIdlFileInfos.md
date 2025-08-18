**Example 1: 查询描述文件详情**

指定集群ID查询描述文件列表

Input: 

```
tccli tcaplusdb DescribeIdlFileInfos --cli-unfold-argument  \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "IdlFileInfos": [
            {
                "FileName": "filename",
                "FileType": "tdr",
                "FileExtType": "tdr",
                "FileSize": 1321230,
                "FileId": 1,
                "FileContent": "content"
            }
        ],
        "RequestId": "1898921-12142"
    }
}
```

**Example 2: 指定集群ID和文件ID查询文件详情**

指定集群ID和文件ID查询文件详情

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

