# Release 3.0.1421.1

## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 164 次发布

发布时间：2026-05-12 01:30:24

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [ProxyConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48097#ProxyConfig)




## Elasticsearch Service(es) 版本：2018-04-16

### 第 107 次发布

发布时间：2026-05-12 01:41:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateClusterSnapshot](http://document.tencentcloudapi.woa.com/document/product/845/85136)

	* 新增入参：MaxSnapshotPerSec

* [DeleteInstance](http://document.tencentcloudapi.woa.com/document/product/845/30632)

	* 新增入参：LockEnabled, LockDuration

* [RestoreClusterSnapshot](http://document.tencentcloudapi.woa.com/document/product/845/85132)

	* 新增入参：MaxRestorePerSec


修改数据结构：

* [CosBackup](http://document.tencentcloudapi.woa.com/document/product/845/30634#CosBackup)

	* 新增成员：MaxSnapshotPerSec, MaxRestorePerSec, InstanceId

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/845/30634#InstanceInfo)

	* 新增成员：IsInRecycleBin, RecycleLockEnabled, MayDestroyPoint, DelayDestroyInterval

* [Operation](http://document.tencentcloudapi.woa.com/document/product/845/30634#Operation)

	* 新增成员：SuspendedReason

* [ProcessDetail](http://document.tencentcloudapi.woa.com/document/product/845/30634#ProcessDetail)

	* 新增成员：EstimatedTimeRemaining

* [Snapshots](http://document.tencentcloudapi.woa.com/document/product/845/30634#Snapshots)

	* 新增成员：MaxSnapshotPerSec, InstanceId




## 人脸核身(faceid) 版本：2018-03-01

### 第 97 次发布

发布时间：2026-05-12 01:43:24

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAMLWebhook](http://document.tencentcloudapi.woa.com/document/product/1007/90152)
* [DeleteAMLWebhook](http://document.tencentcloudapi.woa.com/document/product/1007/90151)
* [ProcessAMLCallback](http://document.tencentcloudapi.woa.com/document/product/1007/90150)
* [UpdateAMLWebhook](http://document.tencentcloudapi.woa.com/document/product/1007/90149)



## 媒体处理(mps) 版本：2019-06-12

### 第 171 次发布

发布时间：2026-05-12 02:02:06

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DetectVideoSubtitleArea](http://document.tencentcloudapi.woa.com/document/product/862/90153)

新增数据结构：

* [SubtitleArea](http://document.tencentcloudapi.woa.com/document/product/862/37615#SubtitleArea)



## 实时音视频(trtc) 版本：2019-07-22

### 第 131 次发布

发布时间：2026-05-12 02:28:11

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeTRTCAIRecognitionUsage](http://document.tencentcloudapi.woa.com/document/product/647/90156)
* [DescribeTRTCDedicatedCloudAccUsage](http://document.tencentcloudapi.woa.com/document/product/647/90155)
* [DescribeTRTCSegmentModerationUsage](http://document.tencentcloudapi.woa.com/document/product/647/90154)

新增数据结构：

* [UsageList](http://document.tencentcloudapi.woa.com/document/product/647/44055#UsageList)



## TSF-Polaris&ZK&网关(tse) 版本：2020-12-07

### 第 103 次发布

发布时间：2026-05-12 02:29:33

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeGovernanceServices](http://document.tencentcloudapi.woa.com/document/product/1364/83469)

	* 新增入参：Type


修改数据结构：

* [GovernanceService](http://document.tencentcloudapi.woa.com/document/product/1364/54942#GovernanceService)

	* 新增成员：Type

* [GovernanceServiceInput](http://document.tencentcloudapi.woa.com/document/product/1364/54942#GovernanceServiceInput)

	* 新增成员：Type




