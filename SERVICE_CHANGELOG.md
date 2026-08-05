# Release 3.0.1468.1

## 云联络中心(ccc) 版本：2020-02-10

### 第 98 次发布

发布时间：2026-08-06 01:18:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAICall](http://document.tencentcloudapi.woa.com/document/product/679/84920)

	* 新增入参：TransferToAgentEnable, TransferToAgentItems, AdvanceSTTConfig, AcquireTimeoutSecond, CustomSTTConfig


新增数据结构：

* [AdvanceSTTConfig](http://document.tencentcloudapi.woa.com/document/product/679/47715#AdvanceSTTConfig)
* [TransferToAgentItem](http://document.tencentcloudapi.woa.com/document/product/679/47715#TransferToAgentItem)



## 消息队列 CKafka 版(ckafka) 版本：2019-08-19

### 第 115 次发布

发布时间：2026-08-06 01:25:12

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateThrottleRule](http://document.tencentcloudapi.woa.com/document/product/597/92182)
* [DeleteThrottleRule](http://document.tencentcloudapi.woa.com/document/product/597/92181)
* [DescribeThrottleRules](http://document.tencentcloudapi.woa.com/document/product/597/92180)
* [ModifyThrottleRule](http://document.tencentcloudapi.woa.com/document/product/597/92179)

新增数据结构：

* [ThrottleRuleDetail](http://document.tencentcloudapi.woa.com/document/product/597/40861#ThrottleRuleDetail)
* [ThrottleRuleResult](http://document.tencentcloudapi.woa.com/document/product/597/40861#ThrottleRuleResult)



## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 9 次发布

发布时间：2026-08-06 01:38:17

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [DBCustomClusterNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomClusterNode)

	* 新增成员：SecurityGroupIds

* [DBCustomNode](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DBCustomNode)

	* 新增成员：SecurityGroupIds




## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 170 次发布

发布时间：2026-08-06 01:39:33

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92195)
* [CreateModelVersion](http://document.tencentcloudapi.woa.com/document/product/1342/92188)
* [GetInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92194)
* [GetModelConfig](http://document.tencentcloudapi.woa.com/document/product/1342/92187)
* [GetModelFiles](http://document.tencentcloudapi.woa.com/document/product/1342/92186)
* [GetModelReadme](http://document.tencentcloudapi.woa.com/document/product/1342/92185)
* [ListInferenceEngines](http://document.tencentcloudapi.woa.com/document/product/1342/92193)
* [ListInferenceServices](http://document.tencentcloudapi.woa.com/document/product/1342/92192)
* [ListModelVersions](http://document.tencentcloudapi.woa.com/document/product/1342/92184)
* [ModifyPartition](http://document.tencentcloudapi.woa.com/document/product/1342/92183)
* [QueryDashboardOverview](http://document.tencentcloudapi.woa.com/document/product/1342/92199)
* [QueryDashboardServiceList](http://document.tencentcloudapi.woa.com/document/product/1342/92198)
* [QueryMonitorOverview](http://document.tencentcloudapi.woa.com/document/product/1342/92197)
* [RestartInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92191)
* [StopInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92190)

新增数据结构：

* [CpuSummaryItem](http://document.tencentcloudapi.woa.com/document/product/1342/53778#CpuSummaryItem)
* [EngineCapabilities](http://document.tencentcloudapi.woa.com/document/product/1342/53778#EngineCapabilities)
* [FileNode](http://document.tencentcloudapi.woa.com/document/product/1342/53778#FileNode)
* [GpuSummaryItem](http://document.tencentcloudapi.woa.com/document/product/1342/53778#GpuSummaryItem)
* [InferenceEngineInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#InferenceEngineInfo)
* [InferenceServiceInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#InferenceServiceInfo)
* [LinkedServiceInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#LinkedServiceInfo)
* [MetricsData](http://document.tencentcloudapi.woa.com/document/product/1342/53778#MetricsData)
* [ModelVersionInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#ModelVersionInfo)
* [OverviewItem](http://document.tencentcloudapi.woa.com/document/product/1342/53778#OverviewItem)
* [ParallelKeyMapping](http://document.tencentcloudapi.woa.com/document/product/1342/53778#ParallelKeyMapping)
* [ReplicaInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#ReplicaInfo)
* [ServiceMetricsItem](http://document.tencentcloudapi.woa.com/document/product/1342/53778#ServiceMetricsItem)

修改数据结构：

* [TaskStatusInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#TaskStatusInfo)

	* 新增成员：Percentage




## 数据传输服务(dts) 版本：2021-12-06

### 第 55 次发布

发布时间：2026-08-06 02:07:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteConsumerGroup](http://document.tencentcloudapi.woa.com/document/product/571/82916)

	* 新增入参：BackendJobId


修改数据结构：

* [SubscribeInfo](http://document.tencentcloudapi.woa.com/document/product/571/78340#SubscribeInfo)

	* 新增成员：ConsumerRoutePhase




## 数据传输服务(dts) 版本：2018-03-30



## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 239 次发布

发布时间：2026-08-06 02:12:11

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSealByImage](http://document.tencentcloudapi.woa.com/document/product/1595/75256)

	* 新增入参：SubSealType




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 腾讯混元大模型(hunyuan) 版本：2023-09-01

### 第 32 次发布

发布时间：2026-08-06 02:17:33

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [SubmitHunyuan3DPartJob](http://document.tencentcloudapi.woa.com/document/product/1744/88614)

	* 新增入参：EnablePostProcess




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 41 次发布

发布时间：2026-08-06 02:31:50

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [EnumOption](http://document.tencentcloudapi.woa.com/document/product/1759/83593#EnumOption)

修改数据结构：

* [ModelParameter](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ModelParameter)

	* 新增成员：EnumOptionList, VisibleOn




## 流计算 Oceanus(oceanus) 版本：2019-04-22

### 第 87 次发布

发布时间：2026-08-06 02:37:24

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [FlinkUIEndpoint](http://document.tencentcloudapi.woa.com/document/product/849/52010#FlinkUIEndpoint)

修改数据结构：

* [Cluster](http://document.tencentcloudapi.woa.com/document/product/849/52010#Cluster)

	* 新增成员：FlinkUIEndpoint

* [JobV1](http://document.tencentcloudapi.woa.com/document/product/849/52010#JobV1)

	* 新增成员：HealthScore, LastDiagnoseTime, ManagerUin, FlinkUIEndpoint




## 云数据库Redis(redis) 版本：2018-04-12

### 第 73 次发布

发布时间：2026-08-06 02:41:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CloneInstances](http://document.tencentcloudapi.woa.com/document/product/239/77351)

	* 新增入参：ProductVersion




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 58 次发布

发布时间：2026-08-06 02:47:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [VerifyHTTPServiceRoute](http://document.tencentcloudapi.woa.com/document/product/876/92200)

新增数据结构：

* [VerifyHTTPServiceRouteCheckItem](http://document.tencentcloudapi.woa.com/document/product/876/34822#VerifyHTTPServiceRouteCheckItem)



## TokenHub(tokenhub) 版本：2026-03-22

### 第 16 次发布

发布时间：2026-08-06 02:59:57

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Model](http://document.tencentcloudapi.woa.com/document/product/1814/90425#Model)

	* 新增成员：DiscontinuedAt




