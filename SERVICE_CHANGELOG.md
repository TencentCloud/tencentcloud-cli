# Release 3.0.1374.1

## 大模型安全网关(apis) 版本：2024-08-01

### 第 6 次发布

发布时间：2026-03-03 01:10:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAgentAppModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88924)
* [CreateModel](http://document.tencentcloudapi.woa.com/document/product/1805/88915)
* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88920)
* [DeleteAgentAppModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88923)
* [DeleteModel](http://document.tencentcloudapi.woa.com/document/product/1805/88914)
* [DeleteModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88919)
* [DescribeAgentAppModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88922)
* [DescribeModel](http://document.tencentcloudapi.woa.com/document/product/1805/88913)
* [DescribeModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88918)
* [DescribeModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88917)
* [DescribeModels](http://document.tencentcloudapi.woa.com/document/product/1805/88912)
* [ModifyAgentAppModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88921)
* [ModifyModel](http://document.tencentcloudapi.woa.com/document/product/1805/88911)
* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88916)

新增数据结构：

* [AgentAppModelServiceDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppModelServiceDTO)
* [AgentAppModelServiceVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AgentAppModelServiceVO)
* [DescribeAgentAppModelServicesResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAgentAppModelServicesResponseVO)
* [DescribeModelResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelResponseVO)
* [DescribeModelServiceResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServiceResponseVO)
* [DescribeModelServicesResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServicesResponseVO)
* [DescribeModelServicesSort](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServicesSort)
* [DescribeModelsResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelsResponseVO)
* [DescribeModelsSort](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelsSort)
* [LimitWindowsDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#LimitWindowsDTO)
* [ResultIDsVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#ResultIDsVO)
* [TargetModelDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TargetModelDTO)
* [TmsConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TmsConfigDTO)
* [TokenLimitConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TokenLimitConfigDTO)



## 应用性能监控(apm) 版本：2021-06-22

### 第 26 次发布

发布时间：2026-03-03 01:12:00

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyApmApplicationConfig](http://document.tencentcloudapi.woa.com/document/product/1463/88214)

	* 新增入参：EnableThresholdConfig, ErrRateThreshold, ResponseDurationWarningThreshold


修改数据结构：

* [ApmAppConfig](http://document.tencentcloudapi.woa.com/document/product/1463/64927#ApmAppConfig)

	* 新增成员：EnableThresholdConfig, ErrRateThreshold, ResponseDurationWarningThreshold

* [ApmApplicationConfigView](http://document.tencentcloudapi.woa.com/document/product/1463/64927#ApmApplicationConfigView)

	* 新增成员：AgentIgnoreOperation, EnableSecurityConfig, IsSqlInjectionAnalysis, IsInstrumentationVulnerabilityScan, IsRemoteCommandExecutionAnalysis, IsMemoryHijackingAnalysis, IsDeleteAnyFileAnalysis, IsReadAnyFileAnalysis, IsUploadAnyFileAnalysis, IsIncludeAnyFileAnalysis, IsDirectoryTraversalAnalysis, IsTemplateEngineInjectionAnalysis, IsScriptEngineInjectionAnalysis, IsExpressionInjectionAnalysis, IsJndiInjectionAnalysis, IsJniInjectionAnalysis, IsWebshellBackdoorAnalysis, IsDeserializationAnalysis, EnableDashboardConfig, IsRelatedDashboard, DashboardTopicID, EnableThresholdConfig, ErrRateThreshold, ResponseDurationWarningThreshold




## 云防火墙(cfw) 版本：2019-09-04

### 第 89 次发布

发布时间：2026-03-03 01:22:51

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [EnterpriseSecurityGroupRuleRuleInfo](http://document.tencentcloudapi.woa.com/document/product/1132/49071#EnterpriseSecurityGroupRuleRuleInfo)

	* 新增成员：RulePartition, Scope

* [SecurityGroupRule](http://document.tencentcloudapi.woa.com/document/product/1132/49071#SecurityGroupRule)

	* 新增成员：Scope

* [SecurityGroupSimplifyRule](http://document.tencentcloudapi.woa.com/document/product/1132/49071#SecurityGroupSimplifyRule)

	* 新增成员：Scope




## 媒体处理(mps) 版本：2019-06-12

### 第 152 次发布

发布时间：2026-03-03 02:02:44

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [EditMedia](http://document.tencentcloudapi.woa.com/document/product/862/43010)

	* 新增入参：ResourceId

* [ProcessLiveStream](http://document.tencentcloudapi.woa.com/document/product/862/39227)

	* 新增入参：ResourceId




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 54 次发布

发布时间：2026-03-03 02:07:23

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ExecuteDBBrainQuery](http://document.tencentcloudapi.woa.com/document/product/409/88925)

新增数据结构：

* [DBBrainFilter](http://document.tencentcloudapi.woa.com/document/product/409/16778#DBBrainFilter)



## 统一Catalog服务(tccatalog) 版本：2024-10-24

### 第 9 次发布

发布时间：2026-03-03 02:14:18

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetUserCosBucketsInfo](http://document.tencentcloudapi.woa.com/document/product/1785/88927)

新增数据结构：

* [BucketInfo](http://document.tencentcloudapi.woa.com/document/product/1785/85705#BucketInfo)



## 私有网络(vpc) 版本：2017-03-12

### 第 241 次发布

发布时间：2026-03-03 02:29:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDesignatedZones](http://document.tencentcloudapi.woa.com/document/product/215/88928)

修改接口：

* [CreateVpnGatewaySslServer](http://document.tencentcloudapi.woa.com/document/product/215/70289)

	* 新增入参：DnsServers

* [ModifyVpnGatewaySslServer](http://document.tencentcloudapi.woa.com/document/product/215/82468)

	* 新增入参：DnsServers


新增数据结构：

* [DesignatedZoneInfoDict](http://document.tencentcloudapi.woa.com/document/product/215/15824#DesignatedZoneInfoDict)
* [DnsServers](http://document.tencentcloudapi.woa.com/document/product/215/15824#DnsServers)

修改数据结构：

* [SslVpnSever](http://document.tencentcloudapi.woa.com/document/product/215/15824#SslVpnSever)

	* 新增成员：DnsServers




