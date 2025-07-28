# Release 3.0.1251.1

## 弹性伸缩(as) 版本：2018-04-19

### 第 50 次发布

发布时间：2025-07-29 01:09:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAutoScalingGroup](http://document.tencentcloudapi.woa.com/document/product/377/20440)

	* 新增入参：ConcurrentScaleOutForDesiredCapacity

* [ModifyAutoScalingGroup](http://document.tencentcloudapi.woa.com/document/product/377/20433)

	* 新增入参：ConcurrentScaleOutForDesiredCapacity


修改数据结构：

* [AutoScalingGroup](http://document.tencentcloudapi.woa.com/document/product/377/20453#AutoScalingGroup)

	* 新增成员：ConcurrentScaleOutForDesiredCapacity




## 内容分发网络 CDN(cdn) 版本：2018-06-06

### 第 65 次发布

发布时间：2025-07-29 01:16:39

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeCdnIp](http://document.tencentcloudapi.woa.com/document/product/228/37868)

	* 新增入参：AllPlatformIp




## 腾讯电子签企业版(ess) 版本：2020-11-11

### 第 154 次发布

发布时间：2025-07-29 01:34:12

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateOrganizationAuthUrl](http://document.tencentcloudapi.woa.com/document/product/1668/83727)

	* 新增入参：BankAccountNumber, BankAccountNumberSame




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 196 次发布

发布时间：2025-07-29 01:35:13

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateConsoleLoginUrl](http://document.tencentcloudapi.woa.com/document/product/1595/75251)

	* 新增入参：BankAccountNumber


修改数据结构：

* [OrganizationAuthorizationOptions](http://document.tencentcloudapi.woa.com/document/product/1595/75258#OrganizationAuthorizationOptions)

	* 新增成员：BankAccountNumberSame




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



## 媒体处理(mps) 版本：2019-06-12

### 第 104 次发布

发布时间：2025-07-29 01:58:05

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeTasks](http://document.tencentcloudapi.woa.com/document/product/862/37613)

	* 新增入参：StartTime, EndTime, ChannelInfo


新增数据结构：

* [ExecRuleTaskData](http://document.tencentcloudapi.woa.com/document/product/862/37615#ExecRuleTaskData)
* [ExecRulesTask](http://document.tencentcloudapi.woa.com/document/product/862/37615#ExecRulesTask)
* [QualityControlStrategy](http://document.tencentcloudapi.woa.com/document/product/862/37615#QualityControlStrategy)
* [RuleConditionItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#RuleConditionItem)
* [Rules](http://document.tencentcloudapi.woa.com/document/product/862/37615#Rules)
* [ScheduleExecRuleTaskResult](http://document.tencentcloudapi.woa.com/document/product/862/37615#ScheduleExecRuleTaskResult)
* [SubtitlePosition](http://document.tencentcloudapi.woa.com/document/product/862/37615#SubtitlePosition)
* [TimeSpotCheck](http://document.tencentcloudapi.woa.com/document/product/862/37615#TimeSpotCheck)

修改数据结构：

* [ActivityPara](http://document.tencentcloudapi.woa.com/document/product/862/37615#ActivityPara)

	* 新增成员：ExecRulesTask

* [ActivityResItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#ActivityResItem)

	* 新增成员：ExecRuleTask

* [ActivityResult](http://document.tencentcloudapi.woa.com/document/product/862/37615#ActivityResult)

	* 新增成员：SkipNode

* [AdaptiveDynamicStreamingTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#AdaptiveDynamicStreamingTaskInput)

	* 新增成员：StdExtInfo

* [AiAnalysisTaskDelLogoOutput](http://document.tencentcloudapi.woa.com/document/product/862/37615#AiAnalysisTaskDelLogoOutput)

	* 新增成员：SubtitlePos

* [MediaAiAnalysisTagItem](http://document.tencentcloudapi.woa.com/document/product/862/37615#MediaAiAnalysisTagItem)

	* 新增成员：SpecialInfo

* [QualityControlTemplate](http://document.tencentcloudapi.woa.com/document/product/862/37615#QualityControlTemplate)

	* 新增成员：Strategy

* [ScheduleAnalysisTaskResult](http://document.tencentcloudapi.woa.com/document/product/862/37615#ScheduleAnalysisTaskResult)

	* <font color="#dd0000">**修改成员**：</font>BeginProcessTime, FinishTime

* [ScheduleTask](http://document.tencentcloudapi.woa.com/document/product/862/37615#ScheduleTask)

	* <font color="#dd0000">**修改成员**：</font>ErrCode, Message

* [SmartSubtitlesTaskInput](http://document.tencentcloudapi.woa.com/document/product/862/37615#SmartSubtitlesTaskInput)

	* 新增成员：OutputStorage, OutputObjectPath




## 集团账号管理(organization) 版本：2021-03-31

### 第 56 次发布

发布时间：2025-07-29 02:01:12

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AddShareUnitsResources](http://document.tencentcloudapi.woa.com/document/product/850/87265)
* [DescribeManagerShareResources](http://document.tencentcloudapi.woa.com/document/product/850/87266)

新增数据结构：

* [ManagerShareResource](http://document.tencentcloudapi.woa.com/document/product/850/67060#ManagerShareResource)
* [ShareUnitInfo](http://document.tencentcloudapi.woa.com/document/product/850/67060#ShareUnitInfo)



## 集团账号管理(organization) 版本：2018-12-25



## SSL 证书(ssl) 版本：2019-12-05

### 第 89 次发布

发布时间：2025-07-29 02:08:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [UploadCertificate](http://document.tencentcloudapi.woa.com/document/product/400/41665)

	* 新增入参：KeyPassword




