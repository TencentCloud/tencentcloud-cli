# Release 3.0.1184.1

## 本地专用集群(cdc) 版本：2020-12-14

### 第 9 次发布

发布时间：2025-04-18 01:10:40

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDedicatedClusterImageCache](http://document.tencentcloudapi.woa.com/document/product/1676/86171)
* [DeleteDedicatedClusterImageCache](http://document.tencentcloudapi.woa.com/document/product/1676/86170)
* [SyncDedicatedClusterImage](http://document.tencentcloudapi.woa.com/document/product/1676/86169)

新增数据结构：

* [TagSpecification](http://document.tencentcloudapi.woa.com/document/product/1676/79502#TagSpecification)
* [Tags](http://document.tencentcloudapi.woa.com/document/product/1676/79502#Tags)



## 主机安全(cwp) 版本：2018-02-28

### 第 121 次发布

发布时间：2025-04-18 01:13:40

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ExportFileTamperEvents](http://document.tencentcloudapi.woa.com/document/product/296/82089)

	* 新增入参：Where


修改数据结构：

* [LicenseBindDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#LicenseBindDetail)

	* 新增成员：InstanceState, AgentState

* [Machine](http://document.tencentcloudapi.woa.com/document/product/296/19867#Machine)

	* 新增成员：AgentStatus, InstanceStatus

* [MalwareInfo](http://document.tencentcloudapi.woa.com/document/product/296/19867#MalwareInfo)

	* 新增成员：FileExists, ProcessExists

* [ReverseShellEventInfo](http://document.tencentcloudapi.woa.com/document/product/296/19867#ReverseShellEventInfo)

	* 新增成员：RiskLevel




## 云游戏(gs) 版本：2019-11-18

### 第 15 次发布

发布时间：2025-04-18 01:20:45

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyAndroidAppVersion](http://document.tencentcloudapi.woa.com/document/product/1162/86172)
* [ModifyAndroidInstancesResolution](http://document.tencentcloudapi.woa.com/document/product/1162/86173)

修改接口：

* [CreateAndroidApp](http://document.tencentcloudapi.woa.com/document/product/1162/86153)

	* 新增入参：AppMode

* [CreateAndroidAppVersion](http://document.tencentcloudapi.woa.com/document/product/1162/86152)

	* 新增入参：Command

* [ModifyAndroidInstanceResolution](http://document.tencentcloudapi.woa.com/document/product/1162/86006)

	* 新增入参：FPS, ResolutionType


修改数据结构：

* [AndroidApp](http://document.tencentcloudapi.woa.com/document/product/1162/40743#AndroidApp)

	* 新增成员：AppMode

* [AndroidAppCosInfo](http://document.tencentcloudapi.woa.com/document/product/1162/40743#AndroidAppCosInfo)

	* 新增成员：FileName

* [AndroidAppVersionInfo](http://document.tencentcloudapi.woa.com/document/product/1162/40743#AndroidAppVersionInfo)

	* 新增成员：Command




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 72 次发布

发布时间：2025-04-18 01:22:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeTWeSeeConfig](http://document.tencentcloudapi.woa.com/document/product/1081/86176)
* [InvokeAISearchService](http://document.tencentcloudapi.woa.com/document/product/1081/86175)
* [ModifyTWeSeeConfig](http://document.tencentcloudapi.woa.com/document/product/1081/86174)

新增数据结构：

* [TargetInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TargetInfo)



## 轻量应用服务器(lighthouse) 版本：2020-03-24

### 第 69 次发布

发布时间：2025-04-18 01:24:28

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除接口**：</font>

* DescribeInstanceLoginKeyPairAttribute
* ModifyInstancesLoginKeyPairAttribute



## 媒体处理(mps) 版本：2019-06-12

### 第 85 次发布

发布时间：2025-04-18 01:26:29

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [StreamUrlDetail](http://document.tencentcloudapi.woa.com/document/product/862/37615#StreamUrlDetail)

修改数据结构：

* [CreateOutputInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#CreateOutputInfo)

	* 新增成员：OutputKind

* [DescribeInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#DescribeInput)

	* 新增成员：StreamUrls

* [DescribeOutput](http://document.tencentcloudapi.woa.com/document/product/862/37615#DescribeOutput)

	* 新增成员：OutputKind, StreamUrls

* [ModifyOutputInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#ModifyOutputInfo)

	* 新增成员：OutputKind




## 云托管 CloudBase Run(tcbr) 版本：2022-02-17

### 第 5 次发布

发布时间：2025-04-18 01:31:09

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ServerBaseConfig](http://document.tencentcloudapi.woa.com/document/product/1711/80400#ServerBaseConfig)

	* 新增成员：InternalAccess




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 73 次发布

发布时间：2025-04-18 01:33:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTrainingTask](http://document.tencentcloudapi.woa.com/document/product/851/74857)

	* 新增入参：CodeRepos


新增数据结构：

* [CodeRepoConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#CodeRepoConfig)

修改数据结构：

* [TrainingTaskDetail](http://document.tencentcloudapi.woa.com/document/product/851/74915#TrainingTaskDetail)

	* 新增成员：CodeRepos




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 40 次发布

发布时间：2025-04-18 01:34:23

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeMigratingTopicList](http://document.tencentcloudapi.woa.com/document/product/1739/86168)

	* <font color="#dd0000">**修改入参**：</font>Offset, Limit

* [DescribeSourceClusterGroupList](http://document.tencentcloudapi.woa.com/document/product/1739/86167)

	* <font color="#dd0000">**修改入参**：</font>Offset, Limit


修改数据结构：

* [ConsumerClient](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumerClient)

	* 新增成员：ChannelProtocol

* [MigratingTopic](http://document.tencentcloudapi.woa.com/document/product/1739/81437#MigratingTopic)

	* 新增成员：NamespaceV4, TopicNameV4, FullNamespaceV4, HealthCheckErrorList




## 私有网络(vpc) 版本：2017-03-12

### 第 207 次发布

发布时间：2025-04-18 01:36:34

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeInstanceJumbo](http://document.tencentcloudapi.woa.com/document/product/215/86177)

修改接口：

* [AssignPrivateIpAddresses](http://document.tencentcloudapi.woa.com/document/product/215/15813)

	* 新增入参：IsCrossTenant, VpcAppId, VpcUin, VpcSubAccountUin

* [UnassignPrivateIpAddresses](http://document.tencentcloudapi.woa.com/document/product/215/15814)

	* 新增入参：IsCrossTenant, VpcAppId, VpcUin, VpcSubAccountUin


新增数据结构：

* [InstanceJumbo](http://document.tencentcloudapi.woa.com/document/product/215/15824#InstanceJumbo)



