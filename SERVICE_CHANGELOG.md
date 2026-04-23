# Release 3.0.1410.1

## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 15 次发布

发布时间：2026-04-24 01:10:11

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateSignOnAgentService](http://document.tencentcloudapi.woa.com/document/product/1805/90048)
* [DeleteSignOnAgentService](http://document.tencentcloudapi.woa.com/document/product/1805/90047)



## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 163 次发布

发布时间：2026-04-24 01:17:26

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstanceUpgradeType](http://document.tencentcloudapi.woa.com/document/product/236/84161)

	* 新增入参：DstFourthZone

* [UpgradeDBInstance](http://document.tencentcloudapi.woa.com/document/product/236/15876)

	* 新增入参：FourthZone




## 日志服务(cls) 版本：2020-10-16

### 第 147 次发布

发布时间：2026-04-24 01:24:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateSearchView](http://document.tencentcloudapi.woa.com/document/product/614/90052)
* [DeleteSearchView](http://document.tencentcloudapi.woa.com/document/product/614/90051)
* [DescribeSearchViews](http://document.tencentcloudapi.woa.com/document/product/614/90050)
* [ModifySearchView](http://document.tencentcloudapi.woa.com/document/product/614/90049)

新增数据结构：

* [SearchViewInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#SearchViewInfo)
* [ViewSearchTopic](http://document.tencentcloudapi.woa.com/document/product/614/56471#ViewSearchTopic)



## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 161 次发布

发布时间：2026-04-24 01:31:57

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AssociateSecurityGroups](http://document.tencentcloudapi.woa.com/document/product/1003/70119)

	* <font color="#dd0000">**修改入参**：</font>Zone

* [DisassociateSecurityGroups](http://document.tencentcloudapi.woa.com/document/product/1003/70117)

	* <font color="#dd0000">**修改入参**：</font>Zone

* [ModifyDBInstanceSecurityGroups](http://document.tencentcloudapi.woa.com/document/product/1003/48096)

	* <font color="#dd0000">**修改入参**：</font>Zone


修改数据结构：

* [CynosdbInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1003/48097#CynosdbInstanceDetail)

	* 新增成员：MasterZone




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 138 次发布

发布时间：2026-04-24 01:42:04

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ReplaceTkeCluster](http://document.tencentcloudapi.woa.com/document/product/589/90053)



## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 27 次发布

发布时间：2026-04-24 01:58:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83721)

	* 新增入参：EnableScope

* [CreateSharedKnowledge](http://document.tencentcloudapi.woa.com/document/product/1759/88288)

	* 新增入参：EsConfig, MultiEmbeddingModel

* [ListRejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83714)

	* 新增入参：Filters

* [ListWorkflowRuns](http://document.tencentcloudapi.woa.com/document/product/1759/88276)

	* 新增入参：Query


新增数据结构：

* [ESConfig](http://document.tencentcloudapi.woa.com/document/product/1759/83593#ESConfig)
* [FilterItem](http://document.tencentcloudapi.woa.com/document/product/1759/83593#FilterItem)

修改数据结构：

* [MsgRecord](http://document.tencentcloudapi.woa.com/document/product/1759/83593#MsgRecord)

	* 新增成员：OptionMode

* [RejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83593#RejectedQuestion)

	* 新增成员：EnableScope

* [WorkFlowSummary](http://document.tencentcloudapi.woa.com/document/product/1759/83593#WorkFlowSummary)

	* 新增成员：OptionMode

* [WorkflowInfo](http://document.tencentcloudapi.woa.com/document/product/1759/83593#WorkflowInfo)

	* 新增成员：OptionMode




## 媒体处理(mps) 版本：2019-06-12

### 第 166 次发布

发布时间：2026-04-24 02:04:04

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeTextToSpeechAsyncTask](http://document.tencentcloudapi.woa.com/document/product/862/90055)
* [TextToSpeechAsync](http://document.tencentcloudapi.woa.com/document/product/862/90054)

修改数据结构：

* [AigcImageExtraParam](http://document.tencentcloudapi.woa.com/document/product/862/37615#AigcImageExtraParam)

	* 新增成员：LogoAdd

* [SSAIChannelInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#SSAIChannelInfo)

	* 新增成员：HlsPlaybackPrefix, DashPlaybackPrefix

* [SSAIConf](http://document.tencentcloudapi.woa.com/document/product/862/37615#SSAIConf)

	* 新增成员：DashOriginManifestType, SlateOnEmptyVast, SCTEMarkerDuration, SecurityGroupId




## 短信(sms) 版本：2021-01-11

### 第 8 次发布

发布时间：2026-04-24 02:13:56

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [SendMultiGlobalSms](http://document.tencentcloudapi.woa.com/document/product/382/90056)

新增数据结构：

* [MultiSmsInfo](http://document.tencentcloudapi.woa.com/document/product/382/52068#MultiSmsInfo)
* [SendMultiStatus](http://document.tencentcloudapi.woa.com/document/product/382/52068#SendMultiStatus)



## 短信(sms) 版本：2019-07-11



## 容器安全服务(tcss) 版本：2020-11-01

### 第 53 次发布

发布时间：2026-04-24 02:19:44

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddOrModifyMaliciousConnectionWhiteList](http://document.tencentcloudapi.woa.com/document/product/1662/90057)
* [AddOrModifyVirusWhiteListRule](http://document.tencentcloudapi.woa.com/document/product/1662/90062)
* [DeleteVirusWhiteListRule](http://document.tencentcloudapi.woa.com/document/product/1662/90061)
* [DescribeVirusMonitorConfig](http://document.tencentcloudapi.woa.com/document/product/1662/90060)
* [DescribeVirusScanConfig](http://document.tencentcloudapi.woa.com/document/product/1662/90059)
* [DescribeVirusWhiteListRules](http://document.tencentcloudapi.woa.com/document/product/1662/90058)

新增数据结构：

* [ScanRangeInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#ScanRangeInfo)
* [VirusWhiteListRuleInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#VirusWhiteListRuleInfo)

修改数据结构：

* [HostInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#HostInfo)

	* 新增成员：ClusterAccessedSubStatus, ClusterAccessedErrorReason

* [SuperNodeListItem](http://document.tencentcloudapi.woa.com/document/product/1662/79121#SuperNodeListItem)

	* 新增成员：ClusterAccessedSubStatus, ClusterAccessedErrorReason




## 高性能计算平台(thpc) 版本：2023-03-21

### 第 29 次发布

发布时间：2026-04-24 02:26:47

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [JobView](http://document.tencentcloudapi.woa.com/document/product/1701/80209#JobView)

	* 新增成员：Creator




## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 127 次发布

发布时间：2026-04-24 02:27:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeBillingResourceGroupAttachedWorkspaces](http://document.tencentcloudapi.woa.com/document/product/851/90063)

新增数据结构：

* [JobBrief](http://document.tencentcloudapi.woa.com/document/product/851/74915#JobBrief)
* [ResourceGroupAttachedWorkspace](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroupAttachedWorkspace)
* [ResourceInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceInstanceInfo)



## TI-ONE 训练平台(tione) 版本：2019-10-22



## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 125 次发布

发布时间：2026-04-24 02:29:10

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRollOutSequence](http://document.tencentcloudapi.woa.com/document/product/457/88169)

	* 新增出参：ID




## 实时音视频(trtc) 版本：2019-07-22

### 第 128 次发布

发布时间：2026-04-24 02:32:17

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AsrParam](http://document.tencentcloudapi.woa.com/document/product/647/44055#AsrParam)

	* 新增成员：FilterDirty, FilterModal, FilterPunc

* [CloudStorage](http://document.tencentcloudapi.woa.com/document/product/647/44055#CloudStorage)

	* 新增成员：EndpointUrl




