# Release 3.0.1447.1

## 凭据管理系统(ssm) 版本：2019-09-23

### 第 17 次发布

发布时间：2026-06-23 01:32:20

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeSecret](http://document.tencentcloudapi.woa.com/document/product/1140/40526)

	* 新增出参：CreateUinString, TargetUinString


修改数据结构：

* [SecretMetadata](http://document.tencentcloudapi.woa.com/document/product/1140/40530#SecretMetadata)

	* 新增成员：CreateUinString, TargetUinString




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 182 次发布

发布时间：2026-06-23 01:35:18

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeRocketMQMsg](http://document.tencentcloudapi.woa.com/document/product/1179/77775)

	* 新增入参：QueryDelayMessage

* [ModifyInternalRocketMQInstance](http://document.tencentcloudapi.woa.com/document/product/1179/85493)

	* 新增入参：AutoCreateConsumeGroupEnabled

* [ModifyRocketMQInstance](http://document.tencentcloudapi.woa.com/document/product/1179/84271)

	* 新增入参：AclEnabled


修改数据结构：

* [InternalRocketMQInstance](http://document.tencentcloudapi.woa.com/document/product/1179/46089#InternalRocketMQInstance)

	* 新增成员：AutoCreateConsumeGroupEnabled

* [RocketMQClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQClusterInfo)

	* 新增成员：AutoCreateConsumeGroupEnabled




## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 81 次发布

发布时间：2026-06-23 01:36:22

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [AdvancedOriginRoutingParameters](http://document.tencentcloudapi.woa.com/document/product/1738/81211#AdvancedOriginRoutingParameters)

修改数据结构：

* [RuleEngineAction](http://document.tencentcloudapi.woa.com/document/product/1738/81211#RuleEngineAction)

	* 新增成员：AdvancedOriginRoutingParameters




## 边缘安全加速平台(teo) 版本：2022-01-06



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 140 次发布

发布时间：2026-06-23 01:37:33

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [RepairTaskInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#RepairTaskInfo)

修改数据结构：

* [Instance](http://document.tencentcloudapi.woa.com/document/product/851/74915#Instance)

	* 新增成员：AvailableResource, InstanceIP, InstanceName, CvmInstanceType, AutoRenew, Isolated, RepairTaskInfo

* [MountConfigureInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#MountConfigureInfo)

	* 新增成员：Address, UserName, Password




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 62 次发布

发布时间：2026-06-23 01:39:29

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateConsumerGroup](http://document.tencentcloudapi.woa.com/document/product/1739/81928)

	* 新增入参：LiteTopic

* [CreateTopic](http://document.tencentcloudapi.woa.com/document/product/1739/81932)

	* 新增入参：AutoExpireDelete, AutoExpireTime

	* <font color="#dd0000">**修改入参**：</font>QueueNum

* [DescribeConsumerGroup](http://document.tencentcloudapi.woa.com/document/product/1739/81926)

	* 新增出参：ConsumeModel, LiteTopic

* [DescribeMessage](http://document.tencentcloudapi.woa.com/document/product/1739/85588)

	* 新增出参：LiteTopic

* [DescribeMessageList](http://document.tencentcloudapi.woa.com/document/product/1739/85587)

	* 新增入参：LiteTopic

* [DescribeMessageTrace](http://document.tencentcloudapi.woa.com/document/product/1739/85582)

	* 新增出参：LiteTopic

* [DescribeTopic](http://document.tencentcloudapi.woa.com/document/product/1739/81930)

	* 新增出参：AutoExpireDelete, AutoExpireTime

* [ModifyTopic](http://document.tencentcloudapi.woa.com/document/product/1739/81929)

	* 新增入参：AutoExpireDelete, AutoExpireTime

* [SendMessage](http://document.tencentcloudapi.woa.com/document/product/1739/88199)

	* 新增入参：LiteTopic




## 私有网络(vpc) 版本：2017-03-12

### 第 251 次发布

发布时间：2026-06-23 01:42:15

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [CcnPolicyBasedRoutingRule](http://document.tencentcloudapi.woa.com/document/product/215/15824#CcnPolicyBasedRoutingRule)

	* 新增成员：DestinationInstanceType, DestinationInstanceId




