# Release 3.0.1308.1

## 云托付物理服务器(chc) 版本：2023-04-18

### 第 3 次发布

发布时间：2025-11-19 01:17:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateQuitWorkOrder](http://document.tencentcloudapi.woa.com/document/product/1790/87369)

	* 新增入参：Building, IdcUnitId, Isp, EmailSet, FactorSet


修改数据结构：

* [DeviceOrderBaseInfo](http://document.tencentcloudapi.woa.com/document/product/1790/87378#DeviceOrderBaseInfo)

	* 新增成员：Building, EmailSet, FactorSet




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 213 次发布

发布时间：2025-11-19 01:32:28

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChannelCreatePrepareFlow](http://document.tencentcloudapi.woa.com/document/product/1595/77207)

	* 新增出参：DraftId

* [CreateConsoleLoginUrl](http://document.tencentcloudapi.woa.com/document/product/1595/75251)

	* 新增入参：ProxyOrganizationIdCardType




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 48 次发布

发布时间：2025-11-19 01:43:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAuditLogFile](http://document.tencentcloudapi.woa.com/document/product/240/88037)
* [DeleteAuditLogFile](http://document.tencentcloudapi.woa.com/document/product/240/88036)
* [DescribeAuditInstanceList](http://document.tencentcloudapi.woa.com/document/product/240/88035)
* [ModifyAuditService](http://document.tencentcloudapi.woa.com/document/product/240/88034)
* [OpenAuditService](http://document.tencentcloudapi.woa.com/document/product/240/88033)

新增数据结构：

* [AuditInstance](http://document.tencentcloudapi.woa.com/document/product/240/38576#AuditInstance)
* [AuditLogFilter](http://document.tencentcloudapi.woa.com/document/product/240/38576#AuditLogFilter)
* [DeliverSummary](http://document.tencentcloudapi.woa.com/document/product/240/38576#DeliverSummary)
* [Filters](http://document.tencentcloudapi.woa.com/document/product/240/38576#Filters)
* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/240/38576#InstanceInfo)
* [LogFilter](http://document.tencentcloudapi.woa.com/document/product/240/38576#LogFilter)



## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 114 次发布

发布时间：2025-11-19 01:45:03

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/51288)

	* 新增入参：IsLoginFree

* [ModifyAlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/51277)

	* 新增入参：IsLoginFree


修改数据结构：

* [AlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/30354#AlarmNotice)

	* 新增成员：IsLoginFree




## 云函数(scf) 版本：2018-04-16

### 第 67 次发布

发布时间：2025-11-19 01:52:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateFunction](http://document.tencentcloudapi.woa.com/document/product/583/18586)

	* 新增入参：Port, ReadinessProbe

* [GetFunction](http://document.tencentcloudapi.woa.com/document/product/583/18584)

	* 新增出参：ReadinessProbe, Port

* [UpdateFunctionConfiguration](http://document.tencentcloudapi.woa.com/document/product/583/18580)

	* 新增入参：Port, ReadinessProbe


新增数据结构：

* [ReadinessProbe](http://document.tencentcloudapi.woa.com/document/product/583/17244#ReadinessProbe)



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 112 次发布

发布时间：2025-11-19 02:02:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74857)

	* 新增入参：ExposeNetworkConfig


新增数据结构：

* [ExposeNetworkConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#ExposeNetworkConfig)
* [InstanceFaultExtraInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#InstanceFaultExtraInfo)
* [InstanceFaultExtraInfoValue](http://document.tencentcloudapi.woa.com/document/product/851/74915#InstanceFaultExtraInfoValue)
* [InstanceFaultInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#InstanceFaultInfo)

修改数据结构：

* [ImageInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ImageInfo)

	* 新增成员：EntryPoint, WorkDir

* [Instance](http://document.tencentcloudapi.woa.com/document/product/851/74915#Instance)

	* 新增成员：FaultInfo

* [PortElement](http://document.tencentcloudapi.woa.com/document/product/851/74915#PortElement)

	* 新增成员：UnbindClb

* [TrainingTaskDetail](http://document.tencentcloudapi.woa.com/document/product/851/74915#TrainingTaskDetail)

	* 新增成员：ExposeNetworkConfig




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 私有网络(vpc) 版本：2017-03-12

### 第 227 次发布

发布时间：2025-11-19 02:07:30

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeNatGatewayZones](http://document.tencentcloudapi.woa.com/document/product/215/88038)

修改接口：

* [CreateNatGateway](http://document.tencentcloudapi.woa.com/document/product/215/36721)

	* 新增入参：EnableInstanceRouteTable

* [DeleteNatGateway](http://document.tencentcloudapi.woa.com/document/product/215/36719)

	* 新增入参：IgnoreOperationRisk

* [DescribeVpcEndPoint](http://document.tencentcloudapi.woa.com/document/product/215/54679)

	* 新增入参：MaxResults, NextToken

	* 新增出参：NextToken

* [DescribeVpcEndPointService](http://document.tencentcloudapi.woa.com/document/product/215/54678)

	* 新增入参：MaxResults, NextToken

	* 新增出参：NextToken


新增数据结构：

* [NatZoneInfo](http://document.tencentcloudapi.woa.com/document/product/215/15824#NatZoneInfo)



