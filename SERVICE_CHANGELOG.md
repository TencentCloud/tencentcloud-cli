# Release 3.0.1362.1

## 语音识别(asr) 版本：2019-06-14

### 第 32 次发布

发布时间：2026-02-04 01:11:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [VoicePrintEnroll](http://document.tencentcloudapi.woa.com/document/product/1093/81019)

	* 新增入参：AudioUrl

	* <font color="#dd0000">**修改入参**：</font>Data

* [VoicePrintUpdate](http://document.tencentcloudapi.woa.com/document/product/1093/81018)

	* 新增入参：AudioUrl

	* <font color="#dd0000">**修改入参**：</font>Data

* [VoicePrintVerify](http://document.tencentcloudapi.woa.com/document/product/1093/81017)

	* 新增入参：AudioUrl

	* <font color="#dd0000">**修改入参**：</font>Data




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 158 次发布

发布时间：2026-02-04 01:16:12

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#InstanceInfo)

	* 新增成员：CpuModel




## 腾讯混元大模型(hunyuan) 版本：2023-09-01

### 第 25 次发布

发布时间：2026-02-04 01:43:05

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [Describe3DSmartTopologyJob](http://document.tencentcloudapi.woa.com/document/product/1744/88754)
* [DescribeHunyuanTo3DUVJob](http://document.tencentcloudapi.woa.com/document/product/1744/88854)
* [QueryHunyuanTo3DTextureEditJob](http://document.tencentcloudapi.woa.com/document/product/1744/88853)
* [Submit3DSmartTopologyJob](http://document.tencentcloudapi.woa.com/document/product/1744/88753)
* [SubmitHunyuanTo3DTextureEditJob](http://document.tencentcloudapi.woa.com/document/product/1744/88852)
* [SubmitHunyuanTo3DUVJob](http://document.tencentcloudapi.woa.com/document/product/1744/88851)

新增数据结构：

* [ImageInfo](http://document.tencentcloudapi.woa.com/document/product/1744/85813#ImageInfo)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 35 次发布

发布时间：2026-02-04 01:45:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateWebResource](http://document.tencentcloudapi.woa.com/document/product/1794/86628)

	* 新增入参：WebGwNoAuth

* [DescribeAggrSoftDeviceList](http://document.tencentcloudapi.woa.com/document/product/1794/87619)

	* 新增入参：GroupId, GroupType

* [DescribeDLPSendFileTrendAnalyse](http://document.tencentcloudapi.woa.com/document/product/1794/86513)

	* 新增入参：DomainInstanceId

* [DescribeDeviceCompliantInfos](http://document.tencentcloudapi.woa.com/document/product/1794/86418)

	* 新增入参：RiskLevel

* [DescribeDeviceGroups](http://document.tencentcloudapi.woa.com/document/product/1794/86352)

	* 新增入参：DomainInstanceId, NewScope

* [DescribeDeviceVirtualGroups](http://document.tencentcloudapi.woa.com/document/product/1794/86349)

	* 新增入参：NewScope

* [DescribeDownloadHardwareChangeInfos](http://document.tencentcloudapi.woa.com/document/product/1794/86344)

	* 新增入参：ExportOrder

* [DescribeHardwareLog](http://document.tencentcloudapi.woa.com/document/product/1794/86340)

	* 新增入参：DomainInstanceId, BeginTime, EndTime

* [DescribeLogDetailTerminalSecurity](http://document.tencentcloudapi.woa.com/document/product/1794/86456)

	* 新增入参：DomainInstanceId, RulePayload, RulePayloadMode

* [DescribeVirtualDevices](http://document.tencentcloudapi.woa.com/document/product/1794/86335)

	* 新增入参：NewScope

* [DescribeVirusRisks](http://document.tencentcloudapi.woa.com/document/product/1794/86413)

	* 新增入参：DomainInstanceId

* [ExportDLPFile](http://document.tencentcloudapi.woa.com/document/product/1794/86504)

	* 新增入参：DomainInstanceId

* [ModifyDLPRiskStatus](http://document.tencentcloudapi.woa.com/document/product/1794/86494)

	* 新增入参：DomainInstanceId

* [ModifyWebResource](http://document.tencentcloudapi.woa.com/document/product/1794/86625)

	* 新增入参：WebGwNoAuth


新增数据结构：

* [RulePayload](http://document.tencentcloudapi.woa.com/document/product/1794/86648#RulePayload)
* [RulePayloadItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#RulePayloadItem)

修改数据结构：

* [AccessUserMessage](http://document.tencentcloudapi.woa.com/document/product/1794/86648#AccessUserMessage)

	* 新增成员：NgnSwitch, NgnMode, CurrentUploadTraffic, CurrentDownloadTraffic, ClientLocalIP, BlackStatusDeadline

	* <font color="#dd0000">**修改成员**：</font>BlackListStatus, AccountGroupName, GroupNamePath, State, LastLoginTime, Id, MacAddress, UpdateTime, UserSource, HostName, UserId, IP, OsType, Ticket, Remark, DeviceName, TimeStamp, LastLogoutTime, GroupName, DeviceType, LoginUser, Os, ClientIP, CreateTime, DeviceId, DeviceUserName, GroupId

* [AggrSoftDeviceRow](http://document.tencentcloudapi.woa.com/document/product/1794/86648#AggrSoftDeviceRow)

	* 新增成员：AssetType, IOAUserName, AccountGroupName, LocalIpList, Mid

* [CompliantDeviceDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#CompliantDeviceDetail)

	* 新增成员：AutoLockResult, AutoLockStatus, AutoLockDetail, InstallSysSafeFileResult, InstallSysSafeFileResultStatus, InstallSysSafeFileDetail, ComputerNameResult, ComputerNameStatus, ComputerNameDetail, UserInfoResult, UserInfoStatus, UserInfoDetail, PolicyName, ClassAsset, LocalIpList, OsType, AccountGroupName

* [Condition](http://document.tencentcloudapi.woa.com/document/product/1794/86648#Condition)

	* 新增成员：RulePayload, RulePayloadMode

* [DescribeBusinessResourceData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeBusinessResourceData)

	* 新增成员：WebGwNoAuth

* [DescribeTaskResultData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeTaskResultData)

	* 新增成员：OsType

* [HardwareChangeInfo](http://document.tencentcloudapi.woa.com/document/product/1794/86648#HardwareChangeInfo)

	* 新增成员：Os, OsVersion, AssetType, AccountGroupName, Hid, LocalIpList

* [PolicyListData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#PolicyListData)

	* 新增成员：HighRiskDeviceCount, MiddleRiskDeviceCount, LowRiskDeviceCount




## 媒体处理(mps) 版本：2019-06-12

### 第 149 次发布

发布时间：2026-02-04 01:58:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ParseLiveStreamProcessNotification](http://document.tencentcloudapi.woa.com/document/product/862/39229)

	* 新增出参：AiSmartSubtitleResultInfo


新增数据结构：

* [LiveSmartSubtitleResult](http://document.tencentcloudapi.woa.com/document/product/862/37615#LiveSmartSubtitleResult)
* [LiveStreamAiSmartSubtitleResultInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#LiveStreamAiSmartSubtitleResultInfo)
* [VideoComprehensionResultItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#VideoComprehensionResultItem)

修改数据结构：

* [AiAnalysisTaskReelOutput](http://document.tencentcloudapi.woa.com/document/product/862/37615#AiAnalysisTaskReelOutput)

	* 新增成员：VideoPaths

* [AiAnalysisTaskVideoComprehensionOutput](http://document.tencentcloudapi.woa.com/document/product/862/37615#AiAnalysisTaskVideoComprehensionOutput)

	* 新增成员：VideoComprehensionExtInfo, VideoComprehensionResultList

* [ChannelInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#ChannelInfo)

	* 新增成员：SecretId, SecretKey, SessionToken




## 集团账号管理(organization) 版本：2021-03-31

### 第 61 次发布

发布时间：2026-02-04 02:01:45

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ManagerShareUnit](http://document.tencentcloudapi.woa.com/document/product/850/67060#ManagerShareUnit)

	* 新增成员：ShareNodeNum




## 集团账号管理(organization) 版本：2018-12-25



## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 113 次发布

发布时间：2026-02-04 02:16:34

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyClusterAttribute](http://document.tencentcloudapi.woa.com/document/product/457/42938)

	* 新增入参：IsHighAvailability

	* 新增出参：IsHighAvailability


修改数据结构：

* [Cluster](http://document.tencentcloudapi.woa.com/document/product/457/31866#Cluster)

	* 新增成员：IsHighAvailability

* [ClusterAdvancedSettings](http://document.tencentcloudapi.woa.com/document/product/457/31866#ClusterAdvancedSettings)

	* 新增成员：IsHighAvailability




