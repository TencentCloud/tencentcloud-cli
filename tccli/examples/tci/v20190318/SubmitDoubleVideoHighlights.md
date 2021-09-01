**Example 1: 提交精彩集锦剪辑任务**

根据客户所提供的视频及参数，生成相关的精彩集锦结果。

Input: 

```
tccli tci SubmitDoubleVideoHighlights --cli-unfold-argument  \
    --FileContent https%3A%2F%2Fefpoc-1255701415.cos.ap-shanghai.myqcloud.com%2Fvideos%2Fefpoc_1_27.mp4 \
    --LibId test_lib \
    --PersonIds 2124123
```

Output: 
```
{
    "Response": {
        "JobId": 278,
        "RequestId": "3c5a7213-e3b5-4732-b5d6-c0ec76897746",
        "NotRegistered": {}
    }
}
```

