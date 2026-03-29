# Release 3.0.1392.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 8 次发布

发布时间：2026-03-30 01:07:42

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AcquireOAuth2AccessToken](http://document.tencentcloudapi.woa.com/document/product/1804/89260)
* [CompleteOAuth2AccessTokenAuth](http://document.tencentcloudapi.woa.com/document/product/1804/89259)
* [CreateWorkloadAccessTokenForUserId](http://document.tencentcloudapi.woa.com/document/product/1804/89258)

修改接口：

* [StartSandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87847)

	* 新增入参：AuthMode, Metadata

* [UpdateSandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87845)

	* 新增入参：Metadata


新增数据结构：

* [CustomParameters](http://document.tencentcloudapi.woa.com/document/product/1804/87854#CustomParameters)
* [MetadataVar](http://document.tencentcloudapi.woa.com/document/product/1804/87854#MetadataVar)

修改数据结构：

* [SandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxInstance)

	* 新增成员：NetworkMode, Metadata




## AI Agent 安全网关(apis) 版本：2024-08-01

### 第 10 次发布

发布时间：2026-03-30 01:10:49

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89006)

	* 新增入参：ResourceIDs

* [ModifyAIMCredential](http://document.tencentcloudapi.woa.com/document/product/1805/89001)

	* 新增入参：ResourceIDs




## 费用中心(billing) 版本：2018-07-09

### 第 114 次发布

发布时间：2026-03-30 01:13:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeMeasureResourceDetails](http://document.tencentcloudapi.woa.com/document/product/555/82323)

	* 新增入参：RegionId

* [DescribeMeasureResources](http://document.tencentcloudapi.woa.com/document/product/555/81765)

	* 新增入参：RegionId




## 日志服务(cls) 版本：2020-10-16

### 第 142 次发布

发布时间：2026-03-30 01:24:30

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateConsole](http://document.tencentcloudapi.woa.com/document/product/614/89264)
* [DeleteConsole](http://document.tencentcloudapi.woa.com/document/product/614/89263)
* [DescribeConsoles](http://document.tencentcloudapi.woa.com/document/product/614/89262)
* [ModifyConsole](http://document.tencentcloudapi.woa.com/document/product/614/89261)

新增数据结构：

* [AccessControlRule](http://document.tencentcloudapi.woa.com/document/product/614/56471#AccessControlRule)
* [AnonymousLoginInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#AnonymousLoginInfo)
* [AuthRoleInfo](http://document.tencentcloudapi.woa.com/document/product/614/56471#AuthRoleInfo)
* [Console](http://document.tencentcloudapi.woa.com/document/product/614/56471#Console)
* [ConsoleAccount](http://document.tencentcloudapi.woa.com/document/product/614/56471#ConsoleAccount)



## 云安全一体化平台(csip) 版本：2022-11-21

### 第 69 次发布

发布时间：2026-03-30 01:27:15

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAKAnalysisDetail](http://document.tencentcloudapi.woa.com/document/product/1726/89265)



## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 150 次发布

发布时间：2026-03-30 01:36:32

本次发布包含了以下内容：

改善已有的文档。

修改数据结构：

* [NotebookSessionInfo](http://document.tencentcloudapi.woa.com/document/product/1342/53778#NotebookSessionInfo)

	* 新增成员：SparkAppName

* [NotebookSessions](http://document.tencentcloudapi.woa.com/document/product/1342/53778#NotebookSessions)

	* 新增成员：KernelId, SparkAppName




## 域名注册(domain) 版本：2018-08-08

### 第 44 次发布

发布时间：2026-03-30 01:38:58

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyDomainOwner](http://document.tencentcloudapi.woa.com/document/product/242/89266)



## 腾讯云可观测平台(monitor) 版本：2023-06-16

### 第 8 次发布

发布时间：2026-03-30 02:02:21

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeAIWorkbenchSREDigitalTwinTaskList](http://document.tencentcloudapi.woa.com/document/product/248/89271)
* [DescribeAIWorkbenchSREDigitalTwinWorkLogDetail](http://document.tencentcloudapi.woa.com/document/product/248/89270)
* [DescribeAIWorkbenchSREDigitalTwinWorkLogList](http://document.tencentcloudapi.woa.com/document/product/248/89269)
* [TriggerAIWorkbenchSREDigitalTwinTask](http://document.tencentcloudapi.woa.com/document/product/248/89268)

新增数据结构：

* [AIWorkbenchSREDigitalTwinTask](http://document.tencentcloudapi.woa.com/document/product/248/81423#AIWorkbenchSREDigitalTwinTask)
* [AIWorkbenchSREDigitalTwinTaskList](http://document.tencentcloudapi.woa.com/document/product/248/81423#AIWorkbenchSREDigitalTwinTaskList)
* [AIWorkbenchSREDigitalTwinWorkLog](http://document.tencentcloudapi.woa.com/document/product/248/81423#AIWorkbenchSREDigitalTwinWorkLog)
* [AIWorkbenchSREDigitalTwinWorkLogDetail](http://document.tencentcloudapi.woa.com/document/product/248/81423#AIWorkbenchSREDigitalTwinWorkLogDetail)
* [AIWorkbenchSREDigitalTwinWorkLogList](http://document.tencentcloudapi.woa.com/document/product/248/81423#AIWorkbenchSREDigitalTwinWorkLogList)
* [TriggerDigitalTwinTaskResp](http://document.tencentcloudapi.woa.com/document/product/248/81423#TriggerDigitalTwinTaskResp)



## 腾讯云可观测平台(monitor) 版本：2018-07-24



## 智能媒资托管(smh) 版本：2021-07-12

### 第 7 次发布

发布时间：2026-03-30 02:11:31

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateLibrary](http://document.tencentcloudapi.woa.com/document/product/1689/79771)

	* 新增出参：AccessDomain




