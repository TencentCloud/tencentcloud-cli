# Release 3.0.1414.1

## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 139 次发布

发布时间：2026-04-30 01:40:48

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateDynamicInstance](http://document.tencentcloudapi.woa.com/document/product/589/90105)
* [DescribeDynamicInstanceList](http://document.tencentcloudapi.woa.com/document/product/589/90106)
* [ModifyDynamicInstance](http://document.tencentcloudapi.woa.com/document/product/589/90104)
* [TerminateDynamicInstances](http://document.tencentcloudapi.woa.com/document/product/589/90103)

新增数据结构：

* [CBSVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#CBSVolume)
* [CFSTurboVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#CFSTurboVolume)
* [CFSVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#CFSVolume)
* [COSVolume](http://document.tencentcloudapi.woa.com/document/product/589/33981#COSVolume)
* [DynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceForm)
* [DynamicInstanceGroup](http://document.tencentcloudapi.woa.com/document/product/589/33981#DynamicInstanceGroup)
* [ModifyDynamicInstanceForm](http://document.tencentcloudapi.woa.com/document/product/589/33981#ModifyDynamicInstanceForm)
* [NameValue](http://document.tencentcloudapi.woa.com/document/product/589/33981#NameValue)
* [RayCluster](http://document.tencentcloudapi.woa.com/document/product/589/33981#RayCluster)
* [VolumeMount](http://document.tencentcloudapi.woa.com/document/product/589/33981#VolumeMount)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 39 次发布

发布时间：2026-04-30 01:50:36

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeResourceGrantedAccountGroups](http://document.tencentcloudapi.woa.com/document/product/1794/90112)
* [DescribeResourceGrantedAccounts](http://document.tencentcloudapi.woa.com/document/product/1794/90111)
* [DescribeResourceGrantedVirtualGroups](http://document.tencentcloudapi.woa.com/document/product/1794/90110)
* [GrantResourcesByAccountGroups](http://document.tencentcloudapi.woa.com/document/product/1794/90109)
* [GrantResourcesByAccounts](http://document.tencentcloudapi.woa.com/document/product/1794/90108)
* [GrantResourcesByVirtualGroups](http://document.tencentcloudapi.woa.com/document/product/1794/90107)
* [ModifyDeviceTrustStatus](http://document.tencentcloudapi.woa.com/document/product/1794/90113)

新增数据结构：

* [DescribeResourceGrantedAccountGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeResourceGrantedAccountGroupsData)
* [DescribeResourceGrantedAccountsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeResourceGrantedAccountsData)
* [DescribeResourceGrantedVirtualGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#DescribeResourceGrantedVirtualGroupsData)
* [GrantResourceOperationByAccountGroups](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourceOperationByAccountGroups)
* [GrantResourceOperationByAccounts](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourceOperationByAccounts)
* [GrantResourceOperationByVirtualGroups](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourceOperationByVirtualGroups)
* [GrantResourcesByAccountGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourcesByAccountGroupsData)
* [GrantResourcesByAccountsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourcesByAccountsData)
* [GrantResourcesByVirtualGroupsData](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantResourcesByVirtualGroupsData)
* [GrantedAccountGroupItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantedAccountGroupItem)
* [GrantedAccountItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantedAccountItem)
* [GrantedVirtualGroupItem](http://document.tencentcloudapi.woa.com/document/product/1794/86648#GrantedVirtualGroupItem)



## 媒体处理(mps) 版本：2019-06-12

### 第 168 次发布

发布时间：2026-04-30 02:03:52

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeVoices](http://document.tencentcloudapi.woa.com/document/product/862/89375)

	* 新增入参：VoiceId, VoiceName, Description, Gender, Age, Languages, Labels, Scenes

* [DesignVoiceAsync](http://document.tencentcloudapi.woa.com/document/product/862/90010)

	* 新增入参：VoiceProfile

* [SyncDubbing](http://document.tencentcloudapi.woa.com/document/product/862/88809)

	* 新增入参：VoiceProfile, ResourceId


新增数据结构：

* [VoiceProfile](http://document.tencentcloudapi.woa.com/document/product/862/37615#VoiceProfile)

修改数据结构：

* [VoiceInfo](http://document.tencentcloudapi.woa.com/document/product/862/37615#VoiceInfo)

	* 新增成员：Age




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 18 次发布

发布时间：2026-04-30 02:37:24

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ExecAdminComputeResourceMeta](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExecAdminComputeResourceMeta)

	* 新增成员：ComputeType, GpuQuota, GpuAvailable, MLEnabled

* [ExperimentDetail](http://document.tencentcloudapi.woa.com/document/product/1607/88970#ExperimentDetail)

	* 新增成员：Location




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



