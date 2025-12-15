# Release 3.0.1327.1

## 日志服务(cls) 版本：2020-10-16

### 第 132 次发布

发布时间：2025-12-16 01:20:21

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeAlarmNotices](http://document.tencentcloudapi.woa.com/document/product/614/56462)

	* 新增入参：HasAlarmShieldCount

* [ModifyConsumer](http://document.tencentcloudapi.woa.com/document/product/614/66225)

	* 新增入参：RoleArn, ExternalId

* [ModifyShipper](http://document.tencentcloudapi.woa.com/document/product/614/58743)

	* 新增入参：RoleArn, ExternalId

* [ModifyTopic](http://document.tencentcloudapi.woa.com/document/product/614/56453)

	* 新增入参：StorageType, Encryption, IsSourceFrom


新增数据结构：

* [AlarmShieldCount](http://document.tencentcloudapi.woa.com/document/product/614/56471#AlarmShieldCount)

修改数据结构：

* [AlarmNotice](http://document.tencentcloudapi.woa.com/document/product/614/56471#AlarmNotice)

	* 新增成员：DeliverStatus, DeliverFlag, AlarmShieldCount

* [LogsetInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#LogsetInfo)

	* 新增成员：AssumerUin, MetricTopicCount

* [ShipperInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#ShipperInfo)

	* 新增成员：RoleArn, ExternalId, TaskStatus

* [TopicInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#TopicInfo)

	* 新增成员：AssumerUin, RoleName, IsSourceFrom




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 11 次发布

发布时间：2025-12-16 01:23:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSensitiveInfoTypes](http://document.tencentcloudapi.woa.com/document/product/1792/87416)

	* 新增入参：IsAggregation




## Elasticsearch Service(es) 版本：2018-04-16

### 第 96 次发布

发布时间：2025-12-16 01:36:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateClusterSnapshot](http://document.tencentcloudapi.woa.com/document/product/845/85136)

	* 新增入参：EsRepositoryType, UserEsRepository, StorageDuration, CosRetention, RetainUntilDate, RetentionGraceTime, RemoteCos, RemoteCosRegion


修改数据结构：

* [CosBackup](http://document.tencentcloudapi.woa.com/document/product/845/30634#CosBackup)

	* 新增成员：SnapshotName, PaasEsRepository, CosRetention, RetainUntilDate, RetentionGraceTime, RemoteCos, RemoteCosRegion, StrategyName, Indices, CreateTime

* [Snapshots](http://document.tencentcloudapi.woa.com/document/product/845/30634#Snapshots)

	* 新增成员：EsRepositoryType, PaasEsRepository, UserEsRepository, StorageDuration, AutoBackupInterval, CosRetention, RetainUntilDate, RetentionGraceTime, IsLocked, RemoteCos, RemoteCosRegion, CosEncryption, KmsKey, StrategyName




## 云游戏(gs) 版本：2019-11-18

### 第 46 次发布

发布时间：2025-12-16 01:39:28

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAndroidInstanceAcceleratorToken](http://document.tencentcloudapi.woa.com/document/product/1162/88094)

	* 新增出参：Token




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 13 次发布

发布时间：2025-12-16 01:47:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GenerateQA](http://document.tencentcloudapi.woa.com/document/product/1759/83690)

	* <font color="#dd0000">**修改入参**：</font>DocBizIds

* [GetWsToken](http://document.tencentcloudapi.woa.com/document/product/1759/83708)

	* 新增出参：VisionModelInputLimit

* [ListUnsatisfiedReply](http://document.tencentcloudapi.woa.com/document/product/1759/83652)

	* 新增入参：HandlingStatuses


新增数据结构：

* [AppModelDetailInfo](http://document.tencentcloudapi.woa.com/document/product/1759/83593#AppModelDetailInfo)
* [NL2SQLModelConfig](http://document.tencentcloudapi.woa.com/document/product/1759/83593#NL2SQLModelConfig)

修改数据结构：

* [AttrLabelDetail](http://document.tencentcloudapi.woa.com/document/product/1759/83593#AttrLabelDetail)

* [Filters](http://document.tencentcloudapi.woa.com/document/product/1759/83593#Filters)

	* 新增成员：HandlingStatuses

* [SearchStrategy](http://document.tencentcloudapi.woa.com/document/product/1759/83593#SearchStrategy)

	* 新增成员：NatureLanguageToSqlModelConfig




## 容器服务(tke) 版本：2022-05-01

### 第 15 次发布

发布时间：2025-12-16 02:10:25

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [CreateNativeNodePoolParam](http://document.tencentcloudapi.woa.com/document/product/457/74869#CreateNativeNodePoolParam)

	* 新增成员：Password

* [UpdateNativeNodePoolParam](http://document.tencentcloudapi.woa.com/document/product/457/74869#UpdateNativeNodePoolParam)

	* 新增成员：Password




## 容器服务(tke) 版本：2018-05-25



