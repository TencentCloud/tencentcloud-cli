# Release 3.0.1409.1

## 腾讯云数据仓库TCHouse-C(cdwch) 版本：2020-09-15

### 第 31 次发布

发布时间：2026-04-23 01:19:21

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InstanceConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1667/79282#InstanceConfigInfo)

	* 新增成员：ConfigEffective




## 文件存储(cfs) 版本：2019-07-19

### 第 42 次发布

发布时间：2026-04-23 01:20:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCfsFileSystem](http://document.tencentcloudapi.woa.com/document/product/582/38174)

	* 新增入参：ClusterId




## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 137 次发布

发布时间：2026-04-23 01:40:36

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateCloudInstance](http://document.tencentcloudapi.woa.com/document/product/589/85470)

	* 新增入参：ContainerExtraConf

* [InstallSoftware](http://document.tencentcloudapi.woa.com/document/product/589/88886)

	* 新增入参：ContainerExtraConf

* [TerminateInstance](http://document.tencentcloudapi.woa.com/document/product/589/34260)

	* 新增入参：RetainTkeCluster


新增数据结构：

* [ContainerExtraConf](http://document.tencentcloudapi.woa.com/document/product/589/33981#ContainerExtraConf)
* [LabelSelector](http://document.tencentcloudapi.woa.com/document/product/589/33981#LabelSelector)
* [LabelSelectorRequirement](http://document.tencentcloudapi.woa.com/document/product/589/33981#LabelSelectorRequirement)
* [PodAffinitySpec](http://document.tencentcloudapi.woa.com/document/product/589/33981#PodAffinitySpec)
* [PodAffinityTerm](http://document.tencentcloudapi.woa.com/document/product/589/33981#PodAffinityTerm)
* [StringMap](http://document.tencentcloudapi.woa.com/document/product/589/33981#StringMap)
* [TopologySpreadConstraint](http://document.tencentcloudapi.woa.com/document/product/589/33981#TopologySpreadConstraint)
* [WeightedPodAffinityTerm](http://document.tencentcloudapi.woa.com/document/product/589/33981#WeightedPodAffinityTerm)

修改数据结构：

* [CloudResource](http://document.tencentcloudapi.woa.com/document/product/589/33981#CloudResource)

	* 新增成员：PodAffinity, PodAntiAffinity, TopologySpreadConstraints, PodLabels, EnableDefaultRayCluster

* [ComputeResourceAdvanceParams](http://document.tencentcloudapi.woa.com/document/product/589/33981#ComputeResourceAdvanceParams)

	* 新增成员：TkeClusterNodePool




## 图片内容安全(ims) 版本：2020-12-29

### 第 14 次发布

发布时间：2026-04-23 01:49:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateImageModerationAsyncTask](http://document.tencentcloudapi.woa.com/document/product/1125/77139)

	* 新增入参：FileUrlList, TextContent




## 图片内容安全(ims) 版本：2020-07-13



## 腾讯云可观测平台(monitor) 版本：2023-06-16



## 腾讯云可观测平台(monitor) 版本：2018-07-24

### 第 122 次发布

发布时间：2026-04-23 02:01:06

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/51288)

	* 新增入参：TimeZoneName

* [ModifyAlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/51277)

	* 新增入参：TimeZoneName


修改数据结构：

* [AlarmNotice](http://document.tencentcloudapi.woa.com/document/product/248/30354#AlarmNotice)

	* 新增成员：TimeZoneName




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 56 次发布

发布时间：2026-04-23 02:07:46

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDBErrlogs](http://document.tencentcloudapi.woa.com/document/product/409/18093)

	* 新增入参：LogFilters


新增数据结构：

* [LogFilter](http://document.tencentcloudapi.woa.com/document/product/409/16778#LogFilter)

修改数据结构：

* [ErrLogDetail](http://document.tencentcloudapi.woa.com/document/product/409/16778#ErrLogDetail)

	* 新增成员：ProcessId, ClientAddr, SessionId, SessionStartTime, VirtualTransactionId, SqlStateCode, ApplicationName

* [RawSlowQuery](http://document.tencentcloudapi.woa.com/document/product/409/16778#RawSlowQuery)

	* 新增成员：ProcessId, SessionId, VirtualTransactionId, SqlStateCode, ApplicationName




## 数据开发治理平台 WeData(wedata) 版本：2025-10-10

### 第 14 次发布

发布时间：2026-04-23 02:37:02

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ListReleasedCodeFile](http://document.tencentcloudapi.woa.com/document/product/1607/89842)

	* 新增入参：CodeFileName


修改数据结构：

* [CodeFileConfig](http://document.tencentcloudapi.woa.com/document/product/1607/88970#CodeFileConfig)

	* 新增成员：Widgets




## 数据开发治理平台 WeData(wedata) 版本：2025-08-06



## 数据开发治理平台 WeData(wedata) 版本：2021-08-20



