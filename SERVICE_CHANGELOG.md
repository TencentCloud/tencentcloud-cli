# Release 3.0.1412.1

## 弹性伸缩(as) 版本：2018-04-19

### 第 56 次发布

发布时间：2026-04-28 01:09:02

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ServiceSettings](http://document.tencentcloudapi.woa.com/document/product/377/20453#ServiceSettings)

	* 新增成员：Confidentiality




## 商业智能分析 BI(bi) 版本：2022-01-05

### 第 36 次发布

发布时间：2026-04-28 01:09:47

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAuthApiKey](http://document.tencentcloudapi.woa.com/document/product/1707/90089)
* [DeleteAuthApiKey](http://document.tencentcloudapi.woa.com/document/product/1707/90088)
* [DescribeAuthApiKeyInfo](http://document.tencentcloudapi.woa.com/document/product/1707/90087)
* [DescribeAuthApiKeyList](http://document.tencentcloudapi.woa.com/document/product/1707/90084)
* [ModifyAuthApiKey](http://document.tencentcloudapi.woa.com/document/product/1707/90086)

新增数据结构：

* [ApiKeyAuthApplyVO](http://document.tencentcloudapi.woa.com/document/product/1707/80324#ApiKeyAuthApplyVO)
* [ApiKeyAuthApplyVOList](http://document.tencentcloudapi.woa.com/document/product/1707/80324#ApiKeyAuthApplyVOList)



## 腾讯云数据仓库TCHouse-C(cdwch) 版本：2020-09-15

### 第 32 次发布

发布时间：2026-04-28 01:12:55

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1667/79282#InstanceInfo)

	* 新增成员：HttpsEnabled




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 16 次发布

发布时间：2026-04-28 01:15:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSubDomain](http://document.tencentcloudapi.woa.com/document/product/1792/88114)

	* 新增入参：DnsType, DnsValue


修改数据结构：

* [DisplaySubDomain](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplaySubDomain)

	* 新增成员：DnsType, DnsValue




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 162 次发布

发布时间：2026-04-28 01:17:29

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBackupConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48094)

	* 新增出参：SparseBackupConfig

* [ModifyBackupConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48090)

	* 新增入参：SparseBackupConfig


新增数据结构：

* [MonthDay](http://document.tencentcloudapi.woa.com/document/product/1003/48097#MonthDay)
* [SparseBackupConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SparseBackupConfig)
* [SparseBackupConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SparseBackupConfigInfo)
* [SparseBackupConfigRsp](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SparseBackupConfigRsp)
* [SparsePeriodTime](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SparsePeriodTime)

修改数据结构：

* [BackupFileInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupFileInfo)

	* 新增成员：BackupPeriodStrategy

* [DeliverSummary](http://document.tencentcloudapi.woa.com/document/product/1003/48097#DeliverSummary)

	* 新增成员：DeliverError




## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 153 次发布

发布时间：2026-04-28 01:19:24

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AnalysisTaskResults](http://document.tencentcloudapi.woa.com/document/product/1342/53778#AnalysisTaskResults)

	* 新增成员：ShuffleWriteBytesSum, GenerateWay

* [TaskFullRespInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#TaskFullRespInfo)

	* 新增成员：ShuffleWriteBytesSum, ActiveCore




## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 38 次发布

发布时间：2026-04-28 01:25:59

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeLocalAccounts](http://document.tencentcloudapi.woa.com/document/product/1794/86311)

	* 新增入参：DomainInstanceId


新增数据结构：

* [DeviceNetworkCardBrief](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceNetworkCardBrief)
* [DeviceVideoCardBrief](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceVideoCardBrief)

修改数据结构：

* [DescribeBusinessResourceData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeBusinessResourceData)

	* 新增成员：ConnectorGroupType, DomainSuffix

* [DescribeWebResourceInfoData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeWebResourceInfoData)

	* 新增成员：FrontDomainSuffixVPC

	* <font color="#dd0000">**修改成员**：</font>FrontDomainSuffix

* [DeviceDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DeviceDetail)

	* 新增成员：NetworkCards, VideoCards

* [PackageDetail](http://document.tencentcloudapi.woa.com/document/product/1794/86648#PackageDetail)

	* 新增成员：Arch, Format

	* <font color="#dd0000">**修改成员**：</font>Url, OsType, Version




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 29 次发布

发布时间：2026-04-28 01:29:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSearchStatsGraph](http://document.tencentcloudapi.woa.com/document/product/1759/88253)

* [ListDoc](http://document.tencentcloudapi.woa.com/document/product/1759/83688)

	* 新增入参：UpdateTime

* [ListQA](http://document.tencentcloudapi.woa.com/document/product/1759/83654)

	* 新增入参：CreateTime, UpdateTime


新增数据结构：

* [TimeRange](http://document.tencentcloudapi.woa.com/document/product/1759/83593#TimeRange)

修改数据结构：

* [QAQuery](http://document.tencentcloudapi.woa.com/document/product/1759/83593#QAQuery)

	* 新增成员：CreateTime, UpdateTime




## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 56 次发布

发布时间：2026-04-28 01:30:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateDBInstance](http://document.tencentcloudapi.woa.com/document/product/240/38571)

	* 新增入参：CpuCore

* [CreateDBInstanceHour](http://document.tencentcloudapi.woa.com/document/product/240/38570)

	* 新增入参：CpuCore

* [InquirePriceCreateDBInstances](http://document.tencentcloudapi.woa.com/document/product/240/43666)

	* 新增入参：ReadonlyNodeNum, Cpu

* [InquirePriceModifyDBInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/240/43665)

	* 新增入参：Cpu

* [ModifyDBInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/240/38565)

	* 新增入参：Cpu, MachineCode




## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 123 次发布

发布时间：2026-04-28 01:31:38

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CheckAddressByPrometheus](http://document.tencentcloudapi.woa.com/document/product/248/90090)



## 媒体处理(mps) 版本：2019-06-12

### 第 167 次发布

发布时间：2026-04-28 01:32:33

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSmartSubtitleTemplate](http://document.tencentcloudapi.woa.com/document/product/862/85944)

	* 新增入参：SpeakerMode, SpeakerLabel

* [ModifySmartSubtitleTemplate](http://document.tencentcloudapi.woa.com/document/product/862/85941)

	* 新增入参：SpeakerMode, SpeakerLabel


修改数据结构：

* [AnimatedGraphicTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#AnimatedGraphicTaskInput)

	* 新增成员：ExtInfo

* [ImageSpriteTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#ImageSpriteTaskInput)

	* 新增成员：ExtInfo

* [RawSmartSubtitleParameter](http://document.tencentcloudapi.woa.com/document/product/862/37615#RawSmartSubtitleParameter)

	* 新增成员：SpeakerMode, SpeakerLabel

* [SampleSnapshotTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#SampleSnapshotTaskInput)

	* 新增成员：ExtInfo

* [SmartSubtitleTaskResultInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#SmartSubtitleTaskResultInput)

	* 新增成员：UserExtPara

* [SmartSubtitleTemplateItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#SmartSubtitleTemplateItem)

	* 新增成员：SubtitleEmbedId, SpeakerMode, SpeakerLabel

* [SnapshotByTimeOffsetTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#SnapshotByTimeOffsetTaskInput)

	* 新增成员：ExtInfo




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 57 次发布

发布时间：2026-04-28 01:34:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CloseAuditService](http://document.tencentcloudapi.woa.com/document/product/409/90099)
* [CreateAuditLogFile](http://document.tencentcloudapi.woa.com/document/product/409/90098)
* [DeleteAuditLogFile](http://document.tencentcloudapi.woa.com/document/product/409/90097)
* [DescribeAuditInstanceList](http://document.tencentcloudapi.woa.com/document/product/409/90096)
* [DescribeAuditLogFiles](http://document.tencentcloudapi.woa.com/document/product/409/90095)
* [DescribeAuditLogs](http://document.tencentcloudapi.woa.com/document/product/409/90094)
* [ModifyAuditService](http://document.tencentcloudapi.woa.com/document/product/409/90093)
* [OpenAuditService](http://document.tencentcloudapi.woa.com/document/product/409/90092)

新增数据结构：

* [AuditInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/409/16778#AuditInstanceInfo)
* [AuditLog](http://document.tencentcloudapi.woa.com/document/product/409/16778#AuditLog)
* [AuditLogFile](http://document.tencentcloudapi.woa.com/document/product/409/16778#AuditLogFile)
* [AuditLogFilter](http://document.tencentcloudapi.woa.com/document/product/409/16778#AuditLogFilter)
* [DeliverSummary](http://document.tencentcloudapi.woa.com/document/product/409/16778#DeliverSummary)
* [LogInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/409/16778#LogInstanceInfo)



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 129 次发布

发布时间：2026-04-28 01:41:57

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/82745)

	* 新增入参：TiProjectId

* [DescribeBillingResourceGroupAttachedWorkspaces](http://document.tencentcloudapi.woa.com/document/product/851/90063)

	* 新增入参：TiProjectId

* [DescribeBillingResourceGroups](http://document.tencentcloudapi.woa.com/document/product/851/74826)

	* 新增入参：TiProjectId

* [DescribeBillingResourceInstanceRunningJobs](http://document.tencentcloudapi.woa.com/document/product/851/82506)

	* 新增入参：TiProjectId

* [DescribeBillingResourceInstances](http://document.tencentcloudapi.woa.com/document/product/851/87617)

	* 新增入参：TiProjectId

* [DescribeDataSource](http://document.tencentcloudapi.woa.com/document/product/851/89012)

	* 新增入参：TiProjectId

* [DescribeModelServiceGroups](http://document.tencentcloudapi.woa.com/document/product/851/76493)

	* 新增入参：TiProjectId

	* 新增出参：GlobalTotalCount

* [DescribeNotebook](http://document.tencentcloudapi.woa.com/document/product/851/85839)

	* 新增入参：TiProjectId

* [DescribeNotebooks](http://document.tencentcloudapi.woa.com/document/product/851/85838)

	* 新增入参：TiProjectId

* [DescribeTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/85835)

	* 新增入参：TiProjectId

* [DescribeTrainingTaskPods](http://document.tencentcloudapi.woa.com/document/product/851/85834)

	* 新增入参：TiProjectId

* [DescribeTrainingTasks](http://document.tencentcloudapi.woa.com/document/product/851/85833)

	* 新增入参：TiProjectId


修改数据结构：

* [NotebookDetail](http://document.tencentcloudapi.woa.com/document/product/851/74915#NotebookDetail)

	* 新增成员：LatestOperatorInfo, WorkerConfig

* [NotebookSetItem](http://document.tencentcloudapi.woa.com/document/product/851/74915#NotebookSetItem)

	* 新增成员：LatestOperatorInfo

* [ResourceInstanceRunningJobInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceInstanceRunningJobInfo)

	* 新增成员：OriginalTaskId




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 16 次发布

发布时间：2026-04-28 01:48:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateFile](http://document.tencentcloudapi.woa.com/document/product/1607/89354)

	* 新增入参：GitConfig


新增数据结构：

* [CommonTagInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CommonTagInfo)

修改数据结构：

* [ColumnInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ColumnInfo)

	* 新增成员：Tags

* [FetchOption](http://document.tencentcloudapi.woa.com/document/product/1607/88970#FetchOption)

	* 新增成员：FetchTags

* [TableInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TableInfo)

	* 新增成员：Tags




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



