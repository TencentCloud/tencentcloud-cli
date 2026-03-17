# Release 3.0.1385.1

## 应用性能监控(apm) 版本：2021-06-22

### 第 28 次发布

发布时间：2026-03-18 01:10:29

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ServiceDetail](http://document.tencentcloudapi.woa.com/document/product/1463/64927#ServiceDetail)

	* 新增成员：EnableThresholdConfig, ErrRateThreshold, ResponseDurationWarningThreshold




## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 32 次发布

发布时间：2026-03-18 01:11:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAcl](http://document.tencentcloudapi.woa.com/document/product/1780/85297)

	* 新增入参：MaxAccessCredentialDuration

* [ModifyAcl](http://document.tencentcloudapi.woa.com/document/product/1780/85291)

	* 新增入参：MaxAccessCredentialDuration


修改数据结构：

* [Acl](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Acl)

	* 新增成员：MaxAccessCredentialDuration

* [Resource](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Resource)

	* 新增成员：ResourceEdition, TimeUnit, TimeSpan, PayMode




## 主机安全(cwp) 版本：2018-02-28

### 第 142 次发布

发布时间：2026-03-18 01:27:07

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAttackType](http://document.tencentcloudapi.woa.com/document/product/296/89042)
* [DescribeInjectRiskyServiceSwitch](http://document.tencentcloudapi.woa.com/document/product/296/89030)
* [DescribeLoginTypeGlobalConf](http://document.tencentcloudapi.woa.com/document/product/296/89033)
* [DescribeLoginTypeHost](http://document.tencentcloudapi.woa.com/document/product/296/89032)
* [DescribeMemShellRules](http://document.tencentcloudapi.woa.com/document/product/296/89046)
* [DescribeRaspEventCWP](http://document.tencentcloudapi.woa.com/document/product/296/89041)
* [DescribeRaspEventDetailCWP](http://document.tencentcloudapi.woa.com/document/product/296/89040)
* [DescribeRaspEventDetailTCSS](http://document.tencentcloudapi.woa.com/document/product/296/89039)
* [DescribeRaspEventTCSS](http://document.tencentcloudapi.woa.com/document/product/296/89038)
* [DescribeRaspLicenseList](http://document.tencentcloudapi.woa.com/document/product/296/89027)
* [DescribeRaspMemShellDetailTCSS](http://document.tencentcloudapi.woa.com/document/product/296/89037)
* [DescribeRaspMemShellListTCSS](http://document.tencentcloudapi.woa.com/document/product/296/89036)
* [DescribeRaspPluginList](http://document.tencentcloudapi.woa.com/document/product/296/89026)
* [DescribeReverseShellRulesAggregation](http://document.tencentcloudapi.woa.com/document/product/296/89045)
* [DescribeReverseShellSystemPolicyConfig](http://document.tencentcloudapi.woa.com/document/product/296/89044)
* [DescribeShellPolicyList](http://document.tencentcloudapi.woa.com/document/product/296/89043)
* [DescribeVulDefenceOverviewCount](http://document.tencentcloudapi.woa.com/document/product/296/89029)
* [DescribeVulDefenceSettingList](http://document.tencentcloudapi.woa.com/document/product/296/89028)
* [DescribeYDRaspBlackWhite](http://document.tencentcloudapi.woa.com/document/product/296/89035)
* [RaspEventOverview](http://document.tencentcloudapi.woa.com/document/product/296/89034)

新增数据结构：

* [ClientSettingHost](http://document.tencentcloudapi.woa.com/document/product/296/19867#ClientSettingHost)
* [MemShellRule](http://document.tencentcloudapi.woa.com/document/product/296/19867#MemShellRule)
* [OrderDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#OrderDetail)
* [RaspAttackTypeListItem](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspAttackTypeListItem)
* [RaspEvent](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspEvent)
* [RaspEventDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspEventDetail)
* [RaspEventOverview](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspEventOverview)
* [RaspLicenseList](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspLicenseList)
* [RaspLicensePlugin](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspLicensePlugin)
* [RaspMemShellDetail](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspMemShellDetail)
* [RaspMemShellEvent](http://document.tencentcloudapi.woa.com/document/product/296/19867#RaspMemShellEvent)
* [ReverseShellRuleAggregation](http://document.tencentcloudapi.woa.com/document/product/296/19867#ReverseShellRuleAggregation)
* [RiskMainClass](http://document.tencentcloudapi.woa.com/document/product/296/19867#RiskMainClass)
* [ShellPolicyList](http://document.tencentcloudapi.woa.com/document/product/296/19867#ShellPolicyList)
* [UuidHostip](http://document.tencentcloudapi.woa.com/document/product/296/19867#UuidHostip)
* [VulDefenceSetting](http://document.tencentcloudapi.woa.com/document/product/296/19867#VulDefenceSetting)
* [YDRaspBlackWhiteListItem](http://document.tencentcloudapi.woa.com/document/product/296/19867#YDRaspBlackWhiteListItem)



## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 156 次发布

发布时间：2026-03-18 01:32:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateBackup](http://document.tencentcloudapi.woa.com/document/product/1003/75917)

	* 新增入参：Vaults

* [DescribeRollbackTimeRange](http://document.tencentcloudapi.woa.com/document/product/1003/48092)

	* 新增入参：VaultId, VaultRegion

* [RollBackCluster](http://document.tencentcloudapi.woa.com/document/product/1003/70115)

	* 新增入参：VaultId




## DNSPod(dnspod) 版本：2021-03-23

### 第 61 次发布

发布时间：2026-03-18 01:38:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeRecordList](http://document.tencentcloudapi.woa.com/document/product/1427/56166)

	* 新增入参：ErrorOnEmpty


修改数据结构：

* [Deals](http://document.tencentcloudapi.woa.com/document/product/1427/56185#Deals)

	* 新增成员：ResourceId




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 221 次发布

发布时间：2026-03-18 01:44:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChannelCreateFlowByFiles](http://document.tencentcloudapi.woa.com/document/product/1595/75257)

	* 新增入参：FlowOperateLimit


新增数据结构：

* [FlowOperateLimit](http://document.tencentcloudapi.woa.com/document/product/1595/75258#FlowOperateLimit)

修改数据结构：

* [FlowInfo](http://document.tencentcloudapi.woa.com/document/product/1595/75258#FlowInfo)

	* 新增成员：FlowOperateLimit




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 容器安全服务(tcss) 版本：2020-11-01

### 第 50 次发布

发布时间：2026-03-18 02:16:22

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeImageDenyEventDetail](http://document.tencentcloudapi.woa.com/document/product/1662/89052)
* [DescribeImageDenyEventList](http://document.tencentcloudapi.woa.com/document/product/1662/89051)
* [DescribeImageDenyEventTendency](http://document.tencentcloudapi.woa.com/document/product/1662/89050)
* [DescribeImageDenyRuleDetail](http://document.tencentcloudapi.woa.com/document/product/1662/89049)
* [DescribeImageDenyRuleList](http://document.tencentcloudapi.woa.com/document/product/1662/89048)
* [DescribeImageDenyRuleSummary](http://document.tencentcloudapi.woa.com/document/product/1662/89047)
* [DescribeMaliciousConnectionBlackList](http://document.tencentcloudapi.woa.com/document/product/1662/89054)
* [DescribeMaliciousConnectionWhiteList](http://document.tencentcloudapi.woa.com/document/product/1662/89053)
* [DescribeReverseShellRegexpWhiteList](http://document.tencentcloudapi.woa.com/document/product/1662/89056)
* [DescribeReverseShellRegexpWhiteListInfo](http://document.tencentcloudapi.woa.com/document/product/1662/89055)

新增数据结构：

* [ImageDenyEvent](http://document.tencentcloudapi.woa.com/document/product/1662/79121#ImageDenyEvent)
* [ImageDenyEventTendency](http://document.tencentcloudapi.woa.com/document/product/1662/79121#ImageDenyEventTendency)
* [ImageDenyRule](http://document.tencentcloudapi.woa.com/document/product/1662/79121#ImageDenyRule)
* [MaliciousConnectionRuleInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#MaliciousConnectionRuleInfo)
* [RegexpRuleInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#RegexpRuleInfo)
* [RegexpRuleListItem](http://document.tencentcloudapi.woa.com/document/product/1662/79121#RegexpRuleListItem)
* [WhiteListRegexpExpressionInfo](http://document.tencentcloudapi.woa.com/document/product/1662/79121#WhiteListRegexpExpressionInfo)



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 119 次发布

发布时间：2026-03-18 02:24:22

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [GitSecret](http://document.tencentcloudapi.woa.com/document/product/851/74915#GitSecret)

	* 新增成员：SecretId




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 容器服务(tke) 版本：2022-05-01

### 第 20 次发布

发布时间：2026-03-18 02:28:02

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeGPUInfo](http://document.tencentcloudapi.woa.com/document/product/457/89057)
* [DescribeZoneInstanceConfigInfos](http://document.tencentcloudapi.woa.com/document/product/457/89058)



## 容器服务(tke) 版本：2018-05-25

### 第 117 次发布

发布时间：2026-03-18 02:25:43

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyClusterSchedulerPolicy](http://document.tencentcloudapi.woa.com/document/product/457/77529)

	* 新增入参：HighPerformance, PoolSchedulerStartArg


新增数据结构：

* [PoolSchedulerStartArg](http://document.tencentcloudapi.woa.com/document/product/457/31866#PoolSchedulerStartArg)



