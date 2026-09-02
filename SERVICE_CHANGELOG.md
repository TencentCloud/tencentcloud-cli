# Release 3.0.1486.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 27 次发布

发布时间：2026-09-03 01:08:06

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AppendEvent](http://document.tencentcloudapi.woa.com/document/product/1804/91853)

* [CreateSession](http://document.tencentcloudapi.woa.com/document/product/1804/91852)

	* 新增入参：Metadata

* [DeleteSession](http://document.tencentcloudapi.woa.com/document/product/1804/91851)

* [DescribeEvents](http://document.tencentcloudapi.woa.com/document/product/1804/91850)

* [DescribeSession](http://document.tencentcloudapi.woa.com/document/product/1804/91849)

* [DescribeSessions](http://document.tencentcloudapi.woa.com/document/product/1804/91848)

	* 新增入参：Filters


修改数据结构：

* [SessionInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SessionInfo)

	* 新增成员：Metadata




## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 25 次发布

发布时间：2026-09-03 01:11:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateMcpServer](http://document.tencentcloudapi.woa.com/document/product/1805/87904)

	* 新增入参：CredentialID, Domain, RequestProtocolType

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88920)

	* 新增入参：Domain, RequestProtocolType

* [ModifyMcpServer](http://document.tencentcloudapi.woa.com/document/product/1805/87898)

	* 新增入参：CredentialID, Domain, RequestProtocolType

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88916)

	* 新增入参：Domain, RequestProtocolType


新增数据结构：

* [TimeRange](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TimeRange)

修改数据结构：

* [AgentAppMcpServerDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppMcpServerDTO)

* [AgentAppServiceDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppServiceDTO)

* [DescribeAIMCredentialResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialResp)

	* 新增成员：ResourceNames

* [DescribeMcpServerResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeMcpServerResponseVO)

	* 新增成员：CredentialID, CredentialName, Domain, RequestProtocolType

* [DescribeModelServiceResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServiceResponseVO)

	* 新增成员：Domain, RequestProtocolType

* [LimitWindowsDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#LimitWindowsDTO)

	* 新增成员：Type, TimeRange

* [ServiceVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#ServiceVO)

	* 新增成员：CredentialID, CredentialName, RequestProtocolType

* [TokenLimitConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TokenLimitConfigDTO)




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 179 次发布

发布时间：2026-09-03 01:26:28

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDatabasesAndTablesForInstance](http://document.tencentcloudapi.woa.com/document/product/236/92490)

新增数据结构：

* [DBInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#DBInfo)



## 主机安全(cwp) 版本：2018-02-28

### 第 152 次发布

发布时间：2026-09-03 01:38:00

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [CWPTags](http://document.tencentcloudapi.woa.com/document/product/296/19867#CWPTags)

修改数据结构：

* [OrderDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#OrderDetail)

	* 新增成员：SourceType

* [RaspLicenseList](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspLicenseList)

	* 新增成员：CWPTags




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 194 次发布

发布时间：2026-09-03 01:41:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteAccounts](http://document.tencentcloudapi.woa.com/document/product/1003/77829)

	* 新增出参：TaskId




## 数据库智能管家 DBbrain(dbbrain) 版本：2021-05-27

### 第 61 次发布

发布时间：2026-09-03 01:44:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRedisBigKeyAnalysisTask](http://document.tencentcloudapi.woa.com/document/product/1130/81033)

	* 新增入参：BackupId




## 数据库智能管家 DBbrain(dbbrain) 版本：2019-10-16



## 游戏多媒体引擎(gme) 版本：2018-07-11

### 第 30 次发布

发布时间：2026-09-03 01:55:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeApplicationList](http://document.tencentcloudapi.woa.com/document/product/607/76709)

	* 新增入参：NewVersion




## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 36 次发布

发布时间：2026-09-03 01:55:29

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [LoadDataAttrs](http://document.tencentcloudapi.woa.com/document/product/1716/81241#LoadDataAttrs)

修改数据结构：

* [LoadTaskAttrs](http://document.tencentcloudapi.woa.com/document/product/1716/81241#LoadTaskAttrs)

	* 新增成员：LoadDataAttrs

* [LoadTaskCreationAttrs](http://document.tencentcloudapi.woa.com/document/product/1716/81241#LoadTaskCreationAttrs)

	* 新增成员：LoadDataAttrs




## 云直播CSS(live) 版本：2018-08-01

### 第 99 次发布

发布时间：2026-09-03 02:09:13

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ChildTemplateInfo](http://document.tencentcloudapi.woa.com/document/product/267/20474#ChildTemplateInfo)

	* 新增成员：Acodec, AudioBitrate




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 44 次发布

发布时间：2026-09-03 02:11:00

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [ConversationMcpApp](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ConversationMcpApp)

修改数据结构：

* [Content](http://document.tencentcloudapi.woa.com/document/product/1759/83593#Content)

	* 新增成员：McpApp




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 68 次发布

发布时间：2026-09-03 02:26:11

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyPGInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/876/92491)



## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 186 次发布

发布时间：2026-09-03 02:32:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRocketMQVipInstance](http://document.tencentcloudapi.woa.com/document/product/1179/81454)

	* 新增入参：BillingFlow, MaxTopicNum, PayMode, RenewFlag

	* <font color="#dd0000">**修改入参**：</font>VpcInfo, TimeSpan

* [DescribeRocketMQMsgTrace](http://document.tencentcloudapi.woa.com/document/product/1179/81794)

	* 新增入参：QueryDelayMessage


新增数据结构：

* [RocketMQVpcInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQVpcInfo)

<font color="#dd0000">**删除数据结构**：</font>

* VpcConfig

修改数据结构：

* [RocketMQClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQClusterInfo)

	* 新增成员：PayMode

	* <font color="#dd0000">**修改成员**：</font>Vpcs

* [RocketMQGroupConfig](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQGroupConfig)

	* 新增成员：TagList

* [RocketMQTopicConfig](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQTopicConfig)

	* 新增成员：TagList




## 高性能计算平台(thpc) 版本：2023-03-21

### 第 37 次发布

发布时间：2026-09-03 02:35:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeClusterActivities](http://document.tencentcloudapi.woa.com/document/product/1701/80189)

	* 新增入参：Filters


修改数据结构：

* [ClusterActivity](http://document.tencentcloudapi.woa.com/document/product/1701/80209#ClusterActivity)

	* 新增成员：QueueName




## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 67 次发布

发布时间：2026-09-03 02:40:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AddUserPurchaseConfig](http://document.tencentcloudapi.woa.com/document/product/1739/85524)

	* 新增入参：InstanceVersion

* [DescribeConsumerClient](http://document.tencentcloudapi.woa.com/document/product/1739/85621)

	* 新增出参：TopicTotalCount

* [DescribeMessage](http://document.tencentcloudapi.woa.com/document/product/1739/85588)

	* 新增出参：DelayMessageStatus

* [DescribeUserPurchaseConfigs](http://document.tencentcloudapi.woa.com/document/product/1739/85518)

	* 新增入参：InstanceVersion


修改数据结构：

* [UserPurchaseConfig](http://document.tencentcloudapi.woa.com/document/product/1739/81437#UserPurchaseConfig)

	* 新增成员：InstanceVersion




## 实时互动-工业能源版(trro) 版本：2022-03-25

### 第 13 次发布

发布时间：2026-09-03 02:41:54

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateBatchVideoAnnotationJob](http://document.tencentcloudapi.woa.com/document/product/1714/92502)
* [CreateVideoAnnotationJob](http://document.tencentcloudapi.woa.com/document/product/1714/92501)
* [DeleteAnnotationJob](http://document.tencentcloudapi.woa.com/document/product/1714/92500)
* [DeleteAnnotationTask](http://document.tencentcloudapi.woa.com/document/product/1714/92499)
* [DescribeAnnotationJobs](http://document.tencentcloudapi.woa.com/document/product/1714/92498)
* [DescribeAnnotationResults](http://document.tencentcloudapi.woa.com/document/product/1714/92497)
* [DescribeAnnotationTasks](http://document.tencentcloudapi.woa.com/document/product/1714/92496)
* [DescribeVideoPlayUrl](http://document.tencentcloudapi.woa.com/document/product/1714/92495)
* [RetryAnnotationTask](http://document.tencentcloudapi.woa.com/document/product/1714/92494)
* [UploadVideoAnnotationResult](http://document.tencentcloudapi.woa.com/document/product/1714/92493)

新增数据结构：

* [AnnotationContext](http://document.tencentcloudapi.woa.com/document/product/1714/80497#AnnotationContext)
* [BatchS3SourceInfo](http://document.tencentcloudapi.woa.com/document/product/1714/80497#BatchS3SourceInfo)
* [CallbackInfo](http://document.tencentcloudapi.woa.com/document/product/1714/80497#CallbackInfo)
* [Job](http://document.tencentcloudapi.woa.com/document/product/1714/80497#Job)
* [OutputInfo](http://document.tencentcloudapi.woa.com/document/product/1714/80497#OutputInfo)
* [OutputStorage](http://document.tencentcloudapi.woa.com/document/product/1714/80497#OutputStorage)
* [ProcessParams](http://document.tencentcloudapi.woa.com/document/product/1714/80497#ProcessParams)
* [S3SourceInfo](http://document.tencentcloudapi.woa.com/document/product/1714/80497#S3SourceInfo)
* [SecretInfo](http://document.tencentcloudapi.woa.com/document/product/1714/80497#SecretInfo)
* [Task](http://document.tencentcloudapi.woa.com/document/product/1714/80497#Task)



