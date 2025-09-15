# Release 3.0.1271.1

## 云托付物理服务器(chc) 版本：2023-04-18

### 第 2 次发布

发布时间：2025-09-11 01:12:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreatePersonnelVisitWorkOrder](http://document.tencentcloudapi.woa.com/document/product/1790/87372)

	* 新增入参：CarSet

* [DescribePersonnelVisitWorkOrderDetail](http://document.tencentcloudapi.woa.com/document/product/1790/87354)

	* 新增出参：CarSet


新增数据结构：

* [PersonnelVisitCar](http://document.tencentcloudapi.woa.com/document/product/1790/87378#PersonnelVisitCar)

修改数据结构：

* [WorkOrderData](http://document.tencentcloudapi.woa.com/document/product/1790/87378#WorkOrderData)

	* 新增成员：TicketId




## 消息队列 CKafka 版(ckafka) 版本：2019-08-19

### 第 111 次发布

发布时间：2025-09-11 01:13:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreatePostPaidInstance](http://document.tencentcloudapi.woa.com/document/product/597/78116)

	* <font color="#dd0000">**修改入参**：</font>SubnetId

* [CreateRoute](http://document.tencentcloudapi.woa.com/document/product/597/70172)

	* 新增入参：Note


修改数据结构：

* [Route](http://document.tencentcloudapi.woa.com/document/product/597/40861#Route)

	* 新增成员：Note

* [ZoneResponse](http://document.tencentcloudapi.woa.com/document/product/597/40861#ZoneResponse)

	* <font color="#dd0000">**删除成员**：</font>Version




## 日志服务(cls) 版本：2020-10-16

### 第 125 次发布

发布时间：2025-09-11 01:17:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAlarm](http://document.tencentcloudapi.woa.com/document/product/614/56466)

	* 新增入参：MonitorNotice

	* <font color="#dd0000">**修改入参**：</font>AlarmNoticeIds

* [ModifyAlarm](http://document.tencentcloudapi.woa.com/document/product/614/56459)

	* 新增入参：MonitorNotice


新增数据结构：

* [MonitorNotice](http://document.tencentcloudapi.woa.com/document/product/614/56471#MonitorNotice)
* [MonitorNoticeRule](http://document.tencentcloudapi.woa.com/document/product/614/56471#MonitorNoticeRule)

修改数据结构：

* [AlarmInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#AlarmInfo)

	* 新增成员：MonitorNotice

* [AlertHistoryRecord](http://document.tencentcloudapi.woa.com/document/product/614/56471#AlertHistoryRecord)

	* 新增成员：SendType




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 4 次发布

发布时间：2025-09-11 01:18:17

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DisplayAsset](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayAsset)

	* 新增成员：Ports, Services, Domains, LastModify




## 专线接入(dc) 版本：2018-04-10

### 第 15 次发布

发布时间：2025-09-11 01:20:59

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DirectConnectTunnel](http://document.tencentcloudapi.woa.com/document/product/216/18418#DirectConnectTunnel)

	* 新增成员：AccessPointName, AccessPointId




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 112 次发布

发布时间：2025-09-11 01:23:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudInstance](http://document.tencentcloudapi.woa.com/document/product/589/85470)

	* 新增入参：DefaultMetaVersion, NeedCdbAudit

* [CreateCluster](http://document.tencentcloudapi.woa.com/document/product/589/76813)

	* 新增入参：DefaultMetaVersion, NeedCdbAudit

* [CreateInstance](http://document.tencentcloudapi.woa.com/document/product/589/34261)

	* 新增入参：DefaultMetaVersion, NeedCdbAudit

* [DescribeNodeDataDisks](http://document.tencentcloudapi.woa.com/document/product/589/85605)

	* 新增入参：Scene

	* 新增出参：MaxThroughputPerformance

* [InquiryPriceCreateInstance](http://document.tencentcloudapi.woa.com/document/product/589/33980)

	* 新增入参：DefaultMetaVersion, NeedCdbAudit


新增数据结构：

* [TagInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#TagInfo)

修改数据结构：

* [CBSInstance](http://document.tencentcloudapi.woa.com/document/product/589/33981#CBSInstance)

	* 新增成员：Tags, ThroughputPerformance

* [LoadAutoScaleStrategy](http://document.tencentcloudapi.woa.com/document/product/589/33981#LoadAutoScaleStrategy)

	* 新增成员：GraceDownProtectFlag

* [TimeAutoScaleStrategy](http://document.tencentcloudapi.woa.com/document/product/589/33981#TimeAutoScaleStrategy)

	* 新增成员：GraceDownProtectFlag




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 163 次发布

发布时间：2025-09-11 01:24:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateMultiFlowSignQRCode](http://document.tencentcloudapi.woa.com/document/product/1668/79347)

	* 新增入参：QrCodeName, QrCodeExpiredOn


修改数据结构：

* [MiniAppCreateFlowOption](http://document.tencentcloudapi.woa.com/document/product/1668/79360#MiniAppCreateFlowOption)

	* 新增成员：ForbidEditFlow




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 203 次发布

发布时间：2025-09-11 01:25:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChannelCreateMultiFlowSignQRCode](http://document.tencentcloudapi.woa.com/document/product/1595/75252)

	* 新增入参：QrCodeName, QrCodeExpiredOn




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 游戏多媒体引擎(gme) 版本：2018-07-11

### 第 28 次发布

发布时间：2025-09-11 01:26:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ControlAIConversation](http://document.tencentcloudapi.woa.com/document/product/607/87635)
* [DeleteVoicePrint](http://document.tencentcloudapi.woa.com/document/product/607/87634)
* [DescribeAIConversation](http://document.tencentcloudapi.woa.com/document/product/607/87633)
* [DescribeVoicePrint](http://document.tencentcloudapi.woa.com/document/product/607/87632)
* [RegisterVoicePrint](http://document.tencentcloudapi.woa.com/document/product/607/87631)
* [StartAIConversation](http://document.tencentcloudapi.woa.com/document/product/607/87630)
* [StopAIConversation](http://document.tencentcloudapi.woa.com/document/product/607/87629)
* [UpdateAIConversation](http://document.tencentcloudapi.woa.com/document/product/607/87628)
* [UpdateVoicePrint](http://document.tencentcloudapi.woa.com/document/product/607/87627)

新增数据结构：

* [AgentConfig](http://document.tencentcloudapi.woa.com/document/product/607/35375#AgentConfig)
* [AmbientSound](http://document.tencentcloudapi.woa.com/document/product/607/35375#AmbientSound)
* [InvokeLLM](http://document.tencentcloudapi.woa.com/document/product/607/35375#InvokeLLM)
* [STTConfig](http://document.tencentcloudapi.woa.com/document/product/607/35375#STTConfig)
* [ServerPushText](http://document.tencentcloudapi.woa.com/document/product/607/35375#ServerPushText)
* [TurnDetection](http://document.tencentcloudapi.woa.com/document/product/607/35375#TurnDetection)
* [VoicePrint](http://document.tencentcloudapi.woa.com/document/product/607/35375#VoicePrint)
* [VoicePrintInfo](http://document.tencentcloudapi.woa.com/document/product/607/35375#VoicePrintInfo)



## 腾讯混元大模型(hunyuan) 版本：2023-09-01

### 第 16 次发布

发布时间：2025-09-11 01:27:51

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [WebSearchOptions](http://document.tencentcloudapi.woa.com/document/product/1744/85813#WebSearchOptions)

	* 新增成员：EnableImage, EnableMusic




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 25 次发布

发布时间：2025-09-11 01:28:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeAggrSoftCategorySoftList](http://document.tencentcloudapi.woa.com/document/product/1794/87590)

	* 新增入参：Condition

* [DescribeAggrSoftDeviceList](http://document.tencentcloudapi.woa.com/document/product/1794/87619)

	* 新增入参：Condition

* [ExportSoftListBySoftCategory](http://document.tencentcloudapi.woa.com/document/product/1794/86202)

	* <font color="#dd0000">**修改出参**：</font>Data




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 88 次发布

发布时间：2025-09-11 01:30:20

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BatchUpdateFirmware](http://document.tencentcloudapi.woa.com/document/product/1081/87643)
* [CreateOtaModule](http://document.tencentcloudapi.woa.com/document/product/1081/87642)
* [DeleteOtaModule](http://document.tencentcloudapi.woa.com/document/product/1081/87641)
* [DescribeFirmwareTaskDevices](http://document.tencentcloudapi.woa.com/document/product/1081/87637)
* [DescribeFirmwareTasks](http://document.tencentcloudapi.woa.com/document/product/1081/87636)
* [ListOtaModules](http://document.tencentcloudapi.woa.com/document/product/1081/87640)
* [ListProductOtaModules](http://document.tencentcloudapi.woa.com/document/product/1081/87639)
* [UpdateOtaModule](http://document.tencentcloudapi.woa.com/document/product/1081/87638)

新增数据结构：

* [DeviceUpdateStatus](http://document.tencentcloudapi.woa.com/document/product/1081/34988#DeviceUpdateStatus)
* [FirmwareTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#FirmwareTaskInfo)
* [OtaModuleInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#OtaModuleInfo)



## 轻量应用服务器(lighthouse) 版本：2020-03-24

### 第 83 次发布

发布时间：2025-09-11 01:32:56

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [RebootInstances](http://document.tencentcloudapi.woa.com/document/product/1207/47572)

	* 新增入参：StopType

* [StopInstances](http://document.tencentcloudapi.woa.com/document/product/1207/47569)

	* 新增入参：StopType




## 知识引擎原子能力(lkeap) 版本：2024-05-22

### 第 32 次发布

发布时间：2025-09-11 01:34:15

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetEmbedding](http://document.tencentcloudapi.woa.com/document/product/1764/85635)

	* 新增入参：TextType, Instruction




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 19 次发布

发布时间：2025-09-11 01:36:00

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstance](http://document.tencentcloudapi.woa.com/document/product/1773/84913)

	* 新增出参：TopicPrefixSlashLimit, MessageRate

* [DescribeMessageDetails](http://document.tencentcloudapi.woa.com/document/product/1773/87119)

	* 新增出参：ContentType, PayloadFormatIndicator, MessageExpiryInterval, ResponseTopic, CorrelationData, SubscriptionIdentifier

* [ModifyInstance](http://document.tencentcloudapi.woa.com/document/product/1773/85729)

	* 新增入参：MessageRate




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 100 次发布

发布时间：2025-09-11 01:42:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/82745)

	* 新增入参：IsRealTime

	* 新增出参：IsHotBackupResourceGroup




## TI-ONE 训练平台(tione) 版本：2019-10-22



