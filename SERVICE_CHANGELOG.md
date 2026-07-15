# Release 3.0.1455.1

## 腾讯云智能体开发平台(adp) 版本：2026-05-20

### 第 4 次发布

发布时间：2026-07-16 01:07:43

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeletePlugin](http://document.tencentcloudapi.woa.com/document/product/1815/91369)

	* 新增入参：LoginUin, LoginSubAccountUin




## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 17 次发布

发布时间：2026-07-16 01:08:14

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAgent](http://document.tencentcloudapi.woa.com/document/product/1804/91754)

	* 新增入参：DefaultEnvironmentTemplateId




## 云原生智能网关(cngw) 版本：2023-04-18

### 第 3 次发布

发布时间：2026-07-16 01:15:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90833)

	* 新增入参：ModelRewriteRules, CustomProviderName, ExternalInstanceId, ExtParams, KeyRotationEnabled, KeyRotationPeriodDays

* [CreateCloudNativeAPIGatewaySecretKey](http://document.tencentcloudapi.woa.com/document/product/1817/90842)

	* 新增入参：JWTCredentialConfig, OAuthCredentialConfig, OIDCCredentialConfig

* [ModifyCloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90829)

	* 新增入参：ModelRewriteRules, ExternalInstanceId, ExtParams, KeyRotationEnabled, KeyRotationPeriodDays

* [ModifyCloudNativeAPIGatewayMCPServerAuth](http://document.tencentcloudapi.woa.com/document/product/1817/90848)

	* 新增入参：JWTAuthConfig, OAuthAuthConfig, OIDCAuthConfig


新增数据结构：

* [AIGWCacheAwareRouteCandidate](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWCacheAwareRouteCandidate)
* [AIGWCacheAwareRouteConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWCacheAwareRouteConfig)
* [AIGWJWTAuthPluginConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWJWTAuthPluginConfig)
* [AIGWJWTCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWJWTCredentialConfig)
* [AIGWLLMModelServiceSubRoute](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWLLMModelServiceSubRoute)
* [AIGWModelRewriteRule](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWModelRewriteRule)
* [AIGWOAuthAuthPluginConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWOAuthAuthPluginConfig)
* [AIGWOAuthCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWOAuthCredentialConfig)
* [AIGWOIDCAuthPluginConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWOIDCAuthPluginConfig)
* [AIGWOIDCCredentialConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWOIDCCredentialConfig)
* [AIGWRouteModelServiceConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWRouteModelServiceConfig)
* [AIGWTokenLengthRoute](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWTokenLengthRoute)
* [AIGWTokenLengthRouteRule](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWTokenLengthRouteRule)
* [KeyValue](http://document.tencentcloudapi.woa.com/document/product/1817/90862#KeyValue)

修改数据结构：

* [AIGWLogConfig](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWLogConfig)

	* 新增成员：RequestLogPayloadMode, ResponseLogPayloadMode

* [AIGWMCPServerAuthResult](http://document.tencentcloudapi.woa.com/document/product/1817/90862#AIGWMCPServerAuthResult)

	* 新增成员：JWTAuthConfig, OAuthAuthConfig, OIDCAuthConfig

* [CNAPIGwSecretKey](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CNAPIGwSecretKey)

	* 新增成员：JWTCredentialConfig, OAuthCredentialConfig, OIDCCredentialConfig, Provider

* [CloudNativeAPIGatewayLLMModelService](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CloudNativeAPIGatewayLLMModelService)

	* 新增成员：ModelRewriteRules, SourceId, Namespace, ServiceName, Protocol, ExtParams, CustomProviderName, KeyRotationEnabled, KeyRotationPeriodDays, ExternalInstanceId

* [CloudNativeAPIGatewayLLMModelServiceRoute](http://document.tencentcloudapi.woa.com/document/product/1817/90862#CloudNativeAPIGatewayLLMModelServiceRoute)

	* 新增成员：CacheAwareRouteConfig, TokenLengthRouteConfig




## 暴露面管理服务(ctem) 版本：2023-11-28

### 第 19 次发布

发布时间：2026-07-16 01:16:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCustomer](http://document.tencentcloudapi.woa.com/document/product/1792/87469)

	* 新增入参：ScanPriority

* [CreateJobRecord](http://document.tencentcloudapi.woa.com/document/product/1792/87474)

	* 新增入参：ScanPriority

* [ModifyCustomer](http://document.tencentcloudapi.woa.com/document/product/1792/87463)

	* 新增入参：ScanPriority


新增数据结构：

* [ScanPriorityDisplay](http://document.tencentcloudapi.woa.com/document/product/1792/87475#ScanPriorityDisplay)
* [ScanPriorityReq](http://document.tencentcloudapi.woa.com/document/product/1792/87475#ScanPriorityReq)

修改数据结构：

* [Customer](http://document.tencentcloudapi.woa.com/document/product/1792/87475#Customer)

	* 新增成员：ScanPriority

* [DisplayLeakageCode](http://document.tencentcloudapi.woa.com/document/product/1792/87475#DisplayLeakageCode)

	* 新增成员：RepoNamespace, RepoName, AuthorName




## 腾讯云数据分析智能体(dataagent) 版本：2025-05-13

### 第 18 次发布

发布时间：2026-07-16 01:18:57

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ChatAI](http://document.tencentcloudapi.woa.com/document/product/1806/87993)

	* 新增入参：ArchVersion




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 167 次发布

发布时间：2026-07-16 01:22:39

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSealPolicy](http://document.tencentcloudapi.woa.com/document/product/1668/79305)

	* 新增入参：AuthorizationFlows


新增数据结构：

* [SealPolicyAuthorizationFlows](http://document.tencentcloudapi.woa.com/document/product/1668/79360#SealPolicyAuthorizationFlows)



## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 234 次发布

发布时间：2026-07-16 01:23:22

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyOrganizationBusinessInfo](http://document.tencentcloudapi.woa.com/document/product/1595/91772)

	* 新增入参：NewLegalMobile




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 人脸核身(faceid) 版本：2018-03-01

### 第 106 次发布

发布时间：2026-07-16 01:23:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ApplySdkVerificationToken](http://document.tencentcloudapi.woa.com/document/product/1007/76415)

	* 新增入参：MetaData, SkipLaunchPage, SkipOcrConfirmPage, HideProgressBar, AllowUploadPhoto

	* 新增出参：ServerParamInfo




## 全球加速(ga2) 版本：2025-01-15

### 第 7 次发布

发布时间：2026-07-16 01:25:11

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateListenerAdditionalCert](http://document.tencentcloudapi.woa.com/document/product/1808/91779)
* [DeleteListenerAdditionalCert](http://document.tencentcloudapi.woa.com/document/product/1808/91778)
* [ReplaceListenerAdditionalCert](http://document.tencentcloudapi.woa.com/document/product/1808/91777)



## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 90 次发布

发布时间：2026-07-16 01:29:53

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [BindTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91787)
* [CreateTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91786)
* [DeleteTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91785)
* [DescribeTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91784)
* [DescribeTWeTalkAgentBinding](http://document.tencentcloudapi.woa.com/document/product/1081/91783)
* [DescribeTWeTalkAgentList](http://document.tencentcloudapi.woa.com/document/product/1081/91782)
* [ModifyTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91781)
* [UnbindTWeTalkAgent](http://document.tencentcloudapi.woa.com/document/product/1081/91780)

新增数据结构：

* [TalkAgentBinding](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkAgentBinding)
* [TalkAgentInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkAgentInfo)
* [TalkConversationConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkConversationConfig)
* [TalkIOTTool](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkIOTTool)
* [TalkLLMConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkLLMConfig)
* [TalkMemoryConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkMemoryConfig)
* [TalkSTTConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkSTTConfig)
* [TalkSTTTRTC](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkSTTTRTC)
* [TalkTTSConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkTTSConfig)
* [TalkTTSFlow](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkTTSFlow)
* [TalkWebhookAuth](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkWebhookAuth)
* [TalkWebhookEndpoint](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkWebhookEndpoint)
* [TalkWebhookTool](http://document.tencentcloudapi.woa.com/document/product/1081/34988#TalkWebhookTool)



## 云数据库 MongoDB(mongodb) 版本：2019-07-25

### 第 62 次发布

发布时间：2026-07-16 01:34:08

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteAccountUser](http://document.tencentcloudapi.woa.com/document/product/240/77441)

	* <font color="#dd0000">**修改入参**：</font>MongoUserPassword




## 云数据库 MongoDB(mongodb) 版本：2018-04-08



## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 131 次发布

发布时间：2026-07-16 01:34:29

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GetMonitorDataInternal](http://document.tencentcloudapi.woa.com/document/product/248/82333)

	* 新增入参：SpecifyStatistics




## 流计算 Oceanus(oceanus) 版本：2019-04-22

### 第 85 次发布

发布时间：2026-07-16 01:35:42

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateOceanusCluster](http://document.tencentcloudapi.woa.com/document/product/849/91791)
* [DeleteOceanusCluster](http://document.tencentcloudapi.woa.com/document/product/849/91790)
* [RenewOceanusCluster](http://document.tencentcloudapi.woa.com/document/product/849/91789)
* [ScaleOceanusCluster](http://document.tencentcloudapi.woa.com/document/product/849/91788)

新增数据结构：

* [SlaveVpcDescriptions](http://document.tencentcloudapi.woa.com/document/product/849/52010#SlaveVpcDescriptions)
* [VPCDescription](http://document.tencentcloudapi.woa.com/document/product/849/52010#VPCDescription)



