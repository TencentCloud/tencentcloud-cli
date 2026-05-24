# Release 3.0.1430.1

## 云加密机(cloudhsm) 版本：2019-11-12

### 第 8 次发布

发布时间：2026-05-25 01:13:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeVsmAttributes](http://document.tencentcloudapi.woa.com/document/product/639/41444)

	* 新增出参：DeployEnv


修改数据结构：

* [ResourceInfo](http://document.tencentcloudapi.woa.com/document/product/639/41450#ResourceInfo)

	* 新增成员：DeployEnv




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 167 次发布

发布时间：2026-05-25 01:16:40

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDarInstance](http://document.tencentcloudapi.woa.com/document/product/1003/90379)
* [DescribeDarPublicKey](http://document.tencentcloudapi.woa.com/document/product/1003/90378)

新增数据结构：

* [ModelConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ModelConfig)



## 人脸核身(faceid) 版本：2018-03-01

### 第 99 次发布

发布时间：2026-05-25 01:21:42

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [GetNFCToken](http://document.tencentcloudapi.woa.com/document/product/1007/90382)
* [GetWxNFCResult](http://document.tencentcloudapi.woa.com/document/product/1007/90381)



## 轻量应用服务器(lighthouse) 版本：2020-03-24

### 第 85 次发布

发布时间：2026-05-25 01:29:59

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [AssociateInstancesKeyPairs](http://document.tencentcloudapi.woa.com/document/product/1207/55544)

	* 新增入参：AssociateType, Username

* [DisassociateInstancesKeyPairs](http://document.tencentcloudapi.woa.com/document/product/1207/55539)

	* 新增入参：DisassociateType, Username


新增数据结构：

* [AssociatedInstanceInfo](http://document.tencentcloudapi.woa.com/document/product/1207/47576#AssociatedInstanceInfo)

修改数据结构：

* [KeyPair](http://document.tencentcloudapi.woa.com/document/product/1207/47576#KeyPair)

	* 新增成员：AssociatedInstanceSet




## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 45 次发布

发布时间：2026-05-25 01:36:53

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**删除数据结构**：</font>

* RestServiceInfo

修改数据结构：

* [PostgreSQLInfo](http://document.tencentcloudapi.woa.com/document/product/876/34822#PostgreSQLInfo)

	* <font color="#dd0000">**删除成员**：</font>Host, Port, RestService, Roles




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 27 次发布

发布时间：2026-05-25 01:45:55

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateComputeResource](http://document.tencentcloudapi.woa.com/document/product/1607/89815)

	* 新增入参：EngineId

* [ListLabels](http://document.tencentcloudapi.woa.com/document/product/1607/89344)

	* 新增入参：SourceTypes, SecurityTypes, PolicyBindStatus


新增数据结构：

* [LabelMaskPolicyBrief](http://document.tencentcloudapi.woa.com/document/product/1607/88970#LabelMaskPolicyBrief)
* [UpdatePolicyBinding](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdatePolicyBinding)
* [UpdateSecurityTypes](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdateSecurityTypes)

修改数据结构：

* [BizLabel](http://document.tencentcloudapi.woa.com/document/product/1607/88970#BizLabel)

	* 新增成员：MaskPolicy

* [CreateLabelInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CreateLabelInfo)

	* 新增成员：PolicyId, PolicyBindingWorkspaceId

* [ExecAdminComputeResourceBasicInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceBasicInfo)

	* 新增成员：ClusterType, EngineId

* [ExecAdminComputeResourceConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceConfig)

	* 新增成员：VpcId, SubnetId, ClusterType, Spec, SpecSnapshot, Ext

* [ExecAdminComputeResourceInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceInfo)

	* 新增成员：ComputeType, GpuQuota, ResourceConfig, Ext

* [HighlightingInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#HighlightingInfo)

	* 新增成员：AliasFragments

* [SearchResult](http://document.tencentcloudapi.woa.com/document/product/1607/88970#SearchResult)

	* 新增成员：Aliases

* [StreamTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#StreamTaskInfo)

	* 新增成员：ConfigCu, RunningCu

* [UpdateLabelInfo](http://document.tencentcloudapi.woa.com/document/product/1607/88970#UpdateLabelInfo)

	* 新增成员：SecurityTypesUpdate, PolicyBindingUpdate




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



