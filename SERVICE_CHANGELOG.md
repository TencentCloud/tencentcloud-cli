# Release 3.0.1215.1

## 云硬盘(cbs) 版本：2017-03-12

### 第 50 次发布

发布时间：2025-06-09 01:09:33

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* GetSnapOverview



## 弹性 MapReduce(emr) 版本：2019-01-03

### 第 98 次发布

发布时间：2025-06-09 01:16:28

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyPodNum](http://document.tencentcloudapi.woa.com/document/product/589/85469)

	* 新增入参：PodNumList

	* <font color="#dd0000">**修改入参**：</font>ServiceType, PodNum

* [ScaleOutInstance](http://document.tencentcloudapi.woa.com/document/product/589/34264)

	* 新增入参：ComputeResourceAdvanceParams


新增数据结构：

* [AutoScaleGroupAdvanceAttrs](http://document.tencentcloudapi.woa.com/document/product/589/33981#AutoScaleGroupAdvanceAttrs)
* [ComputeResourceAdvanceParams](http://document.tencentcloudapi.woa.com/document/product/589/33981#ComputeResourceAdvanceParams)
* [ServiceTypePodNum](http://document.tencentcloudapi.woa.com/document/product/589/33981#ServiceTypePodNum)
* [Taint](http://document.tencentcloudapi.woa.com/document/product/589/33981#Taint)
* [TkeLabel](http://document.tencentcloudapi.woa.com/document/product/589/33981#TkeLabel)

修改数据结构：

* [AutoScaleResourceConf](http://document.tencentcloudapi.woa.com/document/product/589/33981#AutoScaleResourceConf)

	* 新增成员：ExtraAdvanceAttrs

* [CreateComputeResourceConfig](http://document.tencentcloudapi.woa.com/document/product/589/33981#CreateComputeResourceConfig)

	* 新增成员：AdvanceParams

* [ImageInfo](http://document.tencentcloudapi.woa.com/document/product/589/33981#ImageInfo)

	* 新增成员：Image

* [TimeAutoScaleStrategy](http://document.tencentcloudapi.woa.com/document/product/589/33981#TimeAutoScaleStrategy)

	* 新增成员：GraceDownLabel




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 139 次发布

发布时间：2025-06-09 01:17:23

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateContractDiffTaskWebUrl](http://document.tencentcloudapi.woa.com/document/product/1668/86962)
* [DescribeContractDiffTaskWebUrl](http://document.tencentcloudapi.woa.com/document/product/1668/86961)



## 云游戏(gs) 版本：2019-11-18

### 第 25 次发布

发布时间：2025-06-09 01:18:50

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAndroidInstancesAppBlacklist](http://document.tencentcloudapi.woa.com/document/product/1162/86967)
* [DescribeAndroidInstancesByApps](http://document.tencentcloudapi.woa.com/document/product/1162/86969)
* [ImportAndroidInstanceImage](http://document.tencentcloudapi.woa.com/document/product/1162/86963)
* [ModifyAndroidInstancesAppBlacklist](http://document.tencentcloudapi.woa.com/document/product/1162/86966)
* [ModifyAndroidInstancesResources](http://document.tencentcloudapi.woa.com/document/product/1162/86968)
* [SetAndroidInstancesBGAppKeepAlive](http://document.tencentcloudapi.woa.com/document/product/1162/86965)
* [SetAndroidInstancesFGAppKeepAlive](http://document.tencentcloudapi.woa.com/document/product/1162/86964)

新增数据结构：

* [AndroidInstanceAppBlacklist](http://document.tencentcloudapi.woa.com/document/product/1162/40743#AndroidInstanceAppBlacklist)



## 弹性微服务(tem) 版本：2021-07-01

### 第 40 次发布

发布时间：2025-06-09 01:30:13

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyGatewayIngress](http://document.tencentcloudapi.woa.com/document/product/1371/86970)



## 弹性微服务(tem) 版本：2020-12-21



## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 58 次发布

发布时间：2025-06-09 01:30:51

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [AdaptiveFrequencyControl](http://document.tencentcloudapi.woa.com/document/product/1738/81211#AdaptiveFrequencyControl)
* [BandwidthAbuseDefense](http://document.tencentcloudapi.woa.com/document/product/1738/81211#BandwidthAbuseDefense)
* [ChallengeActionParameters](http://document.tencentcloudapi.woa.com/document/product/1738/81211#ChallengeActionParameters)
* [ClientFiltering](http://document.tencentcloudapi.woa.com/document/product/1738/81211#ClientFiltering)
* [DenyActionParameters](http://document.tencentcloudapi.woa.com/document/product/1738/81211#DenyActionParameters)
* [ExceptionRule](http://document.tencentcloudapi.woa.com/document/product/1738/81211#ExceptionRule)
* [ExceptionRules](http://document.tencentcloudapi.woa.com/document/product/1738/81211#ExceptionRules)
* [HttpDDoSProtection](http://document.tencentcloudapi.woa.com/document/product/1738/81211#HttpDDoSProtection)
* [MinimalRequestBodyTransferRate](http://document.tencentcloudapi.woa.com/document/product/1738/81211#MinimalRequestBodyTransferRate)
* [RateLimitingRule](http://document.tencentcloudapi.woa.com/document/product/1738/81211#RateLimitingRule)
* [RateLimitingRules](http://document.tencentcloudapi.woa.com/document/product/1738/81211#RateLimitingRules)
* [RequestBodyTransferTimeout](http://document.tencentcloudapi.woa.com/document/product/1738/81211#RequestBodyTransferTimeout)
* [RequestFieldsForException](http://document.tencentcloudapi.woa.com/document/product/1738/81211#RequestFieldsForException)
* [SlowAttackDefense](http://document.tencentcloudapi.woa.com/document/product/1738/81211#SlowAttackDefense)

修改数据结构：

* [SecurityAction](http://document.tencentcloudapi.woa.com/document/product/1738/81211#SecurityAction)

	* 新增成员：DenyActionParameters, ChallengeActionParameters

* [SecurityPolicy](http://document.tencentcloudapi.woa.com/document/product/1738/81211#SecurityPolicy)

	* 新增成员：HttpDDoSProtection, RateLimitingRules, ExceptionRules




## 边缘安全加速平台(teo) 版本：2022-01-06



