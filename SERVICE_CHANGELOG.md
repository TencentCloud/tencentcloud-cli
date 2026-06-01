# Release 3.0.1436.1

## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 19 次发布

发布时间：2026-06-02 01:11:19

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAgentApp](http://document.tencentcloudapi.woa.com/document/product/1805/87895)

	* 新增入参：ConnectorIDs

* [ModifyAgentApp](http://document.tencentcloudapi.woa.com/document/product/1805/87885)

	* 新增入参：ConnectorIDs


修改数据结构：

* [DescribeAgentAppResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAgentAppResp)

	* 新增成员：ConnectorIDs, ServicesNum

* [DescribeAgentCredentialResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAgentCredentialResp)

	* 新增成员：RelateServiceNum




## 弹性伸缩(as) 版本：2018-04-19

### 第 57 次发布

发布时间：2026-06-02 01:12:23

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ServiceSettings](http://document.tencentcloudapi.woa.com/document/product/377/20453#ServiceSettings)

	* 新增成员：DisableVnc




## 文件存储(cfs) 版本：2019-07-19

### 第 44 次发布

发布时间：2026-06-02 01:22:59

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDataRetrieval](http://document.tencentcloudapi.woa.com/document/product/582/90491)
* [DeleteDataRetrieval](http://document.tencentcloudapi.woa.com/document/product/582/90490)
* [DescribeDataRetrieval](http://document.tencentcloudapi.woa.com/document/product/582/90489)
* [DescribeDataRetrievalTask](http://document.tencentcloudapi.woa.com/document/product/582/90488)
* [ModifyDataRetrieval](http://document.tencentcloudapi.woa.com/document/product/582/90487)
* [RunDataRetrievalTask](http://document.tencentcloudapi.woa.com/document/product/582/90486)

新增数据结构：

* [DataRetrievalInfo](http://document.tencentcloudapi.woa.com/document/product/582/38175#DataRetrievalInfo)
* [DataRetrievalTaskInfo](http://document.tencentcloudapi.woa.com/document/product/582/38175#DataRetrievalTaskInfo)



## 日志服务(cls) 版本：2020-10-16

### 第 151 次发布

发布时间：2026-06-02 01:27:05

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AccessControlRule](http://document.tencentcloudapi.woa.com/document/product/614/56471#AccessControlRule)

	* 新增成员：CidrBlocks, Action




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 18 次发布

发布时间：2026-06-02 01:31:01

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCustomer](http://document.tencentcloudapi.woa.com/document/product/1792/87469)

	* 新增入参：PortScanQps, SingleIPTaskLimit, HighRiskAck, ScanRateAckChecklist

* [CreateJobRecord](http://document.tencentcloudapi.woa.com/document/product/1792/87474)

	* 新增入参：PortScanQps, SingleIPTaskLimit, HighRiskAck, ScanRateAckChecklist

* [ModifyCustomer](http://document.tencentcloudapi.woa.com/document/product/1792/87463)

	* 新增入参：PortScanQps, SingleIPTaskLimit, HighRiskAck, ScanRateAckChecklist


修改数据结构：

* [Customer](http://document.tencentcloudapi.woa.com/document/product/1792/87475#Customer)

	* 新增成员：SingleIPTaskLimit, PortScanQps

* [DisplayApiSec](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayApiSec)

	* 新增成员：AggregationCount

* [DisplayConfig](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayConfig)

	* 新增成员：AggregationCount

* [DisplayHttp](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayHttp)

	* 新增成员：AggregationCount

* [DisplayManage](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayManage)

	* 新增成员：AggregationCount

* [DisplayPort](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayPort)

	* 新增成员：AggregationCount

* [DisplaySensitiveInfo](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplaySensitiveInfo)

	* 新增成员：AggregationCount

* [DisplaySubDomain](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplaySubDomain)

	* 新增成员：AggregationCount

* [DisplaySuspiciousAsset](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplaySuspiciousAsset)

	* 新增成员：AggregationCount




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 48 次发布

发布时间：2026-06-02 02:17:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBillingInfo](http://document.tencentcloudapi.woa.com/document/product/876/89197)

	* 新增入参：EnvIds, Limit, Offset

	* 新增出参：Total




## 云托管 CloudBase Run(tcbr) 版本：2022-02-17

### 第 21 次发布

发布时间：2026-06-02 02:18:01

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [PublicNetConf](http://document.tencentcloudapi.woa.com/document/product/1711/80400#PublicNetConf)

修改数据结构：

* [DiffConfigItem](http://document.tencentcloudapi.woa.com/document/product/1711/80400#DiffConfigItem)

	* 新增成员：PublicNetConf

* [ServerBaseConfig](http://document.tencentcloudapi.woa.com/document/product/1711/80400#ServerBaseConfig)

	* 新增成员：PublicNetConf




## 腾讯云数据仓库TCHouse-X(tchousex) 版本：2023-04-11

### 第 14 次发布

发布时间：2026-06-02 02:19:18

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90550)
* [AuthorizedSql](http://document.tencentcloudapi.woa.com/document/product/1741/90593)
* [CancelCreateInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90549)
* [CancelSqlExecute](http://document.tencentcloudapi.woa.com/document/product/1741/90592)
* [CreateAutoScalePlan](http://document.tencentcloudapi.woa.com/document/product/1741/90548)
* [CreateDatabase](http://document.tencentcloudapi.woa.com/document/product/1741/90629)
* [CreateElasticPlan](http://document.tencentcloudapi.woa.com/document/product/1741/90547)
* [CreateElasticPlanV1](http://document.tencentcloudapi.woa.com/document/product/1741/90546)
* [CreateEngineJob](http://document.tencentcloudapi.woa.com/document/product/1741/90628)
* [CreateFunction](http://document.tencentcloudapi.woa.com/document/product/1741/90627)
* [CreateInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90545)
* [CreateKerberos](http://document.tencentcloudapi.woa.com/document/product/1741/90544)
* [CreateMCPInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90634)
* [CreateNotebookSession](http://document.tencentcloudapi.woa.com/document/product/1741/90626)
* [CreateNotebookSessionStatement](http://document.tencentcloudapi.woa.com/document/product/1741/90625)
* [CreatePartition](http://document.tencentcloudapi.woa.com/document/product/1741/90624)
* [CreateRegularPlan](http://document.tencentcloudapi.woa.com/document/product/1741/90543)
* [CreateRegularPlanV1](http://document.tencentcloudapi.woa.com/document/product/1741/90542)
* [CreateSparkDownloadLog](http://document.tencentcloudapi.woa.com/document/product/1741/90541)
* [CreateTable](http://document.tencentcloudapi.woa.com/document/product/1741/90623)
* [CreateUpdateWarehouseSparkSetting](http://document.tencentcloudapi.woa.com/document/product/1741/90540)
* [CreateVirtualCluster](http://document.tencentcloudapi.woa.com/document/product/1741/90539)
* [DeleteAutoScalePlan](http://document.tencentcloudapi.woa.com/document/product/1741/90538)
* [DeleteElasticPlan](http://document.tencentcloudapi.woa.com/document/product/1741/90537)
* [DeleteElasticPlanV1](http://document.tencentcloudapi.woa.com/document/product/1741/90536)
* [DeleteEngineJob](http://document.tencentcloudapi.woa.com/document/product/1741/90622)
* [DeleteNotebookSession](http://document.tencentcloudapi.woa.com/document/product/1741/90621)
* [DeleteRegularPlan](http://document.tencentcloudapi.woa.com/document/product/1741/90535)
* [DeleteRegularPlanV1](http://document.tencentcloudapi.woa.com/document/product/1741/90534)
* [DeleteSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90533)
* [DeleteSparkTask](http://document.tencentcloudapi.woa.com/document/product/1741/90591)
* [DeleteUserConfig](http://document.tencentcloudapi.woa.com/document/product/1741/90532)
* [DeleteVirtualCluster](http://document.tencentcloudapi.woa.com/document/product/1741/90531)
* [DescribeAccessVipList](http://document.tencentcloudapi.woa.com/document/product/1741/90590)
* [DescribeCLSConfig](http://document.tencentcloudapi.woa.com/document/product/1741/90530)
* [DescribeCLSConfigHistory](http://document.tencentcloudapi.woa.com/document/product/1741/90529)
* [DescribeCkSql](http://document.tencentcloudapi.woa.com/document/product/1741/90528)
* [DescribeDatabaseByName](http://document.tencentcloudapi.woa.com/document/product/1741/90620)
* [DescribeDatabaseList](http://document.tencentcloudapi.woa.com/document/product/1741/90619)
* [DescribeEngineClusterState](http://document.tencentcloudapi.woa.com/document/product/1741/90618)
* [DescribeEngineEncryptMess](http://document.tencentcloudapi.woa.com/document/product/1741/90617)
* [DescribeEngineExtParams](http://document.tencentcloudapi.woa.com/document/product/1741/90616)
* [DescribeEngineInstances](http://document.tencentcloudapi.woa.com/document/product/1741/90615)
* [DescribeEngineJobInfo](http://document.tencentcloudapi.woa.com/document/product/1741/90614)
* [DescribeEngineJobLog](http://document.tencentcloudapi.woa.com/document/product/1741/90613)
* [DescribeEngineJobResult](http://document.tencentcloudapi.woa.com/document/product/1741/90612)
* [DescribeEngineJobState](http://document.tencentcloudapi.woa.com/document/product/1741/90611)
* [DescribeEngineRegions](http://document.tencentcloudapi.woa.com/document/product/1741/90610)
* [DescribeEventList](http://document.tencentcloudapi.woa.com/document/product/1741/90609)
* [DescribeFrontEnd](http://document.tencentcloudapi.woa.com/document/product/1741/90589)
* [DescribeFunctionByName](http://document.tencentcloudapi.woa.com/document/product/1741/90608)
* [DescribeFunctionList](http://document.tencentcloudapi.woa.com/document/product/1741/90607)
* [DescribeGoodsDetail](http://document.tencentcloudapi.woa.com/document/product/1741/90588)
* [DescribeHistoryRecords](http://document.tencentcloudapi.woa.com/document/product/1741/90587)
* [DescribeImpalaAccreditNew](http://document.tencentcloudapi.woa.com/document/product/1741/90527)
* [DescribeImpalaObjectNew](http://document.tencentcloudapi.woa.com/document/product/1741/90526)
* [DescribeImpalaRoleNew](http://document.tencentcloudapi.woa.com/document/product/1741/90525)
* [DescribeImpalaSql](http://document.tencentcloudapi.woa.com/document/product/1741/90586)
* [DescribeImpalaUserNew](http://document.tencentcloudapi.woa.com/document/product/1741/90524)
* [DescribeInstanceConfigHistories](http://document.tencentcloudapi.woa.com/document/product/1741/90523)
* [DescribeInstanceConfigs](http://document.tencentcloudapi.woa.com/document/product/1741/90585)
* [DescribeInstanceForBarad](http://document.tencentcloudapi.woa.com/document/product/1741/90584)
* [DescribeInstanceOperations](http://document.tencentcloudapi.woa.com/document/product/1741/90583)
* [DescribeInstanceOperationsV1](http://document.tencentcloudapi.woa.com/document/product/1741/90582)
* [DescribeInstanceProfile](http://document.tencentcloudapi.woa.com/document/product/1741/90581)
* [DescribeInstanceResourceUsage](http://document.tencentcloudapi.woa.com/document/product/1741/90580)
* [DescribeInstanceVipList](http://document.tencentcloudapi.woa.com/document/product/1741/90579)
* [DescribeInstanceWarehouse](http://document.tencentcloudapi.woa.com/document/product/1741/90578)
* [DescribeInstances](http://document.tencentcloudapi.woa.com/document/product/1741/90577)
* [DescribeLDAPUsers](http://document.tencentcloudapi.woa.com/document/product/1741/90522)
* [DescribeMCPInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90633)
* [DescribeMCPRegionZone](http://document.tencentcloudapi.woa.com/document/product/1741/90576)
* [DescribeMetricSubscription](http://document.tencentcloudapi.woa.com/document/product/1741/90521)
* [DescribeMonitorData](http://document.tencentcloudapi.woa.com/document/product/1741/90575)
* [DescribeMrMetricFiles](http://document.tencentcloudapi.woa.com/document/product/1741/90520)
* [DescribeNextEventId](http://document.tencentcloudapi.woa.com/document/product/1741/90606)
* [DescribeNotebookSession](http://document.tencentcloudapi.woa.com/document/product/1741/90605)
* [DescribeNotebookSessionStatement](http://document.tencentcloudapi.woa.com/document/product/1741/90604)
* [DescribePartitionList](http://document.tencentcloudapi.woa.com/document/product/1741/90603)
* [DescribePhysicalInventory](http://document.tencentcloudapi.woa.com/document/product/1741/90574)
* [DescribePolicy](http://document.tencentcloudapi.woa.com/document/product/1741/90519)
* [DescribePolicyV2](http://document.tencentcloudapi.woa.com/document/product/1741/90518)
* [DescribeRegionZone](http://document.tencentcloudapi.woa.com/document/product/1741/90573)
* [DescribeRoleV2](http://document.tencentcloudapi.woa.com/document/product/1741/90517)
* [DescribeRunningQuery](http://document.tencentcloudapi.woa.com/document/product/1741/90572)
* [DescribeSparkAllSessions](http://document.tencentcloudapi.woa.com/document/product/1741/90571)
* [DescribeSparkAllTasks](http://document.tencentcloudapi.woa.com/document/product/1741/90570)
* [DescribeSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90569)
* [DescribeSparkJobs](http://document.tencentcloudapi.woa.com/document/product/1741/90568)
* [DescribeSparkSqlSpec](http://document.tencentcloudapi.woa.com/document/product/1741/90567)
* [DescribeSparkTask](http://document.tencentcloudapi.woa.com/document/product/1741/90566)
* [DescribeSparkTaskResourceInfos](http://document.tencentcloudapi.woa.com/document/product/1741/90565)
* [DescribeSparkTasks](http://document.tencentcloudapi.woa.com/document/product/1741/90564)
* [DescribeSpec](http://document.tencentcloudapi.woa.com/document/product/1741/90563)
* [DescribeSql](http://document.tencentcloudapi.woa.com/document/product/1741/90562)
* [DescribeSqlDraft](http://document.tencentcloudapi.woa.com/document/product/1741/90561)
* [DescribeSqlExecuteHistory](http://document.tencentcloudapi.woa.com/document/product/1741/90560)
* [DescribeSqlExecuteResult](http://document.tencentcloudapi.woa.com/document/product/1741/90559)
* [DescribeSqlHistoryRecords](http://document.tencentcloudapi.woa.com/document/product/1741/90558)
* [DescribeTCCatalog](http://document.tencentcloudapi.woa.com/document/product/1741/90557)
* [DescribeTableByName](http://document.tencentcloudapi.woa.com/document/product/1741/90602)
* [DescribeTableList](http://document.tencentcloudapi.woa.com/document/product/1741/90601)
* [DescribeUserDefineCos](http://document.tencentcloudapi.woa.com/document/product/1741/90556)
* [DescribeUserV2](http://document.tencentcloudapi.woa.com/document/product/1741/90516)
* [DropDatabase](http://document.tencentcloudapi.woa.com/document/product/1741/90600)
* [DropFunction](http://document.tencentcloudapi.woa.com/document/product/1741/90599)
* [DropPartition](http://document.tencentcloudapi.woa.com/document/product/1741/90598)
* [DropTable](http://document.tencentcloudapi.woa.com/document/product/1741/90597)
* [ExecuteEngineSql](http://document.tencentcloudapi.woa.com/document/product/1741/90596)
* [ExecuteSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90515)
* [ExecuteSql](http://document.tencentcloudapi.woa.com/document/product/1741/90555)
* [ExecuteSqlV1](http://document.tencentcloudapi.woa.com/document/product/1741/90554)
* [InstanceHourRenew](http://document.tencentcloudapi.woa.com/document/product/1741/90514)
* [ModifyCkUserPrivileges](http://document.tencentcloudapi.woa.com/document/product/1741/90513)
* [ModifyConfigs](http://document.tencentcloudapi.woa.com/document/product/1741/90512)
* [ModifyInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90553)
* [ModifyTable](http://document.tencentcloudapi.woa.com/document/product/1741/90595)
* [ModifyUserConfig](http://document.tencentcloudapi.woa.com/document/product/1741/90511)
* [OpenCLSDelivery](http://document.tencentcloudapi.woa.com/document/product/1741/90510)
* [OperateClusterStatus](http://document.tencentcloudapi.woa.com/document/product/1741/90509)
* [OperateDataMask](http://document.tencentcloudapi.woa.com/document/product/1741/90508)
* [OperateLDAP](http://document.tencentcloudapi.woa.com/document/product/1741/90507)
* [OperateMetricSubscription](http://document.tencentcloudapi.woa.com/document/product/1741/90506)
* [OperatePolicyV2](http://document.tencentcloudapi.woa.com/document/product/1741/90505)
* [OperateRoleV2](http://document.tencentcloudapi.woa.com/document/product/1741/90504)
* [OperateRowFilter](http://document.tencentcloudapi.woa.com/document/product/1741/90503)
* [OperateUserV2](http://document.tencentcloudapi.woa.com/document/product/1741/90502)
* [QuerySparkDownloadLogs](http://document.tencentcloudapi.woa.com/document/product/1741/90552)
* [QuerySparkTaskLog](http://document.tencentcloudapi.woa.com/document/product/1741/90551)
* [RestartInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90501)
* [ScaleExtraStorage](http://document.tencentcloudapi.woa.com/document/product/1741/90500)
* [ScaleInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90499)
* [ScaleInstanceV1](http://document.tencentcloudapi.woa.com/document/product/1741/90498)
* [StopCLSDelivery](http://document.tencentcloudapi.woa.com/document/product/1741/90497)
* [TerminateInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90496)
* [TerminateMCPInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90632)
* [UpdateExecSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90495)
* [UpdateInstanceSSL](http://document.tencentcloudapi.woa.com/document/product/1741/90494)
* [UpdateSparkJob](http://document.tencentcloudapi.woa.com/document/product/1741/90493)
* [UpgradeMCPInstance](http://document.tencentcloudapi.woa.com/document/product/1741/90631)
* [VerifyPolicyRule](http://document.tencentcloudapi.woa.com/document/product/1741/90492)

新增数据结构：

* [AccreditObject](http://document.tencentcloudapi.woa.com/document/product/1741/81616#AccreditObject)
* [AsyncActionOperation](http://document.tencentcloudapi.woa.com/document/product/1741/81616#AsyncActionOperation)
* [AutoScalePlan](http://document.tencentcloudapi.woa.com/document/product/1741/81616#AutoScalePlan)
* [BasicUserInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#BasicUserInfo)
* [BatchModifyAccreditReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#BatchModifyAccreditReq)
* [ChargeProperties](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ChargeProperties)
* [CkUserExecuteHistory](http://document.tencentcloudapi.woa.com/document/product/1741/81616#CkUserExecuteHistory)
* [ClsDownLog](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ClsDownLog)
* [ClusterConfHistory](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ClusterConfHistory)
* [CnInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#CnInstanceInfo)
* [Columns](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Columns)
* [ConfigSubmitContext](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ConfigSubmitContext)
* [Database](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Database)
* [DatabaseTable](http://document.tencentcloudapi.woa.com/document/product/1741/81616#DatabaseTable)
* [DescribeAccreditReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#DescribeAccreditReq)
* [ElasticPlan](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ElasticPlan)
* [EngineFilter](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineFilter)
* [EngineInstance](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineInstance)
* [EngineJobAsyncResult](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineJobAsyncResult)
* [EngineJobResult](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineJobResult)
* [EngineJobResultAccessAuth](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineJobResultAccessAuth)
* [EngineJobResultMeta](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineJobResultMeta)
* [EngineRegionInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#EngineRegionInfo)
* [Event](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Event)
* [ExtParamDefine](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ExtParamDefine)
* [ExtParameter](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ExtParameter)
* [Function](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Function)
* [ImpalaUserReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ImpalaUserReq)
* [InstanceConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceConfigInfo)
* [InstanceInfoV1](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceInfoV1)
* [InstanceMCP](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceMCP)
* [InstanceMCPSimple](http://document.tencentcloudapi.woa.com/document/product/1741/81616#InstanceMCPSimple)
* [KerberosConf](http://document.tencentcloudapi.woa.com/document/product/1741/81616#KerberosConf)
* [LdapConfig](http://document.tencentcloudapi.woa.com/document/product/1741/81616#LdapConfig)
* [ManualOperateCluster](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ManualOperateCluster)
* [Map](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Map)
* [MetricSubscriptionReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#MetricSubscriptionReq)
* [ModifyAccreditReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ModifyAccreditReq)
* [ModifyName](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ModifyName)
* [MrMetricFile](http://document.tencentcloudapi.woa.com/document/product/1741/81616#MrMetricFile)
* [NotebookSessionInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#NotebookSessionInfo)
* [NotebookSessionStatement](http://document.tencentcloudapi.woa.com/document/product/1741/81616#NotebookSessionStatement)
* [OrderFields](http://document.tencentcloudapi.woa.com/document/product/1741/81616#OrderFields)
* [Partition](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Partition)
* [PermissionInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#PermissionInfo)
* [Privilege](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Privilege)
* [QueryImpalaLogRecordsRes](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QueryImpalaLogRecordsRes)
* [QueryImpalaLogReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QueryImpalaLogReq)
* [QuerySparkTaskResourceReq](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QuerySparkTaskResourceReq)
* [QuerySparkTaskResourceSummaryInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#QuerySparkTaskResourceSummaryInfo)
* [RegionAreaInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#RegionAreaInfo)
* [RegionInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#RegionInfo)
* [RegularPlan](http://document.tencentcloudapi.woa.com/document/product/1741/81616#RegularPlan)
* [ResourceSpec](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ResourceSpec)
* [Resources](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Resources)
* [ResultOperations](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ResultOperations)
* [RunningQueryRecord](http://document.tencentcloudapi.woa.com/document/product/1741/81616#RunningQueryRecord)
* [SearchTags](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SearchTags)
* [ServerlessSpec](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ServerlessSpec)
* [SparkJobBriefInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkJobBriefInfo)
* [SparkJobDto](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkJobDto)
* [SparkJobInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkJobInfo)
* [SparkSpecMap](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkSpecMap)
* [SparkSpecV1](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkSpecV1)
* [SparkTaskExtendInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkTaskExtendInfo)
* [SparkTaskPodInfos](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SparkTaskPodInfos)
* [SpecMap](http://document.tencentcloudapi.woa.com/document/product/1741/81616#SpecMap)
* [StatementOutput](http://document.tencentcloudapi.woa.com/document/product/1741/81616#StatementOutput)
* [TCLakeSpec](http://document.tencentcloudapi.woa.com/document/product/1741/81616#TCLakeSpec)
* [Table](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Table)
* [TableSimple](http://document.tencentcloudapi.woa.com/document/product/1741/81616#TableSimple)
* [Tag](http://document.tencentcloudapi.woa.com/document/product/1741/81616#Tag)
* [UserCosSpec](http://document.tencentcloudapi.woa.com/document/product/1741/81616#UserCosSpec)
* [UserDefineCosSpec](http://document.tencentcloudapi.woa.com/document/product/1741/81616#UserDefineCosSpec)
* [VersionInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#VersionInfo)
* [ZoneInfo](http://document.tencentcloudapi.woa.com/document/product/1741/81616#ZoneInfo)



## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 80 次发布

发布时间：2026-06-02 02:35:30

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateFunctionReplica](http://document.tencentcloudapi.woa.com/document/product/1738/90638)
* [DeleteFunctionReplica](http://document.tencentcloudapi.woa.com/document/product/1738/90637)
* [DescribeFunctionReplicas](http://document.tencentcloudapi.woa.com/document/product/1738/90636)
* [ModifyFunctionReplica](http://document.tencentcloudapi.woa.com/document/product/1738/90635)

新增数据结构：

* [FunctionReplica](http://document.tencentcloudapi.woa.com/document/product/1738/81211#FunctionReplica)



## 边缘安全加速平台(teo) 版本：2022-01-06



