# Release 3.0.1394.1

## 文件存储(cfs) 版本：2019-07-19

### 第 41 次发布

发布时间：2026-04-01 01:19:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCfsFileSystem](http://document.tencentcloudapi.woa.com/document/product/582/38174)

	* 新增入参：Encrypted




## 日志服务(cls) 版本：2020-10-16

### 第 143 次发布

发布时间：2026-04-01 01:22:48

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateShipper](http://document.tencentcloudapi.woa.com/document/product/614/58747)

	* 新增入参：TimeZone, DSLFilter

* [ModifyShipper](http://document.tencentcloudapi.woa.com/document/product/614/58743)

	* 新增入参：TimeZone, DSLFilter

* [SearchLog](http://document.tencentcloudapi.woa.com/document/product/614/56447)

	* 新增入参：QueryString, QuerySyntax

	* <font color="#dd0000">**修改入参**：</font>Query


修改数据结构：

* [ShipperInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#ShipperInfo)

	* 新增成员：TimeZone, DSLFilter




## Elasticsearch Service(es) 版本：2018-04-16

### 第 104 次发布

发布时间：2026-04-01 01:40:04

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UpdateLogstashInstance](http://document.tencentcloudapi.woa.com/document/product/845/75141)

	* 新增入参：UserDnsIp


修改数据结构：

* [LogstashInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/845/30634#LogstashInstanceInfo)

	* 新增成员：UserDnsIp




## 人脸核身(faceid) 版本：2018-03-01

### 第 94 次发布

发布时间：2026-04-01 01:41:58

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [WebVerificationConfigIntl](http://document.tencentcloudapi.woa.com/document/product/1007/41958#WebVerificationConfigIntl)

	* 新增成员：Version




## 智能导诊(ig) 版本：2021-05-18

### 第 4 次发布

发布时间：2026-04-01 01:47:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetLLMDiagnosisDrug](http://document.tencentcloudapi.woa.com/document/product/1779/88801)

	* 新增入参：Prompt

* [GetLLMDiagnosisDrugChat](http://document.tencentcloudapi.woa.com/document/product/1779/88808)

	* 新增入参：Prompt

* [GetLLMReportInterpretation](http://document.tencentcloudapi.woa.com/document/product/1779/88806)

	* 新增入参：Prompt, QaPrompt




## 设备安全(tds) 版本：2022-08-01

### 第 6 次发布

发布时间：2026-04-01 02:17:25

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeFinanceFraudUltimate](http://document.tencentcloudapi.woa.com/document/product/1719/86697)

	* 新增出参：RiskCheckTimestamp, ExtraInfos

* [DescribeFraudUltimate](http://document.tencentcloudapi.woa.com/document/product/1719/80585)

	* 新增出参：RiskCheckTimestamp, ExtraInfos




## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 118 次发布

发布时间：2026-04-01 02:21:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetMostSuitableImageCache](http://document.tencentcloudapi.woa.com/document/product/457/70858)

	* 新增入参：Snapshotter


修改数据结构：

* [ImageCache](http://document.tencentcloudapi.woa.com/document/product/457/31866#ImageCache)

	* 新增成员：ImageCacheType, Snapshotter




## 私有网络(vpc) 版本：2017-03-12

### 第 245 次发布

发布时间：2026-04-01 02:27:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateHaVip](http://document.tencentcloudapi.woa.com/document/product/215/30652)

	* 新增入参：TerminationProtection, TrafficProtection


修改数据结构：

* [HaVip](http://document.tencentcloudapi.woa.com/document/product/215/15824#HaVip)

	* 新增成员：TerminationProtection, TrafficProtection

* [TrafficMirror](http://document.tencentcloudapi.woa.com/document/product/215/15824#TrafficMirror)

	* 新增成员：IngressFilterRules, EgressFilterRules

* [TrafficMirrorFilter](http://document.tencentcloudapi.woa.com/document/product/215/15824#TrafficMirrorFilter)

	* 新增成员：TrafficMirrorFilterRuleId, Priority, Action, Description, CreatedTime

	* <font color="#dd0000">**修改成员**：</font>SrcNet, DstNet, Protocol




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 2 次发布

发布时间：2026-04-01 02:32:19

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/89335)
* [CreateIntegrationNode](http://document.tencentcloudapi.woa.com/document/product/1607/89310)
* [CreateIntegrationTask](http://document.tencentcloudapi.woa.com/document/product/1607/89309)
* [CreateIntegrationTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89308)
* [CreateWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/89318)
* [CreateWorkflowExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89291)
* [DrawWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/89317)
* [GetCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/89334)
* [GetCodeFileVersion](http://document.tencentcloudapi.woa.com/document/product/1607/89333)
* [GetCodeWorkspace](http://document.tencentcloudapi.woa.com/document/product/1607/89332)
* [GetCodeWorkspaceNetworkInfo](http://document.tencentcloudapi.woa.com/document/product/1607/89331)
* [GetIntegrationNode](http://document.tencentcloudapi.woa.com/document/product/1607/89307)
* [GetIntegrationTask](http://document.tencentcloudapi.woa.com/document/product/1607/89306)
* [GetIntegrationTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89305)
* [GetJobLog](http://document.tencentcloudapi.woa.com/document/product/1607/89324)
* [GetTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89290)
* [GetWorkflowExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89289)
* [GetWorkflowTask](http://document.tencentcloudapi.woa.com/document/product/1607/89316)
* [GetWorkflowTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89288)
* [KillTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89287)
* [KillWorkflowExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89286)
* [ListCatalogs](http://document.tencentcloudapi.woa.com/document/product/1607/89294)
* [ListCodeFileJobs](http://document.tencentcloudapi.woa.com/document/product/1607/89330)
* [ListCodeFileVersions](http://document.tencentcloudapi.woa.com/document/product/1607/89329)
* [ListComputeResources](http://document.tencentcloudapi.woa.com/document/product/1607/89323)
* [ListConnectionTypes](http://document.tencentcloudapi.woa.com/document/product/1607/89322)
* [ListConnections](http://document.tencentcloudapi.woa.com/document/product/1607/89321)
* [ListDataTypes](http://document.tencentcloudapi.woa.com/document/product/1607/89304)
* [ListDatabasesPage](http://document.tencentcloudapi.woa.com/document/product/1607/89303)
* [ListIntegrationTasks](http://document.tencentcloudapi.woa.com/document/product/1607/89302)
* [ListSchemasPage](http://document.tencentcloudapi.woa.com/document/product/1607/89301)
* [ListTablesPage](http://document.tencentcloudapi.woa.com/document/product/1607/89300)
* [ListTaskExecutions](http://document.tencentcloudapi.woa.com/document/product/1607/89285)
* [ListWorkflowExecutions](http://document.tencentcloudapi.woa.com/document/product/1607/89284)
* [ListWorkflowTaskTypes](http://document.tencentcloudapi.woa.com/document/product/1607/89315)
* [ListWorkflowTasks](http://document.tencentcloudapi.woa.com/document/product/1607/89314)
* [ListWorkflows](http://document.tencentcloudapi.woa.com/document/product/1607/89313)
* [ReleaseCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/89328)
* [RerunTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89283)
* [RerunWorkflowExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89282)
* [RunWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/89281)
* [SearchAsset](http://document.tencentcloudapi.woa.com/document/product/1607/89293)
* [StartCodeWorkspace](http://document.tencentcloudapi.woa.com/document/product/1607/89327)
* [StopTaskExecutions](http://document.tencentcloudapi.woa.com/document/product/1607/89280)
* [StopWorkflowExecution](http://document.tencentcloudapi.woa.com/document/product/1607/89279)
* [SubmitCodeFileJob](http://document.tencentcloudapi.woa.com/document/product/1607/89326)
* [TestConnection](http://document.tencentcloudapi.woa.com/document/product/1607/89320)
* [UpdateIntegrationNode](http://document.tencentcloudapi.woa.com/document/product/1607/89299)
* [UpdateIntegrationTask](http://document.tencentcloudapi.woa.com/document/product/1607/89298)
* [UpdateWorkflow](http://document.tencentcloudapi.woa.com/document/product/1607/89312)
* [UploadFilesAndPreview](http://document.tencentcloudapi.woa.com/document/product/1607/89297)
* [VerifyIntegrationTask](http://document.tencentcloudapi.woa.com/document/product/1607/89296)

新增数据结构：

* [AlarmBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#AlarmBrief)
* [AlarmGroup](http://document.tencentcloudapi.woa.com/document/product/1607/88970#AlarmGroup)
* [AsyncActionRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#AsyncActionRsp)
* [Audit](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Audit)
* [Catalog](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Catalog)
* [CodeFileConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileConfig)
* [CodeFileJobInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileJobInfo)
* [CodeFileRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileRsp)
* [CodeFileStorage](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileStorage)
* [CodeFileVersion](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileVersion)
* [CodeFileVersions](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileVersions)
* [CodeWorkspace](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspace)
* [CodeWorkspaceClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspaceClusterInfo)
* [CodeWorkspaceEnvConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspaceEnvConfig)
* [CodeWorkspaceImage](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspaceImage)
* [CodeWorkspaceNetworkInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspaceNetworkInfo)
* [CodeWorkspaceSpecificationInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeWorkspaceSpecificationInfo)
* [ConnectionFileCosInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ConnectionFileCosInfo)
* [ConnectionFileInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ConnectionFileInfo)
* [ConnectionInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ConnectionInfo)
* [ConnectionInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ConnectionInstanceInfo)
* [CreateIntegrationNodeRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateIntegrationNodeRsp)
* [CreateIntegrationTaskExecutionRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateIntegrationTaskExecutionRsp)
* [CreateIntegrationTaskRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateIntegrationTaskRsp)
* [CreateWorkflowRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateWorkflowRsp)
* [DatabaseInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#DatabaseInfo)
* [DatabaseSchemaInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#DatabaseSchemaInfo)
* [DatabaseTableInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#DatabaseTableInfo)
* [DependOnBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#DependOnBrief)
* [ExecAdminComputeResourceBasicInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceBasicInfo)
* [ExecAdminComputeResourceInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceInfo)
* [ExecEngineProxyProxyJobResultJumpInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecEngineProxyProxyJobResultJumpInfo)
* [ExecutionActionBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecutionActionBrief)
* [FieldDefinition](http://document.tencentcloudapi.woa.com/document/product/1607/88970#FieldDefinition)
* [FieldInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#FieldInfo)
* [FieldValue](http://document.tencentcloudapi.woa.com/document/product/1607/88970#FieldValue)
* [FileRowData](http://document.tencentcloudapi.woa.com/document/product/1607/88970#FileRowData)
* [Filter](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Filter)
* [Fragment](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Fragment)
* [GetIntegrationNodeRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetIntegrationNodeRsp)
* [GetIntegrationTaskExecutionRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetIntegrationTaskExecutionRsp)
* [GetIntegrationTaskRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetIntegrationTaskRsp)
* [GetJobLogRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetJobLogRsp)
* [GetStatusRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GetStatusRsp)
* [GitSandboxFolderConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#GitSandboxFolderConfig)
* [Highlighting](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Highlighting)
* [HighlightingInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#HighlightingInfo)
* [IntegrationNodeInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeInfo)
* [IntegrationNodeInfoBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeInfoBrief)
* [IntegrationNodeMapping](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeMapping)
* [IntegrationNodeMappingBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeMappingBrief)
* [IntegrationNodeSchema](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchema)
* [IntegrationNodeSchemaBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchemaBrief)
* [IntegrationNodeSchemaMapping](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchemaMapping)
* [IntegrationNodeSchemaMappingBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchemaMappingBrief)
* [IntegrationNodeSchemaNameMapping](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchemaNameMapping)
* [IntegrationNodeSchemaNameMappingGre](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationNodeSchemaNameMappingGre)
* [IntegrationTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationTaskInfo)
* [IntegrationTaskInfoBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#IntegrationTaskInfoBrief)
* [JobExecution](http://document.tencentcloudapi.woa.com/document/product/1607/88970#JobExecution)
* [KVPair](http://document.tencentcloudapi.woa.com/document/product/1607/88970#KVPair)
* [LabelBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#LabelBrief)
* [ListCatalogsRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListCatalogsRsp)
* [ListCodeFileJobsRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListCodeFileJobsRsp)
* [ListComputeResourcesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListComputeResourcesRsp)
* [ListConnectionTypesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListConnectionTypesRsp)
* [ListConnectionsRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListConnectionsRsp)
* [ListDataTypesRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListDataTypesRsp)
* [ListDatabasesPageRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListDatabasesPageRsp)
* [ListIntegrationTasksResult](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListIntegrationTasksResult)
* [ListOpsWorkflowResult](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListOpsWorkflowResult)
* [ListSchemasPageRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListSchemasPageRsp)
* [ListTablesPageRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListTablesPageRsp)
* [ListWorkflowInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListWorkflowInfo)
* [ListWorkflowTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListWorkflowTaskInfo)
* [ListWorkflowTaskTypeRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ListWorkflowTaskTypeRsp)
* [MetaOwner](http://document.tencentcloudapi.woa.com/document/product/1607/88970#MetaOwner)
* [MonitorMetricBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#MonitorMetricBrief)
* [MonitorMetricItem](http://document.tencentcloudapi.woa.com/document/product/1607/88970#MonitorMetricItem)
* [OrderField](http://document.tencentcloudapi.woa.com/document/product/1607/88970#OrderField)
* [Owner](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Owner)
* [PageReq](http://document.tencentcloudapi.woa.com/document/product/1607/88970#PageReq)
* [PageRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#PageRsp)
* [ParamInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ParamInfo)
* [RecordField](http://document.tencentcloudapi.woa.com/document/product/1607/88970#RecordField)
* [ReleaseCodeFileRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ReleaseCodeFileRsp)
* [ScriptStorageConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ScriptStorageConfig)
* [SearchAssetRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SearchAssetRsp)
* [SearchResult](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SearchResult)
* [SortInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SortInfo)
* [TagInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TagInfo)
* [Task](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Task)
* [TaskBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskBrief)
* [TaskExecutionBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskExecutionBrief)
* [TaskExecutionPage](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskExecutionPage)
* [TaskRetryStrategy](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskRetryStrategy)
* [TaskSchedulingParameter](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskSchedulingParameter)
* [TaskType](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskType)
* [TaskTypeNotebookExt](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskTypeNotebookExt)
* [TaskTypeProperty](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TaskTypeProperty)
* [TestConnectionRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TestConnectionRsp)
* [TriggerAdvancedConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TriggerAdvancedConfig)
* [TypeInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#TypeInfo)
* [UpdateIntegrationNodeRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdateIntegrationNodeRsp)
* [UpdateIntegrationTaskRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdateIntegrationTaskRsp)
* [UpdateWorkflowRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdateWorkflowRsp)
* [UploadFile](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UploadFile)
* [UploadFilesAndPreviewRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UploadFilesAndPreviewRsp)
* [UserActivityInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UserActivityInfo)
* [UserInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UserInfo)
* [VerifyIntegrationTaskRsp](http://document.tencentcloudapi.woa.com/document/product/1607/88970#VerifyIntegrationTaskRsp)
* [Workflow](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Workflow)
* [WorkflowAdvanceConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowAdvanceConfig)
* [WorkflowBaseInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowBaseInfo)
* [WorkflowCanvas](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowCanvas)
* [WorkflowCanvasBaseInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowCanvasBaseInfo)
* [WorkflowDrawResourceGroup](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowDrawResourceGroup)
* [WorkflowExecutionBizEnumBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowExecutionBizEnumBrief)
* [WorkflowExecutionBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowExecutionBrief)
* [WorkflowInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowInfo)
* [WorkflowListResourceGroupInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowListResourceGroupInfo)
* [WorkflowRunInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowRunInfo)
* [WorkflowTaskBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowTaskBrief)
* [WorkflowTaskExecution](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowTaskExecution)
* [WorkflowTaskType](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowTaskType)
* [WorkflowTriggerConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkflowTriggerConfig)
* [WorkspaceGitConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#WorkspaceGitConfig)



## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



