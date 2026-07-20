# Release 3.0.1458.1

## 腾讯云智能体开发平台(adp) 版本：2026-05-20

### 第 6 次发布

发布时间：2026-07-21 01:07:45

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAccountList](http://document.tencentcloudapi.woa.com/document/product/1815/91845)
* [DescribeAuditLogList](http://document.tencentcloudapi.woa.com/document/product/1815/91844)
* [DescribeAuditLogMeta](http://document.tencentcloudapi.woa.com/document/product/1815/91843)

新增数据结构：

* [AccountInfo](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AccountInfo)
* [AuditLog](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AuditLog)
* [AuditLogMetaField](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AuditLogMetaField)



## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 19 次发布

发布时间：2026-07-21 01:09:10

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AppendEvent](http://document.tencentcloudapi.woa.com/document/product/1804/91853)
* [CreateSession](http://document.tencentcloudapi.woa.com/document/product/1804/91852)
* [DeleteSession](http://document.tencentcloudapi.woa.com/document/product/1804/91851)
* [DescribeEvents](http://document.tencentcloudapi.woa.com/document/product/1804/91850)
* [DescribeSession](http://document.tencentcloudapi.woa.com/document/product/1804/91849)
* [DescribeSessions](http://document.tencentcloudapi.woa.com/document/product/1804/91848)
* [ModifySessionTitle](http://document.tencentcloudapi.woa.com/document/product/1804/91847)

新增数据结构：

* [EventActionsInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#EventActionsInfo)
* [EventContentInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#EventContentInfo)
* [EventInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#EventInfo)
* [EventPartInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#EventPartInfo)
* [InlineDataInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#InlineDataInfo)
* [SessionInfo](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SessionInfo)
* [SessionState](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SessionState)



## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 76 次发布

发布时间：2026-07-21 01:25:29

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [WorkloadGroupConfig](http://document.tencentcloudapi.woa.com/document/product/1706/80309#WorkloadGroupConfig)

	* 新增成员：MinCpuPercent, MinMemoryPercent, MaxConcurrencyNum, MaxQueueSize, QueueTimeout




## 云防火墙(cfw) 版本：2019-09-04

### 第 103 次发布

发布时间：2026-07-21 01:26:55

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAlertCenterRuleAsync](http://document.tencentcloudapi.woa.com/document/product/1132/91855)
* [ModifyIsolateTable](http://document.tencentcloudapi.woa.com/document/product/1132/91854)

修改接口：

* [DescribeAssetSync](http://document.tencentcloudapi.woa.com/document/product/1132/81901)

	* 新增出参：CVMCount

* [DescribeCfwAlerts](http://document.tencentcloudapi.woa.com/document/product/1132/91816)

	* 新增入参：StartTime, EndTime, Level, Direction, ActionStatus, KillChain, AttackResult, Strategy, EventName, EventId, SrcIp, DstIp, InstanceId, OrderBy, Order

* [DescribeCfwAssets](http://document.tencentcloudapi.woa.com/document/product/1132/91814)

	* 新增入参：AssetType, Ip, InstanceId, VpcId, SubnetId, InstanceType, NextToken

* [DescribeCfwRiskOverview](http://document.tencentcloudapi.woa.com/document/product/1132/91812)

	* 新增入参：StartTime, EndTime

* [DescribeCfwRuleOptimization](http://document.tencentcloudapi.woa.com/document/product/1132/91811)

	* 新增入参：RuleType, Dimensions

* [DescribeCfwRules](http://document.tencentcloudapi.woa.com/document/product/1132/91810)

	* 新增入参：Enabled, IncludeDisabled, RuleUuid, Protocol, SrcIp, DstIp, Description, Keyword, InstanceId, ExpandNames




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 19 次发布

发布时间：2026-07-21 01:43:26

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [QueryModels](http://document.tencentcloudapi.woa.com/document/product/1806/91857)

新增数据结构：

* [ModelList](http://document.tencentcloudapi.woa.com/document/product/1806/87994#ModelList)



## 全球加速(ga2) 版本：2025-01-15

### 第 8 次发布

发布时间：2026-07-21 01:56:58

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateGlobalAcceleratorAclPolicy](http://document.tencentcloudapi.woa.com/document/product/1808/91863)
* [CreateGlobalAcceleratorAclRule](http://document.tencentcloudapi.woa.com/document/product/1808/91862)
* [DeleteGlobalAcceleratorAclPolicy](http://document.tencentcloudapi.woa.com/document/product/1808/91861)
* [DeleteGlobalAcceleratorAclRule](http://document.tencentcloudapi.woa.com/document/product/1808/91860)
* [ModifyGlobalAcceleratorAclPolicy](http://document.tencentcloudapi.woa.com/document/product/1808/91859)
* [ModifyGlobalAcceleratorAclRule](http://document.tencentcloudapi.woa.com/document/product/1808/91858)

新增数据结构：

* [AclEntries](http://document.tencentcloudapi.woa.com/document/product/1808/90473#AclEntries)



## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 93 次发布

发布时间：2026-07-21 02:07:10

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [ADPConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#ADPConfig)

修改数据结构：

* [TalkLLMConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkLLMConfig)

	* 新增成员：ADP




## 安全凭证服务(sts) 版本：2018-08-13

### 第 12 次发布

发布时间：2026-07-21 02:27:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetCosSessionToken](http://document.tencentcloudapi.woa.com/document/product/1312/91865)
* [ListCosSessionSeedToken](http://document.tencentcloudapi.woa.com/document/product/1312/91864)

新增数据结构：

* [SeedCredentials](http://document.tencentcloudapi.woa.com/document/product/1312/48198#SeedCredentials)



