# Release 3.0.1483.1

## 商业智能分析 BI(bi) 版本：2022-01-05

### 第 41 次发布

发布时间：2026-08-31 01:10:30

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeUserRoleList](http://document.tencentcloudapi.woa.com/document/product/1707/82001)

	* 新增入参：IdentityType


修改数据结构：

* [UserInfo](http://document.tencentcloudapi.woa.com/document/product/1707/80324#UserInfo)

	* 新增成员：IdentityType

* [UserRoleListDataUserRoleInfo](http://document.tencentcloudapi.woa.com/document/product/1707/80324#UserRoleListDataUserRoleInfo)

	* 新增成员：IdentityType




## 负载均衡(clb) 版本：2023-04-17



## 负载均衡(clb) 版本：2018-03-17

### 第 96 次发布

发布时间：2026-08-31 01:15:21

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeUpperModels](http://document.tencentcloudapi.woa.com/document/product/214/91017)

	* 新增入参：CMRPrivateNetworkTunnelId

* [TestModelInputModalities](http://document.tencentcloudapi.woa.com/document/product/214/91011)

	* 新增入参：CMRPrivateNetworkTunnelId

* [TestServiceProviderConnection](http://document.tencentcloudapi.woa.com/document/product/214/91010)

	* 新增入参：CMRPrivateNetworkTunnelId




## 物联网开发平台(iotexplorer) 版本：2019-04-23

### 第 99 次发布

发布时间：2026-08-31 01:31:27

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeTWeSeeSubscription](http://document.tencentcloudapi.woa.com/document/product/1081/91258)

	* 新增出参：SummarizeConfig

* [DescribeTWeSeeTask](http://document.tencentcloudapi.woa.com/document/product/1081/91257)

	* 新增入参：FileURLExpireTime

* [ModifyTWeSeeSubscription](http://document.tencentcloudapi.woa.com/document/product/1081/91248)

	* 新增入参：SummarizeConfig


新增数据结构：

* [SeeSummarizeConfig](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeSummarizeConfig)
* [SeeSummarizeResult](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeSummarizeResult)

修改数据结构：

* [SeeTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1081/34988#SeeTaskInfo)

	* 新增成员：SummarizeResult




## 云数据库 PostgreSQL(postgres) 版本：2017-03-12

### 第 69 次发布

发布时间：2026-08-31 01:37:55

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CloseDBProxyAddress](http://document.tencentcloudapi.woa.com/document/product/409/92475)
* [CreateDBProxyAddress](http://document.tencentcloudapi.woa.com/document/product/409/92474)
* [DescribeDBProxySSLConfig](http://document.tencentcloudapi.woa.com/document/product/409/92473)
* [ModifyDBProxySSLConfig](http://document.tencentcloudapi.woa.com/document/product/409/92472)



## 云开发 CloudBase(tcb) 版本：2018-06-08

### 第 65 次发布

发布时间：2026-08-31 01:41:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateFunction](http://document.tencentcloudapi.woa.com/document/product/876/89198)

	* 新增入参：InitTimeout, CodeSource, VpcConfig, Layers, PublicNetConfig, AsyncRunEnable, TraceEnable, AutoCreateClsTopic, AutoDeployClsTopicIndex, DnsCache, EipConfig


新增数据结构：

* [FunctionEipConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#FunctionEipConfig)
* [FunctionEipConfigFixed](http://document.tencentcloudapi.woa.com/document/product/876/34822#FunctionEipConfigFixed)
* [FunctionLayer](http://document.tencentcloudapi.woa.com/document/product/876/34822#FunctionLayer)
* [FunctionPublicNetConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#FunctionPublicNetConfig)
* [FunctionVpcConfig](http://document.tencentcloudapi.woa.com/document/product/876/34822#FunctionVpcConfig)



## 高性能计算平台(thpc) 版本：2023-03-21

### 第 36 次发布

发布时间：2026-08-31 01:45:47

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateScheduledAction](http://document.tencentcloudapi.woa.com/document/product/1701/92483)
* [DeleteScheduledAction](http://document.tencentcloudapi.woa.com/document/product/1701/92482)
* [DescribeInstanceFamilies](http://document.tencentcloudapi.woa.com/document/product/1701/92481)
* [DescribeQueueAutoScaling](http://document.tencentcloudapi.woa.com/document/product/1701/92480)
* [DescribeQueueAutoScalingOverview](http://document.tencentcloudapi.woa.com/document/product/1701/92479)
* [DescribeScheduledActions](http://document.tencentcloudapi.woa.com/document/product/1701/92478)
* [ModifyScheduledAction](http://document.tencentcloudapi.woa.com/document/product/1701/92477)
* [SetQueueAutoScaling](http://document.tencentcloudapi.woa.com/document/product/1701/92476)

新增数据结构：

* [ExpansionPolicy](http://document.tencentcloudapi.woa.com/document/product/1701/80209#ExpansionPolicy)
* [ExpansionPriority](http://document.tencentcloudapi.woa.com/document/product/1701/80209#ExpansionPriority)
* [ScalingPolicy](http://document.tencentcloudapi.woa.com/document/product/1701/80209#ScalingPolicy)
* [TemplateOverrides](http://document.tencentcloudapi.woa.com/document/product/1701/80209#TemplateOverrides)



## 高性能计算平台(thpc) 版本：2022-04-01



## 高性能计算平台(thpc) 版本：2021-11-09



