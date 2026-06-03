**Example 1: 请求示例**

修改媒体包装SourceLocation信息。

Input: 

```
tccli mps ModifyStreamPackageSourceLocation --cli-unfold-argument  \
    --Id 67D7CBB600005DBB0001 \
    --Name location_name \
    --BaseUrl https://test.com/base \
    --SegmentDeliverEnable True \
    --SegmentDeliverConf.DefaultSegmentUrl https://test.com/ \
    --SegmentDeliverConf.NameServers.0.Name server_name \
    --SegmentDeliverConf.NameServers.0.Url https://testserver.com/ \
    --SegmentDeliverUsePackageEnable True
```

Output: 
```
{
    "Response": {
        "RequestId": "req-xx"
    }
}
```

