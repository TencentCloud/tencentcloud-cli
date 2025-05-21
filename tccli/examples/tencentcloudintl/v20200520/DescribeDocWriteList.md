**Example 1: 通过写写id获取对应文档信息**

通过写写id获取对应文档信息

Input: 

```
tccli tencentcloudintl DescribeDocWriteList --cli-unfold-argument  \
    --WriteNodeId 127809374270681088
```

Output: 
```
{
    "Response": {
        "RequestId": "297b8763-c48e-4923-959a-a18ed01fc83c",
        "Response": {
            "DocWriteData": [
                {
                    "Id": 495,
                    "Lang": "ind",
                    "WriteLatestVersion": "1709778540",
                    "WriteNodeId": "138381141413535744",
                    "WritePublishedVersion": "1709778540"
                },
                {
                    "Id": 495,
                    "Lang": "ko",
                    "WriteLatestVersion": "1700100875",
                    "WriteNodeId": "127809374270681088",
                    "WritePublishedVersion": "1700100875"
                }
            ],
            "RequestId": "297b8763-c48e-4923-959a-a18ed01fc83c"
        }
    }
}
```

