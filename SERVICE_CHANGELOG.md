# Release 3.0.1479.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 24 次发布

发布时间：2026-08-25 01:07:54

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AcquireDeploymentToken](http://document.tencentcloudapi.woa.com/document/product/1804/92415)
* [CreateDeployment](http://document.tencentcloudapi.woa.com/document/product/1804/92414)
* [DeleteDeployment](http://document.tencentcloudapi.woa.com/document/product/1804/92413)
* [DescribeDeployment](http://document.tencentcloudapi.woa.com/document/product/1804/92412)
* [DescribeDeploymentList](http://document.tencentcloudapi.woa.com/document/product/1804/92411)
* [ModifyDeployment](http://document.tencentcloudapi.woa.com/document/product/1804/92410)

新增数据结构：

* [AffinityConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#AffinityConfiguration)
* [ComputerConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#ComputerConfiguration)
* [Deployment](http://document.tencentcloudapi.woa.com/document/product/1804/87854#Deployment)
* [LifecycleConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#LifecycleConfiguration)
* [ScalingConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#ScalingConfiguration)
* [WAAConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#WAAConfiguration)

修改数据结构：

* [SandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxInstance)

	* 新增成员：ComputerConfiguration

* [SandboxTool](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxTool)

	* 新增成员：ComputerConfiguration




## 灾备中心(bdrc) 版本：2026-03-30

### 第 2 次发布

发布时间：2026-08-25 01:13:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyFileBackupPlan](http://document.tencentcloudapi.woa.com/document/product/1824/92335)




## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 176 次发布

发布时间：2026-08-25 01:21:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeClusterInfo](http://document.tencentcloudapi.woa.com/document/product/236/83723)

	* 新增出参：DeployMode




## 云原生智能网关(cngw) 版本：2023-04-18

### 第 6 次发布

发布时间：2026-08-25 01:31:09

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudNativeAPIGatewayConsumer](http://document.tencentcloudapi.woa.com/document/product/1817/90826)

	* 新增入参：Priority

* [CreateCloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1817/90816)

	* 新增入参：MaxDocumentsConfig, SensitiveWordRoute

* [CreateCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90833)

	* 新增入参：LoadBalanceConfig

* [CreateCloudNativeAPIGatewayMCPServer](http://document.tencentcloudapi.woa.com/document/product/1817/90861)

	* 新增入参：PreserveHost

* [CreateCloudNativeAPIGatewaySecretKey](http://document.tencentcloudapi.woa.com/document/product/1817/90842)

	* 新增入参：AKSKCredentialConfig, CAMCredentialConfig, BearerTokenCredentialConfig, CustomHeaderCredentialConfig, QueryParamCredentialConfig, BasicCredentialConfig

* [DescribeCloudNativeAPIGatewayMCPServerList](http://document.tencentcloudapi.woa.com/document/product/1817/90854)

	* 新增入参：SecretKeyId

* [ModifyCloudNativeAPIGatewayConsumer](http://document.tencentcloudapi.woa.com/document/product/1817/90820)

	* 新增入参：Priority

* [ModifyCloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1817/90812)

	* 新增入参：MaxDocumentsConfig, SensitiveWordRoute

* [ModifyCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90829)

	* 新增入参：CustomProviderName, LoadBalanceConfig

* [ModifyCloudNativeAPIGatewayMCPServer](http://document.tencentcloudapi.woa.com/document/product/1817/90850)

	* 新增入参：PreserveHost


新增数据结构：

* [AIGWAKSKCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWAKSKCredentialConfig)
* [AIGWAuthModelScopeItem](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWAuthModelScopeItem)
* [AIGWBasicCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWBasicCredentialConfig)
* [AIGWBearerTokenCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWBearerTokenCredentialConfig)
* [AIGWCAMCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWCAMCredentialConfig)
* [AIGWConsumerModelScope](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWConsumerModelScope)
* [AIGWCustomHeaderCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWCustomHeaderCredentialConfig)
* [AIGWLLMHealthCheckSetting](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWLLMHealthCheckSetting)
* [AIGWLoadBalanceConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWLoadBalanceConfig)
* [AIGWModelScope](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWModelScope)
* [AIGWQueryParamCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWQueryParamCredentialConfig)
* [AIGWRerankMaxDocumentsConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWRerankMaxDocumentsConfig)
* [AIGWSensitiveWordRoute](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWSensitiveWordRoute)
* [AIGWUpstreamTLSConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWUpstreamTLSConfig)

修改数据结构：

* [AIGWMCPServer](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWMCPServer)

	* 新增成员：PreserveHost

* [AIGWMCPUpstreamInfo](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWMCPUpstreamInfo)

	* 新增成员：TLSConfig

* [AIGWMCPUpstreamInfoDetail](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWMCPUpstreamInfoDetail)

	* 新增成员：TLSConfig

* [CNAPIGwConsumer](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CNAPIGwConsumer)

	* 新增成员：Priority, SyncStatus, SourceType, SyncedVersion

* [CNAPIGwConsumerGroup](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CNAPIGwConsumerGroup)

	* 新增成员：SyncStatus, SourceType, SyncedVersion

* [CNAPIGwSecretKey](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CNAPIGwSecretKey)

	* 新增成员：SyncStatus, SourceType, SyncedVersion, AKSKCredentialConfig, CAMCredentialConfig, BearerTokenCredentialConfig, BasicCredentialConfig, CustomHeaderCredentialConfig, QueryParamCredentialConfig

* [CloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CloudNativeAPIGatewayLLMModelAPI)

	* 新增成员：MaxDocumentsConfig, SensitiveWordRoute, ConsumerGroupModelScopes, ConsumerInheritModelScope

* [CloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CloudNativeAPIGatewayLLMModelService)

	* 新增成员：LoadBalanceConfig, CanPublish, PublishStatus, SyncStatus, SourceType, SyncedVersion, Status, EnableHealthCheck, HealthCheck




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 192 次发布

发布时间：2026-08-25 01:38:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [TransferClusterPrepayToPostpay](http://document.tencentcloudapi.woa.com/document/product/1003/92046)

	* 新增入参：ClusterId

	* 新增出参：BigDealIds, TranId, DealNames, ResourceIds, ClusterIds




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 152 次发布

发布时间：2026-08-25 01:51:42

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [AutoScaleResourceConf](http://document.tencentcloudapi.woa.com/document/product/589/33981#AutoScaleResourceConf)

	* 新增成员：CustomNodeName

* [NodeResourceSpec](http://document.tencentcloudapi.woa.com/document/product/589/33981#NodeResourceSpec)

	* 新增成员：CustomNodeName

* [OperationLog](http://document.tencentcloudapi.woa.com/document/product/589/33981#OperationLog)

	* 新增成员：OperatorName




## Elasticsearch Service(es) 版本：2018-04-16

### 第 116 次发布

发布时间：2026-08-25 01:53:15

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/845/30634#InstanceInfo)

	* 新增成员：OldEsVip, OldEsPrivateTcpUrl




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 98 次发布

发布时间：2026-08-25 02:07:53

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateTWeSeePerson](http://document.tencentcloudapi.woa.com/document/product/1081/92424)
* [DeleteTWeSeeFace](http://document.tencentcloudapi.woa.com/document/product/1081/92423)
* [DeleteTWeSeePerson](http://document.tencentcloudapi.woa.com/document/product/1081/92422)
* [DescribeTWeSeeFace](http://document.tencentcloudapi.woa.com/document/product/1081/92421)
* [DescribeTWeSeePerson](http://document.tencentcloudapi.woa.com/document/product/1081/92420)
* [ImportTWeSeeFaces](http://document.tencentcloudapi.woa.com/document/product/1081/92419)
* [ListTWeSeePersons](http://document.tencentcloudapi.woa.com/document/product/1081/92418)
* [ModifyTWeSeeFace](http://document.tencentcloudapi.woa.com/document/product/1081/92417)
* [ModifyTWeSeePerson](http://document.tencentcloudapi.woa.com/document/product/1081/92416)

修改接口：

* [InvokeTWeSeeComprehension](http://document.tencentcloudapi.woa.com/document/product/1081/91252)

	* 新增出参：FaceRecognitionResult


新增数据结构：

* [SeeFaceInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeFaceInfo)
* [SeeFaceRecognitionResult](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeFaceRecognitionResult)
* [SeePersonInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeePersonInfo)
* [SeeTaskFaceInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeTaskFaceInfo)
* [SeeTaskPersonInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeTaskPersonInfo)

修改数据结构：

* [SeeComprehensionConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeComprehensionConfig)

	* 新增成员：EnableFaceDetection, InputRotateDegree

* [SeeTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeTaskInfo)

	* 新增成员：FaceRecognitionResult




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 68 次发布

发布时间：2026-08-25 02:35:07

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyDBInstanceSpec](http://document.tencentcloudapi.woa.com/document/product/409/63689)

	* 新增入参：DryRun


修改数据结构：

* [ClassInfo](http://document.tencentcloudapi.woa.com/document/product/409/16778#ClassInfo)

	* 新增成员：SpecName




## 云数据库Redis(redis) 版本：2018-04-12

### 第 76 次发布

发布时间：2026-08-25 02:37:23

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeInstancePasswordPolicy](http://document.tencentcloudapi.woa.com/document/product/239/92425)



## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 62 次发布

发布时间：2026-08-25 02:44:27

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [SMSCloudFunctionConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#SMSCloudFunctionConfig)

修改数据结构：

* [MgoKeySchema](http://document.tencentcloudapi.woa.com/document/product/876/34822#MgoKeySchema)

	* 新增成员：PartialFilterExpression

* [SMSProviderTemplateConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#SMSProviderTemplateConfig)

	* 新增成员：AuthType, CredentialAuthKeyId, CredentialAuthTypeCode

* [VerificationConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#VerificationConfig)

	* 新增成员：CloudFunction




## 多模态智能数据湖 TCLake(tccatalog) 版本：2024-10-24

### 第 14 次发布

发布时间：2026-08-25 02:45:51

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeMetastoreInstance](http://document.tencentcloudapi.woa.com/document/product/1785/88318)

	* 新增出参：UserAppId


修改数据结构：

* [TableInfo](http://document.tencentcloudapi.woa.com/document/product/1785/85705#TableInfo)

	* 新增成员：TableMode




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 153 次发布

发布时间：2026-08-25 03:07:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/851/76500)

	* 新增入参：InferTemplateId

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/851/76703)

	* 新增入参：InferTemplateId


修改数据结构：

* [ServiceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceInfo)

	* 新增成员：InferTemplateId




## TI-ONE 训练平台(tione) 版本：2019-10-22



## TSF-Polaris&ZK&网关(tse) 版本：2020-12-07

### 第 109 次发布

发布时间：2026-08-25 03:12:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudNativeAPIGatewayCertificate](http://document.tencentcloudapi.woa.com/document/product/1364/81949)

	* 新增入参：CertType, CertUsage

	* <font color="#dd0000">**修改入参**：</font>BindDomains

* [CreateCloudNativeAPIGatewayConsumer](http://document.tencentcloudapi.woa.com/document/product/1364/90360)

	* 新增入参：Priority

* [CreateCloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1364/90358)

	* 新增入参：MaxDocumentsConfig, SensitiveWordRoute

* [CreateCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1364/90357)

	* 新增入参：LoadBalanceConfig

* [CreateCloudNativeAPIGatewaySecretKey](http://document.tencentcloudapi.woa.com/document/product/1364/90356)

	* 新增入参：AKSKCredentialConfig, CAMCredentialConfig, BearerTokenCredentialConfig, CustomHeaderCredentialConfig, QueryParamCredentialConfig, BasicCredentialConfig

* [DescribeCloudNativeAPIGatewayCertificates](http://document.tencentcloudapi.woa.com/document/product/1364/81946)

	* 新增入参：CertType, CertUsage

* [ModifyCloudNativeAPIGatewayConsumer](http://document.tencentcloudapi.woa.com/document/product/1364/90339)

	* 新增入参：Priority

* [ModifyCloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1364/90337)

	* 新增入参：MaxDocumentsConfig, SensitiveWordRoute

* [ModifyCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1364/90336)

	* 新增入参：CustomProviderName, LoadBalanceConfig

* [UpdateCloudNativeAPIGatewayCertificateInfo](http://document.tencentcloudapi.woa.com/document/product/1364/81945)

	* <font color="#dd0000">**修改入参**：</font>BindDomains


新增数据结构：

* [AIGWAKSKCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWAKSKCredentialConfig)
* [AIGWAuthModelScopeItem](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWAuthModelScopeItem)
* [AIGWBasicCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWBasicCredentialConfig)
* [AIGWBearerTokenCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWBearerTokenCredentialConfig)
* [AIGWCAMCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWCAMCredentialConfig)
* [AIGWConsumerModelScope](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWConsumerModelScope)
* [AIGWCustomHeaderCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWCustomHeaderCredentialConfig)
* [AIGWLLMHealthCheckSetting](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWLLMHealthCheckSetting)
* [AIGWLoadBalanceConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWLoadBalanceConfig)
* [AIGWModelScope](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWModelScope)
* [AIGWQueryParamCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWQueryParamCredentialConfig)
* [AIGWRerankMaxDocumentsConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWRerankMaxDocumentsConfig)
* [AIGWSensitiveWordRoute](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWSensitiveWordRoute)

修改数据结构：

* [AIGWLogConfig](http://document.tencentcloudapi.woa.com/document/product/1364/54942#AIGWLogConfig)

	* 新增成员：RequestLogPayloadTruncationPolicy, ResponseLogPayloadTruncationPolicy

* [CNAPIGwConsumer](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CNAPIGwConsumer)

	* 新增成员：Priority, SyncStatus, SourceType, SyncedVersion

* [CNAPIGwConsumerGroup](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CNAPIGwConsumerGroup)

	* 新增成员：SyncStatus, SourceType, SyncedVersion

* [CNAPIGwSecretKey](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CNAPIGwSecretKey)

	* 新增成员：AKSKCredentialConfig, CAMCredentialConfig, BearerTokenCredentialConfig, BasicCredentialConfig, CustomHeaderCredentialConfig, QueryParamCredentialConfig, SyncStatus, SourceType, SyncedVersion

* [CloudNativeAPIGatewayLLMModelAPI](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CloudNativeAPIGatewayLLMModelAPI)

	* 新增成员：MaxDocumentsConfig, SensitiveWordRoute, ConsumerGroupModelScopes, ConsumerInheritModelScope

* [CloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CloudNativeAPIGatewayLLMModelService)

	* 新增成员：LoadBalanceConfig, PublishStatus, CanPublish, SyncStatus, SourceType, SyncedVersion, Status, EnableHealthCheck, HealthCheck

* [CloudNativeAPIGatewayTaskPhase](http://document.tencentcloudapi.woa.com/document/product/1364/54942#CloudNativeAPIGatewayTaskPhase)

	* 新增成员：EstimatedCostSeconds, ActualCostSeconds

* [KongCertificatesPreview](http://document.tencentcloudapi.woa.com/document/product/1364/54942#KongCertificatesPreview)

	* 新增成员：CertType, CertUsage, ReferCount




