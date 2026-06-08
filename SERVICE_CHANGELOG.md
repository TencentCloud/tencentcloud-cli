# Release 3.0.1438.1

## 消息队列 CKafka 版(ckafka) 版本：2019-08-19

### 第 112 次发布

发布时间：2026-06-08 16:47:42

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateMetaAndDataSyncDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90667)
* [CreateMetaDataAndOffsetSyncDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90666)
* [CreateMetaSyncDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90665)
* [DeleteGroupSubscribeTopic](http://document.tencentcloudapi.woa.com/document/product/597/90676)
* [DescribeAccessPolicy](http://document.tencentcloudapi.woa.com/document/product/597/90669)
* [DescribeCkafkaVersion](http://document.tencentcloudapi.woa.com/document/product/597/90675)
* [DescribeModifyType](http://document.tencentcloudapi.woa.com/document/product/597/90670)
* [DescribeRoleTokenPwdRules](http://document.tencentcloudapi.woa.com/document/product/597/90679)
* [DescribeRoleTokenResource](http://document.tencentcloudapi.woa.com/document/product/597/90678)
* [ModifyAccessPolicy](http://document.tencentcloudapi.woa.com/document/product/597/90668)
* [PauseDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90674)
* [ResetInstancePassword](http://document.tencentcloudapi.woa.com/document/product/597/90677)
* [RestartDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90673)
* [ResumeDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/90672)
* [UpgradeBrokerVersion](http://document.tencentcloudapi.woa.com/document/product/597/90671)

<font color="#dd0000">**删除接口**：</font>

* DeleteTopicIpWhiteList
* DescribeAppInfo
* DescribeTopicDiskUsage

修改接口：

* [CreateConnectResource](http://document.tencentcloudapi.woa.com/document/product/597/75538)

	* 新增入参：Tags

* [CreateInstancePre](http://document.tencentcloudapi.woa.com/document/product/597/45847)

	* 新增入参：CustomSSLCertId

* [CreatePostPaidInstance](http://document.tencentcloudapi.woa.com/document/product/597/78116)

	* 新增入参：CustomSSLCertId

* [CreateRoute](http://document.tencentcloudapi.woa.com/document/product/597/70172)

	* 新增入参：SecurityGroupIds, IpWhitelist

* [CreateTopic](http://document.tencentcloudapi.woa.com/document/product/597/40851)

	* 新增入参：LogMsgTimestampType

* [CreateUser](http://document.tencentcloudapi.woa.com/document/product/597/40859)

	* <font color="#dd0000">**修改入参**：</font>Password

* [DescribeACL](http://document.tencentcloudapi.woa.com/document/product/597/40856)

	* <font color="#dd0000">**修改入参**：</font>ResourceName

* [DescribeRoute](http://document.tencentcloudapi.woa.com/document/product/597/45484)

	* 新增入参：MainRouteFlag

* [ModifyDatahubTask](http://document.tencentcloudapi.woa.com/document/product/597/75543)

	* 新增入参：TasksMax, SyncThrottleLimit, AutoExpandFlag

* [ModifyGroupOffsets](http://document.tencentcloudapi.woa.com/document/product/597/40833)

	* <font color="#dd0000">**修改入参**：</font>Topics

* [ModifyInstanceAttributes](http://document.tencentcloudapi.woa.com/document/product/597/40832)

	* 新增入参：RetentionBytes, AdminSecurity, TransactionalIdExpirationMs

* [ModifyTopicAttributes](http://document.tencentcloudapi.woa.com/document/product/597/40844)

	* 新增入参：LogMsgTimestampType


新增数据结构：

* [DescModifyType](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescModifyType)
* [ExternalAccessInfoWrapper](http://document.tencentcloudapi.woa.com/document/product/597/40861#ExternalAccessInfoWrapper)
* [InstanceVersion](http://document.tencentcloudapi.woa.com/document/product/597/40861#InstanceVersion)
* [IpWhitelistDTO](http://document.tencentcloudapi.woa.com/document/product/597/40861#IpWhitelistDTO)
* [LatestBrokerVersion](http://document.tencentcloudapi.woa.com/document/product/597/40861#LatestBrokerVersion)
* [Rule](http://document.tencentcloudapi.woa.com/document/product/597/40861#Rule)

<font color="#dd0000">**删除数据结构**：</font>

* AppIdResponse
* KafkaTopicDiskUsage

修改数据结构：

* [CreateInstancePostData](http://document.tencentcloudapi.woa.com/document/product/597/40861#CreateInstancePostData)

	* 新增成员：EventId

* [CreateInstancePreData](http://document.tencentcloudapi.woa.com/document/product/597/40861#CreateInstancePreData)

	* 新增成员：EventId

* [DatahubTaskInfo](http://document.tencentcloudapi.woa.com/document/product/597/40861#DatahubTaskInfo)

	* 新增成员：TaskMax, SyncThrottleLimit, AutoExpandFlag

* [DescribeConnectResource](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeConnectResource)

	* 新增成员：Tags

* [DescribeConnectResourceResp](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeConnectResourceResp)

	* 新增成员：Tags

* [DescribeDatahubTaskRes](http://document.tencentcloudapi.woa.com/document/product/597/40861#DescribeDatahubTaskRes)

	* 新增成员：TaskMax, SyncThrottleLimit, AutoExpandFlag

* [InstanceAttributesResponse](http://document.tencentcloudapi.woa.com/document/product/597/40861#InstanceAttributesResponse)

	* 新增成员：SystemMaintenanceTime, MaxMessageByte, ElasticBandwidthSwitch, ElasticBandwidthOpenStatus, RetentionBytes, TransactionalIdExpirationMs

* [InstanceDetail](http://document.tencentcloudapi.woa.com/document/product/597/40861#InstanceDetail)

	* 新增成员：RetentionBytes

* [JgwOperateResponse](http://document.tencentcloudapi.woa.com/document/product/597/40861#JgwOperateResponse)

	* 新增成员：DeleteRouteTimestamp

* [KafkaConnectParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#KafkaConnectParam)

	* 新增成员：NetworkType, UniqVpcId, ServiceVip, Port, CrossNetResourceUniqueId, CrossNetVpcSubNetId

* [KafkaParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#KafkaParam)

	* 新增成员：Prefix, Separator, TopicList

* [MqttConnectParam](http://document.tencentcloudapi.woa.com/document/product/597/40861#MqttConnectParam)

	* 新增成员：Port, ServiceVip, Ip

* [Route](http://document.tencentcloudapi.woa.com/document/product/597/40861#Route)

	* 新增成员：Status




## 日志服务(cls) 版本：2020-10-16

### 第 152 次发布

发布时间：2026-06-08 01:24:32

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetClsService](http://document.tencentcloudapi.woa.com/document/product/614/90660)
* [OpenClsService](http://document.tencentcloudapi.woa.com/document/product/614/90659)



## 主机安全(cwp) 版本：2018-02-28

### 第 146 次发布

发布时间：2026-06-08 01:29:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeMachines](http://document.tencentcloudapi.woa.com/document/product/296/19850)

	* 新增入参：MachineAppId

* [DescribeMalwareTimingScanSetting](http://document.tencentcloudapi.woa.com/document/product/296/58240)

	* 新增入参：ProductType

* [DescribeNetAttackSetting](http://document.tencentcloudapi.woa.com/document/product/296/82099)

	* 新增入参：ProductType

* [DescribeReverseShellSystemPolicyConfig](http://document.tencentcloudapi.woa.com/document/product/296/89044)

	* 新增入参：ProductType

* [ModifyMalwareTimingScanSettings](http://document.tencentcloudapi.woa.com/document/product/296/52509)

	* 新增入参：ProductType

* [ModifyNetAttackSetting](http://document.tencentcloudapi.woa.com/document/product/296/82079)

	* 新增入参：ProductType




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 172 次发布

发布时间：2026-06-08 01:34:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [SwitchClusterZone](http://document.tencentcloudapi.woa.com/document/product/1003/75703)

	* 新增出参：TaskId




## 数据加速器 GooseFS(goosefs) 版本：2022-05-19

### 第 29 次发布

发布时间：2026-06-08 01:48:32

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ReplaceDisasterECNode](http://document.tencentcloudapi.woa.com/document/product/1716/90661)



## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 49 次发布

发布时间：2026-06-08 02:16:39

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeUserList](http://document.tencentcloudapi.woa.com/document/product/876/89188)

	* 新增入参：UidList




## TokenHub(tokenhub) 版本：2026-03-22

### 第 4 次发布

发布时间：2026-06-08 02:30:46

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeModelList](http://document.tencentcloudapi.woa.com/document/product/1814/90663)



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 32 次发布

发布时间：2026-06-08 02:39:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetJobExecutionInfo](http://document.tencentcloudapi.woa.com/document/product/1607/89352)

	* 新增入参：WorkspaceId


修改数据结构：

* [GetJobExecutionInfoRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetJobExecutionInfoRsp)

	* 新增成员：EngineJobId

* [SubJobExecutionInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SubJobExecutionInfo)

	* 新增成员：EngineJobId




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



