# Release 3.0.1277.1

## 运维安全中心（堡垒机）(bh) 版本：2023-04-18

### 第 20 次发布

发布时间：2025-09-23 01:08:50

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeAcls](http://document.tencentcloudapi.woa.com/document/product/1780/85293)

	* 新增入参：StatusSet

* [DescribeCmdTemplates](http://document.tencentcloudapi.woa.com/document/product/1780/85292)

	* 新增入参：TypeSet

* [DescribeDevices](http://document.tencentcloudapi.woa.com/document/product/1780/85260)

	* 新增入参：AccountIdSet, ProviderTypeSet, CloudDeviceStatusSet

* [DescribeLoginEvent](http://document.tencentcloudapi.woa.com/document/product/1780/85300)

	* 新增入参：EntrySet, ResultSet

* [DescribeOperationEvent](http://document.tencentcloudapi.woa.com/document/product/1780/85299)

	* 新增入参：KindSet, ResultSet

* [ImportExternalDevice](http://document.tencentcloudapi.woa.com/document/product/1780/85259)

	* 新增入参：AccountId

* [SearchFileBySid](http://document.tencentcloudapi.woa.com/document/product/1780/85310)

	* 新增入参：AuditActionSet

* [SearchSession](http://document.tencentcloudapi.woa.com/document/product/1780/85309)

	* 新增入参：StatusSet, DeviceKindSet


修改数据结构：

* [Device](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Device)

	* 新增成员：ApName, CloudAccountId, CloudAccountName, ProviderType, ProviderName, SyncCloudDeviceStatus

* [ExternalDevice](http://document.tencentcloudapi.woa.com/document/product/1780/85236#ExternalDevice)

	* 新增成员：InstanceId, ApCode, ApName, VpcId, SubnetId, PublicIp

* [Resource](http://document.tencentcloudapi.woa.com/document/product/1780/85236#Resource)

	* 新增成员：DomainName




## 费用中心(billing) 版本：2018-07-09

### 第 100 次发布

发布时间：2025-09-23 01:09:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateBudget](http://document.tencentcloudapi.woa.com/document/product/555/87723)
* [DeleteBudget](http://document.tencentcloudapi.woa.com/document/product/555/87722)
* [DescribeBudget](http://document.tencentcloudapi.woa.com/document/product/555/87721)
* [DescribeBudgetOperationLog](http://document.tencentcloudapi.woa.com/document/product/555/87720)
* [ModifyBudget](http://document.tencentcloudapi.woa.com/document/product/555/87719)

新增数据结构：

* [BudgetExtend](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetExtend)
* [BudgetInfoApiResponse](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetInfoApiResponse)
* [BudgetInfoDiffEntity](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetInfoDiffEntity)
* [BudgetOperationLogEntity](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetOperationLogEntity)
* [BudgetSendInfoDto](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetSendInfoDto)
* [BudgetWarn](http://document.tencentcloudapi.woa.com/document/product/555/19183#BudgetWarn)
* [DataForBudgetInfoPage](http://document.tencentcloudapi.woa.com/document/product/555/19183#DataForBudgetInfoPage)
* [DataForBudgetOperationLogPage](http://document.tencentcloudapi.woa.com/document/product/555/19183#DataForBudgetOperationLogPage)
* [WaveThresholdForm](http://document.tencentcloudapi.woa.com/document/product/555/19183#WaveThresholdForm)



## 人脸核身(faceid) 版本：2018-03-01

### 第 87 次发布

发布时间：2025-09-23 01:18:24

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ApplySdkVerificationToken](http://document.tencentcloudapi.woa.com/document/product/1007/76415)

	* 新增入参：SelectedWarningCodes




## 多网聚合加速(mna) 版本：2021-01-19

### 第 29 次发布

发布时间：2025-09-23 01:22:48

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetFlowStatisticByGroup](http://document.tencentcloudapi.woa.com/document/product/1385/84019)

	* 新增入参：MpApplicationId




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 103 次发布

发布时间：2025-09-23 01:31:16

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Instance](http://document.tencentcloudapi.woa.com/document/product/851/74915#Instance)

	* 新增成员：IsReturnToHotBackup

* [ResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroup)

	* 新增成员：Supervisors




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 数据开发治理平台 WeData(wedata) 版本：2025-08-06

### 第 2 次发布

发布时间：2025-09-23 01:33:28

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/87773)
* [CreateCodeFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87772)
* [CreateDataBackfillPlan](http://document.tencentcloudapi.woa.com/document/product/1607/87753)
* [CreateOpsAlarmRule](http://document.tencentcloudapi.woa.com/document/product/1607/87752)
* [CreateSQLFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87771)
* [CreateSQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87770)
* [DeleteCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/87769)
* [DeleteCodeFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87768)
* [DeleteOpsAlarmRule](http://document.tencentcloudapi.woa.com/document/product/1607/87751)
* [DeleteSQLFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87767)
* [DeleteSQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87766)
* [GetAlarmMessage](http://document.tencentcloudapi.woa.com/document/product/1607/87750)
* [GetCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/87765)
* [GetOpsAlarmRule](http://document.tencentcloudapi.woa.com/document/product/1607/87749)
* [GetOpsAsyncJob](http://document.tencentcloudapi.woa.com/document/product/1607/87748)
* [GetOpsTask](http://document.tencentcloudapi.woa.com/document/product/1607/87747)
* [GetOpsTaskCode](http://document.tencentcloudapi.woa.com/document/product/1607/87746)
* [GetOpsWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/87745)
* [GetSQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87764)
* [GetTaskInstance](http://document.tencentcloudapi.woa.com/document/product/1607/87744)
* [GetTaskInstanceLog](http://document.tencentcloudapi.woa.com/document/product/1607/87743)
* [KillTaskInstancesAsync](http://document.tencentcloudapi.woa.com/document/product/1607/87742)
* [ListAlarmMessages](http://document.tencentcloudapi.woa.com/document/product/1607/87741)
* [ListCodeFolderContents](http://document.tencentcloudapi.woa.com/document/product/1607/87763)
* [ListDataBackfillInstances](http://document.tencentcloudapi.woa.com/document/product/1607/87740)
* [ListDownstreamOpsTasks](http://document.tencentcloudapi.woa.com/document/product/1607/87739)
* [ListDownstreamTaskInstances](http://document.tencentcloudapi.woa.com/document/product/1607/87738)
* [ListOpsAlarmRules](http://document.tencentcloudapi.woa.com/document/product/1607/87737)
* [ListOpsTasks](http://document.tencentcloudapi.woa.com/document/product/1607/87736)
* [ListOpsWorkflows](http://document.tencentcloudapi.woa.com/document/product/1607/87735)
* [ListSQLFolderContents](http://document.tencentcloudapi.woa.com/document/product/1607/87762)
* [ListSQLScriptRuns](http://document.tencentcloudapi.woa.com/document/product/1607/87761)
* [ListTaskInstanceExecutions](http://document.tencentcloudapi.woa.com/document/product/1607/87734)
* [ListTaskInstances](http://document.tencentcloudapi.woa.com/document/product/1607/87733)
* [ListUpstreamOpsTasks](http://document.tencentcloudapi.woa.com/document/product/1607/87732)
* [ListUpstreamTaskInstances](http://document.tencentcloudapi.woa.com/document/product/1607/87731)
* [PauseOpsTasksAsync](http://document.tencentcloudapi.woa.com/document/product/1607/87730)
* [RerunTaskInstancesAsync](http://document.tencentcloudapi.woa.com/document/product/1607/87729)
* [RunSQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87760)
* [SetSuccessTaskInstancesAsync](http://document.tencentcloudapi.woa.com/document/product/1607/87728)
* [StopOpsTasksAsync](http://document.tencentcloudapi.woa.com/document/product/1607/87727)
* [StopSQLScriptRun](http://document.tencentcloudapi.woa.com/document/product/1607/87759)
* [UpdateCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/87758)
* [UpdateCodeFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87757)
* [UpdateOpsAlarmRule](http://document.tencentcloudapi.woa.com/document/product/1607/87726)
* [UpdateOpsTasksOwner](http://document.tencentcloudapi.woa.com/document/product/1607/87725)
* [UpdateSQLFolder](http://document.tencentcloudapi.woa.com/document/product/1607/87756)
* [UpdateSQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87755)

新增数据结构：

* [AlarmGroup](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmGroup)
* [AlarmMessage](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmMessage)
* [AlarmQuietInterval](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmQuietInterval)
* [AlarmRuleData](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmRuleData)
* [AlarmRuleDetail](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmRuleDetail)
* [AlarmWayWebHook](http://document.tencentcloudapi.woa.com/document/product/1607/87707#AlarmWayWebHook)
* [BackfillInstance](http://document.tencentcloudapi.woa.com/document/product/1607/87707#BackfillInstance)
* [BackfillInstanceCollection](http://document.tencentcloudapi.woa.com/document/product/1607/87707#BackfillInstanceCollection)
* [ChildDependencyConfigPage](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ChildDependencyConfigPage)
* [CodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeFile)
* [CodeFileConfig](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeFileConfig)
* [CodeFolderNode](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeFolderNode)
* [CodeStudioFileActionResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeStudioFileActionResult)
* [CodeStudioFolderActionResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeStudioFolderActionResult)
* [CodeStudioFolderResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CodeStudioFolderResult)
* [CreateAlarmRuleData](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CreateAlarmRuleData)
* [CreateDataReplenishmentPlan](http://document.tencentcloudapi.woa.com/document/product/1607/87707#CreateDataReplenishmentPlan)
* [DataBackfillRange](http://document.tencentcloudapi.woa.com/document/product/1607/87707#DataBackfillRange)
* [DeleteAlarmRuleResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#DeleteAlarmRuleResult)
* [InstanceExecution](http://document.tencentcloudapi.woa.com/document/product/1607/87707#InstanceExecution)
* [InstanceExecutionPhase](http://document.tencentcloudapi.woa.com/document/product/1607/87707#InstanceExecutionPhase)
* [InstanceLog](http://document.tencentcloudapi.woa.com/document/product/1607/87707#InstanceLog)
* [JobDto](http://document.tencentcloudapi.woa.com/document/product/1607/87707#JobDto)
* [JobExecutionDto](http://document.tencentcloudapi.woa.com/document/product/1607/87707#JobExecutionDto)
* [KVMap](http://document.tencentcloudapi.woa.com/document/product/1607/87707#KVMap)
* [KVPair](http://document.tencentcloudapi.woa.com/document/product/1607/87707#KVPair)
* [ListAlarmMessages](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ListAlarmMessages)
* [ListAlarmRulesResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ListAlarmRulesResult)
* [ListOpsTasksPage](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ListOpsTasksPage)
* [ModifyAlarmRuleResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ModifyAlarmRuleResult)
* [NotebookSessionInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#NotebookSessionInfo)
* [NotificationFatigue](http://document.tencentcloudapi.woa.com/document/product/1607/87707#NotificationFatigue)
* [OpsAsyncJobDetail](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsAsyncJobDetail)
* [OpsAsyncResponse](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsAsyncResponse)
* [OpsTaskDepend](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsTaskDepend)
* [OpsWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsWorkflow)
* [OpsWorkflowDetail](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsWorkflowDetail)
* [OpsWorkflows](http://document.tencentcloudapi.woa.com/document/product/1607/87707#OpsWorkflows)
* [ParentDependencyConfigPage](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ParentDependencyConfigPage)
* [ProjectInstanceStatisticsAlarmInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ProjectInstanceStatisticsAlarmInfo)
* [ReconciliationStrategyInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#ReconciliationStrategyInfo)
* [SQLContentActionResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SQLContentActionResult)
* [SQLFolderNode](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SQLFolderNode)
* [SQLScript](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SQLScript)
* [SQLScriptConfig](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SQLScriptConfig)
* [SQLStopResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SQLStopResult)
* [SqlCreateResult](http://document.tencentcloudapi.woa.com/document/product/1607/87707#SqlCreateResult)
* [TaskCode](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskCode)
* [TaskInstance](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskInstance)
* [TaskInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskInstanceDetail)
* [TaskInstanceExecutions](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskInstanceExecutions)
* [TaskInstancePage](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskInstancePage)
* [TaskOpsInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TaskOpsInfo)
* [TimeOutStrategyInfo](http://document.tencentcloudapi.woa.com/document/product/1607/87707#TimeOutStrategyInfo)
* [UpdateTasksOwner](http://document.tencentcloudapi.woa.com/document/product/1607/87707#UpdateTasksOwner)



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



