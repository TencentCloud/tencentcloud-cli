**Example 1: 添加直播拉流输入源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddInput
InputEndpoint | 是 | String | Main 或 Backup
InputInfo | 是 | [StreamInputInfo](https://cloud.tencent.com/document/api/1156/40360#StreamInputInfo) | 输入源，InputType 取值 LivePull

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation AddInput \
    --InputEndpoint Main \
    --InputInfo.InputType LivePull \
    --InputInfo.LivePullInputInfo.InputUrl rtmp://liveplay.video-studio.myqcloud.com/output/1250000001-600e8e7fb1cc1c0001293759
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 2: 添加直播推流输入源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddInput
InputEndpoint | 是 | String | Main 或 Backup
InputInfo | 是 | [StreamInputInfo](https://cloud.tencent.com/document/api/1156/40360#StreamInputInfo)| 输入源，InputType 取值 RtmpPush ， 从获取项目列表接口可拿到对应推流输入源的 PushUrl

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation AddInput \
    --InputEndpoint Main \
    --InputInfo.InputType RtmpPush \
    --InputInfo.RtmpPushInputInfo.ExpiredSecond 3600
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "rtmp://liveplay-xx.video-studio.myqcloud.com/output/1250000001-6086674e265b4500018xxx?txSecret=4478cfdfe0fd0eb3820705aebaa328ed&txTime=608FA1CE",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 3: 添加点播拉流输入源且循环播放**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddInput
InputEndpoint | 是 | String | Main 或 Backup
InputInfo | 是 | [StreamInputInfo](https://cloud.tencent.com/document/api/1156/40360#StreamInputInfo)| 输入源，InputType 取值 VodPull ， VodPullInputInfo.LoopTimes 取值-1

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation AddInput \
    --InputEndpoint Main \
    --InputInfo.InputType VodPull \
    --InputInfo.VodPullInputInfo.InputUrls https://1810000001.vod2.myqcloud.com/b64e98advodcq1810000001/85f47b535285890787805464143/AfJuJAzie5QA.mp4 \
    --InputInfo.VodPullInputInfo.LoopTimes -1
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 4: 添加点播拉流输入源且单次播放**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddInput
InputEndpoint | 是 | String | Main 或 Backup
InputInfo | 是 | [StreamInputInfo](https://cloud.tencent.com/document/api/1156/40360#StreamInputInfo) | 输入源，InputType 取值 VodPull ， VodPullInputInfo.LoopTimes 取值 0

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation AddInput \
    --InputEndpoint Main \
    --InputInfo.InputType VodPull \
    --InputInfo.VodPullInputInfo.InputUrls https://1810000001.vod2.myqcloud.com/b64e98advodcq1810000001/85f47b535285890787805464143/AfJuJAzie5QA.mp4 \
    --InputInfo.VodPullInputInfo.LoopTimes 0
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 5: 删除输入源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DeleteInput
InputEndpoint | 是 | String | Main 或 Backup

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation DeleteInput \
    --InputEndpoint Main
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 6: 修改输入源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyInput
InputEndpoint | 是 | String | Main 或 Backup
InputInfo | 是 | [StreamInputInfo](https://cloud.tencent.com/document/api/1156/40360#StreamInputInfo) | 输入源

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation ModifyInput \
    --InputEndpoint Main \
    --InputInfo.InputType VodPull \
    --InputInfo.VodPullInputInfo.InputUrls https://1810000001.vod2.myqcloud.com/b64e98advodcq1810000001/85f47b535285890787805464143/AfJuJAzie5QA.mp4 https://1810000001.vod2.myqcloud.com/b64e98advodcq1810000001/85f47b535285890787805464143/test.mp4 \
    --InputInfo.VodPullInputInfo.LoopTimes -1
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 7: 添加输出源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddOutput
OutputInfo| 是 | [StreamConnectOutput](https://cloud.tencent.com/document/api/1156/40360#StreamConnectOutput)| 输出源，Id 字段若不填则由后端生成

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation AddOutput \
    --OutputInfo.PushUrl rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08xx \
    --OutputInfo.Name test
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 8: 删除输出源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DeleteOutput
OutputInfo| 是 | [StreamConnectOutput](https://cloud.tencent.com/document/api/1156/40360#StreamConnectOutput)| 输出源，Id 字段必填，从获取项目列表接口中拿到对应输出源的 Id

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation DeleteOutput \
    --OutputInfo.Id 12357877
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 9: 修改输出源**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyOutput
OutputInfo| 是 | [StreamConnectOutput](https://cloud.tencent.com/document/api/1156/40360#StreamConnectOutput)| 输出源，Id 字段必填，从获取项目列表中拿到对应输出源的 Id

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation ModifyOutput \
    --OutputInfo.Id 12357877 \
    --OutputInfo.PushUrl rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08xxxx
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 10: 开启云转推**

开启云转推包括开启输入源、输出源转推。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 Start

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation Start
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 11: 停止云转推**

停止云转推包括停止输入源、输出源转推。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 Stop

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation Stop
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 12: 切换输入源**

云转推主备输入源切换，当前转推输入源为Main，切换到Backup输入源。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 SwitchInput
InputEndPoint | 是 | String | Main 或 Backup

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation SwitchInput \
    --InputEndpoint Backup
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 13: 修改转推结束时间**

修改当前正在转推项目的转推预计结束时间。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyCurrentStopTime
CurrentStopTime | 是 | String | 当前转推预计结束时间，ISO 日期格式，不得超过当前时间30天

Input: 

```
tccli cme HandleStreamConnectProject --cli-unfold-argument  \
    --Platform test \
    --ProjectId 12522d74de35ff \
    --Operation ModifyCurrentStopTime \
    --CurrentStopTime 2021-03-23T07:51:18.029Z
```

Output: 
```
{
    "Response": {
        "StreamInputRtmpPushUrl": "",
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

