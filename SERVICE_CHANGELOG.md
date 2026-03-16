# Release 3.0.1384.1

## 腾讯混元生3D(ai3d) 版本：2025-05-13

### 第 12 次发布

发布时间：2026-03-17 01:07:45

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [QueryHunyuanTo3DProJob](http://document.tencentcloudapi.woa.com/document/product/1800/87647)

	* 新增出参：ResultCreditDetails, ResultCreditConsumed




## 大模型安全网关(apis) 版本：2024-08-01

### 第 7 次发布

发布时间：2026-03-17 01:10:18

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89006)
* [DeleteAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89005)
* [DescribeAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89004)
* [DescribeAIMCredentials](http://document.tencentcloudapi.woa.com/document/product/1805/89003)
* [GetAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89002)
* [ModifyAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89001)

新增数据结构：

* [AccessCredential](http://document.tencentcloudapi.woa.com/document/product/1805/87916#AccessCredential)
* [DescribeAIMCredentialResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialResp)
* [DescribeAIMCredentialsResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#DescribeAIMCredentialsResp)
* [GetAIMCredentialResp](http://document.tencentcloudapi.woa.com/document/product/1805/87916#GetAIMCredentialResp)
* [STSCredential](http://document.tencentcloudapi.woa.com/document/product/1805/87916#STSCredential)



## 日志服务(cls) 版本：2020-10-16

### 第 140 次发布

发布时间：2026-03-17 01:24:03

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudProductLogCollection](http://document.tencentcloudapi.woa.com/document/product/614/86055)

	* 新增入参：Tags

* [CreateCloudProductLogTask](http://document.tencentcloudapi.woa.com/document/product/614/83989)

	* 新增入参：Tags

* [CreateSplunkDeliver](http://document.tencentcloudapi.woa.com/document/product/614/88549)

	* 新增入参：ExternalRole

* [DeleteCloudProductLogCollection](http://document.tencentcloudapi.woa.com/document/product/614/86054)

	* 新增入参：IsDeleteTopic, IsDeleteLogset

* [DeleteCloudProductLogTask](http://document.tencentcloudapi.woa.com/document/product/614/83988)

	* 新增入参：IsDeleteTopic, IsDeleteLogset

* [ModifySplunkDeliver](http://document.tencentcloudapi.woa.com/document/product/614/88545)

	* 新增入参：ExternalRole


新增数据结构：

* [ExternalRole](http://document.tencentcloudapi.woa.com/document/product/614/56471#ExternalRole)

修改数据结构：

* [SplunkDeliverInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#SplunkDeliverInfo)

	* 新增成员：ExternalRole




## 云游戏(gs) 版本：2019-11-18

### 第 52 次发布

发布时间：2026-03-17 01:44:53

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAndroidInstanceADB](http://document.tencentcloudapi.woa.com/document/product/1162/86951)

	* 新增入参：ExpiredTime




## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 118 次发布

发布时间：2026-03-17 02:21:15

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDataSource](http://document.tencentcloudapi.woa.com/document/product/851/89016)
* [CreateMountLimit](http://document.tencentcloudapi.woa.com/document/product/851/89015)
* [DeleteDataSource](http://document.tencentcloudapi.woa.com/document/product/851/89014)
* [DeleteMountLimit](http://document.tencentcloudapi.woa.com/document/product/851/89013)
* [DescribeDataSource](http://document.tencentcloudapi.woa.com/document/product/851/89012)
* [DescribeMountInstance](http://document.tencentcloudapi.woa.com/document/product/851/89011)
* [DescribeMountInstances](http://document.tencentcloudapi.woa.com/document/product/851/89010)
* [DescribeMountLimits](http://document.tencentcloudapi.woa.com/document/product/851/89009)
* [UpdateDataSource](http://document.tencentcloudapi.woa.com/document/product/851/89008)
* [UpdateMountLimit](http://document.tencentcloudapi.woa.com/document/product/851/89007)

修改接口：

* [CreateModelService](http://document.tencentcloudapi.woa.com/document/product/851/76500)

	* 新增入参：GatewayConfig

* [DescribeBillingResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/82745)

	* 新增出参：SpaceEditEnabled

* [ModifyModelService](http://document.tencentcloudapi.woa.com/document/product/851/76703)

	* 新增入参：TargetProjectId


新增数据结构：

* [GatewayConfig](http://document.tencentcloudapi.woa.com/document/product/851/74915#GatewayConfig)
* [MountInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#MountInstanceInfo)
* [MountLimitInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#MountLimitInfo)

修改数据结构：

* [ResourceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ResourceGroup)

	* 新增成员：SpaceEditEnabled

* [ServiceCallInfoV2](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceCallInfoV2)

	* 新增成员：GatewayConfig

* [ServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/74915#ServiceGroup)

	* 新增成员：GatewayConfig




## TI-ONE 训练平台(tione) 版本：2019-10-22



## 容器服务(tke) 版本：2022-05-01



## 容器服务(tke) 版本：2018-05-25

### 第 116 次发布

发布时间：2026-03-17 02:23:51

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateExternalNodePool](http://document.tencentcloudapi.woa.com/document/product/457/89025)
* [DeleteExternalNode](http://document.tencentcloudapi.woa.com/document/product/457/89024)
* [DeleteExternalNodePool](http://document.tencentcloudapi.woa.com/document/product/457/89023)
* [DescribeExternalNode](http://document.tencentcloudapi.woa.com/document/product/457/89022)
* [DescribeExternalNodePools](http://document.tencentcloudapi.woa.com/document/product/457/89021)
* [DescribeExternalNodeScript](http://document.tencentcloudapi.woa.com/document/product/457/89020)
* [DrainExternalNode](http://document.tencentcloudapi.woa.com/document/product/457/89019)
* [EnableExternalNodeSupport](http://document.tencentcloudapi.woa.com/document/product/457/89018)
* [ModifyExternalNodePool](http://document.tencentcloudapi.woa.com/document/product/457/89017)

新增数据结构：

* [ClusterExternalConfig](http://document.tencentcloudapi.woa.com/document/product/457/31866#ClusterExternalConfig)
* [ExternalNode](http://document.tencentcloudapi.woa.com/document/product/457/31866#ExternalNode)
* [ExternalNodePool](http://document.tencentcloudapi.woa.com/document/product/457/31866#ExternalNodePool)



