# Release 3.0.1425.1

## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 17 次发布

发布时间：2026-05-18 01:08:23

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModel](http://document.tencentcloudapi.woa.com/document/product/1805/88915)

	* 新增入参：ModelID, Description

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88920)

	* 新增入参：ModelProtocol

* [DescribeModelServices](http://document.tencentcloudapi.woa.com/document/product/1805/88917)

	* 新增入参：ModelProtocol

* [ModifyModel](http://document.tencentcloudapi.woa.com/document/product/1805/88911)

	* 新增入参：ModelID, Description

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/1805/88916)

	* 新增入参：ModelProtocol


修改数据结构：

* [DescribeModelResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelResponseVO)

	* 新增成员：ModelID, Description

* [DescribeModelServiceResponseVO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeModelServiceResponseVO)

	* 新增成员：ModelProtocol

* [PromptModerateConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#PromptModerateConfigDTO)

	* 新增成员：ContextScope

* [SensitiveDataCheckConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#SensitiveDataCheckConfigDTO)

	* 新增成员：ContextScope

* [TmsConfigDTO](http://document.tencentcloudapi.woa.com/document/product/1805/87916#TmsConfigDTO)

	* 新增成员：ContextScope




## 云安全一体化平台(csip) 版本：2022-11-21

### 第 76 次发布

发布时间：2026-05-18 01:15:25

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateCosAssetSyncTask](http://document.tencentcloudapi.woa.com/document/product/1726/90316)
* [CreateCosObjectScanTask](http://document.tencentcloudapi.woa.com/document/product/1726/90315)
* [CreateCosPolicy](http://document.tencentcloudapi.woa.com/document/product/1726/90314)
* [CreateCosRiskScanTask](http://document.tencentcloudapi.woa.com/document/product/1726/90313)
* [DeleteCosAkAsset](http://document.tencentcloudapi.woa.com/document/product/1726/90312)
* [DeleteCosPolicy](http://document.tencentcloudapi.woa.com/document/product/1726/90311)
* [DescribeBucketInvokeIpList](http://document.tencentcloudapi.woa.com/document/product/1726/90310)
* [DescribeCosAccessPermission](http://document.tencentcloudapi.woa.com/document/product/1726/90309)
* [DescribeCosAccessPermissions](http://document.tencentcloudapi.woa.com/document/product/1726/90308)
* [DescribeCosActionList](http://document.tencentcloudapi.woa.com/document/product/1726/90307)
* [DescribeCosAkAsset](http://document.tencentcloudapi.woa.com/document/product/1726/90306)
* [DescribeCosAkInvokeIpList](http://document.tencentcloudapi.woa.com/document/product/1726/90305)
* [DescribeCosAlarmList](http://document.tencentcloudapi.woa.com/document/product/1726/90304)
* [DescribeCosAlarmTrendData](http://document.tencentcloudapi.woa.com/document/product/1726/90303)
* [DescribeCosAsset](http://document.tencentcloudapi.woa.com/document/product/1726/90302)
* [DescribeCosAssetSyncTask](http://document.tencentcloudapi.woa.com/document/product/1726/90301)
* [DescribeCosAuditAppIdList](http://document.tencentcloudapi.woa.com/document/product/1726/90300)
* [DescribeCosAuditDictionaryList](http://document.tencentcloudapi.woa.com/document/product/1726/90299)
* [DescribeCosAuditPayInfo](http://document.tencentcloudapi.woa.com/document/product/1726/90298)
* [DescribeCosBucketBillingInfo](http://document.tencentcloudapi.woa.com/document/product/1726/90297)
* [DescribeCosBucketList](http://document.tencentcloudapi.woa.com/document/product/1726/90296)
* [DescribeCosBucketRisk](http://document.tencentcloudapi.woa.com/document/product/1726/90295)
* [DescribeCosIdentifyFileList](http://document.tencentcloudapi.woa.com/document/product/1726/90294)
* [DescribeCosInvokeUa](http://document.tencentcloudapi.woa.com/document/product/1726/90293)
* [DescribeCosIpInvokeLog](http://document.tencentcloudapi.woa.com/document/product/1726/90292)
* [DescribeCosIpInvokeRecordFile](http://document.tencentcloudapi.woa.com/document/product/1726/90291)
* [DescribeCosOverview](http://document.tencentcloudapi.woa.com/document/product/1726/90290)
* [DescribeCosPolicy](http://document.tencentcloudapi.woa.com/document/product/1726/90289)
* [DescribeCosRiskActionList](http://document.tencentcloudapi.woa.com/document/product/1726/90288)
* [DescribeCosRiskEvidence](http://document.tencentcloudapi.woa.com/document/product/1726/90287)
* [DescribeCosRiskScanTask](http://document.tencentcloudapi.woa.com/document/product/1726/90286)
* [DescribeCosRoleAccessPermission](http://document.tencentcloudapi.woa.com/document/product/1726/90285)
* [DescribeCosRoleAccessPermissions](http://document.tencentcloudapi.woa.com/document/product/1726/90284)
* [DescribeCosSourceIp](http://document.tencentcloudapi.woa.com/document/product/1726/90283)
* [DescribeIpInvokeRecord](http://document.tencentcloudapi.woa.com/document/product/1726/90282)
* [DescribeIpInvokeRecordDetail](http://document.tencentcloudapi.woa.com/document/product/1726/90281)
* [DescribePolicyHitData](http://document.tencentcloudapi.woa.com/document/product/1726/90280)
* [DescribeRiskBucketList](http://document.tencentcloudapi.woa.com/document/product/1726/90279)
* [DescribeRiskItemList](http://document.tencentcloudapi.woa.com/document/product/1726/90278)
* [DescribeRiskTrendData](http://document.tencentcloudapi.woa.com/document/product/1726/90277)
* [ModifyAlarmRiskStatus](http://document.tencentcloudapi.woa.com/document/product/1726/90276)
* [ModifyCosAuditMonitorAccount](http://document.tencentcloudapi.woa.com/document/product/1726/90275)
* [ModifyCosMarkInfo](http://document.tencentcloudapi.woa.com/document/product/1726/90274)
* [ModifyPolicyStatus](http://document.tencentcloudapi.woa.com/document/product/1726/90273)

新增数据结构：

* [CosAccessInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAccessInfo)
* [CosActionInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosActionInfo)
* [CosAkAssetInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAkAssetInfo)
* [CosAkSet](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAkSet)
* [CosAlarmInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAlarmInfo)
* [CosAlarmRiskIdInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAlarmRiskIdInfo)
* [CosAlarmTrendInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAlarmTrendInfo)
* [CosAssetDataScanDetail](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAssetDataScanDetail)
* [CosAssetFileIdentifyInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAssetFileIdentifyInfo)
* [CosAssetInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAssetInfo)
* [CosAssetSyncTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAssetSyncTaskInfo)
* [CosAuditPayInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosAuditPayInfo)
* [CosBucketAccessWay](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosBucketAccessWay)
* [CosBucketBillingInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosBucketBillingInfo)
* [CosBucketId](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosBucketId)
* [CosBucketInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosBucketInfo)
* [CosBucketTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosBucketTaskInfo)
* [CosDictionary](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosDictionary)
* [CosIdentifyCategoryDetail](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosIdentifyCategoryDetail)
* [CosIdentifyRuleDetail](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosIdentifyRuleDetail)
* [CosInvokeDetailInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosInvokeDetailInfo)
* [CosInvokeIpVpcInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosInvokeIpVpcInfo)
* [CosInvokeLog](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosInvokeLog)
* [CosInvokeRecordInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosInvokeRecordInfo)
* [CosOverview](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosOverview)
* [CosPermissionInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosPermissionInfo)
* [CosPolicyInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosPolicyInfo)
* [CosRiskActionInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskActionInfo)
* [CosRiskAlarmInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskAlarmInfo)
* [CosRiskBucketInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskBucketInfo)
* [CosRiskInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskInfo)
* [CosRiskTrendInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskTrendInfo)
* [CosRiskViewInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRiskViewInfo)
* [CosRoleAccessInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosRoleAccessInfo)
* [CosSourceIpInfo](http://document.tencentcloudapi.woa.com/document/product/1726/80814#CosSourceIpInfo)



## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 227 次发布

发布时间：2026-05-18 01:25:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateSealByImage](http://document.tencentcloudapi.woa.com/document/product/1595/75256)

	* 新增出参：PreviewFileUrl, PreviewPdfUrl




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 133 次发布

发布时间：2026-05-18 01:42:18

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeBillingSpecs](http://document.tencentcloudapi.woa.com/document/product/851/75918)

	* 新增入参：TiProjectId, InstanceFamily, AvailableVisibility, Zone


新增数据结构：

* [CBSInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#CBSInfo)
* [LocalDiskType](http://document.tencentcloudapi.woa.com/document/product/851/74915#LocalDiskType)

修改数据结构：

* [Instance](http://document.tencentcloudapi.woa.com/document/product/851/74915#Instance)

	* 新增成员：CBSInfoList

* [Service](http://document.tencentcloudapi.woa.com/document/product/851/74915#Service)

	* 新增成员：Changer, ChangerName

* [ServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroup)

	* 新增成员：Changer, ChangerName

* [Spec](http://document.tencentcloudapi.woa.com/document/product/851/74915#Spec)

	* 新增成员：LocalDiskTypeList




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 24 次发布

发布时间：2026-05-18 01:47:31

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ExperimentInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExperimentInfo)

	* 新增成员：RunCount, LoggedModelCount

* [Task](http://document.tencentcloudapi.woa.com/document/product/1607/88970#Task)

	* 新增成员：InnerTask




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



