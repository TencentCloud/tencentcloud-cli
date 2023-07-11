**Example 1: 创建视频重生模板。**

创建视频重生模板。

Input: 

```
tccli vod CreateRebuildMediaTemplate --cli-unfold-argument  \
    --Name rebuildMediaTestTempalte \
    --Container mp4 \
    --RebuildVideoInfo.RepairInfo.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 20001,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

