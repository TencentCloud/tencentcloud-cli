# Release 3.0.1500.1

## 负载均衡(clb) 版本：2023-04-17



## 负载均衡(clb) 版本：2018-03-17

### 第 101 次发布

发布时间：2026-09-22 01:28:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyModelAliasAttributes](http://document.tencentcloudapi.woa.com/document/product/214/91016)

	* 新增入参：CoefficientTiers, CoefficientSchedule

	* <font color="#dd0000">**修改入参**：</font>Coefficient


新增数据结构：

* [CoefficientScheduleRule](http://document.tencentcloudapi.woa.com/document/product/214/30694#CoefficientScheduleRule)
* [CoefficientTier](http://document.tencentcloudapi.woa.com/document/product/214/30694#CoefficientTier)
* [CoefficientTierCondition](http://document.tencentcloudapi.woa.com/document/product/214/30694#CoefficientTierCondition)

修改数据结构：

* [Coefficient](http://document.tencentcloudapi.woa.com/document/product/214/30694#Coefficient)

	* 新增成员：InputImageCoefficient, InputVideoSecondCoefficient, OutputVideoSecondCoefficient

* [ModelAlias](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelAlias)

	* 新增成员：CoefficientTiers, CoefficientSchedule

* [ServiceProviderCoefficient](http://document.tencentcloudapi.woa.com/document/product/214/30694#ServiceProviderCoefficient)

	* 新增成员：CoefficientTiers, CoefficientSchedule




## 数据库智能管家 DBbrain(dbbrain) 版本：2021-05-27

### 第 62 次发布

发布时间：2026-09-22 01:39:20

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeTopSpaceTablesV2](http://document.tencentcloudapi.woa.com/document/product/1130/92682)

新增数据结构：

* [MongoCollectionDetail](http://document.tencentcloudapi.woa.com/document/product/1130/57812#MongoCollectionDetail)
* [MongoDBTableSpaceItem](http://document.tencentcloudapi.woa.com/document/product/1130/57812#MongoDBTableSpaceItem)
* [MysqlSpaceObjectItem](http://document.tencentcloudapi.woa.com/document/product/1130/57812#MysqlSpaceObjectItem)
* [PostgresSpaceObjectItem](http://document.tencentcloudapi.woa.com/document/product/1130/57812#PostgresSpaceObjectItem)

修改数据结构：

* [SlowLogInfoItem](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SlowLogInfoItem)

	* 新增成员：InstanceId

* [SlowLogTopSqlItem](http://document.tencentcloudapi.woa.com/document/product/1130/57812#SlowLogTopSqlItem)

	* 新增成员：SqlType, InstanceId




## 数据库智能管家 DBbrain(dbbrain) 版本：2019-10-16



## 高性能应用服务(hai) 版本：2023-08-12

### 第 38 次发布

发布时间：2026-09-22 01:52:46

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetServicePodLogs](http://document.tencentcloudapi.woa.com/document/product/1750/92683)



## 智能视图计算平台(iss) 版本：2023-05-17

### 第 36 次发布

发布时间：2026-09-22 02:00:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UpdateUserDevice](http://document.tencentcloudapi.woa.com/document/product/1740/81489)

	* 新增入参：TimeSyncSwitch


新增数据结构：

* [SipCarrierEndpoints](http://document.tencentcloudapi.woa.com/document/product/1740/81572#SipCarrierEndpoints)

修改数据结构：

* [DescribeDeviceData](http://document.tencentcloudapi.woa.com/document/product/1740/81572#DescribeDeviceData)

	* 新增成员：SipFQDN, SipCarrierEndpoints, TimeSyncSwitch




## 腾讯云可观测平台(monitor) 版本：2023-06-16

### 第 15 次发布

发布时间：2026-09-22 02:09:26

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [QueryMetrics](http://document.tencentcloudapi.woa.com/document/product/248/92684)

新增数据结构：

* [Aggregation](http://document.tencentcloudapi.woa.com/document/product/248/81423#Aggregation)
* [FilterWithType](http://document.tencentcloudapi.woa.com/document/product/248/81423#FilterWithType)
* [FiltersList](http://document.tencentcloudapi.woa.com/document/product/248/81423#FiltersList)
* [QueryMetricsData](http://document.tencentcloudapi.woa.com/document/product/248/81423#QueryMetricsData)
* [SeriesData](http://document.tencentcloudapi.woa.com/document/product/248/81423#SeriesData)
* [Sort](http://document.tencentcloudapi.woa.com/document/product/248/81423#Sort)



## 腾讯云可观测平台(monitor) 版本：2018-07-24



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 155 次发布

发布时间：2026-09-22 02:30:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/90327)

	* 新增入参：ScheduleStrategyMode, ScheduleStrategyForm

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/851/76500)

	* 新增入参：Priority

* [DescribeBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/82745)

	* 新增出参：ClusterType, ScheduleStrategyMode, ScheduleStrategyForm, Supplier, HasBoundReservationPlan

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/851/76703)

	* 新增入参：Priority


新增数据结构：

* [ScheduleStrategyForm](http://document.tencentcloudapi.woa.com/document/product/851/74915#ScheduleStrategyForm)
* [ServiceGroupLogConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroupLogConfig)
* [ServiceLogConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceLogConfig)

修改数据结构：

* [EnvVar](http://document.tencentcloudapi.woa.com/document/product/851/74915#EnvVar)

	* 新增成员：IsPrivate

* [ResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroup)

	* 新增成员：ClusterType, ScheduleStrategyMode, ScheduleStrategyForm, Supplier, HasBoundReservationPlan

* [ResourceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceInfo)

	* 新增成员：RdmaNumber, Rdma, ReservedMemory

* [SSHConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#SSHConfig)

	* 新增成员：UserCredentialIdList

* [SanityCheckItem](http://document.tencentcloudapi.woa.com/document/product/851/74915#SanityCheckItem)

	* 新增成员：RunBeforeJob, RunAfterJobFailed

* [ServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroup)

	* 新增成员：ServiceGroupLogConfig




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 70 次发布

发布时间：2026-09-22 02:34:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateConsumerLabels](http://document.tencentcloudapi.woa.com/document/product/1739/92691)
* [DeleteConsumerLabels](http://document.tencentcloudapi.woa.com/document/product/1739/92690)
* [DeleteConsumerRouteConfigs](http://document.tencentcloudapi.woa.com/document/product/1739/92689)
* [DescribeConsumerLabelLists](http://document.tencentcloudapi.woa.com/document/product/1739/92688)
* [DescribeConsumerLabelRoutes](http://document.tencentcloudapi.woa.com/document/product/1739/92687)
* [DescribeConsumerRouteConfigs](http://document.tencentcloudapi.woa.com/document/product/1739/92686)
* [PutConsumerRouteConfigs](http://document.tencentcloudapi.woa.com/document/product/1739/92685)

新增数据结构：

* [ConsumerLabelFailure](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelFailure)
* [ConsumerLabelItem](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelItem)
* [ConsumerLabelKey](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelKey)
* [ConsumerLabelList](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelList)
* [ConsumerLabelRoute](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelRoute)
* [ConsumerLabelRouteItem](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerLabelRouteItem)
* [ConsumerRouteKey](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerRouteKey)
* [ConsumerRouteLabelKey](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerRouteLabelKey)
* [DeleteConsumerRouteConfigFailure](http://document.tencentcloudapi.woa.com/document/product/1739/81437#DeleteConsumerRouteConfigFailure)
* [DescribeConsumerRouteConfigItem](http://document.tencentcloudapi.woa.com/document/product/1739/81437#DescribeConsumerRouteConfigItem)
* [ErrorInfo](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ErrorInfo)
* [PutConsumerRouteConfigFailure](http://document.tencentcloudapi.woa.com/document/product/1739/81437#PutConsumerRouteConfigFailure)
* [PutConsumerRouteConfigItem](http://document.tencentcloudapi.woa.com/document/product/1739/81437#PutConsumerRouteConfigItem)



