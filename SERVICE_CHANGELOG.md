# Release 3.0.1320.1

## 云开发低码(lowcode) 版本：2021-01-08

### 第 29 次发布

发布时间：2025-12-05 01:45:13

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* DescribePermissionForAppPage



## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 165 次发布

发布时间：2025-12-05 02:01:10

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateEnvironment](http://document.tencentcloudapi.woa.com/document/product/1179/46081)

	* 新增入参：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable

	* 新增出参：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable

* [CreateProCluster](http://document.tencentcloudapi.woa.com/document/product/1179/82556)

	* <font color="#dd0000">**修改入参**：</font>StorageSize

* [CreateTopic](http://document.tencentcloudapi.woa.com/document/product/1179/46088)

	* 新增入参：PulsarTopicMessageType

* [DescribeEnvironmentAttributes](http://document.tencentcloudapi.woa.com/document/product/1179/46079)

	* 新增出参：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable

* [DescribeMsgTrace](http://document.tencentcloudapi.woa.com/document/product/1179/82543)

	* 新增入参：TopicName

* [DescribePulsarProInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1179/77492)

	* 新增出参：CertificateList

* [ModifyEnvironmentAttributes](http://document.tencentcloudapi.woa.com/document/product/1179/46077)

	* 新增入参：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable

	* 新增出参：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable


修改数据结构：

* [Cluster](http://document.tencentcloudapi.woa.com/document/product/1179/46089#Cluster)

	* 新增成员：OldPublicEndPoint, OldVpcEndPoint, OldInternalPulsarEndPoint, OldInternalHttpEndPoint

* [Environment](http://document.tencentcloudapi.woa.com/document/product/1179/46089#Environment)

	* 新增成员：SubscriptionExpirationTime, SubscriptionExpirationTimeEnable

* [InternalTenant](http://document.tencentcloudapi.woa.com/document/product/1179/46089#InternalTenant)

	* 新增成员：TagList, TenantSpec

* [PulsarNetworkAccessPointInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#PulsarNetworkAccessPointInfo)

	* 新增成员：SecurityGroupIds

* [Topic](http://document.tencentcloudapi.woa.com/document/product/1179/46089#Topic)

	* 新增成员：PulsarTopicMessageType




## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 54 次发布

发布时间：2025-12-05 02:07:36

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [SendMessage](http://document.tencentcloudapi.woa.com/document/product/1739/88199)
* [VerifyMessageConsumption](http://document.tencentcloudapi.woa.com/document/product/1739/88198)



## 腾讯混元生视频(vclm) 版本：2024-05-23

### 第 6 次发布

发布时间：2025-12-05 02:10:16

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeHunyuanToVideoJob](http://document.tencentcloudapi.woa.com/document/product/1766/88203)
* [DescribeVideoVoiceJob](http://document.tencentcloudapi.woa.com/document/product/1766/88202)
* [SubmitHunyuanToVideoJob](http://document.tencentcloudapi.woa.com/document/product/1766/88201)
* [SubmitVideoVoiceJob](http://document.tencentcloudapi.woa.com/document/product/1766/88200)



## 私有网络(vpc) 版本：2017-03-12

### 第 231 次发布

发布时间：2025-12-05 02:11:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ReturnNormalAddresses](http://document.tencentcloudapi.woa.com/document/product/215/76777)

	* 新增入参：SkipTrafficValidation


修改数据结构：

* [CCN](http://document.tencentcloudapi.woa.com/document/product/215/15824#CCN)

	* 新增成员：RouteTablePolicyValueCommunityFlag, PolicyBasedRoutingFlag

* [ComplianceAddress](http://document.tencentcloudapi.woa.com/document/product/215/15824#ComplianceAddress)

	* <font color="#dd0000">**修改成员**：</font>TagList




