**Example 1: 生成批量下载控制连接地址**

生成批量下载控制连接地址

Input: 

```
tccli essbasic GetDownloadFlowUrl --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8xxxxe9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c5910xxxxaa382cc5ed0e \
    --DownLoadFlows.0.FlowIdList test-flow-id1 test-flow-id2 \
    --DownLoadFlows.0.FileName 文件夹1 \
    --DownLoadFlows.1.FlowIdList test-flow-id3 test-flow-id4 \
    --DownLoadFlows.1.FileName 文件夹2
```

Output: 
```
{
    "Response": {
        "DownLoadUrl": "https://xxx.xxxx.tencent.com/template-preview?channel=PROXYCHANNEL&expiredTime=1639587153&code=yDxjKUUgydjf9pxxxx4adWk38k&token=yDxjKxxxpruUuO4zjES4adWk38k&operate=downloadFlow",
        "RequestId": "s16221xxx14775648"
    }
}
```

