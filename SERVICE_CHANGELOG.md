# Release 3.0.1239.1

## 弹性伸缩(as) 版本：2018-04-19

### 第 48 次发布

发布时间：2025-07-11 01:09:40

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [RefreshSettings](http://document.tencentcloudapi.woa.com/document/product/377/20453#RefreshSettings)

	* 新增成员：CheckInstanceTargetHealthTimeout




## 腾讯云数据仓库 TCHouse-D(cdwdoris) 版本：2021-12-28

### 第 66 次发布

发布时间：2025-07-11 01:17:40

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateBackUpSchedule](http://document.tencentcloudapi.woa.com/document/product/1706/84371)

	* 新增入参：SnapshotRemainPolicy, DataRemoteRegion

* [DescribeSqlApis](http://document.tencentcloudapi.woa.com/document/product/1706/84359)

	* 新增入参：UserNames

* [ModifyUserPrivilegesV3](http://document.tencentcloudapi.woa.com/document/product/1706/84350)

	* 新增入参：DefaultComputeGroup


新增数据结构：

* [SnapshotRemainPolicy](http://document.tencentcloudapi.woa.com/document/product/1706/80309#SnapshotRemainPolicy)

修改数据结构：

* [BackUpJobDisplay](http://document.tencentcloudapi.woa.com/document/product/1706/80309#BackUpJobDisplay)

	* 新增成员：SnapshotRemainPolicy

* [BackupCosInfo](http://document.tencentcloudapi.woa.com/document/product/1706/80309#BackupCosInfo)

	* 新增成员：Region

* [InstanceNode](http://document.tencentcloudapi.woa.com/document/product/1706/80309#InstanceNode)

	* 新增成员：VirtualZone

* [NodeInfo](http://document.tencentcloudapi.woa.com/document/product/1706/80309#NodeInfo)

	* 新增成员：VirtualZone

* [NodeInfos](http://document.tencentcloudapi.woa.com/document/product/1706/80309#NodeInfos)

	* 新增成员：VirtualZone

* [RestoreStatus](http://document.tencentcloudapi.woa.com/document/product/1706/80309#RestoreStatus)

	* 新增成员：ID




## 混沌演练平台(cfg) 版本：2021-08-20

### 第 24 次发布

发布时间：2025-07-11 01:18:42

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [Template](http://document.tencentcloudapi.woa.com/document/product/1694/79907#Template)

	* 新增成员：TemplateScenario, TemplatePurpose




## 云游戏(gs) 版本：2019-11-18

### 第 35 次发布

发布时间：2025-07-11 01:37:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAndroidInstanceImage](http://document.tencentcloudapi.woa.com/document/product/1162/85982)

	* 新增入参：AndroidInstanceImageDescription

* [DescribeAndroidInstanceImages](http://document.tencentcloudapi.woa.com/document/product/1162/85980)

	* 新增入参：Filters


修改数据结构：

* [AndroidInstanceImage](http://document.tencentcloudapi.woa.com/document/product/1162/40743#AndroidInstanceImage)

	* 新增成员：AndroidInstanceImageDescription, CreateTime




## 智能全局流量管理(igtm) 版本：2023-10-24

### 第 10 次发布

发布时间：2025-07-11 01:39:46

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDetectPackageDetail](http://document.tencentcloudapi.woa.com/document/product/1696/87187)
* [DescribeDetectTaskPackageList](http://document.tencentcloudapi.woa.com/document/product/1696/87186)
* [DescribeInstancePackageList](http://document.tencentcloudapi.woa.com/document/product/1696/87185)

新增数据结构：

* [CostItem](http://document.tencentcloudapi.woa.com/document/product/1696/83274#CostItem)
* [DetectTaskPackage](http://document.tencentcloudapi.woa.com/document/product/1696/83274#DetectTaskPackage)
* [InstancePackage](http://document.tencentcloudapi.woa.com/document/product/1696/83274#InstancePackage)



## 智能全局流量管理(igtm) 版本：2021-09-07



## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 79 次发布

发布时间：2025-07-11 01:43:26

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* CancelAssignTWeCallLicense



## 腾讯健康组学平台(omics) 版本：2022-11-28

### 第 18 次发布

发布时间：2025-07-11 02:10:31

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ClusterOption](http://document.tencentcloudapi.woa.com/document/product/1725/80781#ClusterOption)

	* 新增成员：SystemNodeInstanceType, SystemNodeCount

* [ResourceIds](http://document.tencentcloudapi.woa.com/document/product/1725/80781#ResourceIds)

	* 新增成员：TKEId, TKESystemNodePoolId




## 云函数(scf) 版本：2018-04-16

### 第 62 次发布

发布时间：2025-07-11 02:14:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateFunction](http://document.tencentcloudapi.woa.com/document/product/583/18586)

	* 新增入参：GooseFsConfigs

* [GetFunction](http://document.tencentcloudapi.woa.com/document/product/583/18584)

	* 新增出参：GooseFsConfigs

* [UpdateFunctionConfiguration](http://document.tencentcloudapi.woa.com/document/product/583/18580)

	* 新增入参：GooseFsConfigs




## 邮件推送(ses) 版本：2020-10-02

### 第 33 次发布

发布时间：2025-07-11 02:15:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateEmailIdentity](http://document.tencentcloudapi.woa.com/document/product/1288/51048)

	* 新增入参：TagList

* [ListEmailIdentities](http://document.tencentcloudapi.woa.com/document/product/1288/51045)

	* 新增入参：TagList, Limit, Offset

	* 新增出参：Total


新增数据结构：

* [TagList](http://document.tencentcloudapi.woa.com/document/product/1288/51053#TagList)

修改数据结构：

* [EmailIdentity](http://document.tencentcloudapi.woa.com/document/product/1288/51053#EmailIdentity)

	* 新增成员：TagList




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 153 次发布

发布时间：2025-07-11 02:23:10

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [PulsarProClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#PulsarProClusterInfo)

	* 新增成员：DeleteProtection




## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 62 次发布

发布时间：2025-07-11 02:25:07

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateWebSecurityTemplate](http://document.tencentcloudapi.woa.com/document/product/1738/87195)
* [DeleteWebSecurityTemplate](http://document.tencentcloudapi.woa.com/document/product/1738/87194)
* [DescribeWebSecurityTemplate](http://document.tencentcloudapi.woa.com/document/product/1738/87193)
* [DescribeWebSecurityTemplates](http://document.tencentcloudapi.woa.com/document/product/1738/87192)
* [ModifyWebSecurityTemplate](http://document.tencentcloudapi.woa.com/document/product/1738/87191)

新增数据结构：

* [BindDomainInfo](http://document.tencentcloudapi.woa.com/document/product/1738/81211#BindDomainInfo)
* [SecurityPolicyTemplateInfo](http://document.tencentcloudapi.woa.com/document/product/1738/81211#SecurityPolicyTemplateInfo)



## 边缘安全加速平台(teo) 版本：2022-01-06



