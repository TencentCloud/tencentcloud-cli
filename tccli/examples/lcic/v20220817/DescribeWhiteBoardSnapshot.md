**Example 1: 查询白板板书截图**



Input: 

```
tccli lcic DescribeWhiteBoardSnapshot --cli-unfold-argument  \
    --RoomId 345740000
```

Output: 
```
{
    "Response": {
        "RequestId": "2fbab292-694c-437c-9182-5f9af464ebb0",
        "Result": [
            "https://example.cos.ap-shanghai.myqcloud.com/snapshot1.png",
            "https://example.cos.ap-shanghai.myqcloud.com/snapshot2.png",
            "https://example.cos.ap-shanghai.myqcloud.com/snapshot3.png",
            "https://example.cos.ap-shanghai.myqcloud.com/snapshot4.png",
            "https://example.cos.ap-shanghai.myqcloud.com/snapshot5.png"
        ],
        "Status": 3,
        "Total": 5,
        "WhiteBoardSnapshotMode": 1
    }
}
```

