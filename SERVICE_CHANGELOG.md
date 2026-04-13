# Release 3.0.1402.1

## 配置审计(config) 版本：2022-08-02

### 第 9 次发布

发布时间：2026-04-14 01:24:50

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddAlarmPolicy](http://document.tencentcloudapi.woa.com/document/product/1751/89976)
* [DeleteAlarmPolicy](http://document.tencentcloudapi.woa.com/document/product/1751/89972)
* [ListAlarmPolicy](http://document.tencentcloudapi.woa.com/document/product/1751/89975)
* [UpdateAlarmPolicy](http://document.tencentcloudapi.woa.com/document/product/1751/89974)

修改接口：

* [AddConfigRule](http://document.tencentcloudapi.woa.com/document/product/1751/89129)

	* 新增出参：RuleId


新增数据结构：

* [AlarmPolicyRsp](http://document.tencentcloudapi.woa.com/document/product/1751/82623#AlarmPolicyRsp)



## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 160 次发布

发布时间：2026-04-14 01:30:54

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AuditLog](http://document.tencentcloudapi.woa.com/document/product/1003/48097#AuditLog)

	* 新增成员：ClientPort




## 人脸核身(faceid) 版本：2018-03-01

### 第 95 次发布

发布时间：2026-04-14 01:43:32

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [VideoLivenessCompare](http://document.tencentcloudapi.woa.com/document/product/1007/76416)



## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 55 次发布

发布时间：2026-04-14 02:01:05

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [RestoreDBInstance](http://document.tencentcloudapi.woa.com/document/product/240/89977)

新增数据结构：

* [RestoreCollection](http://document.tencentcloudapi.woa.com/document/product/240/38576#RestoreCollection)
* [RestoreDatabases](http://document.tencentcloudapi.woa.com/document/product/240/38576#RestoreDatabases)



## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 25 次发布

发布时间：2026-04-14 02:05:10

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstance](http://document.tencentcloudapi.woa.com/document/product/1773/84913)

	* 新增出参：BlockRuleLimit




## 腾讯健康组学平台(omics) 版本：2022-11-28

### 第 25 次发布

发布时间：2026-04-14 02:06:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribePublicApplications](http://document.tencentcloudapi.woa.com/document/product/1725/89948)

	* 新增入参：ParentAppId, AppType




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 38 次发布

发布时间：2026-04-14 02:14:54

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ExecutePGSql](http://document.tencentcloudapi.woa.com/document/product/876/89978)



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 126 次发布

发布时间：2026-04-14 02:25:34

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [RoleReplicasInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#RoleReplicasInfo)

修改数据结构：

* [ModelInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ModelInfo)

	* 新增成员：GooseFS

* [ServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroup)

	* 新增成员：RoleReplicasInfo

* [ServiceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceInfo)

	* 新增成员：RoleReplicasInfo

* [VolumeMount](http://document.tencentcloudapi.woa.com/document/product/851/74915#VolumeMount)

	* 新增成员：GooseFSx, GooseFS




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 61 次发布

发布时间：2026-04-14 02:29:12

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateMigrationTask](http://document.tencentcloudapi.woa.com/document/product/1739/89979)



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 9 次发布

发布时间：2026-04-14 02:37:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLogicTable](http://document.tencentcloudapi.woa.com/document/product/1607/89418)

	* 新增入参：ResourceId

* [GetLogicTable](http://document.tencentcloudapi.woa.com/document/product/1607/89415)

	* 新增入参：ResourceId

* [ListStreamDatabasesPage](http://document.tencentcloudapi.woa.com/document/product/1607/89546)

	* 新增入参：ResourceId

	* <font color="#dd0000">**修改入参**：</font>MaxResults, PageToken, ConnectionId, Keyword, SubType

* [ListStreamSchemasPage](http://document.tencentcloudapi.woa.com/document/product/1607/89545)

	* 新增入参：ResourceId

	* <font color="#dd0000">**修改入参**：</font>MaxResults, PageToken, DatabaseName, ConnectionId, Keyword

* [ListStreamTablesPage](http://document.tencentcloudapi.woa.com/document/product/1607/89544)

	* 新增入参：CatalogName, ResourceId

	* <font color="#dd0000">**修改入参**：</font>ConnectionId

* [ListTableByRegex](http://document.tencentcloudapi.woa.com/document/product/1607/89407)

	* 新增入参：ResourceId

	* <font color="#dd0000">**修改入参**：</font>DatabaseName, RegexTable, WorkspaceId

* [OperateDataValidateTask](http://document.tencentcloudapi.woa.com/document/product/1607/89403)

	* 新增入参：OperateVersion, OperateType


修改数据结构：

* [GetStreamTaskRunningInfoRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetStreamTaskRunningInfoRsp)

	* 新增成员：PreparePhase

* [IntegrationNodeSchema](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchema)

	* 新增成员：TableName

* [ListStreamTasksRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListStreamTasksRsp)

	* 新增成员：PageNumber, PageSize

* [StreamTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#StreamTaskInfo)

	* 新增成员：ValidateIsCheck

* [SyncPhaseOverview](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SyncPhaseOverview)

	* 新增成员：SchemaNum, DatabaseNum, TotalTableNum, TotalSchemaNum, TotalDatabaseNum, TotalTopicNum, StopTime




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



