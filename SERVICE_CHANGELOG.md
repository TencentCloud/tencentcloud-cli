# Release 3.0.1480.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 25 次发布

发布时间：2026-08-26 01:08:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSandboxTool](http://document.tencentcloudapi.woa.com/document/product/1804/87843)

	* 新增入参：ComputerConfiguration

* [UpdateSandboxTool](http://document.tencentcloudapi.woa.com/document/product/1804/87840)

	* 新增入参：ComputerConfiguration




## 灾备中心(bdrc) 版本：2026-03-30

### 第 3 次发布

发布时间：2026-08-26 01:13:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateFileBackupPlan](http://document.tencentcloudapi.woa.com/document/product/1824/92363)

	* 新增入参：ResourceType

	* <font color="#dd0000">**修改入参**：</font>BackupStorageId




## 云联络中心(ccc) 版本：2020-02-10

### 第 100 次发布

发布时间：2026-08-26 01:21:02

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeSTTGlobalConfig](http://document.tencentcloudapi.woa.com/document/product/679/92426)

修改接口：

* [CreateAIAgentCall](http://document.tencentcloudapi.woa.com/document/product/679/85667)

	* 新增入参：AcquireTimeoutSecond




## 云原生智能网关(cngw) 版本：2023-04-18

### 第 7 次发布

发布时间：2026-08-26 01:32:03

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AIGWLogConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWLogConfig)

	* 新增成员：RequestLogPayloadTruncationPolicy, ResponseLogPayloadTruncationPolicy




## TDSQL MySQL 版(dcdb) 版本：2018-04-11

### 第 58 次发布

发布时间：2026-08-26 01:43:18

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UpgradeDCDBInstance](http://document.tencentcloudapi.woa.com/document/product/557/16136)

	* 新增入参：SwitchInterval

* [UpgradeDedicatedDCDBInstance](http://document.tencentcloudapi.woa.com/document/product/557/77817)

	* 新增入参：SwitchInterval

* [UpgradeHourDCDBInstance](http://document.tencentcloudapi.woa.com/document/product/557/76984)

	* 新增入参：SwitchInterval




## 边缘可用区(edgezone) 版本：2026-04-01

### 第 3 次发布

发布时间：2026-08-26 01:51:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstances](http://document.tencentcloudapi.woa.com/document/product/1812/91504)

	* 新增入参：Password, SSHKey

	* <font color="#dd0000">**修改入参**：</font>InstanceName

* [DescribeInstanceTypes](http://document.tencentcloudapi.woa.com/document/product/1812/91503)

	* 新增入参：Offset, Limit

* [DescribeInstances](http://document.tencentcloudapi.woa.com/document/product/1812/91502)

	* 新增入参：PublicNetworkId, PrivateNetworkId

* [DescribeZones](http://document.tencentcloudapi.woa.com/document/product/1812/91501)

	* 新增入参：FilterByAppId

* [ModifyInstanceAttribute](http://document.tencentcloudapi.woa.com/document/product/1812/91500)


修改数据结构：

* [Instance](http://document.tencentcloudapi.woa.com/document/product/1812/91507#Instance)

	* 新增成员：FileSystemType, InstanceFamily, InstanceFamilyName, CpuType, Cpu, Memory

* [InstanceTypeQuota](http://document.tencentcloudapi.woa.com/document/product/1812/91507#InstanceTypeQuota)

	* 新增成员：InstanceFamilyName




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 153 次发布

发布时间：2026-08-26 01:52:11

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudInstance](http://document.tencentcloudapi.woa.com/document/product/589/85470)

	* 新增入参：ComputeResourceGroupIds, TerminateProtection


新增数据结构：

* [GpuImageDriverSpec](http://document.tencentcloudapi.woa.com/document/product/589/33981#GpuImageDriverSpec)

修改数据结构：

* [ComputeMultiZoneSetting](http://document.tencentcloudapi.woa.com/document/product/589/33981#ComputeMultiZoneSetting)

	* 新增成员：AdvanceParams, GroupName, NodeType

* [DynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceForm)

	* 新增成员：EnableHistoryServer

* [Resource](http://document.tencentcloudapi.woa.com/document/product/589/33981#Resource)

	* 新增成员：CustomNodeName, GpuImageDriver

* [UserManagerUserBriefInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#UserManagerUserBriefInfo)

	* 新增成员：Groups, Uin, State, DisplayPasswdUpdateTime, PasswdUpdateTime, PasswdUsedDay, PasswdUsedHour




## 腾讯云智能体开发平台(lke) 版本：2023-11-30

### 第 42 次发布

发布时间：2026-08-26 02:22:34

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateRejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83721)

	* 新增入参：CustomReply

* [ModifyRejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83712)

	* 新增入参：CustomReply


新增数据结构：

* [CustomReplyConfig](http://document.tencentcloudapi.woa.com/document/product/1759/83593#CustomReplyConfig)

修改数据结构：

* [RejectedQuestion](http://document.tencentcloudapi.woa.com/document/product/1759/83593#RejectedQuestion)

	* 新增成员：CustomReply




## 腾讯云可观测平台(monitor) 版本：2023-06-16

### 第 12 次发布

发布时间：2026-08-26 02:28:39

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CancelAIWorkbenchChat](http://document.tencentcloudapi.woa.com/document/product/248/92453)
* [CreateAIWorkbenchAgent](http://document.tencentcloudapi.woa.com/document/product/248/92452)
* [CreateAIWorkbenchTask](http://document.tencentcloudapi.woa.com/document/product/248/92451)
* [DeleteAIWorkbenchAgent](http://document.tencentcloudapi.woa.com/document/product/248/92450)
* [DeleteAIWorkbenchTask](http://document.tencentcloudapi.woa.com/document/product/248/92449)
* [DescribeAIWorkbenchAgent](http://document.tencentcloudapi.woa.com/document/product/248/92448)
* [DescribeAIWorkbenchArtifact](http://document.tencentcloudapi.woa.com/document/product/248/92447)
* [DescribeAIWorkbenchExecution](http://document.tencentcloudapi.woa.com/document/product/248/92446)
* [DescribeAIWorkbenchSession](http://document.tencentcloudapi.woa.com/document/product/248/92445)
* [DescribeAIWorkbenchSkill](http://document.tencentcloudapi.woa.com/document/product/248/92444)
* [GetAIWorkbenchArtifactDownloadURL](http://document.tencentcloudapi.woa.com/document/product/248/92443)
* [ListAIWorkbenchAgents](http://document.tencentcloudapi.woa.com/document/product/248/92442)
* [ListAIWorkbenchArtifacts](http://document.tencentcloudapi.woa.com/document/product/248/92441)
* [ListAIWorkbenchExecutions](http://document.tencentcloudapi.woa.com/document/product/248/92440)
* [ListAIWorkbenchMCPs](http://document.tencentcloudapi.woa.com/document/product/248/92439)
* [ListAIWorkbenchMessages](http://document.tencentcloudapi.woa.com/document/product/248/92438)
* [ListAIWorkbenchResourceInstances](http://document.tencentcloudapi.woa.com/document/product/248/92437)
* [ListAIWorkbenchResourceMaps](http://document.tencentcloudapi.woa.com/document/product/248/92436)
* [ListAIWorkbenchSessions](http://document.tencentcloudapi.woa.com/document/product/248/92435)
* [ListAIWorkbenchSkills](http://document.tencentcloudapi.woa.com/document/product/248/92434)
* [ListAIWorkbenchTasks](http://document.tencentcloudapi.woa.com/document/product/248/92433)
* [TriggerAIWorkbenchTask](http://document.tencentcloudapi.woa.com/document/product/248/92432)
* [UpdateAIWorkbenchAgent](http://document.tencentcloudapi.woa.com/document/product/248/92431)

新增数据结构：

* [AgentInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#AgentInfo)
* [ArtifactInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#ArtifactInfo)
* [ContentBlockInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#ContentBlockInfo)
* [EnvEntry](http://document.tencentcloudapi.woa.com/document/product/248/81423#EnvEntry)
* [EnvVar](http://document.tencentcloudapi.woa.com/document/product/248/81423#EnvVar)
* [ExecutionInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#ExecutionInfo)
* [InstructionConfig](http://document.tencentcloudapi.woa.com/document/product/248/81423#InstructionConfig)
* [MCPInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#MCPInfo)
* [MessageInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#MessageInfo)
* [PageByNumParams](http://document.tencentcloudapi.woa.com/document/product/248/81423#PageByNumParams)
* [PageByNumResult](http://document.tencentcloudapi.woa.com/document/product/248/81423#PageByNumResult)
* [ResourceInstance](http://document.tencentcloudapi.woa.com/document/product/248/81423#ResourceInstance)
* [ResourceMapInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#ResourceMapInfo)
* [SessionInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#SessionInfo)
* [SkillInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#SkillInfo)
* [Tag](http://document.tencentcloudapi.woa.com/document/product/248/81423#Tag)
* [TaskInfo](http://document.tencentcloudapi.woa.com/document/product/248/81423#TaskInfo)



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 136 次发布

发布时间：2026-08-26 02:26:28

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAlarmHistoryShield](http://document.tencentcloudapi.woa.com/document/product/248/92430)
* [DeleteAlarmHistoryShields](http://document.tencentcloudapi.woa.com/document/product/248/92429)
* [DescribeAlarmHistoryShield](http://document.tencentcloudapi.woa.com/document/product/248/92428)
* [ModifyAlarmHistoryShield](http://document.tencentcloudapi.woa.com/document/product/248/92427)

修改数据结构：

* [PrometheusClusterAgentBasic](http://document.tencentcloudapi.woa.com/document/product/248/30354#PrometheusClusterAgentBasic)

	* 新增成员：CollectAll




## 配额中心(quota) 版本：2024-12-04

### 第 2 次发布

发布时间：2026-08-26 02:36:53

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeAggregateUserQuotas](http://document.tencentcloudapi.woa.com/document/product/1803/91628)

	* 新增入参：QuotaName




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 154 次发布

发布时间：2026-08-26 02:54:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/90327)

	* 新增入参：ResourceMode


新增数据结构：

* [TideInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#TideInfo)
* [TideInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/851/74915#TideInstanceSpec)

修改数据结构：

* [ResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroup)

	* 新增成员：ResourceMode, TideInfo

* [WorkspaceBriefInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#WorkspaceBriefInfo)

	* <font color="#dd0000">**修改成员**：</font>TiProjectId, TiProjectName




## TI-ONE 训练平台(tione) 版本：2019-10-22



## TSF-Polaris&ZK&网关(tse) 版本：2020-12-07

### 第 110 次发布

发布时间：2026-08-26 03:00:32

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeCloudNativeAPIGatewayLatestTaskPhases](http://document.tencentcloudapi.woa.com/document/product/1364/81721)

	* 新增出参：EstimatedTotalCostSeconds, ActualTotalCostSeconds




