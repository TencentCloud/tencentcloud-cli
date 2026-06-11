# Release 3.0.1441.1

## 应用性能监控(apm) 版本：2021-06-22

### 第 33 次发布

发布时间：2026-06-12 01:11:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeApmInstances](http://document.tencentcloudapi.woa.com/document/product/1463/65103)

	* 新增入参：PageIndex, PageSize, Keyword, OrderDirection, OrderBy

	* 新增出参：TotalCount, PageIndex, PageSize

* [DescribeMetricRecords](http://document.tencentcloudapi.woa.com/document/product/1463/68254)

	* 新增入参：ServiceID

* [DescribeTopologyNew](http://document.tencentcloudapi.woa.com/document/product/1463/88567)

	* 新增入参：EnableResourceLink

	* 新增出参：OverviewStats


新增数据结构：

* [OverviewStats](http://document.tencentcloudapi.woa.com/document/product/1463/64927#OverviewStats)
* [TopologyNodeStats](http://document.tencentcloudapi.woa.com/document/product/1463/64927#TopologyNodeStats)

修改数据结构：

* [TopologyEdgeNew](http://document.tencentcloudapi.woa.com/document/product/1463/64927#TopologyEdgeNew)

	* 新增成员：ReqCnt

* [TopologyNode](http://document.tencentcloudapi.woa.com/document/product/1463/64927#TopologyNode)

	* 新增成员：ReqCnt, ConsumerReqCnt




## 费用中心(billing) 版本：2018-07-09

### 第 120 次发布

发布时间：2026-06-12 01:14:07

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ConsumptionBusinessSummaryDataItem](http://document.tencentcloudapi.woa.com/document/product/555/19183#ConsumptionBusinessSummaryDataItem)

	* 新增成员：LeftRealTotalCost

* [ConsumptionProjectSummaryDataItem](http://document.tencentcloudapi.woa.com/document/product/555/19183#ConsumptionProjectSummaryDataItem)

	* 新增成员：LeftRealTotalCost

* [ConsumptionRegionSummaryDataItem](http://document.tencentcloudapi.woa.com/document/product/555/19183#ConsumptionRegionSummaryDataItem)

	* 新增成员：LeftRealTotalCost

* [ConsumptionResourceSummaryDataItem](http://document.tencentcloudapi.woa.com/document/product/555/19183#ConsumptionResourceSummaryDataItem)

	* 新增成员：LeftRealTotalCost




## 云硬盘(cbs) 版本：2017-03-12

### 第 56 次发布

发布时间：2026-06-12 01:18:33

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AttachRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90694)

	* 新增入参：InstanceId, RemoteDiskIds

* [CreateRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90693)

	* 新增入参：DiskChargeType, DiskSize, InstanceId, Placement, DiskChargePrepaid, DiskCount, DiskName

* [DescribeRemoteDisksDeniedActions](http://document.tencentcloudapi.woa.com/document/product/362/90690)

	* 新增入参：RemoteDiskIds

* [DetachRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90689)

	* 新增入参：InstanceId, RemoteDiskIds, ForceDetach

* [InquirePriceCreateRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90688)

	* 新增入参：DiskChargeType, DiskSize, DiskChargePrepaid, DiskCount

* [InquirePriceRenewRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90687)

	* 新增入参：DiskChargePrepaidSet, RemoteDiskIds

* [ModifyRemoteDiskAttributes](http://document.tencentcloudapi.woa.com/document/product/362/90686)

	* 新增入参：RemoteDiskIds, DiskName, ProjectId

* [RenewRemoteDisk](http://document.tencentcloudapi.woa.com/document/product/362/90685)

	* 新增入参：DiskChargePrepaid, RemoteDiskId

* [TerminateRemoteDisks](http://document.tencentcloudapi.woa.com/document/product/362/90682)

	* 新增入参：RemoteDiskIds


新增数据结构：

* [RemoteDiskChargePrepaid](http://document.tencentcloudapi.woa.com/document/product/362/15669#RemoteDiskChargePrepaid)



## 文件存储(cfs) 版本：2019-07-19

### 第 45 次发布

发布时间：2026-06-12 01:22:56

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLifecycleDataTask](http://document.tencentcloudapi.woa.com/document/product/582/87275)

	* 新增入参：ListPath

	* <font color="#dd0000">**修改入参**：</font>TaskPath


修改数据结构：

* [LifecycleDataTaskInfo](http://document.tencentcloudapi.woa.com/document/product/582/38175#LifecycleDataTaskInfo)

	* 新增成员：ListPath




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 175 次发布

发布时间：2026-06-12 01:35:28

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CancelClusterServerlessScalePlan](http://document.tencentcloudapi.woa.com/document/product/1003/90733)
* [CreateClusterPeriodScalePolicy](http://document.tencentcloudapi.woa.com/document/product/1003/90732)
* [DeleteClusterPeriodScalePolicy](http://document.tencentcloudapi.woa.com/document/product/1003/90731)
* [DescribeClusterPeriodScalePolicy](http://document.tencentcloudapi.woa.com/document/product/1003/90730)
* [DescribeClusterServerlessScalePlans](http://document.tencentcloudapi.woa.com/document/product/1003/90729)
* [ModifyClusterPeriodScalePolicy](http://document.tencentcloudapi.woa.com/document/product/1003/90728)
* [OpenAIOptimizer](http://document.tencentcloudapi.woa.com/document/product/1003/90734)

修改接口：

* [DescribeInstanceSpecs](http://document.tencentcloudapi.woa.com/document/product/1003/48084)

	* 新增入参：ClusterLevel


新增数据结构：

* [ClusterPeriodScalePolicy](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ClusterPeriodScalePolicy)
* [ClusterServerlessScalePlan](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ClusterServerlessScalePlan)

修改数据结构：

* [CynosdbClusterDetail](http://document.tencentcloudapi.woa.com/document/product/1003/48097#CynosdbClusterDetail)

	* 新增成员：ClusterLevel




## 数据传输服务(dts) 版本：2021-12-06

### 第 48 次发布

发布时间：2026-06-12 01:44:06

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [StepDetailInfo](http://document.tencentcloudapi.woa.com/document/product/571/78340#StepDetailInfo)

	* 新增成员：FinishTime

* [StepInfo](http://document.tencentcloudapi.woa.com/document/product/571/78340#StepInfo)

	* 新增成员：FinishTime




## 数据传输服务(dts) 版本：2018-03-30



## 高性能应用服务(hai) 版本：2023-08-12

### 第 31 次发布

发布时间：2026-06-12 01:52:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeployInferService](http://document.tencentcloudapi.woa.com/document/product/1750/89080)

	* 新增入参：SecurityType




## 媒体处理(mps) 版本：2019-06-12

### 第 178 次发布

发布时间：2026-06-12 02:08:18

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAigcAudioTask](http://document.tencentcloudapi.woa.com/document/product/862/90736)
* [DescribeAigcAudioTask](http://document.tencentcloudapi.woa.com/document/product/862/90735)

新增数据结构：

* [AiTryOnConfig](http://document.tencentcloudapi.woa.com/document/product/862/37615#AiTryOnConfig)
* [AigcAudioExtraParam](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcAudioExtraParam)
* [AigcAudioOutputAudioInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcAudioOutputAudioInfo)
* [AigcAudioOutputVideoInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcAudioOutputVideoInfo)
* [AigcAudioReferenceAudioInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcAudioReferenceAudioInfo)
* [AigcAudioReferenceVideoInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcAudioReferenceVideoInfo)

修改数据结构：

* [ImageTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#ImageTaskInput)

	* 新增成员：AiTryOnConfig




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 61 次发布

发布时间：2026-06-12 02:13:56

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateBaseBackup](http://document.tencentcloudapi.woa.com/document/product/409/77304)

	* 新增入参：BackupMethod

* [ModifyBackupPlan](http://document.tencentcloudapi.woa.com/document/product/409/68067)

	* 新增入参：BackupMethod




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 181 次发布

发布时间：2026-06-12 02:27:06

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeRabbitMQTokenPwdRules](http://document.tencentcloudapi.woa.com/document/product/1179/90739)
* [DescribeRabbitMQTokenResource](http://document.tencentcloudapi.woa.com/document/product/1179/90738)
* [DescribeRoleTokenRotateConfig](http://document.tencentcloudapi.woa.com/document/product/1179/90741)
* [ResetInstancePassword](http://document.tencentcloudapi.woa.com/document/product/1179/90740)
* [ResetRabbitMQInstancePwd](http://document.tencentcloudapi.woa.com/document/product/1179/90737)

新增数据结构：

* [PasswordRule](http://document.tencentcloudapi.woa.com/document/product/1179/46089#PasswordRule)



## 互动白板(tiw) 版本：2019-09-19

### 第 21 次发布

发布时间：2026-06-12 02:33:14

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateSnapshot](http://document.tencentcloudapi.woa.com/document/product/1137/90747)
* [DescribeSnapshot](http://document.tencentcloudapi.woa.com/document/product/1137/90746)
* [DescribeSnapshotCallback](http://document.tencentcloudapi.woa.com/document/product/1137/90745)
* [SetSnapshotCallback](http://document.tencentcloudapi.woa.com/document/product/1137/90744)
* [SetSnapshotCallbackKey](http://document.tencentcloudapi.woa.com/document/product/1137/90743)

新增数据结构：

* [SnapshotCosBucket](http://document.tencentcloudapi.woa.com/document/product/1137/40068#SnapshotCosBucket)



## 向量数据库(vdb) 版本：2023-06-16

### 第 15 次发布

发布时间：2026-06-12 02:40:59

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1758/83305#InstanceInfo)

	* 新增成员：UpgradeVersion, IsInternal

* [Network](http://document.tencentcloudapi.woa.com/document/product/1758/83305#Network)

	* 新增成员：IsSSL




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 34 次发布

发布时间：2026-06-12 02:45:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ListComputeResourceMetrics](http://document.tencentcloudapi.woa.com/document/product/1607/89781)

	* 新增入参：WorkspaceId


修改数据结构：

* [ExecAdminResourceMetricInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminResourceMetricInfo)

	* 新增成员：GpuUsage, GpuLoad




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



