# Release 3.0.1253.1

## Elasticsearch Service(es) 版本：2018-04-16

### 第 87 次发布

发布时间：2025-08-06 01:35:17

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateInstance](http://document.tencentcloudapi.woa.com/document/product/845/30633)

	* 新增入参：AutoScaleDiskInfoList, EnableKibanaPublicAccess

* [UpdateInstance](http://document.tencentcloudapi.woa.com/document/product/845/30629)

	* 新增入参：AutoScaleDiskInfoList, AutoScaleDiskDeleteNodeTypeList


新增数据结构：

* [AutoScaleDiskInfo](http://document.tencentcloudapi.woa.com/document/product/845/30634#AutoScaleDiskInfo)

修改数据结构：

* [Operation](http://document.tencentcloudapi.woa.com/document/product/845/30634#Operation)

	* 新增成员：AutoScaleTag




## SSL 证书(ssl) 版本：2019-12-05

### 第 92 次发布

发布时间：2025-08-06 02:02:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeManagerDetail](http://document.tencentcloudapi.woa.com/document/product/400/52673)

	* 新增出参：ManagerIdType, ManagerIdNumber, ContactIdType, ContactIdNumber




## 消息队列 TDMQ(tdmq) 版本：2020-02-17

### 第 154 次发布

发布时间：2025-08-06 02:08:16

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [InternalRocketMQInstance](http://document.tencentcloudapi.woa.com/document/product/1179/46089#InternalRocketMQInstance)

	* 新增成员：AutoCreateTopicEnabled, AdminFeatureEnabled

* [RocketMQClusterInfo](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQClusterInfo)

	* 新增成员：AutoCreateTopicEnabled, AdminFeatureEnabled, AdminAccessKey, AdminSecretKey, EnableDeletionProtection

* [RocketMQGroup](http://document.tencentcloudapi.woa.com/document/product/1179/46089#RocketMQGroup)

	* 新增成员：SubscribeTopicNum




## 高性能计算平台(thpc) 版本：2023-03-21

### 第 19 次发布

发布时间：2025-08-06 02:11:30

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DeleteJob](http://document.tencentcloudapi.woa.com/document/product/1701/87539)
* [DescribeJobSubmitInfo](http://document.tencentcloudapi.woa.com/document/product/1701/87538)
* [DescribeJobs](http://document.tencentcloudapi.woa.com/document/product/1701/87537)
* [DescribeJobsOverview](http://document.tencentcloudapi.woa.com/document/product/1701/87536)
* [SubmitJob](http://document.tencentcloudapi.woa.com/document/product/1701/87535)
* [TerminateJob](http://document.tencentcloudapi.woa.com/document/product/1701/87534)

新增数据结构：

* [Application](http://document.tencentcloudapi.woa.com/document/product/1701/80209#Application)
* [CommandItem](http://document.tencentcloudapi.woa.com/document/product/1701/80209#CommandItem)
* [Docker](http://document.tencentcloudapi.woa.com/document/product/1701/80209#Docker)
* [EnvVar](http://document.tencentcloudapi.woa.com/document/product/1701/80209#EnvVar)
* [Job](http://document.tencentcloudapi.woa.com/document/product/1701/80209#Job)
* [JobView](http://document.tencentcloudapi.woa.com/document/product/1701/80209#JobView)
* [OutputRedirect](http://document.tencentcloudapi.woa.com/document/product/1701/80209#OutputRedirect)
* [StorageMount](http://document.tencentcloudapi.woa.com/document/product/1701/80209#StorageMount)
* [Task](http://document.tencentcloudapi.woa.com/document/product/1701/80209#Task)
* [TaskDependence](http://document.tencentcloudapi.woa.com/document/product/1701/80209#TaskDependence)



## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



## 消息队列 RocketMQ 版(trocket) 版本：2023-03-08

### 第 49 次发布

发布时间：2025-08-06 02:14:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeConsumerGroupList](http://document.tencentcloudapi.woa.com/document/product/1739/82583)

	* 新增入参：SortedBy, SortOrder


修改数据结构：

* [ConsumeGroupItem](http://document.tencentcloudapi.woa.com/document/product/1739/81437#ConsumeGroupItem)

	* 新增成员：SubscribeTopicNum, CreateTime




