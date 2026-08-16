# Release 3.0.1473.1

## 应用性能监控(apm) 版本：2021-06-22

### 第 38 次发布

发布时间：2026-08-17 01:10:40

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyApmApplicationConfig](http://document.tencentcloudapi.woa.com/document/product/1463/88214)

	* 新增入参：CrossAccountStatus, CrossAccountPeerId

* [ModifyApmInstance](http://document.tencentcloudapi.woa.com/document/product/1463/77278)

	* 新增入参：CrossAccountStatus, CrossAccountPeerId


修改数据结构：

* [ApmAppConfig](http://document.tencentcloudapi.woa.com/document/product/1463/64927#ApmAppConfig)

	* 新增成员：CrossAccountStatus, CrossAccountPeerId

* [ApmInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1463/64927#ApmInstanceDetail)

	* 新增成员：CrossAccountStatus, CrossAccountPeerId




## 负载均衡(clb) 版本：2023-04-17



## 负载均衡(clb) 版本：2018-03-17

### 第 93 次发布

发布时间：2026-08-17 01:15:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateModelRouter](http://document.tencentcloudapi.woa.com/document/product/214/90910)

	* 新增入参：EipAddressId, Bandwidth


新增数据结构：

* [ModelRouterBillingConfigOutput](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelRouterBillingConfigOutput)
* [StickyConfig](http://document.tencentcloudapi.woa.com/document/product/214/30694#StickyConfig)

修改数据结构：

* [ModelRouterDetail](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelRouterDetail)

	* 新增成员：BillingConfig

* [ModelRouterSet](http://document.tencentcloudapi.woa.com/document/product/214/30694#ModelRouterSet)

	* 新增成员：BillingConfig

* [RouterSettingWithFallBack](http://document.tencentcloudapi.woa.com/document/product/214/30694#RouterSettingWithFallBack)

	* 新增成员：StickyConfig

* [RouterSettingWithoutFallBack](http://document.tencentcloudapi.woa.com/document/product/214/30694#RouterSettingWithoutFallBack)

	* 新增成员：StickyConfig




## 数据库智能管家 DBbrain(dbbrain) 版本：2021-05-27

### 第 59 次发布

发布时间：2026-08-17 01:19:41

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDBDiagEvents](http://document.tencentcloudapi.woa.com/document/product/1130/65947)

	* 新增入参：DiagItems




## 数据库智能管家 DBbrain(dbbrain) 版本：2019-10-16



## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 174 次发布

发布时间：2026-08-17 01:20:28

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInferenceModel](http://document.tencentcloudapi.woa.com/document/product/1342/92171)

	* 新增入参：ResourceTags, GooseFSConfig, StorageType

	* 新增出参：ResourceTags

* [CreateInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92195)

	* 新增入参：AdvancedOptions, ImagePullType, ResourceTags, DeploymentMode, IsCustom, ImagePullSecret, ModelSourceType, AnonymousCosUri, ModelPath, EngineType, GpuArch, ImportPath, CodePackageUri, CodePackageOriginalName, RuntimeEnv, CrOverrides, MountPath, CodePackageSource, CodePackageVersion, RoutePrefix

	* 新增出参：AdvancedOptions, ResourceTags, DeploymentMode, RoutePrefix, IsCustom

* [CreateModelVersion](http://document.tencentcloudapi.woa.com/document/product/1342/92188)

	* 新增入参：GooseFSConfig, StorageType

* [DescribeMCPTaskResult](http://document.tencentcloudapi.woa.com/document/product/1342/91838)

	* 新增入参：NextToken

* [GetInferenceModel](http://document.tencentcloudapi.woa.com/document/product/1342/92170)

	* 新增出参：ResourceTags

* [GetInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92194)

	* 新增出参：DeploymentMode, RoutePrefix, IsCustom, ResourceTags

* [RestartInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92191)

	* 新增出参：ResourceTags

* [StopInferenceService](http://document.tencentcloudapi.woa.com/document/product/1342/92190)

	* 新增出参：ResourceTags, DeploymentMode, RoutePrefix, IsCustom

* [UpdateInferenceModel](http://document.tencentcloudapi.woa.com/document/product/1342/92168)

	* 新增入参：ResourceTags

	* 新增出参：ResourceTags


新增数据结构：

* [CrOverrides](http://document.tencentcloudapi.woa.com/document/product/1342/53778#CrOverrides)
* [GooseFSConfig](http://document.tencentcloudapi.woa.com/document/product/1342/53778#GooseFSConfig)

修改数据结构：

* [InferenceModelInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#InferenceModelInfo)

	* 新增成员：ResourceTags




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 96 次发布

发布时间：2026-08-17 01:32:00

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateTWeSeeDirectUploadCredential](http://document.tencentcloudapi.woa.com/document/product/1081/91264)

	* 新增入参：UploadTarget

* [ListTWeSeeTasks](http://document.tencentcloudapi.woa.com/document/product/1081/91250)

	* 新增入参：Filters


新增数据结构：

* [VisionRecognitionTaskFilter](http://document.tencentcloudapi.woa.com/document/product/1081/34988#VisionRecognitionTaskFilter)

修改数据结构：

* [SeeTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeTaskInfo)

	* 新增成员：COSURI




## 多网聚合加速(mna) 版本：2021-01-19

### 第 37 次发布

发布时间：2026-08-17 01:35:43

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddCustomerGatewayCluster](http://document.tencentcloudapi.woa.com/document/product/1385/92290)
* [AddGateway](http://document.tencentcloudapi.woa.com/document/product/1385/92289)
* [DeleteCustomerGatewayCluster](http://document.tencentcloudapi.woa.com/document/product/1385/92288)
* [DeleteGateway](http://document.tencentcloudapi.woa.com/document/product/1385/92287)
* [DescribeAccessPointList](http://document.tencentcloudapi.woa.com/document/product/1385/92286)
* [GetCustomerGatewayClusterList](http://document.tencentcloudapi.woa.com/document/product/1385/92285)
* [ModifyDeviceAccessScope](http://document.tencentcloudapi.woa.com/document/product/1385/92284)
* [UpdateCustomerGatewayCluster](http://document.tencentcloudapi.woa.com/document/product/1385/92283)

新增数据结构：

* [AccessPointInfo](http://document.tencentcloudapi.woa.com/document/product/1385/55846#AccessPointInfo)
* [GatewayClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1385/55846#GatewayClusterInfo)



## TokenHub(tokenhub) 版本：2026-03-22

### 第 17 次发布

发布时间：2026-08-17 01:45:41

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Model](http://document.tencentcloudapi.woa.com/document/product/1814/90425#Model)

	* 新增成员：ExtraModelIds

* [ModelChargingItem](http://document.tencentcloudapi.woa.com/document/product/1814/90425#ModelChargingItem)

	* 新增成员：Specification, Usage, ReferencePrice

* [ModelEndpointView](http://document.tencentcloudapi.woa.com/document/product/1814/90425#ModelEndpointView)

	* 新增成员：ExtraModelIds, ModelStatus




