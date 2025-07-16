# Release 3.0.1243.1

## 主机安全(cwp) 版本：2018-02-28

### 第 127 次发布

发布时间：2025-07-17 01:13:34

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Machine](http://document.tencentcloudapi.woa.com/document/product/296/19867#Machine)

	* 新增成员：AgentVersion




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 134 次发布

发布时间：2025-07-17 01:14:53

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AddClusterSlaveZone](http://document.tencentcloudapi.woa.com/document/product/1003/75706)

	* 新增入参：SemiSyncTimeout

* [ModifyClusterSlaveZone](http://document.tencentcloudapi.woa.com/document/product/1003/75705)

	* 新增入参：SemiSyncTimeout


修改数据结构：

* [SlaveZoneAttrItem](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SlaveZoneAttrItem)

	* 新增成员：SemiSyncTimeout




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 152 次发布

发布时间：2025-07-17 01:18:40

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateBatchInformationExtractionTask](http://document.tencentcloudapi.woa.com/document/product/1668/87220)
* [DescribeInformationExtractionTask](http://document.tencentcloudapi.woa.com/document/product/1668/87219)

新增数据结构：

* [ExtractionField](http://document.tencentcloudapi.woa.com/document/product/1668/79360#ExtractionField)



## 云直播CSS(live) 版本：2018-08-01

### 第 91 次发布

发布时间：2025-07-17 01:24:11

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAuditKeywords](http://document.tencentcloudapi.woa.com/document/product/267/87199)

	* 新增入参：Keywords, LibId

	* 新增出参：KeywordIds, DupInfos

* [DeleteAuditKeywords](http://document.tencentcloudapi.woa.com/document/product/267/87198)

	* 新增入参：KeywordIds, LibId

	* 新增出参：SuccessCount, Infos

* [DescribeAuditKeywords](http://document.tencentcloudapi.woa.com/document/product/267/87197)

	* 新增入参：Offset, Limit, LibId, Content, Labels

	* 新增出参：Total, Infos


新增数据结构：

* [AuditKeyword](http://document.tencentcloudapi.woa.com/document/product/267/20474#AuditKeyword)
* [AuditKeywordDeleteDetail](http://document.tencentcloudapi.woa.com/document/product/267/20474#AuditKeywordDeleteDetail)
* [AuditKeywordInfo](http://document.tencentcloudapi.woa.com/document/product/267/20474#AuditKeywordInfo)



## 知识引擎原子能力(lkeap) 版本：2024-05-22

### 第 29 次发布

发布时间：2025-07-17 01:25:16

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetReconstructDocumentResult](http://document.tencentcloudapi.woa.com/document/product/1764/85632)

	* 新增出参：Usage

* [ReconstructDocumentSSE](http://document.tencentcloudapi.woa.com/document/product/1764/84923)

	* 新增出参：FailPageNum, SuccessPageNum


修改数据结构：

* [CreateReconstructDocumentFlowConfig](http://document.tencentcloudapi.woa.com/document/product/1764/84021#CreateReconstructDocumentFlowConfig)

	* 新增成员：IgnoreFailedPage

* [CreateSplitDocumentFlowConfig](http://document.tencentcloudapi.woa.com/document/product/1764/84021#CreateSplitDocumentFlowConfig)

	* 新增成员：IgnoreFailedPage

* [DocumentUsage](http://document.tencentcloudapi.woa.com/document/product/1764/84021#DocumentUsage)

	* 新增成员：SuccessPageNum, FailPageNum

* [ReconstructDocumentSSEConfig](http://document.tencentcloudapi.woa.com/document/product/1764/84021#ReconstructDocumentSSEConfig)

	* 新增成员：IgnoreFailedPage




## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 104 次发布

发布时间：2025-07-17 01:26:21

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ModifyConditionsTemplateRequestEventCondition](http://document.tencentcloudapi.woa.com/document/product/248/30354#ModifyConditionsTemplateRequestEventCondition)

	* 新增成员：MetricName, Description

	* <font color="#dd0000">**修改成员**：</font>AlarmNotifyPeriod, AlarmNotifyType, EventID




## 媒体处理(mps) 版本：2019-06-12

### 第 102 次发布

发布时间：2025-07-17 01:27:07

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeWordSamples](http://document.tencentcloudapi.woa.com/document/product/862/39440)

	* 新增入参：ChannelInfo


修改数据结构：

* [EvaluationTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#EvaluationTaskInput)

* [MediaProcessTaskTranscodeResult](http://document.tencentcloudapi.woa.com/document/product/862/37615#MediaProcessTaskTranscodeResult)

	* <font color="#dd0000">**修改成员**：</font>FinishTime




## 腾讯健康组学平台(omics) 版本：2022-11-28

### 第 19 次发布

发布时间：2025-07-17 01:29:07

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClusterOption](http://document.tencentcloudapi.woa.com/document/product/1725/80781#ClusterOption)

	* 新增成员：AutoUpgradeClusterLevel




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 87 次发布

发布时间：2025-07-17 01:34:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/851/76703)

	* 新增入参：ResourceGroupId




## TI-ONE 训练平台(tione) 版本：2019-10-22



