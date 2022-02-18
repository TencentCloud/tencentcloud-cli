**Example 1: 修改场景**



Input: 

```
tccli iotvideoindustry ModifyScene --cli-unfold-argument  \
    --IntId 2 \
    --SceneName 测试场景1 \
    --SceneTrigger {"2":{"Name":"设备报警","WarnType":{"1":"视频丢失报警","2":"设备防拆报警","3":"存储设备磁盘满报警","4":"设备高温报警","5":"设备低温报警"}}} \
    --RecordDuration 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f"
    }
}
```

