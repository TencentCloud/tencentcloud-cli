**Example 1: 修改结束时间**

如果项目是 Working 状态，将按照修改后的结束时间结束项目。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyPlaySetting。
PlaySetting | 是 | [MediaCastPlaySetting](https://cloud.tencent.com/document/api/1156/40360#MediaCastPlaySetting) | 播放参数。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation ModifyPlaySetting \
    --PlaySetting.EndTime 2022-12-20T20:00:00Z \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 2: 修改输出源**

修改输出源的名称或者输出地址，如果项目状态是 Working 状态并且修改了输出地址， 将断开原来输出源地址的直播流，向新的输出源地址输出直播流。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyDestination。
DestinationInfos| 是 | Array of [MediaCastDestinationInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastDestinationInfo)| 输出源信息。一次修改一个输出源。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation ModifyDestination \
    --DestinationInfos.0.Id dt_01 \
    --DestinationInfos.0.Name new name \
    --DestinationInfos.0.PushUrl rtmp://test.com/new?t=abc \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 3: 修改输出的媒体配置**

修改输出的媒体配置，项目状态是 Working 状态时不能修改输出的媒体配置。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyOutputMediaSetting。
OutputMediaSetting | 是 | [MediaCastOutputMediaSetting](https://cloud.tencent.com/document/api/1156/40360#MediaCastOutputMediaSetting) | 输出的媒体配置。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation ModifyOutputMediaSetting \
    --OutputMediaSetting.VideoSetting.Width 1920 \
    --OutputMediaSetting.VideoSetting.Height 1080 \
    --OutputMediaSetting.VideoSetting.Bitrate 2500 \
    --OutputMediaSetting.VideoSetting.FrameRate 30 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 4: 停止输出源**

项目状态是 Working 状态时，停止输出源将断开该输出源的直播流。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DisableDestination。
DestinationInfos| 是 | Array of [MediaCastDestinationInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastDestinationInfo) | 输出源信息。只需要带上输出源的 Id 参数。一次只能停止一个输出源。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation DisableDestination \
    --DestinationInfos.0.Id dt_01 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 5: 切换当前播放的输入源**

项目状态为 Working 状态时切换生效，切换后从该输入源开始播放。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 SwitchSource。
SourceInfos| 是 |  Array of  [MediaCastSourceInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastSourceInfo) | 输入源信息，只需要带上输入源的 Id  。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation SwitchSource \
    --SourceInfos.0.Id st_02 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 6: 删除输入源**

如果项目状态是 Working 状态，不能删除正在播放的输入源。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DeleteSource。
SourceInfos| 是 | Array of  [MediaCastSourceInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastSourceInfo) | 输入源信息，只需要带上输入源的 Id 。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation DeleteSource \
    --SourceInfos.0.Id st_02 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 7: 删除输出源**

项目状态是 Working 状态时，删除输出源将停止该输出源的直播输出。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DeleteDestination。
DestinationInfos| 是 | Array of [MediaCastDestinationInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastDestinationInfo)| 输出源信息，只需要带上输出源的 Id 参数。一次只能删除一个输出源。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation DeleteDestination \
    --DestinationInfos.0.Id dt_02 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 8: 启动输出源**

重新启动已经停止的输出源，项目状态是 Working 状态时进行操作。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 EnableDestination。
DestinationInfos| 是 | Array of [MediaCastDestinationInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastDestinationInfo)| 输出源信息。只需要带上输出源的 Id 参数。一次只能启动一个输出源。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation EnableDestination \
    --DestinationInfos.0.Id dt_02 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 9: 添加输入源**

新添加的输入源加到输入源列表的后面。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddSource。
Position | 否 | Integer | 输入源列表中的位置，0表示第一个位置。默认添加到输入源列表的后面。
SourceInfos | 是 | Array of [MediaCastSourceInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastSourceInfo) | 输入源信息。输入源个数最大为100个。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation AddSource \
    --Position 0 \
    --SourceInfos.0.Type CME \
    --SourceInfos.0.MaterialId 5fd8ad3d628dc30001bd0895 \
    --SourceInfos.1.Type VOD \
    --SourceInfos.1.FileId 5285485487985271487 \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [
            {
                "Id": "st_01",
                "Type": "CME",
                "MaterialId": "5fd8ad3d628dc30001bd0895"
            },
            {
                "Id": "st_02",
                "Type": "VOD",
                "FileId": "5285485487985271487"
            }
        ],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 10: 添加输出源**

项目状态为 Working 状态时，添加输出源后，将向新的输出源推送直播流。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 AddDestination。
DestinationInfos| 是 | Array of [MediaCastDestinationInfo](https://cloud.tencent.com/document/api/1156/40360#MediaCastDestinationInfo) | 输出源信息。一次添加一个输出源。输出源个数最大为10。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation AddDestination \
    --DestinationInfos.0.Name test \
    --DestinationInfos.0.PushUrl rtmp://test.com/live/abc?t=xxx \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [
            {
                "Id": "dt_02",
                "PushUrl": "rtmp://test.com/live/aa?t=xx"
            }
        ],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 11: 停止媒体转推**

停止媒体转推。停止操作将停止输入源的播放并断开直播流，项目状态变为 Idle 状态。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 Stop。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation Stop \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 12: 启动媒体转推**

启动媒体转推。启动成功后项目状态变为 Working 状态，从输入源列表的第一个输入源开始播放，向输出源列表推送直播流。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 Start。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation Start \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 13: 查询媒体转推项目的播放信息**

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 DescribePlayInfo。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation DescribePlayInfo \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": {
            "Status": "Working",
            "CurrentSourceId": "st_0123",
            "CurrentSourcePosition": 100,
            "CurrentSourceDuration": 3490,
            "LoopCount": 1,
            "DestinationStatusSet": [
                {
                    "Id": "dt_123",
                    "PushUrl": "rtmp://test.com/live/aa?t=xx",
                    "Status": "Working"
                }
            ]
        },
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 14: 确认媒体转推项目启动**

发起 Start 操作成功后， 媒体转推项目开始启动，在30秒内还需要发起 Confirm 操作进行确认。如果超时没有确认，该项目会被自动停止掉。

**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 Confirm。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation Confirm \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

**Example 15: 设置定时转推**

项目需要是 Idle 状态，设置自动转推时间后在指定时间内启动项目进行转推。
**输入参数：**
除公共参数及 Platform、ProjectId 之外，其余参数填写规范如下：

参数名称 | 必选 | 类型 | 描述
------- | ------- | ------- | -------
Operation | 是 | String | 请填写 ModifyPlaySetting。
PlaySetting | 是 | [MediaCastPlaySetting](https://cloud.tencent.com/document/api/1156/40360#MediaCastPlaySetting) | 播放参数。

Input: 

```
tccli cme HandleMediaCastProject --cli-unfold-argument  \
    --Platform test \
    --Operation ModifyPlaySetting \
    --PlaySetting.AutoStartTime 2022-12-20T20:00:00Z \
    --ProjectId 12522d74de35ff
```

Output: 
```
{
    "Response": {
        "PlayInfo": null,
        "SourceInfoSet": [],
        "DestinationInfoSet": [],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5x"
    }
}
```

